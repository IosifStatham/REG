import csv
import re
from collections import defaultdict

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

contacts_list_1 = []
for i in contacts_list:
  list_1 = []
  for n in range(3):
    list_1.append(i[n])
  i_str_1 = ' '.join(list_1)
  i_spl_1 = i_str_1.split()
  lastname, firstname = i_spl_1[0], i_spl_1[1]
  if len(i_spl_1) > 2:
    surname = i_spl_1[2]
  else:
    surname = ''
  organization, position, phone, email = i[3], i[4], i[5], i[6]
  contacts_list_1.append([lastname, firstname, surname, organization, position, phone, email])

for i in contacts_list_1:
  pattern = r"(\+7|8)\s?\(?(\d\d\d)\)?[\s-]?(\d\d\d)[-\s]?(\d\d)[-\s]?(\d\d)[\s]?\(?(доб\.)?\s?(\d+)?\)?"
  subst_patter = r"+7(\2)\3-\4-\5 \6\7"
  phone = i[5]
  result = re.sub(pattern, subst_patter, phone)
  i.pop(5)
  i.insert(5, result)

data = defaultdict(list)
for i in contacts_list_1:
  tup = tuple(i[:2])
  for d in i:
    if d not in data[tup]:
      data[tup].append(d)
data_list = list(data.values())

with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(data_list)