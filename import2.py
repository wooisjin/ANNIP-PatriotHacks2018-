import csv
import simplejson
import pickle

cc = []
with open("C:/Users/Owner/PycharmProjects/PatriotHacks2018/Excelit/hackathon_els_data_set.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        try:
            _row = [int(x) for x in row]
            cc.append(_row)
        except ValueError:
                pass
with open("excel_data10.pkl", "wb") as afile:
    pickle.dump(cc, afile)

"""
with open("C:/Users/Owner/PycharmProjects/PatriotHacks2018/Excelit/answerkeyinex.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        try:
            _row = [int(x) for x in row]
            cc+= _row
        except ValueError:
            pass

    with open("anskey.pkl","wb") as file:
        pickle.dump(cc, file)
f = open("answerkey.txt", "w")
simplejson.dump(cc, f)
f.close()
"""