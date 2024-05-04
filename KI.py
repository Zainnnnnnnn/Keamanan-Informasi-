from cryptography.fernet import Fernet

def generate_key():
    """
    Generate kunci dan menyimpannya kedalam file
    """
    key = Fernet.generate_key()
    with open("kuncirahasia.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Mengambil kunci dari direktori saat ini bernama `kuncirahasia.key`
    """
    return open("kuncirahasia.key", "rb").read()

def encrypt_message(message, key):
    """
    Enkripsi kata-kata menggunakan kunci yang disediakan
    """
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    mendekripsi kata-kata yang terenkripsi mengunakan kunci yang disediakan.
    """
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate dan mengambil kunci
generate_key()
key = load_key()

# Contoh Penggunaan
message = "Faiq Pataya Zain"
encrypted_message = encrypt_message(message, key)
print("Pesan Terenkripsi:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Pesan Terdeskripsi:", decrypted_message)
