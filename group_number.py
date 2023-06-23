def a_group_number(number):
    try:
        word="からグループワークが始まります"
        number = int(number)
        if 0<number<23:
            hour=13
            minute=30
            times=str(hour)+":"+str(minute)
            zyu_tims=times+word
            return zyu_tims,hour,minute
        if 22<number<43:
            hour=14
            minute=20
            times=str(hour)+":"+str(minute)
            zyu_tims=times+word
            return zyu_tims,hour,minute
        if 42<number<63:
            hour=15
            minute=10
            times=str(hour)+":"+str(minute)
            zyu_tims=times+word
            return zyu_tims,hour,minute
        else:
            zyu_tims="入力された数値に誤りがあります"
            hour=0
            minute=0
            return zyu_tims,hour,minute
    except ValueError:
        zyu_tims=""
        hour=""
        minute=""
        return zyu_tims,hour,minute
def d_group_number(number):
    try:
        word="からグループワークが始まります"
        number = int(number)
        if 0<number<23:
            hour=13
            minute=30
            times=str(hour)+":"+str(minute)
            zyu_tims=times+word
            return zyu_tims,hour,minute
        if 22<number<43:
            hour=14
            minute=20
            times=str(hour)+":"+str(minute)
            zyu_tims=times+word
            return zyu_tims,hour,minute
        if 42<number<63:
            hour=15
            minute=10
            times=str(hour)+":"+str(minute)
            zyu_tims=times+word
            return zyu_tims,hour,minute
        else:
            zyu_tims="入力された数値に誤りがあります"
            hour=0
            minute=0
            return zyu_tims,hour,minute
    except ValueError:
        zyu_tims=""
        hour=""
        minute=""
        return zyu_tims,hour,minute