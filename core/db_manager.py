# NeuroSort/core/db_manager.py

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
import json
import numpy as np 

from utils.config import DATABASE

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True, nullable=False)
    title = Column(String)
    content = Column(Text, nullable=False)
    
    vector_representation = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Document(filename='{self.filename}', title='{self.title}')>"

class DBManager:
    def __init__(self):
        db_url = (
            f"postgresql://{DATABASE['USER']}:{DATABASE['PASSWORD']}@"
            f"{DATABASE['HOST']}:{DATABASE['PORT']}/{DATABASE['NAME']}"
        )
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.create_tables()

    def create_tables(self):
        # Base.metadata.drop_all(self.engine) 
        Base.metadata.create_all(self.engine)
        print("Database tables created or already exist.")

    def add_document(self, filename, title, content, vector_representation):
        session = self.Session()
        try:
          
            vector_json_str = json.dumps(vector_representation.tolist()) if isinstance(vector_representation, np.ndarray) else vector_representation
            
            document = Document(
                filename=filename,
                title=title,
                content=content,
                vector_representation=vector_json_str
            )
            session.add(document)
            session.commit()
            print(f"Document '{filename}' added successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error adding document '{filename}': {e}")
        finally:
            session.close()

    def get_all_documents(self):
        session = self.Session()
        try:
            documents = session.query(Document).all()
       
            for doc in documents:
                if doc.vector_representation:
                    doc.vector_representation = np.array(json.loads(doc.vector_representation))
            return documents
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
        finally:
            session.close()

    def get_document_by_filename(self, filename):
        session = self.Session()
        try:
            document = session.query(Document).filter_by(filename=filename).first()
            if document and document.vector_representation:
                document.vector_representation = np.array(json.loads(document.vector_representation))
            return document
        except Exception as e:
            print(f"Error retrieving document '{filename}': {e}")
            return None
        finally:
            session.close()

    def update_document_vector(self, filename, new_vector_representation):
        session = self.Session()
        try:
            document = session.query(Document).filter_by(filename=filename).first()
            if document:
                vector_json_str = json.dumps(new_vector_representation.tolist()) if isinstance(new_vector_representation, np.ndarray) else new_vector_representation
                document.vector_representation = vector_json_str
                session.commit()
                print(f"Vector for '{filename}' updated successfully.")
            else:
                print(f"Document '{filename}' not found.")
        except Exception as e:
            session.rollback()
            print(f"Error updating vector for '{filename}': {e}")
        finally:
            session.close()

    def close(self):
        self.engine.dispose()
        print("Database connection closed.")