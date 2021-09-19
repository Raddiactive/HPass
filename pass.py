import hashlib
import pandas as pd
import ast
username = "Rad"
password = "admin"

df = pd.read_csv('uid.csv',delimiter=",")
for i in range(len(df)):
    user = df.iloc[i,1]
    if user == username:
        salt = df.iloc[i,2]
        salt = ast.literal_eval(salt)
        key = df.iloc[i,3]
        new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        if ast.literal_eval(key) == new_key:
            print("Contraseña y usuarios correctos.")
        else: print("Contraseña incorrecta.")
    else: print("Usario incorrecto.")
