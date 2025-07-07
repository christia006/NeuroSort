# NeuroSort/core/nlp_processor.py

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils.config import SPACY_MODEL

class NLPProcessor:
    def __init__(self):
        try:
            self.nlp = spacy.load(SPACY_MODEL)
            # Pastikan stop_words diakses dengan benar dari model yang dimuat
            self.stop_words = self.nlp.Defaults.stop_words
            self.vectorizer = TfidfVectorizer()
            # self.document_vectors = {} # Ini tidak lagi diperlukan karena vektor disimpan di DB
        except OSError:
            print(f"Error: spaCy model '{SPACY_MODEL}' not found. Please run 'python -m spacy download {SPACY_MODEL}'")
            exit()
        except Exception as e:
            print(f"An error occurred during NLPProcessor initialization: {e}")
            exit()

    def preprocess_text(self, text):
        """Tokenize, lemmatize, and remove stop words."""
        if not text:
            return ""
        doc = self.nlp(text.lower())
        # Filter out punctuation, numbers, and stopwords
        tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        return " ".join(tokens)

    def fit_vectorizer(self, corpus):
        """Fits the TF-IDF vectorizer to a corpus of preprocessed texts."""
        if not corpus:
            print("Warning: Empty corpus provided to TF-IDF vectorizer.")
            return
        self.vectorizer.fit(corpus)

    def transform_text(self, text):
        """Transforms a single preprocessed text into its TF-IDF vector."""
        if not hasattr(self.vectorizer, 'vocabulary_') or not self.vectorizer.vocabulary_:
            # Fallback for empty vocabulary, though fit_vectorizer should handle it
            print("Warning: TF-IDF vectorizer has no vocabulary. Returning empty vector.")
            return np.array([])
        
        # Ensure text is in a list format for transformation
        transformed_vector = self.vectorizer.transform([text])
        # Convert sparse matrix to dense array for easier handling (and JSON serialization)
        return transformed_vector.toarray()[0] # [0] because transform returns a 2D array for a single document

    def calculate_cosine_similarity(self, query_vector, document_vectors):
        """Calculates cosine similarity between query vector and multiple document vectors."""
        if query_vector.ndim == 1:
            query_vector = query_vector.reshape(1, -1) # Reshape to 2D for cosine_similarity

        # Ensure document_vectors is a list of 2D arrays or single 2D array
        if isinstance(document_vectors, list):
            doc_vecs_reshaped = [vec.reshape(1, -1) if vec.ndim == 1 else vec for vec in document_vectors]
            # Concatenate if multiple, otherwise keep as single
            if len(doc_vecs_reshaped) > 0:
                doc_vectors_array = np.vstack(doc_vecs_reshaped)
            else:
                return np.array([0.0]) # No documents to compare against
        else: # Single document vector
            doc_vectors_array = document_vectors.reshape(1, -1) if document_vectors.ndim == 1 else document_vectors

        if query_vector.shape[1] != doc_vectors_array.shape[1]:
            # This can happen if the query contains words not in the training corpus
            # or vice-versa. Pad with zeros to match dimensions.
            # A more robust solution might involve re-fitting the vectorizer
            # or using a fixed vocabulary if the corpus is stable.
            max_dim = max(query_vector.shape[1], doc_vectors_array.shape[1])
            if query_vector.shape[1] < max_dim:
                pad_width = ((0, 0), (0, max_dim - query_vector.shape[1]))
                query_vector = np.pad(query_vector, pad_width, 'constant')
            if doc_vectors_array.shape[1] < max_dim:
                pad_width = ((0, 0), (0, max_dim - doc_vectors_array.shape[1]))
                doc_vectors_array = np.pad(doc_vectors_array, pad_width, 'constant')
        
        if query_vector.shape[1] == 0 or doc_vectors_array.shape[1] == 0:
            return np.array([0.0]) # Handle cases where vectors are empty

        similarities = cosine_similarity(query_vector, doc_vectors_array)
        return similarities[0] # Return the first (and only) row of similarities

    def get_document_embedding(self, text):
        """Generates a spaCy document embedding (vector) for semantic similarity."""
        if not text:
            return np.zeros(self.nlp.vocab.vectors.shape[1]) # Return a zero vector for empty text
        return self.nlp(text).vector

    def calculate_semantic_similarity(self, query_embedding, document_embedding):
        """Calculates semantic similarity between query and document embeddings."""
        # Handle zero vectors to prevent division by zero
        if np.linalg.norm(query_embedding) == 0 or np.linalg.norm(document_embedding) == 0:
            return 0.0
        return query_embedding.dot(document_embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(document_embedding))