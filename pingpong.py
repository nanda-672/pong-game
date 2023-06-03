import turtle as trt
import time as tm

# jumlah skor yang dibutuhkan untuk menang
skorwin = 10

# mendeklarasikan variabel pengali kecepatan bola
multiplier = 1.5

# warna
# putih = #f6f7f1
# biru  = #349fa4
# merah = #f67e7d
# ungu  = #843b62

# layar 
# mendeklarasikan variabel untuk layar 
lyr = trt.Screen()

# mengatur komponen komponen layar 
lyr.title("PINGPONG")                                                   # judul program
lyr.bgcolor("#f6f7f1")                                                  # warna layar 
lyr.setup(width=800, height = 600)                                      # ukuran layar permainan
lyr.tracer(0)                                                           # supaya layar bisa berubah ketika ditekan 

# Background kanan kiri
# Background kanan
#bg1 = trt.Turtle()
#bg1.shape("square")                                                     # bentuk bg1
#bg1.color("#349fa4")                                                    # warna bg1
#bg1.penup()                                                             # supaya tidak mengeluarkan garis ketika terpantul
#bg1.shapesize(stretch_wid=30, stretch_len=20)                             # ukuran bg1
#bg1.goto (200,0)                                                        # posisi bg1 di awal game
#bg1.speed (0)                                                           # kecepatan bg1

# Background kiri
#bg2 = trt.Turtle()
#bg2.shape("square")                                                     # bentuk bg2
#bg2.color("#f67e7d")                                                    # warna bg2
#bg2.penup()                                                             # supaya tidak mengeluarkan garis ketika terpantul
#bg2.shapesize(stretch_wid=30, stretch_len=20)                             # ukuran bg2
#bg2.goto (-200,0)                                                        # posisi bg2 di awal game
#bg2.speed (0)                                                           # kecepatan bg2

# PINGPONG 
# deklarasikan variabel untuk bola pingpong 
pong = trt.Turtle() 
pong.shape("circle")              # bentuk bola
pong.color("#ffeead")             # warna bola
pong.penup()                      # untuk supaya tidak mengeluarkan garis ketika terpantul
pong.goto (0,0)                   # posisi bola di awal game
pong.speed (0)                    # kecepatan bola
pong.dx = 0.25
pong.dy = 0.25

# TONgKAT 
# deklarasi variabel tongkat1 
tongkat1 = trt.Turtle()
tongkat1.shape("square")                                                # bentuk tongkat1
tongkat1.color("#349fa4")                                               # warna tongkat1
tongkat1.penup()                                                        # supaya tidak mengeluarkan garis ketika terpantul
tongkat1.shapesize(stretch_wid=5, stretch_len=1)                        # ukuran tongkat1
tongkat1.goto (-360,0)                                                  # posisi tongkat1 di awal game
tongkat1.speed (0)                                                      # kecepatan tongkat1

# deklarasi variabel tongkat2 
tongkat2 = trt.Turtle()
tongkat2.shape("square")                                                # bentuk tongkat2
tongkat2.color("#f67e7d")                                               # warna tongkat2
tongkat2.penup()                                                        # untuk supaya tidak mengeluarkan garis ketika terpantul
tongkat2.shapesize(stretch_wid=5, stretch_len=1)                        # ukuran tongkat2
tongkat2.goto (360,0)                                                   # posisi tongkat2 di awal game
tongkat2.speed (0)                                                      # kecepatan tongkat2


# deklarasi menghentikan game v
berhenti = trt.Turtle()
berhenti.speed(0)
berhenti.penup()
berhenti.hideturtle()
berhenti.goto(0, -260)
berhenti.color("#349fa4")
berhenti.write("Press Esc to exit the game",align= "center",font=("Arial", 18, "normal"))

# inisiasi variabel jumlah skor v
skor12 = [0,0]

# deklarasi variabel sistem skor v
skor = trt.Turtle()
skor.speed(0)
skor.penup()
skor.hideturtle()
skor.goto(-100,250)
skor.color("#349fa4")
skor.write("SKOR P1: " + str (skor12[0]) ,align= "center",font=("Arial", 24, "normal"))

skor2 = trt.Turtle()
skor2.speed(0)
skor2.penup()
skor2.hideturtle()
skor2.goto(100,250)
skor2.color("#f67e7d")
skor2.write(" SKOR P2: "+ str (skor12[1]),align= "center",font=("Arial", 24, "normal"))

# mendeklarasikan variabel popup menang v
popup = trt.Turtle()
popup.speed(0)
popup.penup()
popup.hideturtle()
popup.goto(0,0)
popup.color("#349fa4")

# GUIDE v

#Guide kiri atas v
guide1 = trt.Turtle()
guide1.speed(0)
guide1.penup()
guide1.hideturtle()
guide1.goto(-360, 250)
guide1.color("#349fa4")
guide1.write("W",align= "center",font=("Arial", 20, "normal"))

