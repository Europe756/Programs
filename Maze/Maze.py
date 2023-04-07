#!/bin/python3

def zeigeAnweisungen():
    #Zeige ein Hauptmenü und die möglichen Befehle
    print('''
RPG Spiel (Labyrinth)
========

Suche den Schlüssel und den Zaubertrank und versuche dann, in den Garten zu entkommen.
Lass dich nicht von den Monstern fressen!

Verbindungen:
  [Zimmer]->([Richtung], [Richtung])

Befehle:
  gehe [w(Vorwärts),a(Rechts),s(Rückwärts),d(Links),q(Ab),e(Auf)]
  nimm [Gegenstand]
  hilfe
''')

def zeigeZustand():
  #Zeige den aktuellen Zustand des Spielers
  print('---------------------------')
  print('Du bist im Zimmer: ' + aktuellesZimmer)
  #Zeige das aktuelle Inventar
  print('Inventar : ' + str(inventar))
  #Zeige einen Gegenstand an, wenn einer im Zimmer vorhanden ist
  if "Gegenstand" in zimmer[aktuellesZimmer]:
      print('Du siehst einen ' + zimmer[aktuellesZimmer]['Gegenstand'])
  print("---------------------------")

#Das Inventar ist beim Start leer
inventar = []
gone = 0
#Ein Dictionary (Wörterbuch) verbindet ein Zimmer mit anderen Zimmern
zimmer = {
#Erdgeschoss
            'Diele (Links, Rechts)' : {
                  's' : 'Tür (Rückwärts, Vorwärts)',
                  'a' : 'Gang (Links, Rechts)',
                  'q' : 'Treppe (EG)(Auf, Links)'},        
                
            'Gang (Links, Rechts)' : {
                  'd' : 'Diele (Links, Rechts)',
                  'a' : 'Esszimmer (Rechts, Rückwärts)',
                  'Gegenstand'  : 'Monster'},        
                
            'Esszimmer (Rechts, Rückwärts)' : {
                  'd' : 'Gang (Links, Rechts)',
                  's' : 'Garten (Vorwärts)',
                  'Gegenstand'  : 'Zaubertrank'},
                
            'Garten (Vorwärts)' : {
                  'w' : 'Esszimmer (Rechts, Rückwärts)'},
                
            'Treppe (EG)(Auf, Links)' : {
                  'a' : 'Diele (Links, Rechts)',
                  'e' : 'Treppe (OG)(Ab, Rechts)'},
            
            'Leiter (EG)(Ab, Vorwärts)' : {
                  'w' : 'Tür (Rückwärts, Vorwärts)',
                  'q' : 'Leiter (UG)(Auf, Rechts)',
                  'Gegenstand'  : 'Monster'},
            
            'Tür (Rückwärts, Vorwärts)' : {
                  'w' : 'Diele (Links, Rechts)',
                  's' : 'Leiter (EG)(Ab, Vorwärts)'},
#Obergeschoss                
            'Treppe (OG)(Ab, Rechts)' : {
                  'q' : 'Treppe (EG)(Auf, Links)',
                  'a' : 'Gang 1 (Links, Rechts, Rückwärts)'},
            
            'Gang 1 (Links, Rechts, Rückwärts)' : {
                  'a' : 'Gang 2 (Links, Rechts, Vorwärts, Rückwärts)',
                  's' : 'Gang 4 (Links, Rechts, Vorwärts)',
                  'd' : 'Treppe (OG)(Ab, Rechts)'},
                        
            'Gang 2 (Links, Rechts, Vorwärts, Rückwärts)' : {
                  'a' : 'Gang 3 (Links, Rechts, Vorwärts)',
                  'd' : 'Gang 1 (Links, Rechts, Rückwärts)',
                  's' : 'Gang 5 (Links, Rechts, Rückwärts)',
                  'w' : 'Garderobe (Rückwärts, Vorwärts)'},
            
            
            'Garderobe (Rückwärts, Vorwärts)' : {
                  'w' : 'Balkon (Rückwärts)',
                  's' : 'Gang 2 (Links, Rechts, Vorwärts, Rückwärts)',
                  'Gegenstand'  : 'Monster'},
            
            'Balkon (Rückwärts)' : {
                  's' : 'Garderobe (Rückwärts, Vorwärts)',
                  'Gegenstand'  : 'Mysteriöses Teil 1/3'},
            
            'Gang 3 (Links, Rechts, Vorwärts)' : {
                  'a' : 'Gang 4 (Links, Rechts, Vorwärts)',
                  'd' : 'Gang 2 (Links, Rechts, Vorwärts, Rückwärts)',
                  'w' : 'Gang 6 (Links, Rechts, Rückwärts)'},
            
            'Gang 4 (Links, Rechts, Vorwärts)' : {
                  'a' : 'Gang 5 (Links, Rechts, Rückwärts)',
                  'd' : 'Gang 3 (Links, Rechts, Vorwärts)',
                  'w' : 'Gang 2 (Links, Rechts, Vorwärts, Rückwärts)'},
            
            'Gang 5 (Links, Rechts, Rückwärts)' : {
                  'a' : 'Gang 6 (Links, Rechts, Rückwärts)',
                  'd' : 'Gang 4 (Links, Rechts, Vorwärts)',
                  's' : 'Dachboden (Vorwärts)'},
            
            'Dachboden (Vorwärts)' : {
                  'w' : 'Gang 5 (Links, Rechts, Rückwärts)',
                  'Gegenstand'  : 'Schwert'},
            
            'Gang 6 (Links, Rechts, Rückwärts)' : {
                  'a' : 'Gang 7 (Links, Rechts, Vorwärts)',
                  'd' : 'Gang 5 (Links, Rechts, Rückwärts)',
                  's' : 'Tresorraum (Vorwärts)'},
            
            'Tresorraum (Vorwärts)' : {
                  'w' : 'Gang 6 (Links, Rechts, Rückwärts)',
                  'Gegenstand'  : 'Monster'},
            
            'Gang 7 (Links, Rechts, Vorwärts)' : {
                  'd' : 'Gang 6 (Links, Rechts, Rückwärts)',
                  'a' : 'Schlafzimmer (Rechts)',
                  'w' : 'Gang 3 (Links, Rechts, Vorwärts)'},
            
            'Schlafzimmer (Rechts)' : {
                  'd' : 'Gang 7 (Links, Rechts, Vorwärts)',
                  'Gegenstand'  : 'Schlüssel'},
#Untergeschoss            
            'Leiter (UG)(Auf, Rechts)' : {
                  'e' : 'Leiter (EG)(Ab, Vorwärts)',
                  'd' : 'Keller (Links, Rechts)'},
            
            'Keller (Links, Rechts)' : {
                  'a' : 'Leiter (UG)(Auf, Rechts)',
                  'd' : 'Fahrradgarage (Links)',
                  'Gegenstand'  : 'Mysteriöses Teil 2/3'},
            
            'Fahrradgarage (Links)' : {
                  'a' : 'Keller (Links, Rechts)'},
#???
            '§$%%&$%@ (Auf)' : {'e' : 'Diele (Links, Rechts)'},
         }

