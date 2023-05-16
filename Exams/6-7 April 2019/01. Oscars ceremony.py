rent = int(input())

statues = rent * 0.7
catering = statues * 0.85
sounds = catering * 0.5

total = rent + statues + catering + sounds

print(f"{total:.2f}")
