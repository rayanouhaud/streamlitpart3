import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

#lesDonneesDesComptes = {
#    'usernames': {
#        'utilisateur': {
#            'name': 'utilisateur',
#            'password': 'utilisateurMDP',
#            'email': 'utilisateur@gmail.com',
#            'failed_login_attemps': 0,  # Sera géré automatiquement
#            'logged_in': False,          # Sera géré automatiquement
#            'role': 'utilisateur'
#        },
#        'root': {
#            'name': 'root',
#            'password': 'rootMDP',
#            'email': 'admin@gmail.com',
#            'failed_login_attemps': 0,  # Sera géré automatiquement
#            'logged_in': False,          # Sera géré automatiquement
#            'role': 'administrateur'
#        }
#    }
#}

df = pd.read_csv("login.csv")

dataUser = {"usernames": {}}
for _, row in df.iterrows():
    dataUser["usernames"][row["name"]] = {
        "name": row["name"],
        "password": row["password"],
        "email": row["email"],
        "role": row["role"],
        "failed_login_attemps": row["failed_login_attemps"],
        "logged_in": row["logged_in"]
    }
authenticator = Authenticate(
    dataUser,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue {st.session_state['name']}")
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Les photos de mon chat"],
            icons=['house', 'list-task', 'person']
        )
    if selection == "Accueil":
        st.title("Bienvenue sur ma page")
    if selection == "Les photos de mon chat":
        st.title("Bienvenue dans l'album de mon chat")
        st.image(["chat1.jpg", "chat2.jpg", "chat3.jpg"], width=200)


if st.session_state["authentication_status"]:
  accueil()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')