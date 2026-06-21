meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHHESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek / Sinirlenmek",
            "ASAP": "Mümkün olan en kısa sürede",
            "BTW": "Bu arada"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
