# Making a dice output counter and judging how fair the dice is.

import msvcrt
from tabulate import tabulate

TABLE_HEAD = 'Roll/Prob'

def read():
  if msvcrt.kbhit():
    r = msvcrt.getch().decode()
    return r

db = {TABLE_HEAD: 'Total: 0', '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

def post_roll(roll):
  tot = db[TABLE_HEAD].split()
  db[TABLE_HEAD] = ''.join(tot[:-1]) + ' ' + str(int(tot[-1]) + 1)
  tot = db[TABLE_HEAD].split()

  db[roll] += 1
  probs = {TABLE_HEAD: 'Prob (/1)'}

  for (k, v) in list(db.items())[1:]:
    probs[k] = "%.2f" % (v/int(tot[-1]))

  return f'Roll no: {tot[-1]}\n' + tabulate([db, probs], headers='keys', tablefmt='github') + '\n\n'

print('Press q to quit.')
f = open('out.txt', 'w')
while True:
  k = read()
  if k == None: continue
  if k == 'q': break
  table = post_roll(k)
  print(table)
  f.write(table)

f.close()
