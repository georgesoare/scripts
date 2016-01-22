import argparse
import os
import xml.etree.ElementTree as ET


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Default path is current directory")
args = vars(parser.parse_args())


PATH = "."
if args["path"]:
    PATH = args["path"]

out_path = os.path.join(PATH,"stats.txt")
out = open(out_path, "w", encoding="utf-8")

files = []
for name in os.listdir(PATH):
    if name.endswith(".xml"):
        files.append(name)

total_em = 0
total_words = 0
total_sentences = 0
total_type = {}


def print_stats(file_name):
    global total_em, total_type, total_words, total_sentences
    s = "Numele fisierului: " + file_name + "\n"
    out.write(s)
    em_count = 0
    words_count = 0
    sentence_count = 0
    type_count = {}
    tree = ET.parse(file_name)
    root = tree.getroot()

    for w in root.iter('Word'):
        words_count += 1
    total_words += words_count

    for sen in root.iter('Sentence'):
        sentence_count += 1
    total_sentences += sentence_count

    for EM in root.iter('EM'):
        em_count += 1
        t = EM.get('type')
        if t in type_count:
            type_count[t] += 1
        else:
            type_count[t] = 1

    total_em += em_count
    s = "\tNumarul de propozitii: " + str(sentence_count) + "\n"
    out.write(s)
    s = "\tNumarul de cuvinte: " + str(words_count) + "\n"
    out.write(s)
    s = "\tNumarul de EM: " + str(em_count) + "\n"
    out.write(s)
    out.write("\tEmotii:\n")

    for x in type_count:
        name = x
        value = type_count[x]
        if x in total_type:
            total_type[x] += type_count[x]
        else:
            total_type[x] = type_count[x]
        s = '\t\t"' + name + '": ' + str(value) + "\n"
        out.write(s)
    out.write("\n\n")


for file_name in files:
    print_stats(os.path.join(PATH, file_name))

s = "\n\nNumarul total de propozitii: " + str(total_sentences) + "\n"
out.write(s)
s = "Numarul total de cuvinte: " + str(total_words) + "\n"
out.write(s)
s = "Numarul total de EM: " + str(total_em) + "\n"
out.write(s)
out.write("Numarul total de emotii:\n")

for i in total_type:
    name = i
    value = total_type[i]
    s = '\tTotal "' + name + '": ' + str(value) + "\n"
    out.write(s)