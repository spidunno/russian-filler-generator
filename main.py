import random
phrases = """
Лорем>ипсум>долор>сит>амет>вим>еним>лаудем>долорум>не>облияуе>вивендо>аццусам>усу>еу>Веро>саперет>те>при>еи>яуем>абхорреант>еам>фалли>перципитур>ат>нам>Инсоленс>иудицабит>еи>меа>диам>инсоленс>цонсецтетуер>при>ад>Еум>ат>ерипуит>пондерум>инструцтиор>Ин>усу>чоро>вереар>хас>ут>опортеат>елецтрам>Инани>долор>саепе>не>вим>дуис>моллис>промпта>ид>еам>еам>нолуиссе>сплендиде>цонтентионес>еу>Ад>ест>лаборес>цонцлудатуряуе>но>сед>мелиоре>сусципит>Иисяуе>яуаеяуе>цум>ин>ин>вис>цибо>волуптуа>яуис>дицат>алтерум>пер>ин>Омиттам>персеяуерис>еа>мел>сеа>интеллегат>персеяуерис>еу>Еа>утамур>волуптуа>диссентиас>дуо>инвидунт>яуалисяуе>
""".split('>')

def generate():
  positionA,positionB,positionC,positionD,positionE,positionF = random.randint(0,102),random.randint(0,102),random.randint(0,102),random.randint(0,102),random.randint(0,102),random.randint(0,102)

  wordA = phrases[positionA:positionA + 1]
  wordB = phrases[positionB:positionB + 1]
  wordC = phrases[positionC:positionC + 1]
  wordD = phrases[positionD:positionD + 1]
  wordE = phrases[positionE:positionE + 1]
  wordF = phrases[positionF:positionF + 1]

  final_phrase = ''.join(wordA) + ' ' + ''.join(wordB) + ' ' + ''.join(wordC) + ' ' + ''.join(wordD) + ' ' + ''.join(wordE) + ''.join(wordF)
  return final_phrase
