import random

def trekke_vinnertall():
    vinnertall = random.sample(range(1, 35), 7)
    vinnertall.sort()
    tilleggstall = random.choice(range(1, 35))
    return vinnertall, tilleggstall

vinnertall, tilleggstall = trekke_vinnertall()
print("Vinnertall: ", vinnertall)
print("Tilleggstall: ", tilleggstall)

def sjekk_lottokupong(kupong, vinnertall, tilleggstall):
    riktige_tall = len(set(kupong).intersection(vinnertall))
    har_tilleggstall = tilleggstall in kupong
    
    if riktige_tall == 7 and har_tilleggstall:
        return "Gratulerer! Du har vunnet førstepremien!"
    elif riktige_tall == 7:
        return "Du har 7 riktige tall uten tilleggstall og har vunnet andrepremien!"
    elif riktige_tall == 6 and har_tilleggstall:
        return "Du har 6 riktige tall pluss tilleggstall og har vunnet tredjepremien!"
    elif riktige_tall == 6:
        return "Du har 6 riktige tall uten tilleggstall og har vunnet fjerdepremien!"
    elif riktige_tall == 5:
        return "Du har 5 riktige tall og har vunnet femtepremien!"
    elif riktige_tall == 4:
        return "Du har 4 riktige tall og har vunnet sjettepremien!"
    elif riktige_tall == 3:
        return "Du har 3 riktige tall og har vunnet syvendepremien!"
    else:
        return "Dessverre, ingen gevinster denne gangen."

# Eksempelkupong
min_kupong = [2, 5, 11, 17, 20, 28, 33]





resultat = sjekk_lottokupong(min_kupong, vinnertall, tilleggstall)
print("Resultat for din kupong:", resultat)




def generer_lottorekker(antall_rekker, antall_tall=7, min_verdi=1, max_verdi=34):
    lottorekker = []

    for _ in range(antall_rekker):
        rekke = random.sample(range(min_verdi, max_verdi + 1), antall_tall)
        rekke.sort()
        lottorekker.append(rekke)

    return lottorekker

antall_rekker = int(input("Hvor mange lottorekker vil du generere? "))

lottorekker = generer_lottorekker(antall_rekker)

for i, rekke in enumerate(lottorekker, 1):
    print(f"Rekke {i}: {rekke}")
