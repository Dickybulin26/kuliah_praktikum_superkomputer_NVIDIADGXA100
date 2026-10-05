# =============================================================================
# Tugas: Membuat modifikasi data dari batu-gunting-kertas menggunakan sistem AI Markov
# Penjelasan dalam bentuk komentar pada kode
# =============================================================================

# -----------------------------------------------------------------------------
# SEL 1: Bot battle (Bot 1: algoritma heuristik, Bot 2: Markov Chain)
# -----------------------------------------------------------------------------

# botbattle!!!! The algorithm based bot is Bot 1 and the Markov Chain Based one is Bot 2
import random

# Inisialisasi variabel untuk menyimpan pilihan dan skor
bot1choice = 0
bot2choice = 0
bot1prevchoice = 0
bot2prevchoice = 0
results = ""
results2 = ""
bot1score = [0,0,0]  # [menang, kalah, seri] untuk Bot1
bot2score = [0,0,0]  # [menang, kalah, seri] untuk Bot2

# Tiga matriks transisi Markov untuk kondisi: menang, kalah, seri
# Masing-masing dictionary menyimpan frekuensi transisi dari state (prev, current)
buildTMatrix = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixL = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixT = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}

n = 3
m = 3
# Matriks probabilitas transisi (3x3) untuk setiap kondisi
tMatrix = [[0] * m for i in range(n)]   # untuk kondisi menang
tMatrixL = [[0] * m for i in range(n)]  # untuk kondisi kalah
tMatrixT = [[0] * m for i in range(n)]  # untuk kondisi seri

# Probabilitas awal untuk setiap pilihan (sama rata)
probabilitiesRPS = [1/3, 1/3, 1/3]

def init():
    """Inisialisasi awal permainan bot vs bot."""
    global bot1prevchoice, bot1choice, bot2prevchoice, bot2choice, results, results2
    # Asumsi awal: pilihan sebelumnya batu, pilihan sekarang batu (hasil seri)
    bot1prevchoice, bot1choice = bot1(0, 0, "Tied!")
    bot2prevchoice, bot2choice = bot2(0, 0, "Tied!")
    results = checkWin(bot1choice, bot2choice)
    if results == "Win!":
        results2 = "Lose!"
    elif results == "Lose!":
        results2 = "Win!"
    else:
        results2 = "Tied!"
    # Jalankan 100.000 ronde pertarungan
    fight(100000)

def fight(rounds):
    """Melakukan sejumlah ronde pertarungan antara bot1 dan bot2."""
    global bot1prevchoice, bot1choice, bot2prevchoice, bot2choice, results, results2, bot1score, bot2score
    choose = ["Rock", "Paper", "Scissors"]
    for i in range(rounds):
        # Bot1 bermain dengan melihat pilihan sebelumnya dari bot2 dan hasil (results2)
        bot1prevchoice, bot1choice = bot1(bot2prevchoice, bot2choice, results2)
        # Bot2 (Markov) bermain dengan melihat pilihan bot1 dan hasil
        bot2prevchoice, bot2choice = bot2(bot1prevchoice, bot1choice, results)
        # Evaluasi hasil ronde ini
        results = checkWin(bot1choice, bot2choice)
        if results == "Win!":
            results2 = "Lose!"
        elif results == "Lose!":
            results2 = "Win!"
        else:
            results2 = "Tied!"
        # Update skor
        if results == "Win!":
            bot2score[1] += 1  # Bot2 kalah? Wait: checkWin dari perspektif bot1?
            bot1score[0] += 1
        elif results == "Lose!":
            bot1score[1] += 1
            bot2score[0] += 1
        else:
            bot2score[2] += 1
            bot1score[2] += 1
    print("Bot1 won %s times, lost %s times, and tied %s times.\n\nTo check:\n\nBot2 won %s times, lost %s times, and tied %s times." 
          % (bot1score[0], bot1score[1], bot1score[2], bot2score[0], bot2score[1], bot2score[2]))

