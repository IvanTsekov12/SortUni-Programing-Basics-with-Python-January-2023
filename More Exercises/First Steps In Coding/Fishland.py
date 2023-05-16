skumriq_price = float(input())
caca_price = float(input())
palmud_kilos = float(input())
safrid_kilos = float(input())
midi_kilos = int(input())
palmud_price = skumriq_price + (skumriq_price * 0.6)
sum_of_palmud = palmud_price * palmud_kilos
safrid_price = caca_price + (caca_price * 0.8)
sum_of_safrid = safrid_price * safrid_kilos
sum_of_midi = midi_kilos * 7.5
total = sum_of_midi + sum_of_safrid + sum_of_palmud
print(f"{total:.2f}")