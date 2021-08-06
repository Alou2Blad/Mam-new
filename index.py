prop_GC=(4500 + 2575) / 14800
print("prop GC(2 deci.) = {0:.2f}, prop GC(3 deci.) = {0:.3f}".format(prop_GC))

# print("{:0>6d}".format(10)) ; print("{:0>6d}".format(1000))

nb_G = 4500
nb_C = 2575
print("Ce génome contient {:d} G et {:d} C, soit une prop de GC de {:.2f}" \
    .format(nb_G ,nb_C , prop_GC))
perc_GC = prop_GC * 100
print ("ce génome contient {:d} G et {:d} de C, soit un %GC de {:.2f} %" \
    .format(nb_G ,nb_C , perc_GC))
print("{:7.3f}".format(perc_GC))
print("{:10.3f}".format(perc_GC))

print("{:e}".format(1_000_000_000))
print("{:e}".format(0.000_000_001))

avogadro_number = 6.022_140_76e23
print("{:.0e}".format(avogadro_number))
print("{:.3e}".format(avogadro_number))
print("{:.6e}".format(avogadro_number))


#code deux version du prog

nb_G = 4500
nb_C = 2575
print("Ce génome contient {:d} G et {:d} C, soit une prop de GC de {:.2f}" \
    .format(nb_G ,nb_C , prop_GC))
perc_GC = prop_GC * 100
print ("ce génome contient {:d} G et {:d} de C, soit un %GC de {:.2f} %" \
    .format(nb_G ,nb_C , perc_GC))
print("{:7.3f}".format(perc_GC))
print("{:10.3f}".format(perc_GC))

print("{:e}".format(1_000_000_000))
print("{:e}".format(0.000_000_001))

avogadro_number = 6.022_140_76e23
print("{:.0e}".format(avogadro_number))
print("{:.3e}".format(avogadro_number))
print("{:.6e}".format(avogadro_number))