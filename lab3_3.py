import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def preuzmi_podatke_pm10():
    adresa = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'
    odgovor = urllib.request.urlopen(adresa).read()
    return ET.fromstring(odgovor)

def obradi_pm10_podatke(xml_korijen):
    zapisi = []

    for zapis in xml_korijen:
        elementi = list(zapis)
        if len(elementi) >= 3:
            vrijednost = elementi[0].text
            vrijeme = elementi[2].text

            try:
                zapisi.append({
                    'vrijednost_pm10': float(vrijednost),
                    'vrijeme_mjerenja': vrijeme
                })
            except:
                continue

    tabela = pd.DataFrame(zapisi)
    tabela['vrijeme_mjerenja'] = pd.to_datetime(tabela['vrijeme_mjerenja'], utc=True)
    tabela['mjesec'] = tabela['vrijeme_mjerenja'].dt.month
    tabela['dan_u_sedmici'] = tabela['vrijeme_mjerenja'].dt.dayofweek

    return tabela

def prikazi_graf(tabela):
    tabela.plot(x='vrijeme_mjerenja', y='vrijednost_pm10', figsize=(12, 5))
    plt.title('PM10 koncentracija kroz 2017. godinu')
    plt.xlabel('Datum')
    plt.ylabel('PM10 (µg/m³)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tri_najgora_dana(tabela):
    najgori = tabela.sort_values('vrijednost_pm10', ascending=False)
    return najgori.head(3)

if __name__ == '__main__':
    korijen = preuzmi_podatke_pm10()
    podaci = obradi_pm10_podatke(korijen)
    prikazi_graf(podaci)
    
    print("Tri dana sa najvišim nivoom PM10 čestica:")
    print(tri_najgora_dana(podaci))
