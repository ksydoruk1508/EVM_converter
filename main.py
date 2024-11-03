from eth_account import Account
from eth_utils import to_checksum_address
import os

# Убедитесь, что приватный ключ или мнемоника не хранятся в виде строки в коде
# Задача 1: Приватный ключ -> Мнемоника, Адрес

def private_key_to_mnemonic_and_address(private_key):
    account = Account.from_key(private_key)
    mnemonic = Account.encrypt(private_key, os.urandom(16))['mnemonic']
    address = to_checksum_address(account.address)
    return mnemonic, address

# Задача 2: Мнемоника -> Приватный ключ, Адрес

def mnemonic_to_private_key_and_address(mnemonic):
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic)
    private_key = account.key.hex()
    address = to_checksum_address(account.address)
    return private_key, address

if __name__ == "__main__":
    while True:
        print("Выберите опцию:")
        print("1. Приватный ключ -> Мнемоника и номер кошелька")
        print("2. Мнемоника -> Приватный ключ и номер кошелька")
        print("3. Выйти")
        option = input("Введите номер опции: ")

        if option == '1':
            try:
                with open('private_keys.txt', 'r') as file:
                    private_keys = file.readlines()
                for private_key in private_keys:
                    private_key = private_key.strip()
                    mnemonic, address = private_key_to_mnemonic_and_address(private_key)
                    print(f"Приватный ключ: {private_key}")
                    print(f"Мнемоника: {mnemonic}")
                    print(f"Адрес: {address}\n")
            except Exception as e:
                print(f"Ошибка: {str(e)}")

        elif option == '2':
            try:
                with open('mnemonics.txt', 'r') as file:
                    mnemonics = file.readlines()
                for mnemonic in mnemonics:
                    mnemonic = mnemonic.strip()
                    private_key, address = mnemonic_to_private_key_and_address(mnemonic)
                    print(f"Мнемоника: {mnemonic}")
                    print(f"Приватный ключ: {private_key}")
                    print(f"Адрес: {address}\n")
            except Exception as e:
                print(f"Ошибка: {str(e)}")

        elif option == '3':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
