from vpython import *
from time import *

cc_chairs = 0
Thickness_Chair = 3
RowChair = 0 
WallThick=.1
roomWidth, roomDepth, roomHeight, Num_chairs = [0,0,0,0]

def Insert_Data ():
    global roomDepth,roomHeight, roomWidth, Num_chairs
    roomWidth = int(input("Inserisci la larghezza (in cm): "))
    roomDepth= int(input("Inserisci la profondità (in cm): "))
    roomHeight= int(input("Inserisci l'altezza (in cm): "))
    if (Room_chairs == 'Sedie'):
        print ("Attenzione, è importante che la grandezza della stanza sia proporzionata al numero di sedie che si vorranno inserire. Il massimo è: " 
               +" "+ str(Control_Chairs(cc_chairs)))    
        Num_chairs = int(input("Inserisci il numero di sedie: "))
        
def Room ():
    floor = box (pos =vector(0,-roomHeight/2,0), color =color.white, size=vector(roomWidth,WallThick,roomDepth))
    ceiling = box (pos=vector(0,roomHeight/2,0), color =color.blue,size=vector(roomWidth,WallThick,roomDepth))
    leftwall =box (pos=vector (-roomWidth/2,0,0), color = color.blue, size=vector(WallThick,roomHeight,roomDepth))
    rightwall =box (pos=vector (roomWidth/2,0,0), color = color.blue, size=vector(WallThick,roomHeight,roomDepth))
    backwall =box (pos=vector (0,0,-roomDepth/2), color = color.white, size=vector(roomWidth,roomHeight,WallThick))   

def Chairs ():
    global RowChair; count = roomWidth/2+1; control = True; Count_chairs = 0
    if (roomDepth == 10 or roomDepth == 20): #necessaria per non far sforare le sedie
         num_rows = int(roomDepth/5)
    elif (roomDepth%5 == 0):
         num_rows = int(roomDepth/5)-1
    else:
         num_rows = int(roomDepth/5)
   
    if (Room_chairs == 'Grandezza' or Room_chairs == 'Sedie'):
        for y in range (0, num_rows):
            if (Room_chairs == 'Sedie'):
                if control == False:
                    break
            for x in range (int(-roomWidth/2+1), 1):
                backChair = box (pos =vector(-count+2,-roomHeight/2+1,RowChair), color =color.yellow, size=vector(1,2,1)) # 1 = larghezza sedia. 2. profondità sedia. 1.altezza sedia
                DownChair= box (pos =vector(-count+2,-roomHeight/2+.5,RowChair-1), color =color.yellow, size=vector(1,1,1))
                count = count-2
                if (Room_chairs == 'Sedie'):
                    Count_chairs = Count_chairs + 1
                    if (Count_chairs == Num_chairs):
                        control = False
                        break
            count = roomWidth/2+1
            RowChair =RowChair+ Thickness_Chair

def Control_Chairs (c_chairs):
    global cc_chairs, Thickness_Chair
    cc_chairs = 0
    RowChair = 0
    count = roomWidth/2+1
    for y in range (0,int(roomDepth/5)):
        for x in range (int(-roomWidth/2+1), 1):
            cc_chairs = cc_chairs+1
        count = roomWidth/2+1
        RowChair =RowChair + Thickness_Chair
    return cc_chairs


while True:
    try: 
        print ("Vuoi modificare il numero di sedie o la grandezza della stanza (le sedie saranno generate automaticamente)")
        Room_chairs = str(input("Scrivi 'Sedie' o 'Grandezza':  "))
        if Room_chairs == 'Grandezza': #se si scrive Grandezza    
            Insert_Data ()
            Room ()  
            Chairs()
            break
        elif Room_chairs == 'Sedie': #se si scrive Sedie  
                Insert_Data ()
                if Num_chairs <= Control_Chairs(cc_chairs):
                    Room ()
                    Chairs() 
                    break
                else:
                     print("Inserisci un numero di sedie proporzionato!")
        else:
             print ("INSERISCI LA PAROLA GRANDEZZA O SEDIE")         
    except ValueError :
                print("Inserisci nuovamente i dati, devono essere degli interi")
                pass    