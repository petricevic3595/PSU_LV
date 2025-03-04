brojevi= []
print("Unesite brojeve te napisite 'done' kada ste gotovi")

while True:
    unos=input("Unesite broj ")
    if unos.lower() == "done":
        break
    try:
        broj=float(unos)
        brojevi.append(broj)
    except ValueError:
        print("Pogresan unos! Ponovite ili unesite 'done' za prekid")
    
if not brojevi : 
    print("Niste unijeli niti jedan broj")

else:
    brojac=len(brojevi)
    srednja=sum(brojevi)/brojac
    min=min(brojevi)
    max=max(brojevi)
    brojevi.sort()

    print("Korisnik je pohranio: ",brojac)
    print("Srednja vrijednost je: ",srednja)
    print("Najveca vrijednost je: ",max)
    print("Najmanja vrijednost je: ",min)
    print("Sortirana lista je: ",brojevi)