#Beim Start ist der Spieler in der Diele
aktuellesZimmer = 'Diele (Links, Rechts)'

zeigeAnweisungen()

#Ewige Schleife
while True:

  zeigeZustand()

  #Warte auf den 'nächsten Spielzug (die nächste Bewegung)' des Spielers
  #.split() teilt ihn in ein Array auf
  #Wenn du z.B. 'gehenach osten' eintippst, erhältst du folgende Liste:
  #['gehenach','osten']
  spielzug = ''
  while spielzug == '':  
    spielzug = input('>')
    
  spielzug = spielzug.split()
#please do not change - in German the object names start with uppercase letter

  #Wenn das Eingetippte mit 'gehenach' beginnt
  if spielzug[0] == 'gehe':
    #Prüfe, ob der Spieler auch dorthin gehen kann, wo er hin will
    if spielzug[1] in zimmer[aktuellesZimmer]:
      #Mache das neue Zimmer zum aktuellen Zimmer
      aktuellesZimmer = zimmer[aktuellesZimmer][spielzug[1]]
    #Es gibt keine Tür (Verbindung) zum neuen Zimmer
    else:
      print('Du kannst nicht in diese Richtung gehen!')
      
  if spielzug[0] == 'hilfe':
      zeigeAnweisungen()

  #Wenn das Eingetippte mit 'nimm' beginnt
  if spielzug[0] == 'nimm' :
    #Wenn das Zimmer einen Gegenstand enthält, und du genau diesen Gegenstand nehmen willst
    if spielzug[1] == 'Monster':
        print('Das Monster ist zu schwer!')
    elif "Gegenstand" in zimmer[aktuellesZimmer] and spielzug[1] in zimmer[aktuellesZimmer]['Gegenstand']:
      #Füge den Gegenstand dem Inventar des Spielers hinzu
      inventar += [spielzug[1]]
      #Zeige eine hilfreiche Mitteilung
      print(spielzug[1] + ' wurde genommen!')
      #Lösche den Gegenstand vom Zimmer
      del zimmer[aktuellesZimmer]['Gegenstand']
    #Andernfalls ist der Gegenstand nicht vorhanden und kann auch nicht genommen werden
    else:
      #Sage dem Spieler, dass er diesen Gegenstand nicht nehmen kann
      print('Du kannst ' + spielzug[1] + ' nicht nehmen!')
      
  #Der Spieler verliert, wenn er ein Zimmer mit einem Monster betritt
  if "Gegenstand" in zimmer[aktuellesZimmer] and 'Monster' in zimmer[aktuellesZimmer]['Gegenstand'] and 'Schwert' in inventar:
    print('Du hast das Monster ohnmächtig gemacht, aber es wird bald wieder aufwachen!')
  elif "Gegenstand" in zimmer[aktuellesZimmer] and 'Monster' in zimmer[aktuellesZimmer]['Gegenstand']:  
    print('Du wurdest von einem hungrigen Monster gefressen... DAS SPIEL IST AUS!')
    aktuellesZimmer = 'Diele (Links, Rechts)'
    inventar = []
    

  #Der Spieler gewinnt, wenn er mit dem Schlüssel und dem Zaubertrank den Garten erreicht
  if aktuellesZimmer == 'Garten (Vorwärts)' and 'Schlüssel' in inventar and 'Zaubertrank' in inventar:
    zeigeZustand()
    print('Du bist aus dem Haus entkommen... DU HAST GEWONNEN!')
    break
  
  if aktuellesZimmer == 'Tür (Rückwärts, Vorwärts)' and not 'Schlüssel' in inventar: 
    print("Du brauchst einen Schlüssel")
    aktuellesZimmer = 'Diele (Links, Rechts)'
    
  if 'Mysteriöses Teil 1/3' in inventar and 'Mysteriöses Teil 2/3' in inventar and 'Mysteriöses Teil 3/3' in inventar and not gone == 1:
      print('Alle Teile wurden gefunden! Du hast einen neuen Raum entdeckt!')
      print('Du kannst nur einmal hierherkommen, wenn du weggehst gibt es keinen weg zurück')
      print('"e" ist der einzige Ausgang')
      print('Die anderen Wege musst du selbst herausfinden')
      aktuellesZimmer = '§$%%&$%@ (Auf)'
      gone = 1
    
