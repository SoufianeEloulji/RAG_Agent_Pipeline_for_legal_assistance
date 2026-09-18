from crewai_agents import extracteur, analyste_rag, redacteur
from crewai import Crew, Process
from tasks import tache_1, tache_2, tache_3 

crew_legal = Crew(
    agents=[extracteur, analyste_rag, redacteur],
    tasks=[tache_1, tache_2, tache_3],
    process=Process.sequential 
)

if __name__ == "__main__":
    print("Bienvenue dans votre assistant juridique IA (Propulsé par Bonsai & CrewAI).")
    print("Tapez 'quitter' à tout moment pour fermer le programme.\n")
    
    while True:

        litige_client = input("Décrivez le litige du client :\n> ")
        
        if litige_client.lower() in ['quitter', 'q', 'exit']:
            print("Fermeture de l'assistant. Au revoir !")
            break

        if not litige_client.strip():
            print("Veuillez décrire un litige valide.")
            continue
            
        print("\n Lancement de l'équipe d'agents... (Analyse en cours)")
        
        resultat_final = crew_legal.kickoff(inputs={"litige": litige_client})
        print("\n==========================================")
        print("NOTE DE SYNTHÈSE FINALE POUR L'AVOCAT")
        print("==========================================")
        print(resultat_final)
        print("\n------------------------------------------\n")