import enum

class dictionary:
    id:int
    word:str
    type:str
    origin:str
    explanation:str

    def __init__(self, id:int, word:str, type:str, origin:str, explanation:str):
        self.id = id
        self.word = word
        self.type = type
        self.origin = origin
        self.explanation = explanation

    def __str__(self):
        return f"{self.id}: {self.word} - [{self.type} {self.origin}] - {self.explanation}"
    

class Type(enum):
    isim = "is"
    sifet = "sif"
    fel = "f"
    feli_isim = "f.is"
    feli_sifet = "f.sif"
    mechul_fel = "məch"
    sira_say = "sıra s"
    zerf = "(z.)"
    miqdar_sayi = "miqd. s"