import bcrypt

def criptografar(senha: str):
    """
    Criptografa a senha do usuário.

    Args:
        senha (str): Senha do usuário.

    Returns:
        hashed: hash da senha.
    """
    senha_bites = senha.encode("UTF-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bites, salt)
    return hashed

def checar_senha(senha: str, hashed):
    """
    Checa se a senha do usuário está criptografada na hora da autenticação.

    Args:
        senha (str): Senha do usuário.
        hashed: hash da senha

    Returns:
        Checa se a senha do usuário está criptografada na hora da autenticação.
    """
    senha_bites = senha.encode("UTF-8")
    return bcrypt.checkpw(senha_bites, hashed)