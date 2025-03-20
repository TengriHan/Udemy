print(f"""
{"-" * 80}
Haftanın günü (Pazartesi, Salı, …) 
girilince, o günün haftanın kaçıncı günü olduğunu bulan program.
{"-" * 80}
""")

days = {
    "Pazartesi": 1, "Salı": 2, "Çarşamba": 3,
    "Perşembe": 4, "Cuma": 5, "Cumartesi": 6, "Pazar": 7
}

day = input("Haftanın bir gününü giriniz: ").capitalize()

if day in days:
    print(f"{day}, haftanın {days[day]}. günüdür.")
else:
    print("Geçerli bir gün ismi giriniz!")
