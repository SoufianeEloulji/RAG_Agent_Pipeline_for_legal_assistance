import os
from crewai import Agent, LLM
from crewai.tools import tool
import chromadb
from chromadb.utils import embedding_functions
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI

print("Connexion au modèle local Bonsai...")

llm_bonsai = LLM(
    model="openai/bonsai", 
    base_url="http://127.0.0.1:1234/v1", 
    api_key="aucune-cle-necessaire", 
    temperature=0.0 
)



@tool("recherche_jurisprudence_vectorielle")
def recherche_jurisprudence(requete: str = "", properties: dict = None, **kwargs) -> str:
    """Utilise cet outil pour chercher des décisions de justice similaires dans la base de données vectorielle."""
 
    texte_recherche = requete
    if properties and "requete" in properties:
        texte_recherche = str(properties["requete"])
    elif not texte_recherche:
        texte_recherche = str(kwargs)

    chemin_db = os.path.join(os.getcwd(), "chroma_db")
    client = chromadb.PersistentClient(path=chemin_db)
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-MiniLM-L12-v2")
    collection = client.get_collection(name="jurisprudence_poc", embedding_function=emb_fn)

    resultats = collection.query(query_texts=[texte_recherche], n_results=2)
    
    if not resultats['documents'][0]:
        return "Aucune jurisprudence trouvée pour cette requête."
    docs_raccourcis = [doc[:600] + "... [TEXTE TRONQUÉ]" for doc in resultats['documents'][0]]
    return "\n\n--- NOUVEAU CAS ---\n\n".join(docs_raccourcis)


extracteur = Agent(
    role="Extracteur et Qualificateur Juridique",
    goal="Analyser le récit du client et extraire les concepts juridiques clés (mots-clés purs).",
    backstory="Tu es un expert en droit. Tu sais lire une histoire banale et en sortir les termes juridiques exacts pour faire une recherche.",
    llm=llm_bonsai,
    verbose=True,
    allow_delegation=False
)

analyste_rag = Agent(
    role="Analyste RAG",
    goal="Trouver des jurisprudences pertinentes sans halluciner de faux verdicts.",
    backstory="Spécialiste de la recherche juridique. Tu ne te bases QUE sur les résultats de ton outil de recherche vectorielle.",
    tools=[recherche_jurisprudence], 
    llm=llm_bonsai,
    verbose=True,
    allow_delegation=False
)

redacteur = Agent(
    role="Rédacteur de Synthèse Juridique",
    goal="Rédiger une note claire et stratégique pour l'avocat, basée EXCLUSIVEMENT sur les jurisprudences fournies.",
    backstory="Tu es un avocat senior. Tu détestes les hallucinations. Tu cites toujours tes sources et tu donnes un avis tranché sur les chances de succès.",
    llm=llm_bonsai,
    verbose=True,
    allow_delegation=False
)



