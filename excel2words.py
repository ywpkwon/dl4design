from xlrd import open_workbook
import re

team_topics = ['autonomous driving',
                'autonomous underwater vehicle',
                'beyond smart phone #1',
                'beyond smart phone #2',
                'cad to control',
                'oscillating wind power',
                'ear drop',
                'exploring commercializ...',
                'nasa tensegrity Robot Kit',
                'streat Nature Score',
                'surgical Instrument for Spine',
                'ultra spine',
                'wave energy',
                'wearable animatronic Cost']
# student_data = {i: {'teamno': team_topics[i]} for i in range(14)}

wb = open_workbook('Code_11262017.xlsx')
nrows = wb.sheets()[0].nrows

student_data = []
for r in range(1, nrows):
    teamno = int(wb.sheets()[0].cell(r,0).value)
    cnct = wb.sheets()[0].cell(r,1).value
    desc = wb.sheets()[0].cell(r,2).value
    student_data.append((teamno, cnct, desc))

# team data
team1 = [item for item in student_data if item[0]==1]

# descriptions
desc = [item[2] for item in team1]

# group no. and words
# filtered_words = re.findall(r"[a-zA-Z0-9']+", texts)

words_in_group = [(i, w.lower()) for i,d in enumerate(desc) for w in re.findall(r"[a-zA-Z0-9']+", d)]

import pickle
with open('team1words.pickle', 'wb') as f:
    pickle.dump(words_in_group, f)
