ukoly = []

def hlavni_menu():   
    while True:       
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4): ")
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
             zobrazit_ukoly()
        elif volba == "3":
             odstranit_ukol()
        elif volba == "4":
           print("Konec programu.")
           break
        else:
           print("Neplatná volba. Zkuste to znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue
        ukoly.append({"název": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def zobrazit_ukoly():   
    if not ukoly:
       print("Seznam úkolů je prázdný.")   
    else:
       print("Seznam úkolů:")
       for i, ukol in enumerate(ukoly, start=1):
           print(f"{i}. {ukol['název']} - {ukol['popis']}")

def odstranit_ukol():   
    zobrazit_ukoly() 
    if not ukoly:
       return
    
    while True:
        try:
            index = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= index <= len(ukoly):
              odstraneny = ukoly.pop(index - 1)
              print(f"Úkol '{odstraneny['název']}' byl odstraněn.")
              break
            else:
                print("Neplatné číslo. Zkuste to znovu.")
        except ValueError:
            print("Prosím, zadejte platné číslo.")

hlavni_menu()