#Guide kiri bawah v
guide2 = trt.Turtle()
guide2.speed(0)
guide2.penup()
guide2.hideturtle()
guide2.goto(-360, -260)
guide2.color("#349fa4")
guide2.write("S",align= "center",font=("Arial", 20, "normal"))

#Guide kanan atas v
guide3 = trt.Turtle()
guide3.speed(0)
guide3.penup()
guide3.hideturtle()
guide3.goto(360, 235)
guide3.color("#f67e7d")
guide3.write("⇧",align= "center",font=("Arial", 40, "normal"))

#Guide kanan bawah v
guide4 = trt.Turtle()
guide4.speed(0)
guide4.penup()
guide4.hideturtle()
guide4.goto(360, -275)
guide4.color("#f67e7d")
guide4.write("⇩",align= "center",font=("Arial", 40, "normal"))

# untuk gerakan tongkat v
def tongkat1up():
# diberi batas agar tidak keluar layar
    if tongkat1.ycor() <= 251:
        y = tongkat1.ycor() # koordinat tongkat1
        y = y + 20
        tongkat1.sety(y)

def tongkat1down():
# diberi batas agar tidak keluar layar
    if tongkat1.ycor() >= -251:
        y = tongkat1.ycor() # koordinat tongkat1
        y = y - 20
        tongkat1.sety(y)

def tongkat2up():
# diberi batas agar tidak keluar layar    
    if tongkat2.ycor() <= 251:
        y = tongkat2.ycor() # koordinat tongkat2
        y = y + 20
        tongkat2.sety(y)

def tongkat2down():
# diberi batas agar tidak keluar layar
    if tongkat2.ycor() >= -251:
        y = tongkat2.ycor() # koordinat tongkat2
        y = y - 20
        tongkat2.sety(y)

# definisikan fungsi untuk menghentikan permainan v
def stop():
    global play
    play = False 

# definisikan gerakan tongkat dengan tombol di keyboard v
lyr.listen()
lyr.onkeypress(tongkat1up, "w")         # 

lyr.listen()
lyr.onkeypress(tongkat1down, "s")

lyr.listen()
lyr.onkeypress(tongkat2up, "Up")

lyr.listen()
lyr.onkeypress(tongkat2down, "Down")

# definisi input dari player untuk menghentikan permainan
lyr.onkeypress(stop,"Escape")

play = True


#looping utama berjalannya game
while play:
    # digunakan agar layar terupdate terus/te-refresh
    lyr.update()

    # menggerakkan pongpong 
    pong.setx(pong.xcor() + pong.dx)
    pong.sety(pong.ycor() + pong.dy)

    # manipulasi dinding penghalang atas bawah 
    if pong.ycor() < -290:
        pong.sety (-290)
        pong.dy = pong.dy * -1
    
    if pong.ycor() > 290:
        pong.sety (290)
        pong.dy = pong.dy * -1
  
    # manipulasi dinding penghalang  kiri 
    if pong.xcor() < -390:
        pong.goto (0,0)
        pong.dx = -0.25
        skor12[1] = skor12[1] + 1
        skor2.clear()
        skor2.write(" SKOR P2: "+ str (skor12[1]),align= "center",font=("Arial", 24, "normal"))
    
    # manipulasi dinding penghalang  kanan 
    if pong.xcor() > 390:
        pong.goto (0,0)
        pong.dx = 0.25
        skor12[0] = skor12[0] + 1
        skor.clear()
        skor.write("SKOR P1: " + str (skor12[0]) ,align= "center",font=("Arial", 24, "normal"))
    

    # pemantulan bola pada tongkat2
    if (pong.xcor() > 350 and pong.xcor() < 360 and pong.ycor() < tongkat2.ycor()+ 50 and pong.ycor() > tongkat2.ycor() - 50):
        pong.dx = pong.dx * -1 * multiplier
    
    # pemantulan bola pada tongkat1
    if (pong.xcor() < -350 and pong.xcor() > -360 and pong.ycor() < tongkat1.ycor()+ 50 and pong.ycor() > tongkat1.ycor() - 50):
        pong.dx = pong.dx * -1 * multiplier

    
    if skor12[1] == skorwin:
        lyr.clear() # membersihkan layar
        popup.write("P2 is the winner",align= "center",font=("Arial", 50, "normal"))
        tm.sleep(5) # menghentikan proses selama 5 detik
        play = False # menghentikan game

    if skor12[0] == skorwin:
        lyr.clear() # membersihkan layar
        popup.write("P1 is the winner",align= "center",font=("Arial", 50, "normal"))
        tm.sleep(5) # menghentikan proses selama 5 detik
        play = False # menghentikan game
       