from tkinter import *


def on_click():
    """หาbmiอะแหละค่ะ"""
    height = tv_height.get()
    weight = tv_weight.get()
    height_mate = height / 100
    use_height = height_mate ** 2
    cal_bmi = weight / use_height
    num_bmi = float("%.2f"%cal_bmi)
    least_weight = 18.5 * use_height
    normal_weight = 24.9 * use_height
    bmi_result.set(num_bmi)
    if num_bmi < 18.5:
        bmi_range.set("You are in the underweight range.")
        you_should.set("You should weight between %.2f and %.2f."%(least_weight, normal_weight))
    elif 18.5 <= num_bmi <= 24.9:
        bmi_range.set("You are in the Normal weight range.")
        you_should.set("")
    elif 25 <= num_bmi <= 29.9:
        bmi_range.set("You are in the Overweight range.")
        you_should.set("You should weight between %.2f and %.2f."%(least_weight, normal_weight))
    elif num_bmi >= 30:
        bmi_range.set("You are in the Obesity range.")
        you_should.set("You should weight between %.2f and %.2f."%(least_weight, normal_weight))
        

def on_click2():
    """เก็บสัดส่วนวันแรก"""
    global first_tonkan
    global first_tonka
    global first_waist
    global first_hip
    global first_chest
    global check_day
    global list_chest, list_hip, list_tonka, list_tonkan, list_waist
    list_tonkan = []
    list_tonka = []
    list_waist = []
    list_hip = []
    list_chest = []
    first_tonkan = tv_tonkan.get()
    first_tonka = tv_tonka.get()
    first_waist = tv_waist.get()
    first_hip = tv_hip.get()
    first_chest = tv_chest.get()
    list_tonkan.append(first_tonkan)
    list_tonka.append(first_tonka)
    list_waist.append(first_waist)
    list_hip.append(first_hip)
    list_chest.append(first_chest)
    check_day = 0
    


def on_click3():
    """เก็บสัดส่วน"""
    global tonkan
    global tonka
    global waist
    global hip
    global chest
    global list_chest, list_hip, list_tonka, list_tonkan, list_waist
    global check_day
    tonkan = tv_tonkan.get()
    tonka = tv_tonka.get()
    waist = tv_waist.get()
    hip = tv_hip.get()
    chest = tv_chest.get()
    list_tonkan.append(tonkan) #เก็บเข้าlist
    list_tonka.append(tonka)
    list_waist.append(waist)
    list_hip.append(hip)
    list_chest.append(chest)
    check_day += 1

"""เก็บตัวแปร"""
list_tonkan = []
list_tonka = []
list_waist = []
list_hip = []
list_chest = []
check_day = -1

def on_click4():
    """เทียบกับวันแรก"""
    """ต้นแขน"""
    if tonkan < first_tonkan:
        Label(root, text = "Your Upper Arm has Decreased").grid(row = 4, column = 2)
    elif tonkan == first_tonkan:
        Label(root, text = "Your Upper Arm hasn't Changed").grid(row = 4, column = 2)
    elif tonkan > first_tonkan:
        Label(root, text = "Your Upper Arm has Increased").grid(row = 4, column = 2)
    """ต้นขา"""
    if tonka < first_tonka:
        Label(root, text = "Your Thigh has Decreased").grid(row = 5, column = 2)
    elif tonka == first_tonka:
        Label(root, text = "Your Thigh hasn't Changed").grid(row = 5, column = 2)
    elif tonka > first_tonka:
        Label(root, text = "Your Thigh has Increased").grid(row = 5, column = 2)
    """เอว"""
    if waist < first_waist:
        Label(root, text = "Your Waist has Decreased").grid(row = 6, column = 2)
    elif waist == first_waist:
        Label(root, text = "Your Waist hasn't Changed").grid(row = 6, column = 2)
    elif waist > first_waist:
        Label(root, text = "Your Waist has Increased").grid(row = 6, column = 2)
    """สะโพก"""
    if hip < first_hip:
        Label(root, text = "Your Hip has Decreased").grid(row = 7, column = 2)
    elif hip == first_hip:
        Label(root, text = "Your Hip hasn't Changed").grid(row = 7, column = 2)
    elif hip > first_hip:
        Label(root, text = "Your Hip has Increased").grid(row = 7, column = 2)
    "หน้าอก"
    if chest < first_chest:
        Label(root, text = "Your Chest has Decreased").grid(row = 8, column = 2)
    elif chest == first_chest:
        Label(root, text = "Your Chest hasn't Changed").grid(row = 8, column = 2)
    elif chest > first_chest:
        Label(root, text = "Your Chest has Increased").grid(row = 8, column = 2)



