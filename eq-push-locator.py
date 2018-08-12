import re
 
eqLogFile = 'eqlog_character_luclin.txt'
pushbackFile = 'pushback-list.csv'
pushupFile = 'pushup-list.csv'

logSpell = re.compile('\[(?P<EQTIME>\w+\s\w+\s+\d+\s\d+:\d+:\d+\s\d+)\]\s(?P<CHARACTER>\w+)\sbegins\sto\scast\sa\sspell\.\s\<(?P<SPELL>.+)\>')
logSong = re.compile('\[(?P<EQTIME>\w+\s\w+\s+\d+\s\d+:\d+:\d+\s\d+)\]\s(?P<CHARACTER>\w+)\sbegin(s)\sto\ssing\sa\ssong\.\s\<(?P<SPELL>.+)\>')
logfile = open(eqLogFile, 'r')
pushupReader = open(pushupFile, 'r')
pushbackReader = open(pushbackFile, 'r')

pushbackset = set(pushbackLine.strip() for pushbackLine in pushbackReader)
pushupset = set(pushupLine.strip() for pushupLine in pushupReader)
pushupReader.close()
pushbackReader.close()

while True:
  line = logfile.readline()
  spellresult = logSpell.search(line)
  songresult = logSong.search(line)
  if spellresult is not None:
      if spellresult.group('SPELL') in pushbackset:
          print("{} PUSHBACK: {}".format(spellresult.group('CHARACTER'),spellresult.group('SPELL')))
      if spellresult.group('SPELL') in pushupset:
          print("{} PUSHUP: {}".format(spellresult.group('CHARACTER'),spellresult.group('SPELL')))
  if songresult is not None:
      if songresult.group('SPELL') in pushbackset:
          print("{} PUSHBACK: {}".format(songresult.group('CHARACTER'),songresult.group('SPELL')))
      if songresult.group('SPELL') in pushupset:
          print("{} PUSHUP: {}".format(songresult.group('CHARACTER'),songresult.group('SPELL')))

logfile.close()
