import random

values = 32*[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
random.shuffle(values)
banker = 0
player = 0
tie = 0
while len(values) > 22:
    bh = 0
    ph = 0
    counter = 0
    first_bhloc = random.randint(0,len(values)-1)
    first_bh = values[first_bhloc]
    bh += first_bh
    del values[first_bhloc]
    second_bhloc = random.randint(0, len(values) - 1)
    second_bh = values[second_bhloc]
    bh += second_bh
    del values[second_bhloc]
    first_phloc = random.randint(0, len(values) - 1)
    first_ph = values[first_phloc]
    ph += first_ph
    del values[first_phloc]
    second_phloc = random.randint(0, len(values) - 1)
    second_ph = values[second_phloc]
    ph += second_ph
    del values[second_phloc]
    if bh >= 10:
        bh -= 10
    if ph >= 10:
        ph -= 10
    if ph >= 8 or bh >= 8:
        if ph > bh:
            player += 1
        if bh > ph:
            banker += 1
        if bh == ph:
            tie += 1
        print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
        continue
    if ph in [6,7]:
        if bh in [6,7]:
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
        else:
            third_bhloc = random.randint(0, len(values) - 1)
            third_bh = values[third_bhloc]
            bh += third_bh
            del values[third_bhloc]
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
    if ph <= 5:
        third_phloc = random.randint(0, len(values) - 1)
        third_ph = values[third_phloc]
        ph += third_ph
        del values[third_phloc]
        counter = third_ph
        if bh <= 2:
            third_bhloc = random.randint(0, len(values) - 1)
            third_bh = values[third_bhloc]
            bh += third_bh
            del values[third_bhloc]
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
        if bh == 3 and counter != 8:
            third_bhloc = random.randint(0, len(values) - 1)
            third_bh = values[third_bhloc]
            bh += third_bh
            del values[third_bhloc]
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
        if bh == 4 and counter in [2,3,4,5,6,7]:
            third_bhloc = random.randint(0, len(values) - 1)
            third_bh = values[third_bhloc]
            bh += third_bh
            del values[third_bhloc]
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
        if bh == 5 and counter in [4,5,6,7]:
            third_bhloc = random.randint(0, len(values) - 1)
            third_bh = values[third_bhloc]
            bh += third_bh
            del values[third_bhloc]
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
        if bh == 6 and counter in [6,7]:
            third_bhloc = random.randint(0, len(values) - 1)
            third_bh = values[third_bhloc]
            bh += third_bh
            del values[third_bhloc]
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
        else:
            if bh >= 10:
                bh -= 10
            if ph >= 10:
                ph -= 10
            if ph > bh:
                player += 1
            if bh > ph:
                banker += 1
            if bh == ph:
                tie += 1
            print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
            continue
print("This round, Banker has scored " + str(bh) + " and Player has scored " + str(ph) + ".\nThe points total is now Banker: " + str(banker) + " vs Player: " + str(player) + " and Ties: " + str(tie) + "\n")
tooot = banker + player + tie
print("Total hands in shoe: " + str(tooot))

