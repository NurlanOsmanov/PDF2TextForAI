from enum import Enum

class dictionary:
    word:str
    type:str
    origin:str
    explanation:str

    def __init__():
        pass
    def __init__(self, word:str = "", type:str = "", origin:str = "", explanation:str = ""):
        self.word = word
        self.type = type
        self.origin = origin
        self.explanation = explanation

    def __str__(self):
        return f"{self.id}: {self.word} - [{self.type} {self.origin}] - {self.explanation}"
    

class WordType(Enum):
    isim = "is."
    sifet = "sif."
    fel = "f."
    feli_isim = "f.is."
    feli_sifet = "f.sif."
    mechul_fel = "məch."
    sira_say = "sıra s."
    zerf = "(z.)"
    miqdar_sayi = "miqd. s."
    nida = "nida."
    baglayici = "bağl."
    edat = "əd."
    əvəzlik = "əvəz."
    tesirli_fel = "t-li."
    tesirsiz_fel = "t-siz."
    
class WordOrgin(Enum):
    azərbaycanca = "az."
    almanca = "alm."
    ingilisce = "ing."
    cigatayca = "cıgat."
    farsca = "fars."
    rusca = "rus."
    erebce = "ər."
    cince = "çin."
    fransizca = "fr."
    hollandca = "holl."
    ispanca = "isp."
    italyanca = "ital."
    qazaxca = "qazax."
    latinca = "lat."
    macarca = "mac."
    yunanca = "yun."
    monqolca = "monq."
    ozbekce = "özb."
    polyakca = "pol."
    sanksritce = "sanskr."
    skandinavca = "skand."
    tatarca = "tat."
    turkce = "türk."
    ukraynaca = "ukr."
    yehudice = "yəh."