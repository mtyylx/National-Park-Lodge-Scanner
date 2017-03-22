from LodgeScanner import LodgeScanner

scanner = LodgeScanner()
print """
Please enter search info, separated by comma:
Format: PARK,YEAR,MONTH,DAY,METHOD
PARK:
    Grand Canyon = gc
    Crater Lake = cl
    Zion Park = zp
    Glacier Park = gp
METHOD:
    PhantomJS = p   (Headless Browser)
    Chrome = c      (Normal Browser)

Example:
    gc,2017,4,9,p
    zp,2017,4,3,c
"""
r = raw_input(">>> Enter Here: ")
if r is not "":
    r = r.split(",")
    scanner.config(r[0], r[1], r[2], r[3], r[4])
scanner.run()
