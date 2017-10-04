import re 

hand = open('fle_1.txt')
lines = hand.read()
number_list= []
y = re.findall('[0-9]+',lines)
for number in y:
	number_list.append(int(number))
print(sum(number_list))
	