def bot1(prev, choit, res):
    """
    Bot1: menggunakan heuristik sederhana (bukan Markov).
    Parameter:
        prev: pilihan sebelumnya dari lawan (bot2)
        choit: pilihan bot1 sebelumnya (tidak digunakan secara langsung)
        res: hasil sebelumnya dari perspektif bot1
    Mengembalikan (pilihan_lama, pilihan_baru) - aneh karena return choit, machineChoice.
    """
    choices = ["Rock", "Paper", "Scissors"]
    prevChoice = prev
    choice = choit
    result = res
    streak = 0
    won = 0
    alt = 0
    numoff = 0

    # Logika sederhana: deteksi streak, pola menang/kalah, dll.
    if prevChoice == choice:
        streak += 1
    else:
        streak -= 1
        if streak < 0:
            streak = 0
    winprev = prevChoice + 1
    if winprev > 2:
        winprev = 0
    if choice == winprev:
        alt += 1
    else:
        alt -= 1
        if alt < 0:
            alt = 0
    if alt > 3:
        machineChoice = winprev + 1
        if machineChoice > 2:
            machineChoice = 0
    elif streak > 3:
        machineChoice = prevChoice - 2
        if machineChoice < 0:
            machineChoice += 3
    elif won > 9:
        machineChoice = random.randint(0, 2)
    elif won > 3 and won < 10:
        machineChoice = prevChoice
    else:
        if result == "Win!":
            machineChoice = prevChoice - 2
            if machineChoice < 0:
                machineChoice += 3
        elif result == "Lose!":
            machineChoice = prevChoice + 1
            if machineChoice > 2:
                machineChoice -= 3
            machineChoice -= 2
            if machineChoice < 0:
                machineChoice += 3
        else:
            machineChoice = random.randint(0, 2)

    result_check = checkWin(choice, machineChoice)
    if result_check == "Win!":
        won += 1
    else:
        won -= 2
        if won < 0:
            won = 0
    return choit, machineChoice

def checkWin(user, machine):
    """Menentukan hasil permainan: 'Win!', 'Lose!', atau 'Tied!' dari perspektif user."""
    win = False
    tie = False
    if user == 0:  # Batu
        if machine == 2:   # Gunting -> menang
            win = True
        elif machine == 1: # Kertas -> kalah
            win = False
        elif machine == 0:
            tie = True
    elif user == 1:  # Kertas
        if machine == 0:   # Batu -> menang
            win = True
        elif machine == 2: # Gunting -> kalah
            win = False
        elif machine == 1:
            tie = True
    else:            # Gunting
        if machine == 1:   # Kertas -> menang
            win = True
        elif machine == 0: # Batu -> kalah
            win = False
        elif machine == 2:
            tie = True

    if tie:
        return "Tied!"
    elif win:
        return "Win!"
    else:
        return "Lose!"

def bot2(previ, choit, res):
    """
    Bot2: menggunakan Markov Chain.
    Memprediksi gerakan lawan berdasarkan riwayat transisi.
    Parameter:
        previ: pilihan sebelumnya dari lawan (bot1)
        choit: pilihan bot2 sebelumnya (tidak dipakai)
        res: hasil sebelumnya dari perspektif bot2
    Mengembalikan (pilihan_lama, pilihan_baru) - aneh juga.
    """
    global probabilitiesRPS
    choices = ["Rock","Paper","Scissors"]
    choi = ['r','p','s']
    prevChoice = previ
    result = res
    choice = choit

    # Dapatkan matriks transisi berdasarkan hasil terakhir
    transMatrix = buildTransitionProbabilities(prevChoice, choice, result)
    # Pilih gerakan berdasarkan probabilitas dari matriks transisi untuk state sebelumnya
    machineChoice = random.randint(1, 100)
    probabilitiesRPS[0] = transMatrix[prevChoice][0]  # probabilitas batu
    probabilitiesRPS[1] = transMatrix[prevChoice][1]  # probabilitas kertas
    probabilitiesRPS[2] = transMatrix[prevChoice][2]  # probabilitas gunting
    rangeR = probabilitiesRPS[0] * 100
    rangeP = probabilitiesRPS[1] * 100 + rangeR
    if machineChoice <= rangeR:
        machineChoice = 1   # ??? Seharusnya 0 untuk batu. Mungkin ada bug.
    elif machineChoice <= rangeP:
        machineChoice = 2
    else:
        machineChoice = 0
    return choit, machineChoice

def buildTransitionProbabilities(pC, c, winloss):
    """
    Memperbarui frekuensi transisi berdasarkan hasil (menang/kalah/seri).
    pC: previous choice (0=batu,1=kertas,2=gunting)
    c: current choice
    winloss: "Win!", "Lose!", "Tied!"
    """
    global buildTMatrix, buildTMatrixL, buildTMatrixT
    choi = ['r','p','s']
    key = '%s%s' % (choi[pC], choi[c])
    if winloss == "Win!":
        if key in buildTMatrix:
            buildTMatrix[key] += 1
    elif winloss == "Tied!":
        if key in buildTMatrixT:
            buildTMatrixT[key] += 1
    else:  # Lose!
        if key in buildTMatrixL:
            buildTMatrixL[key] += 1
    # Kembalikan matriks probabilitas yang telah diperbarui
    return buildTransitionMatrix(winloss)

