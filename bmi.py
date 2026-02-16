from tkinter import *

window = Tk()
def bmi():
    weight=float(e_w.get())
    height = float(e_h.get())/100
    result = weight/(height*height)
    result=round(result,2)

    if result < 18.5 :
        s="لاغری"
    elif 18.5<=result<25:
        s="وزن مناسب"
    elif 25<=result:
        s="چاقی"

    lb_r.config(text=f"bmi={result}/{s}")



window.geometry("800x450")
window.title("BMI برنامه ")
lb = Label(window,text="به برنامه شاخص توده بدنی خوش آمدید",font=("Arial",20),fg=("red"))
lb.pack()
lb_h = Label(window,text=":قد خود را وارد کنید",font=("Arial",20)).pack(pady=10)
e_h = Entry(window,font=("Arial",20))
e_h.pack()
lb_w = Label(window,text=":وزن خود را وارد کنید",font=("Arial",20)).pack()
e_w = Entry(window,font=("Arial",20))
e_w.pack()
btn = Button(window,text="حساب کن",command=bmi)
btn.pack(pady=10)
lb_r=Label(window,text="",font=("Arial",20))
lb_r.pack()
window.mainloop()
