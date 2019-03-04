import mido

fN = 'Bach_My_Heart_Ever_Faithful_BWV34.mid'
import parseMidi as pm

a = pm.parse(fN)
f = open("test1.txt", "w")

s = ''
t = 0
for i in a:
	s += str(i) + "\n"
	t += i[-1]

f.write(s)
print(str(t/1000))