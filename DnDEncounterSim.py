#Created by Jordan Henry
# This program is not associated with Wizards of the Coast, or any other company, and is unofficial fan content under the Fan Content Policy.
# This means this program is not endorsed by Wizards of the Coast, and some materials used such as the game mechanics and classes are property of Wizards of the Coast.
# This progam is not the full experience of Dungeons and Dragons, and so you will need to purchase the relevant material from an approved vendor

import random
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

duelingFighter = {
    "hp": 36,
    "ac": 16,
    "hitDC": 9,
    "attackDiceAmount": 1,
    "attackDiceValue": 8,
    "attackBonus": 6,
    "initiative": 2,
}

twoHandedFighter = {
    "hp": 36,
    "ac": 16,
    "hitDC": 6,
    "attackDiceAmount": 1,
    "attack1DiceValue": 6,
    "attack2DiceValue": 4,
    "attackBonus": 4,
    "initiative": 4,
}

defenseFighter = {
    "hp": 36,
    "ac": 21,
    "hitDC": 6,
    "attackDiceAmount": 1,
    "attackDiceValue": 8,
    "attackBonus": 4,
    "initiative": 2,
}

print("******************************************************************")
print("               Welcome to the DnD Fighter Simulator")
option = int(0)


def option1():
    print("Running dueling fighter vs two-handed (dex) fighter...")
    # Reset counting variables n prep 1000 loop
    encounter = int(0)

    # Dueler specific
    duelDamage = int(0)
    duelCRIT = int(0)
    duelWin = int(0)
    duelHit = int(0)
    duelMiss = int(0)
    duelFirst = int(0)

    # Two-handed specific
    twoDamage = int(0)
    twoCRIT = int(0)
    twoWin = int(0)
    twoHit = int(0)
    twoMiss = int(0)
    twoFirst = int(0)
    while encounter < 1000:
        print("Encounter: " + str(encounter + 1))
        # reset hp of fighters, and roll for their initiative to see who goes first
        duelingFighter["hp"] = 36
        duelInit = random.randint(1, 20) + duelingFighter["initiative"]
        twoHandedFighter["hp"] = 36
        twoInit = random.randint(1, 20) + twoHandedFighter["initiative"]
        if duelInit > twoInit:
            # duel goes first
            duelFirst += 1
            while duelingFighter["hp"] > 0 or twoHandedFighter["hp"] > 0:

                ###Dueling Fighter's Turn###

                duelAttack = random.randint(1, 20) + duelingFighter["hitDC"]
                # if CRIT, more damage applied
                if duelAttack - duelingFighter["hitDC"] == 20 or duelAttack - duelingFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            duelingFighter[
                                                                                                                "attackDiceValue"]) +
                                      duelingFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    duelCRIT += 1
                    if twoHandedFighter["hp"] <= 0:
                        print("Dueling fighter wins!")
                        duelWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif duelAttack >= twoHandedFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, duelingFighter["attackDiceValue"]) + duelingFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    if twoHandedFighter["hp"] <= 0:
                        duelWin += 1
                        print("Dueling fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    duelMiss += 1
                    print("Dueling fighter misses...")

                ###Two-Handed Fighter's Turn###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack1DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= duelingFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if duelingFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                    ###Two-Weapon Fighting Attack###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("NAT 20! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack2DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= duelingFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if duelingFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

        elif duelInit < twoInit:
            # twoInit goes first
            twoFirst += 1
            while duelingFighter["hp"] > 0 or twoHandedFighter["hp"] > 0:
                ###Two-Handed Fighter's Turn###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack1DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= duelingFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if duelingFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                    ###Two-Weapon Fighting Attack###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack2DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= duelingFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if duelingFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("TwoHanded fighter misses...")

                ###Dueling Fighter's Turn###

                duelAttack = random.randint(1, 20) + duelingFighter["hitDC"]
                # if CRIT, more damage applied
                if duelAttack - duelingFighter["hitDC"] == 20 or duelAttack - duelingFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            duelingFighter[
                                                                                                                "attackDiceValue"]) +
                                      duelingFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    duelCRIT += 1
                    if twoHandedFighter["hp"] <= 0:
                        print("Dueling fighter wins!")
                        duelWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif duelAttack >= twoHandedFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, duelingFighter["attackDiceValue"]) + duelingFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    if twoHandedFighter["hp"] <= 0:
                        duelWin += 1
                        print("Dueling fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    duelMiss += 1
                    print("Dueling fighter misses...")

        else:
            # TwoInit goes first as higher dex
            twoFirst += 1
            while duelingFighter["hp"] > 0 or twoHandedFighter["hp"] > 0:
                ###Two-Handed Fighter's Turn###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack1DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= duelingFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if duelingFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("TwoHanded fighter misses...")

                    ###Two-Weapon Fighting Attack###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack2DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= duelingFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    duelingFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if duelingFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                ###Dueling Fighter's Turn###

                duelAttack = random.randint(1, 20) + duelingFighter["hitDC"]
                # if CRIT, more damage applied
                if duelAttack - duelingFighter["hitDC"] == 20 or duelAttack - duelingFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            duelingFighter[
                                                                                                                "attackDiceValue"]) +
                                      duelingFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    duelCRIT += 1
                    if twoHandedFighter["hp"] <= 0:
                        print("Dueling fighter wins!")
                        duelWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif duelAttack >= twoHandedFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, duelingFighter["attackDiceValue"]) + duelingFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    if twoHandedFighter["hp"] <= 0:
                        duelWin += 1
                        print("Dueling fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    duelMiss += 1
                    print("Dueling fighter misses...")
        encounter += 1

    print("******************************************************************")
    print("                       Testing finished")
    print("******************************************************************")

    print("Dueling fighter wins: " + str(duelWin))
    print("Dueling fighter win %: " + str(duelWin / 1000 * 100))
    print("Two-Handed fighter wins: " + str(twoWin))
    print("Two-Handed fighter win %: " + str(twoWin / 1000 * 100))
    print("Dueling fighter first strikes: " + str(duelFirst))
    print("Two-Handed fighter first strikes: " + str(twoFirst))
    print("Dueling fighter total damage: " + str(duelDamage))
    print("Two-Handed fighter total damage: " + str(twoDamage))
    print("Dueling fighter hits: " + str(duelHit))
    print("Dueling fighter misses: " + str(duelMiss))
    print("Two-Handed fighter hits: " + str(twoHit))
    print("Two-Handed fighter misses: " + str(twoMiss))
    print("Dueling fighter CRITs: " + str(duelCRIT))
    print("Two-Handed fighter CRITs: " + str(twoCRIT))

    # CSV Writing as a Dictionary
    fieldnames = ['Name', 'Wins', 'First_Strikes', 'Hits', 'Misses', 'Critical_Hits']
    data = [
        {'Name': 'DexFighter', 'Wins': twoWin, 'First_Strikes': twoFirst, 'Hits': twoHit, 'Misses': twoMiss,
         'Critical_Hits': twoCRIT},
        {'Name': 'DuelFighter', 'Wins': duelWin, 'First_Strikes': duelFirst, 'Hits': duelHit, 'Misses': duelMiss,
         'Critical_Hits': duelCRIT},

    ]
    with open("dexVSduelLog.csv", "w") as f:

        defDexLogWrite = csv.DictWriter(f, fieldnames=fieldnames)
        defDexLogWrite.writeheader()
        defDexLogWrite.writerows(data)
        print("File dexVSduelLog.csv has been made")


def option2():
    print("Running defensive fighter vs Dueling fighter...")
    # Reset counting variables n prep 1000 loop
    encounter = int(0)

    # Dueler specific
    defDamage = int(0)
    defCRIT = int(0)
    defWin = int(0)
    defHit = int(0)
    defMiss = int(0)
    defFirst = int(0)

    # dueling specific
    duelDamage = int(0)
    duelCRIT = int(0)
    duelWin = int(0)
    duelHit = int(0)
    duelMiss = int(0)
    duelFirst = int(0)
    while encounter < 1000:
        print("Encounter: " + str(encounter + 1))
        # reset hp of fighters
        defenseFighter["hp"] = 36
        defInit = random.randint(1, 20) + defenseFighter["initiative"]
        duelingFighter["hp"] = 36
        duelInit = random.randint(1, 20) + duelingFighter["initiative"]
        if defInit > duelInit:
            # duel goes first
            defFirst += 1
            print("defInit > duelInit")
            while defenseFighter["hp"] > 0 or duelingFighter["hp"] > 0:

                ###DefenseFighter's Turn###

                defAttack = random.randint(1, 20) + defenseFighter["hitDC"]
                # if CRIT, more damage applied
                if defAttack - defenseFighter["hitDC"] == 20 or defAttack - defenseFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, defenseFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            defenseFighter[
                                                                                                                "attackDiceValue"]) +
                                      defenseFighter["attackBonus"])
                    duelingFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    defCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Defense fighter wins!")
                        defWin += 1
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif defAttack >= duelingFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, defenseFighter["attackDiceValue"]) + defenseFighter["attackBonus"])
                    duelingFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    if duelingFighter["hp"] <= 0:
                        defWin += 1
                        print("Defense fighter wins!")
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                else:
                    defMiss += 1
                    print("Defense fighter misses...")

                ###Dueling Fighter's Turn###

                duelAttack = random.randint(1, 20) + duelingFighter["hitDC"]
                # if CRIT, more damage applied
                if duelAttack - duelingFighter["hitDC"] == 20 or duelAttack - duelingFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            duelingFighter[
                                                                                                                "attackDiceValue"]) +
                                      duelingFighter["attackBonus"])
                    defenseFighter["hp"] -= duelDamageTemp
                    print("Two-Handed fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    duelCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Dueling fighter wins!")
                        duelWin += 1
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif duelAttack >= defenseFighter["ac"]:
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + duelingFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    if defenseFighter["hp"] <= 0:
                        duelWin += 1
                        print("Dueling fighter wins!")
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                else:
                    duelMiss += 1
                    print("Dueling fighter misses...")

        elif defInit < duelInit:
            # duelInit goes first
            duelFirst += 1
            print("defInit < duelInit")
            while defenseFighter["hp"] > 0 or duelingFighter["hp"] > 0:
                ###Dueling Fighter's Turn###

                duelAttack = random.randint(1, 20) + duelingFighter["hitDC"]
                # if CRIT, more damage applied
                if duelAttack - duelingFighter["hitDC"] == 20 or duelAttack - duelingFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            duelingFighter[
                                                                                                                "attackDiceValue"]) +
                                      duelingFighter["attackBonus"])
                    defenseFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    duelCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Dueling fighter wins!")
                        duelWin += 1
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif duelAttack >= defenseFighter["ac"]:
                    duelDamageTemp = (random.randint(1, duelingFighter["attackDiceValue"]) + duelingFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= duelDamageTemp
                    print("Dueling fighter hits and deals " + str(duelDamageTemp) + ".")
                    duelDamage += duelDamageTemp
                    duelHit += 1
                    if defenseFighter["hp"] <= 0:
                        duelWin += 1
                        print("Dueling fighter wins!")
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                else:
                    duelMiss += 1
                    print("Dueling fighter misses...")

                ###Defense Fighter's Turn###

                defAttack = random.randint(1, 20) + defenseFighter["hitDC"]
                # if CRIT, more damage applied
                if defAttack - defenseFighter["hitDC"] == 20 or defAttack - defenseFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, defenseFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            defenseFighter[
                                                                                                                "attackDiceValue"]) +
                                      defenseFighter["attackBonus"])
                    duelingFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    defCRIT += 1
                    if duelingFighter["hp"] <= 0:
                        print("Defense fighter wins!")
                        defWin += 1
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif defAttack >= duelingFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, defenseFighter["attackDiceValue"]) + defenseFighter["attackBonus"])
                    duelingFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    if duelingFighter["hp"] <= 0:
                        defWin += 1
                        print("Defense fighter wins!")
                        encounter += 1
                        break
                    else:
                        print("Opponent still stands")
                else:
                    defMiss += 1
                    print("Defense fighter misses...")

        else:
            # As both have some dex, skip over else and reroll
            # encounter count done on a win by win case to make up for this
            print("Same initiative, REROLL!")

    print("******************************************************************")
    print("                       Testing finished")
    print("******************************************************************")

    print("Defense fighter wins: " + str(defWin))
    print("Defense fighter win %: " + str(defWin / 1000 * 100))
    print("Dueling fighter wins: " + str(duelWin))
    print("Dueling fighter win %: " + str(duelWin / 1000 * 100))
    print("Defense fighter first strikes: " + str(defFirst))
    print("Dueling fighter first strikes: " + str(duelFirst))
    print("Defense fighter total damage: " + str(defDamage))
    print("Dueling fighter total damage: " + str(duelDamage))
    print("Defense fighter hits: " + str(defHit))
    print("Defense fighter misses: " + str(defMiss))
    print("Dueling fighter hits: " + str(duelHit))
    print("Dueling fighter misses: " + str(duelMiss))
    print("Defense fighter CRITs: " + str(defCRIT))
    print("Dueling fighter CRITs: " + str(duelCRIT))

    # CSV Writing as a Dictionary
    fieldnames = ['Name', 'Wins', 'First_Strikes', 'Hits', 'Misses', 'Critical_Hits']
    data = [
        {'Name': 'DefFighter', 'Wins': defWin, 'First_Strikes': defFirst, 'Hits': defHit, 'Misses': defMiss,
         'Critical_Hits': defCRIT},
        {'Name': 'DuelFighter', 'Wins': duelWin, 'First_Strikes': duelFirst, 'Hits': duelHit, 'Misses': duelMiss,
         'Critical_Hits': duelCRIT}
    ]
    with open("defVSduelLog.csv", "w") as f:

        defDexLogWrite = csv.DictWriter(f, fieldnames=fieldnames)
        defDexLogWrite.writeheader()
        defDexLogWrite.writerows(data)
        print("File defVSduelLog.csv has been made")


