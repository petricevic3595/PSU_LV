try:
    x=float(input("Unesite ocjenu od 0.0 do 1.0"))
    if x<0.0 or x > 1.0:
        print("Pogresan unos ")
    else:
        if x >= 0.9 :
            print("Ocjena je A")
        elif x>= 0.8 :
            print("Ocjena je B")
        elif x>= 0.7 : 
            print("Ocjena je C")
        elif x>= 0.6 :
            print("Ocjena je D")
        elif x < 0.6 :
            print("Ocjena je F")

except:
    print("Pogreska prilikom unosa")