def buildTransitionMatrix(winlosstwo):
    """
    Membangun matriks probabilitas transisi 3x3 dari frekuensi yang terkumpul.
    winlosstwo: menentukan matriks mana yang akan dikembalikan (menang/kalah/seri).
    """
    global tMatrix, tMatrixL, tMatrixT
    choi = ['r','p','s']
    if winlosstwo == "Win!":
        # Hitung total untuk setiap state sebelumnya (rock, paper, scissors)
        rock = buildTMatrix['rr'] + buildTMatrix['rs'] + buildTMatrix['rp']
        paper = buildTMatrix['pr'] + buildTMatrix['ps'] + buildTMatrix['pp']
        scissors = buildTMatrix['sr'] + buildTMatrix['ss'] + buildTMatrix['sp']
        for row_index, row in enumerate(tMatrix):
            for col_index, item in enumerate(row):
                a = buildTMatrix['%s%s' % (choi[row_index], choi[col_index])]
                if row_index == 0:
                    c = a / rock if rock > 0 else 0
                elif row_index == 1:
                    c = a / paper if paper > 0 else 0
                else:
                    c = a / scissors if scissors > 0 else 0
                row[col_index] = float(c)
        return tMatrix
    elif winlosstwo == "Tied!":
        rock = buildTMatrixT['rr'] + buildTMatrixT['rs'] + buildTMatrixT['rp']
        paper = buildTMatrixT['pr'] + buildTMatrixT['ps'] + buildTMatrixT['pp']
        scissors = buildTMatrixT['sr'] + buildTMatrixT['ss'] + buildTMatrixT['sp']
        for row_index, row in enumerate(tMatrixT):
            for col_index, item in enumerate(row):
                a = buildTMatrixT['%s%s' % (choi[row_index], choi[col_index])]
                if row_index == 0:
                    c = a / rock if rock > 0 else 0
                elif row_index == 1:
                    c = a / paper if paper > 0 else 0
                else:
                    c = a / scissors if scissors > 0 else 0
                row[col_index] = float(c)
        return tMatrixT
    else:  # Lose!
        rock = buildTMatrixL['rr'] + buildTMatrixL['rs'] + buildTMatrixL['rp']
        paper = buildTMatrixL['pr'] + buildTMatrixL['ps'] + buildTMatrixL['pp']
        scissors = buildTMatrixL['sr'] + buildTMatrixL['ss'] + buildTMatrixL['sp']
        for row_index, row in enumerate(tMatrixL):
            for col_index, item in enumerate(row):
                a = buildTMatrixL['%s%s' % (choi[row_index], choi[col_index])]
                if row_index == 0:
                    c = a / rock if rock > 0 else 0
                elif row_index == 1:
                    c = a / paper if paper > 0 else 0
                else:
                    c = a / scissors if scissors > 0 else 0
                row[col_index] = float(c)
        return tMatrixL

# init() dipanggil di akhir sel pertama (tidak dalam fungsi)
# init()  # Baris ini dieksekusi saat sel dijalankan

# -----------------------------------------------------------------------------
# SEL 2: Human vs Markov Chain bot (versi sederhana)
# -----------------------------------------------------------------------------

#!/usr/bin/env python3
import random
winEas, loseEas, tieEas = 0.0, 0.0, 0.0

# Inisialisasi ulang matriks transisi (sama seperti sebelumnya)
buildTMatrix = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixL = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
buildTMatrixT = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
n = 3; m = 3
tMatrix = [[0]*m for _ in range(n)]
tMatrixL = [[0]*m for _ in range(n)]
tMatrixT = [[0]*m for _ in range(n)]
probabilitiesRPS = [1/3, 1/3, 1/3]

