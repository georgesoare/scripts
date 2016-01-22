import os
import xml.etree.ElementTree as ET


PATH = "."
out_path = os.path.join(PATH, "checked.txt")
out = open(out_path, "w", encoding="utf-8")


files = []
for name in os.listdir(PATH):
    if name.endswith(".xml"):
        files.append(name)


types = ["admirație", "apreciere", "atașament", "curiozitate", "satisfacție", "enervare", "dispreț", "neplăcere", "amuzament", "neliniște", "incertitudine"]
types.sort()


msg = '---------------------------------------------\n'
msg +='Atentie! Tagul "type" trebuie sa contina: '
for a in types:
    msg += '\n- ' + str(a) + ' '
msg += '\n---------------------------------------------'
msg += '\n\n\n'
out.write(msg)


def check_file(file_name):
    global types
    s = "Numele fisierului: " + file_name + "\n"
    out.write(s)
    ok = 1
    tree = ET.parse(file_name)
    root = tree.getroot()
    wrong_type = []
    for EM in root.iter('EM'):
        t = EM.get('type')
        if t not in types:
            ok = 0
            wrong_type.append(t)

    s = ''

    if ok is 1:
        s = '\tFisierul este OK!'
    elif ok is 0:
        s += '\tType scris gresit:\n'
        for i in wrong_type:
            s += '\t\ttype="' + str(i) + '"\n'

    out.write(s)
    out.write("\n\n\n")


for file_name in files:
    check_file(os.path.join(PATH, file_name))