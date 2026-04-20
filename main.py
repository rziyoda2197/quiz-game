import random

class Quiz:
    def __init__(self):
        self.sovarlar = {
            "Matematika": {
                "Q1": "2+2?",
                "Q2": "5-3?",
                "Q3": "7*2?",
                "Q4": "10/2?",
                "Q5": "8-4?"
            },
            "Tarix": {
                "Q1": "Qayta tiklangan Sovet Ittifoqi qachon tuzilgan?",
                "Q2": "Sovet Ittifoqi qachon parchalanib ketgan?",
                "Q3": "Sovet Ittifoqi qachon tugagan?",
                "Q4": "Sovet Ittifoqi qachon tuzilgan?",
                "Q5": "Sovet Ittifoqi qachon parchalanib ketgan?"
            },
            "Fizika": {
                "Q1": "1 kg massali jismning kuchlanishi qancha?",
                "Q2": "1 kg massali jismning tezligi qancha?",
                "Q3": "1 kg massali jismning energiyasi qancha?",
                "Q4": "1 kg massali jismning kuchlanishi qancha?",
                "Q5": "1 kg massali jismning tezligi qancha?"
            }
        }

    def oyna(self):
        sovarlar = list(self.sovarlar.keys())
        sovar = random.choice(sovarlar)
        savollar = list(self.sovarlar[sovar].keys())
        savol = random.choice(savollar)
        javob = input(f"{sovar}: {self.sovarlar[sovar][savol]}\n")
        if javob == str(eval(self.sovarlar[sovar][savol])):
            print("To'gri javob!")
        else:
            print(f"Xato! To'gri javob {eval(self.sovarlar[sovar][savol])}")

    def boshlash(self):
        while True:
            print("1. O'ynash")
            print("2. Chiqish")
            tanlov = input("Izoh: ")
            if tanlov == "1":
                self.oyna()
            elif tanlov == "2":
                break
            else:
                print("Xato tanlov!")

quiz = Quiz()
quiz.boshlash()