def markov():
    """Permainan interaktif manusia vs komputer dengan AI Markov."""
    global probabilitiesRPS
    choices = ["Rock","Paper","Scissors"]
    choi = ['r','p','s']
    continuePlaying = True
    prevChoice = ""   # akan diisi integer
    choice = 3
    # --- Input pertama ---
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
    except ValueError:
        print("you must enter an integer \n")
    # Validasi input
    if choice > 2 or choice < 0:
        print("You must enter an integer less than three and greater than 0\n")
        while choice > 2 or choice < 0:
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")
    # Gerakan komputer awal: random
    machineChoice = random.randint(0, 2)
    result = checkWin(choice, machineChoice, 1)   # mode 1 untuk update statistik
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machineChoice])
    print("You %s" % result)
    prevChoice = choice

    # --- Loop permainan ---
    while continuePlaying:
        choice = 3
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
            print("you must enter an integer \n")
        if (choice > 2 or choice < 0) and choice != 5:
            print("You must enter an integer less than three and greater than 0 or choose 5 to exit.\n")
            while (choice > 2 or choice < 0) and choice != 5:
                try:
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 5:
            print("Thanks for Playing!")
            print("You won %d times!" % int(winEas))
            print("You lost %d times!" % int(loseEas))
            print("You tied %d times!" % int(tieEas))
            total = winEas + loseEas + tieEas
            percentWon = "{percent:.2%}".format(percent=(winEas / total if total > 0 else 0))
            print("Your win percentage is %s from a total of %d games" % (percentWon, int(total)))
            continuePlaying = False
        else:
            # Update matriks transisi berdasarkan hasil sebelumnya
            transMatrix = buildTransitionProbabilities(prevChoice, choice, result)
            # Pilih gerakan komputer berdasarkan probabilitas Markov
            machineChoice = random.randint(1, 100)
            probabilitiesRPS[0] = transMatrix[prevChoice][0]
            probabilitiesRPS[1] = transMatrix[prevChoice][1]
            probabilitiesRPS[2] = transMatrix[prevChoice][2]
            rangeR = probabilitiesRPS[0] * 100
            rangeP = probabilitiesRPS[1] * 100 + rangeR
            if machineChoice <= rangeR:
                machineChoice = 1   # Kembali bug: seharusnya 0
            elif machineChoice <= rangeP:
                machineChoice = 2
            else:
                machineChoice = 0
            result = checkWin(choice, machineChoice, 1)
            prevChoice = choice
            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machineChoice])
            print("You %s" % result)
    # Tampilkan matriks transisi akhir (opsional)
    print("Your winning transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrix[0], tMatrix[1], tMatrix[2]))
    print("Your losing transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixL[0], tMatrixL[1], tMatrixL[2]))
    print("Your tying transition matrix is:\nr: %s\np: %s\ns: %s\n" % (tMatrixT[0], tMatrixT[1], tMatrixT[2]))

# Fungsi buildTransitionProbabilities, buildTransitionMatrix, checkWin (dengan parameter mode) sudah didefinisikan ulang di sini.
# Perbedaan checkWin di sel ini menerima parameter mode untuk update statistik.
def checkWin(user, machine, mode):
    """Sama seperti sebelumnya, tapi mode digunakan untuk memanggil checkStats."""
    win = False; tie = False
    # ... (logika sama seperti checkWin sebelumnya)
    # Setelah menentukan win/tie, panggil checkStats
    if tie:
        checkStats(2, mode)
        return "Tied!"
    elif win:
        checkStats(0, mode)
        return "Win!"
    else:
        checkStats(1, mode)
        return "Lose!"

def checkStats(wlt, modeChosen):
    """Update statistik global berdasarkan mode (1 untuk easy/human vs Markov)."""
    global winEas, loseEas, tieEas
    if modeChosen == 1:
        if wlt == 0:
            winEas += 1
        elif wlt == 1:
            loseEas += 1
        else:
            tieEas += 1

# markov()  # Dieksekusi di sel ini

# -----------------------------------------------------------------------------
# SEL 3: Game lengkap dengan berbagai mode (Beginner/Random, Intermediate/AI,
#        Expert/Markov, Super Hard, dan mode tersembunyi Big Bang)
# -----------------------------------------------------------------------------

#!/usr/bin/env python3
import random
# ANSI color codes untuk tampilan
X = '\033[0m'
Bold = '\033[1;36m'
HighB = '\033[1;44m'

# Statistik untuk setiap mode
winEas = loseEas = tieEas = 0.0
winInt = loseInt = tieInt = 0.0
winHard = loseHard = tieHard = 0.0
winExp = loseExp = tieExp = 0.0
winspec = losespec = tiespec = 0.0

hiddenfound = False

# Matriks transisi untuk mode Expert (RPS 3 pilihan)
buildTMatrix = {'rr':1,'rp':1,'rs':1,'pr':1,'pp':1,'ps':1,'sr':1,'sp':1,'ss':1}
buildTMatrixL = {'rr':1,'rp':1,'rs':1,'pr':1,'pp':1,'ps':1,'sr':1,'sp':1,'ss':1}
buildTMatrixT = {'rr':1,'rp':1,'rs':1,'pr':1,'pp':1,'ps':1,'sr':1,'sp':1,'ss':1}
n=3; m=3
tMatrix = [[0]*m for _ in range(n)]
tMatrixL = [[0]*m for _ in range(n)]
tMatrixT = [[0]*m for _ in range(n)]
probabilitiesRPS = [1/3,1/3,1/3]

# Matriks transisi untuk mode Big Bang (5 pilihan: Rock, Paper, Scissors, Lizard, Spock)
buildTMatrixrpsclsp = {'rr':1,'rp':1,'rsc':1,'rl':1,'rsp':1,'pr':1,'pp':1,'psc':1,'pl':1,'psp':1,
                       'scr':1,'scp':1,'scsc':1,'scl':1,'scsp':1,'lr':1,'lp':1,'lsc':1,'ll':1,'lsp':1,
                       'spr':1,'spp':1,'spsc':1,'spl':1,'spsp':1}
buildTMatrixLrpsclsp = dict(buildTMatrixrpsclsp)  # salinan untuk kalah
buildTMatrixTrpsclsp = dict(buildTMatrixrpsclsp)  # salinan untuk seri
sheldon = 5
cooper = 5
tMatrixrpsclsp = [[0]*sheldon for _ in range(cooper)]
tMatrixLrpsclsp = [[0]*sheldon for _ in range(cooper)]
tMatrixTrpsclsp = [[0]*sheldon for _ in range(cooper)]
probabilitiesrpsclsp = [1/5,1/5,1/5,1/5,1/5]

intro = """
Welcome to Rock Paper Scissors the Ultimate Version! There are four modes: Beginner, Intermediate, Expert, and Super Hard. Beginner is random, Intermediate uses AI, Expert uses Machine Learning, and Super Hard is... well... super hard.
P.S. There is a hidden mode that is pretty easy to figure out if you look at the code but thats no fun so try using your ingenuity to figure it out. Here's a hint: Bazinga!!!
"""
print(Bold)
print(intro)
print(X)

def chooseMode():
    """Meminta user memilih mode: 1=Beginner, 2=Intermediate, 3=Expert, 4=Super Hard, 73=Hidden Big Bang."""
    mode = 6
    try:
        mode = int(input("What Mode do you want to play in? 1: beginner, 2: intermediate, 3: expert, or 4: super hard? Enter a number \n"))
    except ValueError:
        print("you must enter an integer \n")
    if mode > 4 and mode != 73:
        print("You must enter an integer less than five \n")
        while mode > 4 and mode != 73:
            try:
                mode = int(input("What Mode do you want to play in? 1: begginner, 2: intermediate, 3: expert, or 4: super hard? Enter a number \n"))
            except ValueError:
                print("you must enter an integer \n")
    return mode

def easyMode():
    """Mode Beginner: komputer memilih secara acak (random)."""
    choices = ["Rock","Paper","Scissors"]
    continuePlaying = True
    # Input pertama
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
    except ValueError:
        print("you must enter an integer \n")
    # Validasi
    if choice > 2 or choice < 0:
        print("You must enter an integer less than three and greater than 0\n")
        while choice > 2 or choice < 0:
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")
    # Komputer random
    machineChoice = random.randint(0, 2)
    result = checkWin(choice, machineChoice, 1)  # mode 1 = easy
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machineChoice])
    print("You %s" % result)
    # Loop
    while continuePlaying:
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
            print("you must enter an integer \n")
        if (choice > 2 or choice < 0) and choice != 5:
            print("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
            while (choice > 2 or choice < 0) and choice != 5:
                try:
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 5:
            print("Thanks for Playing!")
            continuePlaying = False
        else:
            machineChoice = random.randint(0, 2)
            result = checkWin(choice, machineChoice, 1)
            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machineChoice])
            print("You %s" % result)

