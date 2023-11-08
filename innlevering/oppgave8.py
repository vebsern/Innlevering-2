
def fordel_spillere_i_biler(spillere, antall_biler, plasser_i_bil):
    spillere.sort(key=lambda x: len(x))
    return [spillere[i:i + plasser_i_bil] for i in range(0, len(spillere), plasser_i_bil)][:antall_biler]

spillere = ["Spiller 1", "Spiller 2", "Spiller 3", "Spiller 4", "Spiller 5", "Spiller 6"]
antall_biler = 2
plasser_i_bil = 3

biler = fordel_spillere_i_biler(spillere, antall_biler, plasser_i_bil)
print(biler)
