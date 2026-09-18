import chromadb
from chromadb.utils import embedding_functions
from datasets import load_dataset
import os

def preparer_base_poc():
    CHEMIN_DB = os.path.join(os.getcwd(), "chroma_db")
    chroma_client = chromadb.PersistentClient(path=CHEMIN_DB)

    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    collection = chroma_client.get_or_create_collection(
        name="jurisprudence_poc",
        embedding_function=emb_fn
    )
    dataset = load_dataset("antoinejeannot/jurisprudence", split="cour_de_cassation[:50]")

    textes = [str(texte) for texte in dataset['text']]
    ids = [f"cas_{i}" for i in range(len(textes))]

    collection.add(documents=textes, ids=ids)

if __name__ == "__main__":
    preparer_base_poc()