def intermediateMode():
    """Mode Intermediate: komputer menggunakan heuristik (bukan Markov murni) yang menyesuaikan dengan pola pemain."""
    choices = ["Rock","Paper","Scissors"]
    continuePlaying = True
    prevChoice = ""
    prevMachineChoice = ""
    result = ""
    streak = 0
    won = 0
    alt = 0
    numoff = 0
    choice = 3
    # Input pertama
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
    except ValueError:
        print("you must enter an integer \n")
    if choice > 2 or choice < 0:
        print("You must enter an integer less than three and greater than or equal to 0.\n")
        while choice > 2 or choice < 0:
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")
    # Komputer random untuk langkah pertama
    machineChoice = random.randint(0, 2)
    result = checkWin(choice, machineChoice, 2)  # mode 2 = intermediate
    if result == "Win!":
        won += 1
    else:
        numoff += 1
        if numoff == 3:
            won -= 3
            numoff = 0
        if won < 0:
            won = 0
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machineChoice])
    print("You %s" % result)
    prevChoice = choice
    prevMachineChoice = machineChoice
    streak += 1
    # Loop
    while continuePlaying:
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
            print("you must enter an integer \n")
        if (choice > 2 or choice < 0) and choice != 5:
            print("You must enter an integer less than three and greater than or equal to 0. Or put 5 to exit\n")
            while (choice > 2 or choice < 0) and choice != 5:
                try:
                    print("You must enter an integer less than three and greater than or equal to 0. Or put 5 to exit\n")
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 5:
            print("Thanks for Playing!")
            continuePlaying = False
        else:
            # Logika heuristik untuk menentukan gerakan komputer
            if prevChoice == choice:
                streak += 1
            else:
                streak -= 1
                if streak < 0:
                    streak = 0
            if streak > 3:
                machineChoice = prevChoice - 2
                if machineChoice < 0:
                    machineChoice += 3
            elif won > 9:
                print("Yo. Stop cheating...")
                machineChoice = random.randint(0,2)
            elif won > 3 and won < 10:
                machineChoice = prevChoice
            else:
                if result == "Win!":
                    machineChoice = prevChoice - 2
                    if machineChoice < 0:
                        machineChoice += 3
                elif result == "Lose!":
                    machineChoice = prevChoice + 1
                    if machineChoice > 2:
                        machineChoice -= 3
                    machineChoice -= 2
                    if machineChoice < 0:
                        machineChoice += 3
                else:
                    machineChoice = random.randint(0,2)
            result = checkWin(choice, machineChoice, 2)
            if result == "Win!":
                won += 1
            else:
                won -= 2
                if won < 0:
                    won = 0
            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machineChoice])
            print("You %s" % result)
            prevChoice = choice