def on_click5():
    """เทียบกับวันก่อนหน้า"""
    """ต้นแขน"""
    if tonkan < list_tonkan[check_day-1]:
        Label(root, text = "Your Upper Arm has Decreased").grid(row = 4, column = 2)
    elif tonkan == list_tonkan[check_day-1]:
        Label(root, text = "Your Upper Arm hasn't Changed").grid(row = 4, column = 2)
    elif tonkan > list_tonkan[check_day-1]:
        Label(root, text = "Your Upper Arm has Increased").grid(row = 4, column = 2)
    """ต้นขา"""
    if tonka < list_tonka[check_day-1]:
        Label(root, text = "Your Thigh has Decreased").grid(row = 5, column = 2)
    elif tonka == list_tonka[check_day-1]:
        Label(root, text = "Your Thigh hasn't Changed").grid(row = 5, column = 2)
    elif tonka > list_tonka[check_day-1]:
        Label(root, text = "Your Thigh has Increased").grid(row = 5, column = 2)
    """เอว"""
    if waist < list_waist[check_day-1]:
        Label(root, text = "Your Waist has Decreased").grid(row = 6, column = 2)
    elif waist == list_waist[check_day-1]:
        Label(root, text = "Your Waist hasn't Changed").grid(row = 6, column = 2)
    elif waist > list_waist[check_day-1]:
        Label(root, text = "Your Waist has Increased").grid(row = 6, column = 2)
    """สะโพก"""
    if hip < list_hip[check_day-1]:
        Label(root, text = "Your Hip has Decreased").grid(row = 7, column = 2)
    elif hip == list_hip[check_day-1]:
        Label(root, text = "Your Hip hasn't Changed").grid(row = 7, column = 2)
    elif hip > list_hip[check_day-1]:
        Label(root, text = "Your Hip has Increased").grid(row = 7, column = 2)
    "หน้าอก"
    if chest < list_chest[check_day-1]:
        Label(root, text = "Your Chest has Decreased").grid(row = 8, column = 2)
    elif chest == list_chest[check_day-1]:
        Label(root, text = "Your Chest hasn't Changed").grid(row = 8, column = 2)
    elif chest > list_chest[check_day-1]:
        Label(root, text = "Your Chest has Increased").grid(row = 8, column = 2)


root = Tk()
"""เก็บตัวแปร"""
tv_height = DoubleVar()
tv_weight = DoubleVar()
bmi_result = DoubleVar()
bmi_range = StringVar()
you_should = StringVar()
tv_tonkan = DoubleVar()
tv_tonka = DoubleVar()
tv_waist = DoubleVar()
tv_hip = DoubleVar()
tv_chest = DoubleVar()



"""ช่วงคำนวณBMI"""
root.title("OVERWEIGHT")
Label(root, text = "BMI Calculator").grid()
Label(root, text = "ส่วนสูง(Height)").grid(row = 1, column = 0)
Entry(root, textvariable = tv_height).grid(row = 1, column = 1) #ใส่ส่วนสูง
Label(root, text = "(cm)").grid(row = 1, column = 2)
Label(root, text = "น้ำหนัก(Weight)").grid(row = 2, column = 0)
Entry(root, textvariable = tv_weight).grid(row = 2, column = 1) #ใส่น้ำหนัก
Label(root, text = "(kg)").grid(row = 2, column = 2)
Button(root, text = "Calculate BMI", fg="green", bd=6, font = "20", command = on_click).grid(row = 3, column = 0)
Label(root, text = "Your BMI", font = "20").grid(row = 1, column = 3)
Label(root, textvariable = bmi_result).grid(row = 2, column = 3) #ผลbmi
Label(root, textvariable = bmi_range).grid(row = 3, column = 3) #bmi range
Label(root, textvariable = you_should).grid(row = 3, column = 4) #น้ำหนักที่ควรได้

"""วัดสัดส่วนค่ะ"""
Label(root, text = "(cm)").grid(row = 3, column = 1)
Label(root, text = "ต้นแขน(Upper Arm)").grid(row = 4, column = 0)
Entry(root, textvariable = tv_tonkan, width = 6).grid(row = 4, column = 1)
Label(root, text = "ต้นขา(Thigh)").grid(row = 5, column = 0)
Entry(root, textvariable = tv_tonka, width = 6).grid(row = 5, column = 1)
Label(root, text = "เอว(Waist)").grid(row = 6, column = 0)
Entry(root, textvariable = tv_waist, width = 6).grid(row = 6, column = 1)
Label(root, text = "สะโพก(Hip)").grid(row = 7, column = 0)
Entry(root, textvariable = tv_hip, width = 6).grid(row = 7, column = 1)
Label(root, text = "หน้าอก(Chest)").grid(row = 8, column = 0)
Entry(root, textvariable = tv_chest, width = 6).grid(row = 8, column = 1)
Button(root, text = "Set First Day", fg="orange", bd=7, font = "20", command = on_click2).grid(row = 9, column = 1)
Button(root, text = "Submit Body Measurements", fg="red", bd=6, font = "20", command = on_click3).grid(row = 10, column = 1)
Button(root, text = "Compare with First day", fg="blue", bd=6, font = "20", command = on_click4).grid(row = 11, column = 1)
Button(root, text = "Compare with Last Submit", fg="blue", bd=6, font = "20", command = on_click5).grid(row = 12, column = 1)

"ต้นแขน ต้นขา เอว สะโพก หน้าอก"
# var = StringVar()
# label = Label( root, textvariable = var, relief = RAISED )

# var.set("Hey!? How are you doing?")
# label.pack()
root.mainloop()
