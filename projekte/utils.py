def getPercent(p):
    p.prozent = (p.spenden / p.ziel) * 100
    if p.prozent == 100:
        p.order = 2
    else:
        p.order = 1
    return p
