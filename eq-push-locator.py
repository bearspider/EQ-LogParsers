import re
 
eqLogFile = 'eqlog_character_luclin.txt'
pushbackFile = 'pushback-list.csv'
pushupFile = 'pushup-list.csv'

logSpell = re.compile('\[(?P<EQTIME>\w+\s\w+\s+\d+\s\d+:\d+:\d+\s\d+)\]\s(?P<CHARACTER>\w+)\sbegins\sto\scast\sa\sspell\.\s\<(?P<SPELL>.+)\>')
logfile = open(eqLogFile, 'r')
pushupReader = open(pushupFile, 'r')
pushbackReader = open(pushbackFile, 'r')

pushbackset = set(pushbackLine.strip() for pushbackLine in pushbackReader)
pushupset = set(pushupLine.strip() for pushupLine in pushupReader)
pushupReader.close()
pushbackReader.close()

while True:
  line = logfile.readline()
  result = logSpell.search(line)
  if result is not None:
      if result.group('SPELL') in pushbackset:
          print("{} PUSHBACK: {}".format(result.group('CHARACTER'),result.group('SPELL')))
      if result.group('SPELL') in pushupset:
          print("{} PUSHUP: {}".format(result.group('CHARACTER'),result.group('SPELL')))

logfile.close()
