# NeuroSort/main.py

import os
from core.db_manager import DBManager
from core.nlp_processor import NLPProcessor
import numpy as np # Untuk manipulasi array numpy

def load_documents_from_folder(folder_path):
    """Loads text content from all .txt files in a given folder."""
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                  
                    title = os.path.splitext(filename)[0].replace("_", " ").title()
                    documents.append({"filename": filename, "title": title, "content": content})
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
    return documents

def index_documents(db_manager, nlp_processor, documents):
    """Preprocesses and indexes documents into the database."""
    print("\n--- Indexing Documents ---")
    
    if not documents:
        print("No documents to index.")
        return

    # 1. Preprocess all documents to build the corpus for TF-IDF vectorizer
    corpus = [nlp_processor.preprocess_text(doc["content"]) for doc in documents]
    
    # 2. Fit the TF-IDF vectorizer to the entire corpus
    nlp_processor.fit_vectorizer(corpus)

    # 3. Process and add each document to the database
    for i, doc_data in enumerate(documents):
        print(f"Processing document: {doc_data['filename']}")
        preprocessed_content = nlp_processor.preprocess_text(doc_data["content"])
        
        # Generate TF-IDF vector for the current document
        tf_idf_vector = nlp_processor.transform_text(preprocessed_content)
        
        # Add to DB
        db_manager.add_document(
            doc_data["filename"],
            doc_data["title"],
            doc_data["content"],
            tf_idf_vector # tf_idf_vector is already a numpy array from transform_text
        )
    print("Document indexing complete.")

def search_documents(db_manager, nlp_processor, query):
    """Performs semantic search on indexed documents."""
    print(f"\n--- Searching for: '{query}' ---")
    
    # Preprocess the query
    preprocessed_query = nlp_processor.preprocess_text(query)
    
    # Get TF-IDF vector for the query
    query_tf_idf_vector = nlp_processor.transform_text(preprocessed_query)
    
    # Get spaCy embedding for the query
    query_embedding = nlp_processor.get_document_embedding(query)

    all_indexed_documents = db_manager.get_all_documents()
    if not all_indexed_documents:
        print("No documents indexed yet. Please add documents first.")
        return

    results = []
    
    # Extract all document TF-IDF vectors and content for batch processing or comparison
    document_tf_idf_vectors = []
    document_contents = []
    for doc in all_indexed_documents:
        if doc.vector_representation is not None: # Ensure vector exists
            document_tf_idf_vectors.append(doc.vector_representation)
        document_contents.append(doc.content)

    # Calculate TF-IDF similarities in a batch
    # Make sure query_tf_idf_vector and document_tf_idf_vectors are compatible for calculate_cosine_similarity
    if document_tf_idf_vectors: # Only proceed if there are actual document vectors
        tf_idf_similarities = nlp_processor.calculate_cosine_similarity(query_tf_idf_vector, document_tf_idf_vectors)
    else:
        tf_idf_similarities = [0.0] * len(all_indexed_documents) # No TF-IDF if no vectors

    # Calculate semantic similarities
    # This part might be slightly slower as spaCy embeddings are generated one by one
    # or you could pre-calculate them if performance is critical for very large corpus.
    semantic_similarities = []
    for content in document_contents:
        doc_embedding = nlp_processor.get_document_embedding(content)
        semantic_similarities.append(nlp_processor.calculate_semantic_similarity(query_embedding, doc_embedding))


    for i, doc in enumerate(all_indexed_documents):
        try:
            tf_idf_sim = tf_idf_similarities[i]
            semantic_sim = semantic_similarities[i]

            # Combine similarities (simple weighted average, can be adjusted)
            # You might want to experiment with weights based on your data and desired behavior
            combined_similarity = (tf_idf_sim * 0.6) + (semantic_sim * 0.4) # Example weighting

            results.append({
                "filename": doc.filename,
                "title": doc.title,
                "tf_idf_similarity": tf_idf_sim,
                "semantic_similarity": semantic_sim,
                "combined_similarity": combined_similarity
            })
        except Exception as e:
            print(f"Error processing document '{doc.filename}': {e}")
            continue

    # Sort results by combined similarity in descending order
    results.sort(key=lambda x: x["combined_similarity"], reverse=True)

    if results:
        print("\nSearch Results:")
        for res in results[:5]: # Display top 5 results
            print(f"- Title: {res['title']} (TF-IDF Sim: {res['tf_idf_similarity']:.4f}, Semantic Sim: {res['semantic_similarity']:.4f}, Combined Sim: {res['combined_similarity']:.4f})")
    else:
        print("No relevant documents found.")


if __name__ == "__main__":
    db_manager = DBManager()
    nlp_processor = NLPProcessor()

    # --- Step 1: Add Sample Documents ---
    # Create some dummy text files in data/sample_documents/
    sample_docs_folder = "data/sample_documents"
    if not os.path.exists(sample_docs_folder):
        os.makedirs(sample_docs_folder)
        print(f"Created folder: {sample_docs_folder}. Please put some .txt files here.")
        # Create some dummy files for demonstration if the folder was just created
        with open(os.path.join(sample_docs_folder, "nlp_basics.txt"), "w", encoding="utf-8") as f:
            f.write("Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and human language.")
        with open(os.path.join(sample_docs_folder, "machine_learning_overview.txt"), "w", encoding="utf-8") as f:
            f.write("Machine learning is a subfield of artificial intelligence that involves training algorithms to learn from data and make predictions or decisions without being explicitly programmed.")
        with open(os.path.join(sample_docs_folder, "data_science_trends.txt"), "w", encoding="utf-8") as f:
            f.write("Data science combines various fields, including statistics, computer science, and domain expertise, to extract knowledge and insights from structured and unstructured data.")
        with open(os.path.join(sample_docs_folder, "cybersecurity_fundamentals.txt"), "w", encoding="utf-8") as f:
            f.write("Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks.")
        print("Sample documents created in 'data/sample_documents/'.")


    documents_to_index = load_documents_from_folder(sample_docs_folder)
    if documents_to_index:
        index_documents(db_manager, nlp_processor, documents_to_index)
    else:
        print("No documents found in 'data/sample_documents/'. Please add some text files.")

    # --- Step 2: Perform Searches ---
    while True:
        query = input("\nEnter your search query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        if query:
            search_documents(db_manager, nlp_processor, query)
        else:
            print("Query cannot be empty.")

    db_manager.close()
    print("Application closed.")