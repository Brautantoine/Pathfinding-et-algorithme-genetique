#!usr/bin/env python

from ville import cVille

iut = cVille(48.787858,2.328314,"IUT_cachan")
flamanville = cVille(49.537207,-1.881484,"flamanville")

print "La distance IUT - flamanville est de:", str(iut.distance(flamanville))

