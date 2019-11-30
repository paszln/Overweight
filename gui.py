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
    if num_bmi < 18.5:
        bmi_range.set("You are in the underweight range.")
        you_should.set("You should weigh between %.2f and %.2f."%(least_weight, normal_weight))
    elif 18.5 <= num_bmi <= 24.9:
        bmi_range.set("You are in the Normal weight range.")
    elif 25 <= num_bmi <= 29.9:
        bmi_range.set("You are in the Overweight range.")
        you_should.set("You should weigh between %.2f and %.2f."%(least_weight, normal_weight))
    elif num_bmi >= 30:
        bmi_range.set("You are in the Obesity range.")
        you_should.set("You should weigh between %.2f and %.2f."%(least_weight, normal_weight))


root = Tk()
tv_height = DoubleVar()
tv_weight = DoubleVar()
bmi_result = DoubleVar()
bmi_range = StringVar()
you_should = StringVar()

root.title("BMI")
Label(root, text="hi").grid()
Entry(root, textvariable=tv_height).grid(row=1, column=0) #ใส่ส่วนสูง
Label(root, text="cm").grid(row=1, column=1)
Entry(root, textvariable=tv_weight).grid(row=2, column=0) #ใส่น้ำหนัก
Label(root, text="kg").grid(row=2, column=1)
Button(root, text="calculate", font="20", command=on_click).grid(row=3, column=0)
Label(root,text="Your BMI").grid(row=1, column=2)
Label(root, textvariable=bmi_result).grid(row=2, column=2) #ผลbmi
Label(root, textvariable=bmi_range).grid(row=3, column=2)
Label(root, textvariable=you_should).grid(row=3, column=3)

"ต้นแขน ต้นขา เอว สะโพก หน้าอก"
# var = StringVar()
# label = Label( root, textvariable = var, relief = RAISED )

# var.set("Hey!? How are you doing?")
# label.pack()
root.mainloop()

