while True:
    meme_dict = {
                "CRINGE": "Algo vergonhoso ou constrangedor",
                "STALKEAR": "Investigar a vida de alguém online",
                "VDD": "Abreviação da palavra verdade",
                "HATER": "Pessoa que está constantemente criticando os outros",
                "VLW": "Abreviação da palavra valeu",
                "PPRT": "Abreviação da gíria papo reto",
                "QND": "Abreviação da palavra quando",
                "ATT": "Abreviação da palavra ata",
                "SLK": "Abreviação da palavra seloko",
                "PDC": "Abreviação da palavra pode crer",
                "NGM": "Abreviação da palavra ninguém"
                }
    
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Desculpe, não temos essa palavra no nosso dicionário")