def expertMode():
    """
    Mode Expert: komputer menggunakan Markov Chain (machine learning).
    Memperbarui matriks transisi berdasarkan hasil sebelumnya dan memilih gerakan
    dengan probabilitas tertinggi dari state sebelumnya.
    """
    global probabilitiesRPS
    choices = ["Rock","Paper","Scissors"]
    choi = ['r','p','s']
    continuePlaying = True
    prevChoice = ""
    choice = 3
    # Input pertama
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
    except ValueError:
        print("you must enter an integer \n")
    if choice > 2 or choice < 0:
        print("You must enter an integer less than three and greater than or equal to 0\n")
        while choice > 2 or choice < 0:
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")
    # Komputer random untuk langkah pertama
    machineChoice = random.randint(0, 2)
    result = checkWin(choice, machineChoice, 3)  # mode 3 = expert
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machineChoice])
    print("You %s" % result)
    prevChoice = choice
    # Loop
    while continuePlaying:
        choice = 3
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
            print("you must enter an integer \n")
        if (choice > 2 or choice < 0) and choice != 5:
            print("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
            while (choice > 2 or choice < 0) and choice != 5:
                try:
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 5:
            print("Thanks for Playing!\n")
            continuePlaying = False
        else:
            # Bangun matriks transisi berdasarkan hasil sebelumnya
            transMatrix = buildTransitionProbabilities(prevChoice, choice, result)
            # Pilih gerakan komputer berdasarkan probabilitas Markov
            machineChoice = random.randint(1, 100)
            probabilitiesRPS[0] = transMatrix[prevChoice][0]
            probabilitiesRPS[1] = transMatrix[prevChoice][1]
            probabilitiesRPS[2] = transMatrix[prevChoice][2]
            rangeR = probabilitiesRPS[0] * 100
            rangeP = probabilitiesRPS[1] * 100 + rangeR
            if machineChoice <= rangeR:
                machineChoice = 1   # Bug: seharusnya 0
            elif machineChoice <= rangeP:
                machineChoice = 2
            else:
                machineChoice = 0
            result = checkWin(choice, machineChoice, 3)
            prevChoice = choice
            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machineChoice])
            print("You %s" % result)

# Fungsi buildTransitionProbabilities, buildTransitionMatrix (untuk 3 pilihan) sama seperti sebelumnya
# (tidak diulang di sini untuk menghemat ruang, tetapi ada di kode asli)

def superHard():
    """Mode Super Hard: komputer selalu memilih gerakan yang mengalahkan pilihan pemain."""
    choices = ["Rock","Paper","Scissors"]
    continuePlaying = True
    result = ""
    print("I am going to play %s" % choices[random.randint(0,2)])  # Bluff
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
    except ValueError:
        print("you must enter an integer \n")
    if choice > 2 or choice < 0:
        print("You must enter an integer less than three and greater than or equal to 0\n")
        while choice > 2 or choice < 0:
            try:
                print("You must enter an integer less than three and greater than or equal to 0\n")
                choice = int(input("0: Rock, 1: Paper, 2: Scissors \n"))
            except ValueError:
                print("you must enter an integer \n")
    # Komputer memilih gerakan yang mengalahkan pemain: (choice+1) mod 3 ? Sebenarnya di sini choice-2.
    machineChoice = choice - 2
    if machineChoice < 0:
        machineChoice += 3
    result = checkWin(choice, machineChoice, 4)  # mode 4 = super hard
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machineChoice])
    print("You %s" % result)
    # Loop
    while continuePlaying:
        print("I am going to play %s" % choices[random.randint(0,2)])
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
        except ValueError:
            print("you must enter an integer \n")
        if (choice > 2 or choice < 0) and choice != 5:
            print("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
            while (choice > 2 or choice < 0) and choice != 5:
                try:
                    print("You must enter an integer less than three and greater than or equal to 0 or choose 5 to exit.\n")
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors, 5: exit \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 5:
            print("Giving up? How sad :(")
            continuePlaying = False
        else:
            machineChoice = choice - 2
            if machineChoice < 0:
                machineChoice += 3
            result = checkWin(choice, machineChoice, 4)
            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machineChoice])
            print("You %s" % result)

