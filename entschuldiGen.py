#!/usr/bin/env python
# coding=iso-8859-1
import random, datetime
daysOfWeek=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
excuseList = ["Wegen starken Magenschmerzen konnte ich den Schulunterricht nicht wahrnehmen.",u"Aufgrund von starken Kopfschmerzen war es mir nicht möglich, den Unterricht zu besuchen.","Da ich derzeit an einer Magendarm-Erkrankung leide, bin ich dem Unterricht fern geblieben.","Aufgrund eines grippalen Infektes musste ich die Schule meiden.","Bedingt durch akute Kopf- und Gliederschmerzen konnte ich den Unterricht nicht besuchen.",u"Wegen eines Zahnarzttermines war es mir nicht möglich, die Anwesenheit im Unterricht zu erfüllen."]
date = raw_input("An welchem Datum hast du gefehlt? ")
frame = raw_input("Den (g)anzen Tag, (a)nfangs oder (e)nde? ")
if(frame == "a" or frame == "e"):
	course = raw_input("Welches Fach? ")

dateList = date.split('.')
dow = datetime.datetime(int(dateList[2]),int(dateList[1]),int(dateList[0])).weekday()

print("Sehr geehrter Herr Maass,")
if (frame == "a"):
	print("hiermit entschuldige ich meine Verspätung im "+ course + " Unterricht am "+ daysOfWeek[dow]+ ', den ' + date + ".")
elif(frame == "e"):
	print("hiermit entschuldige ich mein Fehlen im " + course + " Unterricht am "+ daysOfWeek[dow]+ ', den ' + date + ".")
else:
	#TODO: Wochentag einfügen
	print("hiermit entschuldige ich mein Fehlen am "+ daysOfWeek[dow]+ ', den ' + date + ".")
rng = random.randint(0, len(excuseList)-1)
print(excuseList[rng])

