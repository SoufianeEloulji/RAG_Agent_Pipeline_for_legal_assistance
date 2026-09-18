from crewai import Task
from crewai_agents import extracteur, analyste_rag, redacteur

tache_1 = Task(
    description="Lis ce litige : '{litige}'. Extrais une phrase de recherche courte contenant uniquement les concepts juridiques clés.",
    expected_output="Une phrase de recherche contenant 3 à 5 mots-clés juridiques.",
    agent=extracteur
)

tache_2 = Task(
    description="Prends les mots-clés de l'Extracteur et utilise l'outil 'recherche_jurisprudence_vectorielle' pour trouver des cas. Retourne le texte brut des cas trouvés.",
    expected_output="Le texte complet des jurisprudences trouvées dans la base de données.",
    agent=analyste_rag

)

tache_3 = Task(
    description="Prends les jurisprudences trouvées par l'Analyste. Rédige une synthèse avec 3 parties : 1) Les Faits, 2) Les Précédents (cite les cas), 3) Les chances de succès. RÈGLE STRICTE : N'invente aucun article de loi. Si un détail n'est pas dans les cas fournis, dis que tu ne sais pas.",
    expected_output="Une note de synthèse juridique structurée en markdown.",
    agent=redacteur
)