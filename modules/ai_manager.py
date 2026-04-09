from groq import Groq

client = Groq(
    api_key="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"
)

def ai_play(tableau):
    prompt = f"""
        Tu joues au morpion (tic-tac-toe).

        Voici le plateau actuel :
        {tableau}

        Les cases sont nommées comme ceci :
        A1 A2 A3
        B1 B2 B3
        C1 C2 C3

        Règles :
        - Tu dois choisir la MEILLEURE case pour gagner ou empêcher l'adversaire de gagner.
        - Réponds uniquement avec UNE case valide (ex: A1, B3, C2).
        - Ne mets RIEN d'autre dans ta réponse.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    coup = response.choices[0].message.content
    if coup is None:
        coup = ""
    else:
        coup = coup.strip()

    return coup