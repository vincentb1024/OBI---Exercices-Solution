lista = [input() for _ in range(6)]
vitorias = lista.count("V")
if vitorias == 5 or vitorias == 6:
  print("1")
elif vitorias == 3 or vitorias == 4:
  print("2")
elif vitorias == 1 or vitorias == 2:
  print("3")
else:
  print("-1")
