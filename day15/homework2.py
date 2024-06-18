#მოსწავლეს შემოატანინეთ სკოლის ტესტში მიღებული ნიშანი, თუ ეს მიღებული ნიშანი უდრის 10 - ს, მაგ შემთხვევაში მასწავლებელმა, მშობელთან შეაქოს მოსწავლე, თუ მიღებული ნიშანი უდრის 8 -ს ან 9 - ს, მაგ შემთხვევაში, მასწავლებელმა, მშობელს პატარა შენიშვნა მისცეს. თუ მიღებული ქულა უდრის 5  - ს მაგ შემთხვევაში, მასწავლებელმა, მშობელს მისცეს შენიშვნა, ხოლო თუ მიღებული ნიშანი ნაკლებია 5 ზე, მაგ შემთხვევაში, მასწავლებელმა გააგდოს მოსწავლე სკოლიდან
grade = int(input("Dear student please enter your math score: "))
if grade == 10:
    print("Mr.JoMaMa your son is very smart")
elif grade == 9 or grade == 8:
    print("Mr.JoMaMa your son is smart but he can do more better")
elif grade == 5:
    print("Mr.JoMaMa you need to control your son")
elif grade < 5:
    print("Mr.JoMaMa your son is really dumb")