def bigbang():
    """
    Mode tersembunyi: Rock-Paper-Scissors-Lizard-Spock (dari The Big Bang Theory).
    Menggunakan Markov Chain dengan 5 pilihan.
    """
    global hiddenfound, probabilitiesRPS
    choices = ["Rock","Paper","Scissors","Lizard","Spock"]
    choi = ['r','p','sc','l','sp']
    continuePlaying = True
    prevChoice = ""
    choice = 8
    # Input pertama
    try:
        choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock \n"))
    except ValueError:
        print("you must enter an integer \n")
    if choice > 4 or choice < 0:
        print("You must enter an integer less than five and greater than or equal to 0\n")
        while choice > 4 or choice < 0:
            try:
                choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock \n"))
            except ValueError:
                print("you must enter an integer \n")
    # Komputer random untuk langkah pertama
    machineChoice = random.randint(0, 4)
    result = checkWin(choice, machineChoice, 73)  # mode 73 = bigbang
    print("You chose %s" % choices[choice])
    print("The machine chose %s" % choices[machineChoice])
    print("You %s" % result)
    prevChoice = choice
    # Loop
    while continuePlaying:
        choice = 8
        try:
            choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 7: exit \n"))
        except ValueError:
            print("you must enter an integer \n")
        if (choice > 4 or choice < 0) and choice != 7:
            print("You must enter an integer less than five and greater than or equal to 0 or choose 5 to exit.\n")
            while (choice > 4 or choice < 0) and choice != 7:
                try:
                    choice = int(input("0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 7: exit \n"))
                except ValueError:
                    print("you must enter an integer \n")
        if choice == 7:
            hiddenfound = True
            print("\033[1;36m\nThere's just no pleasing you, is there, Leonard?" + X)
            continuePlaying = False
        else:
            # Bangun matriks transisi untuk 5 pilihan
            transMatrix = buildTransitionProbabilitiesrpsclsp(prevChoice, choice, result)
            machineChoice = random.randint(1, 100)
            probabilitiesrpsclsp[0] = transMatrix[prevChoice][0]
            probabilitiesrpsclsp[1] = transMatrix[prevChoice][1]
            probabilitiesrpsclsp[2] = transMatrix[prevChoice][2]
            probabilitiesrpsclsp[3] = transMatrix[prevChoice][3]
            probabilitiesrpsclsp[4] = transMatrix[prevChoice][4]
            rangeR = probabilitiesrpsclsp[0] * 100
            rangeP = probabilitiesrpsclsp[1] * 100 + rangeR
            rangeSC = probabilitiesrpsclsp[2] * 100 + rangeP
            rangeL = probabilitiesrpsclsp[3] * 100 + rangeSC
            oneOrTwo = random.randint(1,2)
            if machineChoice <= rangeR:
                machineChoice = 1 if oneOrTwo == 1 else 4
            elif machineChoice <= rangeP:
                machineChoice = 2 if oneOrTwo == 1 else 3
            elif machineChoice <= rangeSC:
                machineChoice = 4 if oneOrTwo == 1 else 0
            elif machineChoice <= rangeL:
                machineChoice = 2 if oneOrTwo == 1 else 0
            else:
                machineChoice = 1 if oneOrTwo == 1 else 3
            result = checkWin(choice, machineChoice, 73)
            prevChoice = choice
            print("You chose %s" % choices[choice])
            print("The machine chose %s" % choices[machineChoice])
            print("You %s" % result)

# Fungsi buildTransitionProbabilitiesrpsclsp, buildTransitionMatrixrpsclsp, checkWin (dengan mode), checkStats, main, dll.
# (Implementasi lengkap ada di kode asli)

def main():
    """Fungsi utama: loop permainan, memilih mode, menampilkan statistik."""
    global winEas, loseEas, tieEas, winInt, loseInt, tieInt, winHard, loseHard, tieHard, winExp, loseExp, tieExp, winspec, losespec, tiespec, hiddenfound
    playAgain = True
    while playAgain:
        chosenMode = chooseMode()
        if chosenMode == 1:
            easyMode()
            # Tampilkan statistik mode Easy
            print(HighB)
            print("Your stats:")
            print(X)
            displaystats(winEas, loseEas, tieEas, "Easy Mode")
            displayOtherModes("Easy Mode")
        elif chosenMode == 2:
            intermediateMode()
            print(HighB)
            print("Your stats:")
            print(X)
            displaystats(winInt, loseInt, tieInt, "Intermediate Mode")
            displayOtherModes("Intermediate Mode")
        elif chosenMode == 3:
            expertMode()
            print(HighB)
            print("Your stats:")
            print(X)
            displaystats(winExp, loseExp, tieExp, "Expert Mode")
            displayOtherModes("Expert Mode")
        elif chosenMode == 4:
            superHard()
            print(HighB)
            print("Your stats:")
            print(X)
            displaystats(winHard, loseHard, tieHard, "Super Hard")
            displayOtherModes("Super Hard Mode")
        elif chosenMode == 73:
            bigbang()
            print(HighB)
            print("Your stats:")
            print(X)
            displaystats(winspec, losespec, tiespec, "Big Bang Mode")
            displayOtherModes("Big Bang Mode")
        else:
            print("I guess we will move on to whether or not ya wanna play again...\n")
        # Tanya apakah ingin bermain lagi
        notyesorno = True
        while notyesorno:
            continueGame = input("Do you wanna play again? Type Yes or No \n")
            if continueGame.lower() == "yes":
                print("Coolio. \n")
                notyesorno = False
                playAgain = True
            elif continueGame.lower() == "no":
                print("Aw that's too bad. :( \n")
                finalstats()
                notyesorno = False
                playAgain = False
            else:
                print("Nah... That's not an acceptable answer. Please type Yes or No")
                notyesorno = True

