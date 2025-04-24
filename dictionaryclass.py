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
    

class LexicalSuffix(Enum):
    ci0 = "çı"
    ci1 = "çi"
    cu0 = "çu"
    cu1 = "çü"
    liq0 = "lıq"
    lik0 = "lik"
    luq0 = "luq"
    luk0 = "lük"
    suz0 = "sız"
    suz1 = "siz"
    dar0 = "dar"
    dar1 = "dər"
    dash0 = "daş"
    vari0 = "varı"
    cik0 = "cıq"
    cik1 = "cik"
    cuq0 = "cuq"
    cuk0 = "cük"
    kimi0 = "kimi"
    ar0 = "ar"
    ek0 = "ək"
    im0 = "ım"
    inci0 = "inci"
    qan0 = "qan"
    qar0 = "qar"
    qaq0 = "qaq"
    gar0 = "gər"
    kar0 = "kar"
    per0 = "pər"
    ma0 = "ma"
    ma1 = "mə"
    il0 = "ıl"
    il1 = "il"
    il2 = "ul"
    il3 = "ül"
    is0 = "ış"
    is1 = "iş"
    is2 = "uş"
    is3 = "üş"
    las0 = "laş"
    las1 = "ləş"
    dır0 = "dır"
    dır1 = "dir"
    lan0 = "lan"
    lan1 = "lən"
    casina0 = "casına"
    casina1 = "cəsinə"
    xana0 = "xana"
    xana1 = "xanə"


class GrammaticalSuffix(Enum):
    maq0 = "maq"
    maq1 = "mək"
    lar0 = "lar"
    lar1 = "lər"
    in0 = "ın"
    in1 = "in"
    in2 = "un"
    in3 = "ün"
    da0 = "da"
    da1 = "də"
    dan0 = "dan"
    dan1 = "dən"
    a0 = "a"
    a1 = "ə"
    ya0 = "ya"
    ya1 = "yə"
    ni0 = "nı"
    ni1 = "ni"
    ni2 = "nu"
    ni3 = "nü"
    mi0 = "mı"
    mi1 = "mi"
    mi2 = "mu"
    mi3 = "mü"
    ki0 = "ki"
    la0 = "la"
    la1 = "lə"
    n0 = "n"
    m0 = "m"
    s0 = "s"

    