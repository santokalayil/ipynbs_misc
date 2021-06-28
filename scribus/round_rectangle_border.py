from scribus import *
print("Hi")


if newDocument(PAPER_A4, (10, 10, 10, 10), PORTRAIT, 1, UNIT_POINTS, NOFACINGPAGES, FIRSTPAGERIGHT, 1):
    print('New Doucment is here')
    spx=20
    spy=20		    # starting point of y axis
    wth=595         # A4 width in points
    dph=842         # Depth of frame - adjust to suit
    a=8             # Line width
    b="Black"       # add other colors as required
    b1="Blue"
    w="White"
    h = createRect(spx,spy,wth-2*spx,dph-2*spy)
    setCornerRadius(20, h)
    setLineWidth(8, h)
    setFillColor(w, h)
    setLineColor(b, h)
    saveDocAs("Border_2.sla") #Make sure this is writable