def option3():
    print("Running defensive fighter vs two-handed (dex) fighter...")
    # Reset counting variables n prep 1000 loop
    encounter = int(0)

    # Defense specific
    defDamage = int(0)
    defCRIT = int(0)
    defWin = int(0)
    defHit = int(0)
    defMiss = int(0)
    defFirst = int(0)

    # Two-handed specific
    twoDamage = int(0)
    twoCRIT = int(0)
    twoWin = int(0)
    twoHit = int(0)
    twoMiss = int(0)
    twoFirst = int(0)
    while encounter < 1000:
        print("Encounter: " + str(encounter + 1))
        # reset hp of fighters
        defenseFighter["hp"] = 36
        defInit = random.randint(1, 20) + defenseFighter["initiative"]
        twoHandedFighter["hp"] = 36
        twoInit = random.randint(1, 20) + twoHandedFighter["initiative"]
        if defInit > twoInit:
            # Def goes first
            defFirst += 1
            print("defInit > twoInit")
            while defenseFighter["hp"] > 0 or twoHandedFighter["hp"] > 0:

                ###DefenseFighter's Turn###

                defAttack = random.randint(1, 20) + defenseFighter["hitDC"]
                # if CRIT, more damage applied
                if defAttack - defenseFighter["hitDC"] == 20 or defAttack - defenseFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    defDamageTemp = (random.randint(1, defenseFighter["attackDiceValue"]) + random.randint(1,
                                                                                                           defenseFighter[
                                                                                                               "attackDiceValue"]) +
                                     defenseFighter["attackBonus"])
                    twoHandedFighter["hp"] -= defDamageTemp
                    print("Defense fighter hits and deals " + str(defDamageTemp) + ".")
                    defDamage += defDamageTemp
                    defHit += 1
                    defCRIT += 1
                    if twoHandedFighter["hp"] <= 0:
                        print("Defense fighter wins!")
                        defWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif defAttack >= twoHandedFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, defenseFighter["attackDiceValue"]) + defenseFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    if twoHandedFighter["hp"] <= 0:
                        defWin += 1
                        print("Defense fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    defMiss += 1
                    print("Defense fighter misses...")

                ###Two-Handed Fighter's Turn###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack1DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= defenseFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if defenseFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                    ###Two-Weapon Fighting Attack###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("NAT 20! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack2DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= defenseFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if defenseFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

        elif defInit < twoInit:
            # twoInit goes first
            twoFirst += 1
            print("defInit < twoInit")
            while defenseFighter["hp"] > 0 or twoHandedFighter["hp"] > 0:
                ###Two-Handed Fighter's Turn###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack1DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= defenseFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if defenseFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                    ###Two-Weapon Fighting Attack###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack2DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= defenseFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if defenseFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                ###Defense Fighter's Turn###

                defAttack = random.randint(1, 20) + defenseFighter["hitDC"]
                # if CRIT, more damage applied
                if defAttack - defenseFighter["hitDC"] == 20 or defAttack - defenseFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    defDamageTemp = (random.randint(1, defenseFighter["attackDiceValue"]) + random.randint(1,
                                                                                                           defenseFighter[
                                                                                                               "attackDiceValue"]) +
                                     defenseFighter["attackBonus"])
                    twoHandedFighter["hp"] -= defDamageTemp
                    print("Defense fighter hits and deals " + str(defDamageTemp) + ".")
                    defDamage += defDamageTemp
                    defHit += 1
                    defCRIT += 1
                    if twoHandedFighter["hp"] <= 0:
                        print("Defense fighter wins!")
                        defWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif defAttack >= twoHandedFighter["ac"]:
                    duelDamageTemp = (
                            random.randint(1, defenseFighter["attackDiceValue"]) + defenseFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    if twoHandedFighter["hp"] <= 0:
                        defWin += 1
                        print("Defense fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    defMiss += 1
                    print("Defense fighter misses...")

        else:
            # TwoInit goes first as higher dex
            twoFirst += 1
            print("else")
            while defenseFighter["hp"] > 0 or twoHandedFighter["hp"] > 0:
                ###Two-Handed Fighter's Turn###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack1DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= defenseFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack1DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if defenseFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                    ###Two-Weapon Fighting Attack###

                twoAttack = random.randint(1, 20) + twoHandedFighter["hitDC"]
                # if CRIT, more damage applied
                if twoAttack - twoHandedFighter["hitDC"] == 20 or twoAttack - twoHandedFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + random.randint(1,
                                                                                                              twoHandedFighter[
                                                                                                                  "attack2DiceValue"]) +
                                     twoHandedFighter["attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    twoCRIT += 1
                    if defenseFighter["hp"] <= 0:
                        print("Two-Handed fighter wins!")
                        twoWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif twoAttack >= defenseFighter["ac"]:
                    twoDamageTemp = (random.randint(1, twoHandedFighter["attack2DiceValue"]) + twoHandedFighter[
                        "attackBonus"])
                    defenseFighter["hp"] -= twoDamageTemp
                    print("Two-Handed fighter hits and deals " + str(twoDamageTemp) + ".")
                    twoDamage += twoDamageTemp
                    twoHit += 1
                    if defenseFighter["hp"] <= 0:
                        twoWin += 1
                        print("Two-Handed fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    twoMiss += 1
                    print("Two-Handed fighter misses...")

                ###Defense Fighter's Turn###

                defAttack = random.randint(1, 20) + defenseFighter["hitDC"]
                # if CRIT, more damage applied
                if defAttack - defenseFighter["hitDC"] == 20 or defAttack - defenseFighter["hitDC"] == 19:
                    print("CRIT! ATTACK DICE DOUBLED!")
                    duelDamageTemp = (random.randint(1, defenseFighter["attackDiceValue"]) + random.randint(1,
                                                                                                            defenseFighter[
                                                                                                                "attackDiceValue"]) +
                                      defenseFighter["attackBonus"])
                    twoHandedFighter["hp"] -= duelDamageTemp
                    print("Defense fighter hits and deals " + str(duelDamageTemp) + ".")
                    defDamage += duelDamageTemp
                    defHit += 1
                    defCRIT += 1
                    if twoHandedFighter["hp"] <= 0:
                        print("Defense fighter wins!")
                        defWin += 1
                        break
                    else:
                        print("Opponent still stands")
                # checks if without CRIT, the target is hit
                elif defAttack >= twoHandedFighter["ac"]:
                    defDamageTemp = (
                            random.randint(1, defenseFighter["attackDiceValue"]) + defenseFighter["attackBonus"])
                    twoHandedFighter["hp"] -= defDamageTemp
                    print("Defense fighter hits and deals " + str(defDamageTemp) + ".")
                    defDamage += defDamageTemp
                    defHit += 1
                    if twoHandedFighter["hp"] <= 0:
                        defWin += 1
                        print("Defense fighter wins!")
                        break
                    else:
                        print("Opponent still stands")
                else:
                    defMiss += 1
                    print("Defense fighter misses...")
        encounter += 1

    print("******************************************************************")
    print("                       Testing finished")
    print("******************************************************************")

    print("Defense fighter wins: " + str(defWin))
    print("Defense fighter win %: " + str(defWin / 1000 * 100))
    print("Two-Handed fighter wins: " + str(twoWin))
    print("Two-Handed fighter win %: " + str(twoWin / 1000 * 100))
    print("Defense fighter first strikes: " + str(defFirst))
    print("Two-Handed fighter first strikes: " + str(twoFirst))
    print("Defense fighter total damage: " + str(defDamage))
    print("Two-Handed fighter total damage: " + str(twoDamage))
    print("Defense fighter hits: " + str(defHit))
    print("Defense fighter misses: " + str(defMiss))
    print("Two-Handed fighter hits: " + str(twoHit))
    print("Two-Handed fighter misses: " + str(twoMiss))
    print("Defense fighter CRITs: " + str(defCRIT))
    print("Two-Handed fighter CRITs: " + str(twoCRIT))

    # CSV Writing as a Dictionary
    fieldnames = ['Name', 'Wins', 'First_Strikes', 'Hits', 'Misses', 'Critical_Hits']
    data = [
        {'Name': 'DexFighter', 'Wins': twoWin, 'First_Strikes': twoFirst, 'Hits': twoHit, 'Misses': twoMiss,
         'Critical_Hits': twoCRIT},
        {'Name': 'DefFighter', 'Wins': defWin, 'First_Strikes': defFirst, 'Hits': defHit, 'Misses': defMiss,
         'Critical_Hits': defCRIT}
    ]
    with open("defVSdexLog.csv", "w") as f:

        defDexLogWrite = csv.DictWriter(f, fieldnames=fieldnames)
        defDexLogWrite.writeheader()
        defDexLogWrite.writerows(data)
        print("File defVSdexLog.csv has been made")


def option4():
    visualise = 0
    while visualise != 9:
        print("******************************************************************")
        print("            Please choose one of the following options:")
        print("******************************************************************")
        print("1. Dueling fighter vs two-handed (dex) fighter")
        print("2. Defensive fighter vs dueling fighter")
        print("3. Two-handed (dex) fighter vs defensive fighter")
        print("9. Back")

        ### NOTE: csvFile requires an absolute path, when running on another machine, please replace the path with the one respective to each file

        visualise = input("Selection: ")
        if visualise == "1":
            sns.set_context('paper')

            # Load Dataset
            csvFile = pd.read_csv(
                # SET OWN PATH TO WHERE YOU WOULD LIKE TO STORE THE CSV FILES
                "...\\dexVSduelLog.csv",
                index_col=0)

            # Plots the data to a bar graph
            csvFile.T.plot.bar()

            plt.title('Dexterity vs Duelling Fighter')
            plt.show()
            return

        elif visualise == "2":
            sns.set_context('paper')

            # Load Dataset
            csvFile = pd.read_csv(
                # SET OWN PATH TO WHERE YOU WOULD LIKE TO STORE THE CSV FILES
                "...\\defVSduelLog.csv",
                index_col=0)

            # Plots the data to a bar graph
            csvFile.T.plot.bar()

            plt.title('Defensive vs Duelling Fighter')
            plt.show()
            return

        elif visualise == "3":
            sns.set_context('paper')

            # Load Dataset
            csvFile = pd.read_csv(
                #SET OWN PATH TO WHERE YOU WOULD LIKE TO STORE THE CSV FILES
                "...\\defVSdexLog.csv",
                index_col=0)

            # Plots the data to a bar graph
            csvFile.T.plot.bar()

            plt.title('Defensive vs Dexterity Fighter')
            plt.show()
            return
        elif visualise == "9":
            break
        else:
            print("Not a valid input, please try again")


while option != 9:
    print("******************************************************************")
    print("            Please choose one of the following options:")
    print("******************************************************************")
    print("1. Dueling fighter vs two-handed (dex) fighter")
    print("2. Defensive fighter vs dueling fighter")
    print("3. Two-handed (dex) fighter vs defensive fighter")
    print("4. Visualise data")
    print("9. Quit")

    option = input("Selection: ")

    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "9":
        break
    else:
        print("Not a valid input, please try again")

print("Thank you for using the DnD Fighter Simulator")
