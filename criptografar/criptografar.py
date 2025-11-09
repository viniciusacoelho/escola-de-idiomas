import bcrypt

def criptografar(senha: str):
    senha_bites = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bites, salt)
    return hashed

def checar_senha(senha: str, hashed):
    senha_bites = senha.encode("utf-8")
    return bcrypt.checkpw(senha_bites, hashed)