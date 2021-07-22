Oshi = {
    "nama" : "Anin",
    "why" : "lucu,tentu jelas cantik"
}
print ("pacar saya adalh %s" % Oshi["nama"])
print ("Karena %s" % Oshi["why"])

for key in Oshi:
    print(Oshi[key])

for key, val in Oshi.items():
    print("%s : %s" % (key, val))