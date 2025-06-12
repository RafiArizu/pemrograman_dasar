def main():
    print(f"\n{"="*12} SELAMAT DATANG DI MENU VOTING {"="*12}")
    print(f"\n{" "*12} SILAHKAN PILIH KANDIDAT {" "*12}")
    print(f"\n{"-"*21}| Kandidat |{"-"*21}")
    print("-"*50)
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","No","|", "Pilihan Kandidat", "|"))
    print("-"*50)
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","1","|", "Jean", "|"))
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","2","|", "Kevin", "|"))
    print("{:<0} {:<5} {:<0} {:<38} {:<0}".format("|","3","|", "Agus", "|"))
    print("-"*50)

def pilihan_kandidat():
    while True:        
        pilihan = input("Masukan Pilihan Anda: ")
        if pilihan == "1":
            print("Anda Memilih Jean")
            break
        elif pilihan == "2":
            print("Anda Memilih Kevin")
            break
        elif pilihan == "3":
            print("Anda Memilih Kevin")
            break
        else:
            print("Silahkan Masukan Pilihan Yang Benar")

main()
pilihan_kandidat()