def displaystats(wmode, lmode, tmode, mode):
    """Menampilkan statistik untuk suatu mode."""
    print("\nYou won %d times!\n" % int(wmode))
    print("You lost %d times!\n" % int(lmode))
    print("You tied %d times!\n" % int(tmode))
    total = wmode + lmode + tmode
    percentWon = "{percent:.2%}".format(percent=(wmode / total if total > 0 else 0))
    print("You have a %s win rate on %s! \n" % (percentWon, mode))

def displayOtherModes(mode):
    """Menampilkan statistik dari mode lain (selain yang sedang dimainkan)."""
    global winEas,loseEas,tieEas,winInt,loseInt,tieInt,winHard,loseHard,tieHard,winExp,loseExp,tieExp,winspec,losespec,tiespec,hiddenfound
    modes = ["Easy Mode", "Intermediate Mode","Expert Mode","Super Hard Mode","Big Bang Mode"]
    print(HighB)
    print("Your stats in other modes:")
    print(X)
    if not hiddenfound:
        for m in modes:
            if m != mode:
                print(Bold)
                if m != "Big Bang Mode":
                    print(m)
                else:
                    print("Hidden Mode not yet discovered!!!")
                print(X)
                if m == "Easy Mode":
                    displaystats(winEas,loseEas,tieEas,"Easy Mode")
                elif m == "Intermediate Mode":
                    displaystats(winInt,loseInt,tieInt,"Intermediate Mode")
                elif m == "Expert Mode":
                    displaystats(winExp,loseExp,tieExp,"Expert Mode")
                elif m == "Super Hard Mode":
                    displaystats(winHard,loseHard,tieHard,"Super Hard Mode")
    else:
        for m in modes:
            if m != mode:
                print(Bold)
                print(m)
                print(X)
                if m == "Easy Mode":
                    displaystats(winEas,loseEas,tieEas,"Easy Mode")
                elif m == "Intermediate Mode":
                    displaystats(winInt,loseInt,tieInt,"Intermediate Mode")
                elif m == "Expert Mode":
                    displaystats(winExp,loseExp,tieExp,"Expert Mode")
                elif m == "Super Hard Mode":
                    displaystats(winHard,loseHard,tieHard,"Super Hard Mode")
                elif m == "Big Bang Mode":
                    displaystats(winspec,losespec,tiespec,"Big Bang Mode")

def finalstats():
    """Menampilkan statistik akhir semua mode saat keluar."""
    global winEas,loseEas,tieEas,winInt,loseInt,tieInt,winHard,loseHard,tieHard,winExp,loseExp,tieExp,winspec,losespec,tiespec,hiddenfound
    print(HighB)
    print("These are your final stats:")
    print(X)
    # Hitung persentase kemenangan untuk setiap mode
    def percent(win, loss, tie):
        total = win+loss+tie
        return "{percent:.2%}".format(percent=(win/total if total>0 else 0))
    print(Bold)
    print("You have a %s win rate on Easy Mode!" % percent(winEas,loseEas,tieEas))
    print("You have a %s win rate on Intermediate Mode!" % percent(winInt,loseInt,tieInt))
    print("You have a %s win rate on Expert Mode!" % percent(winExp,loseExp,tieExp))
    print("You have a %s win rate on Super Hard Mode!" % percent(winHard,loseHard,tieHard))
    if not hiddenfound:
        print("YOU NEVER FOUND THE HIDDEN MODE SCRUB!!!")
    else:
        print("You have a %s win rate on Big Bang Mode!" % percent(winspec,losespec,tiespec))
    print(X)

# Fungsi checkWin dan checkStats yang sudah disesuaikan dengan mode (1-4,73)
# (Implementasi lengkap ada di kode asli)

# Memulai program
main()