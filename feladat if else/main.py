zoldsegleves: bool= False
husleves: bool= False
gyumolcsleves: bool= False
sultcsirkecomb: bool= False
sultCsirkemell: bool= False
rakottzoldseg: bool= False
spagetti: bool= False
pizza: bool= False
rizs: bool= False
paroltzoldseg: bool= False
gyumolcs: bool= False
sultkrumpli: bool= False
salata: bool= False
kola: bool= False
eloetel: int=None
foetel: int=None
koret: int=None
ertekeles: str=None
menu: str="A mai menü: "

print("Előételek\n1-Zöldségleves\n2-Húsleves\n3-Gyümöcsleves\nMit választ: ")
eloetel=int(input())

print("Főétel\n1-Sültcsirkecomb\n2-Sült csirkemell\n3-Rakottzöldség\n4-Spagetti\n5-Pizza\nMit választ: ")
foetel=int(input())

print("Köret\n1-Rizs\n2-Pároltzöldség\n3-Gyümölcs\n4-Sültkrumpli\n5-Saláta\n6-Kóla\nMit választ: ")
koret=int(input())

if(eloetel == 1):
    menu += "zöldségleves, "
    zoldsegleves=True
elif(eloetel == 2):
    menu += "húsleves, "
    husleves=True
else:
    menu += "gyümölcsleves, "
    gyumolcsleves=True



if(foetel == 1):
    menu += "sültcsirkecomb, "
    sultcsirkecomb=True
elif(foetel == 2):
    menu += "sült csirkemell, "
    sultCsirkemell=True
elif(foetel == 3):
    menu += "rakottzöldség, "
    rakottzoldseg=True
elif(foetel == 4):
    menu += "spagetti, "
    spagetti=True
else:
    menu += "pizza, "
    pizza=True



if(koret == 1):
    menu += "rizs, "
    rizs=True
elif(koret == 2):
    menu += "pároltzöldség, "
    paroltzoldseg=True
elif(koret == 3):
    menu += "gyümölcs, "
    gyumolcs=True
elif(koret == 4):
    menu += "sültkrumpli, "
    sultkrumpli=True
elif(koret == 5):
    menu += "saláta, "
    salata=True
else:
    menu += "kóla"
    kola=True

if(eloetel != None and foetel !=None and koret !=None and zoldsegleves and spagetti and gyumolcs or salata and not pizza and not rakottzoldseg):
    ertekeles= "A menü értékelése: Kiváló."
elif(zoldsegleves and sultCsirkemell and not sultkrumpli and rizs):
    ertekeles= "A menü értékelése: Fitnesz menü."
elif(husleves and sultcsirkecomb and sultkrumpli or salata and not pizza and not rakottzoldseg):
    ertekeles= "A menü értékelése: Vasárnapi menü."
elif(pizza or spagetti and gyumolcs and kola and not rakottzoldseg and not paroltzoldseg):
    ertekeles= "A menü értékelése: Napi menü."

print(menu)
print(ertekeles)