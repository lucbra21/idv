import streamlit_authenticator as stauth
from pathlib import Path
import pickle

names = ["Mauro Ceruti"]
usernames = ["mauroceruti"]
passwords = ["IDV2024"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
  pickle.dump(hashed_passwords, file)