def ihk_prozent_wertcalc(erreichtenPunkte : int , moeglichenPunkte : int):
    typeCheck = isinstance(erreichtenPunkte, int) and isinstance(moeglichenPunkte , int )
    valueCheck1 = erreichtenPunkte < moeglichenPunkte 
    valueCheck2 = erreichtenPunkte > 0
    valueCheck3 = moeglichenPunkte > 0
    if typeCheck and valueCheck3 and valueCheck1 and valueCheck2:
        prozent : int = erreichtenPunkte * 100 / moeglichenPunkte
        print(prozent)
        return prozent
    if typeCheck == False:
        raise TypeError
    else:
        raise ValueError
    
def ihk_noten_schriftlich(prozent):
    if type(prozent) != int:
        raise TypeError
    if prozent > 100:
        raise ValueError
    else:
        if 92 <= prozent <= 100:
            print("sehr gut")
            return "sehr gut"
        if  81 <= prozent <= 91:
            print("gut")
            return "gut"
        if  67 <= prozent <= 80:
            print("befriedigend")
            return "befriedigend"
        if 50<= prozent <=66:
            print("ausreichend")
            return "ausreichend"
        if 31 <= prozent <= 49:
            print("mangelhaft")
            return "mangelhaft"
        if 0 <= prozent <=29:
            print("ungenügend")
            return "ungenügend"
        