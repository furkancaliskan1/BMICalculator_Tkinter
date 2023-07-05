import tkinter as tk
def main():
    window = tk.Tk()
    window.title("BMI")
    window.minsize(height=250,width=200)
    window.maxsize(height=250,width=200)
    window.config(pady=30)
    def widgets():
        def bmi_calculate():
            we = int(entry_weight.get())
            he = int(entry_height.get()) / 100
            bmi = ( we /(he ** 2))
            if bmi < 18.5 :
                label_calculate = tk.Label(text=f"your bmi is {int(bmi)} you're week.")
                label_calculate.place(x=30,y=160)
            elif bmi >= 18.5 and bmi < 25:
                label_calculate = tk.Label(text=f"your bmi is {int(bmi)} you're normal.")
                label_calculate.place(x=30, y=160)
            elif bmi >= 25 and bmi < 30 :
                label_calculate = tk.Label(text=f"your bmi is {int(bmi)} you're fat.")
                label_calculate.place(x=30, y=160)
            elif bmi >= 30 :
                label_calculate = tk.Label(text=f"your bmi is {int(bmi)} you're obese.")
                label_calculate.place(x=30, y=160)

        label_weight=tk.Label(text="Enter Your Weight (kg)")
        label_weight.pack()
        label_weight.config(pady=10)
        entry_weight=tk.Entry(width=10)
        entry_weight.pack()
        entry_weight.config()
        label_height = tk.Label(text="Enter Your Height (cm)")
        label_height.pack()
        label_height.config(pady=10)
        entry_height = tk.Entry(width=10)
        entry_height.pack()
        button_calculate = tk.Button(text="Calculate",height=1,command=bmi_calculate)
        button_calculate.place(x=70,y=125)
    widgets()
    window.mainloop()
main()

