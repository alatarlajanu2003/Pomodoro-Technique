from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F1583F"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", foreground=GREEN)
    label_2["text"] = ""
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        count_down(work_sec)
        label_1.config(text="Timer", foreground=GREEN)
    elif reps % 2 == 0 and reps != 8:
        count_down(short_break)
        label_1.config(text="Break", foreground=PINK)
    else:
        count_down(long_break)
        label_1.config(text="Break", foreground=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = int(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✓"
        label_2.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro")
window.config(background=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

label_1 = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 30, "bold"), background=YELLOW)
label_1.grid(column=1, row=0)

label_2 = Label(foreground=GREEN, font=(FONT_NAME, 15, "bold"), background=YELLOW)
label_2.grid(column=1, row=3)

button_1 = Button(text="Start", font=(FONT_NAME, 10), command=start_timer)
button_1.grid(column=0, row=2)

button_1 = Button(text="Reset", font=(FONT_NAME, 10), command=reset_timer)
button_1.grid(column=2, row=2)


window.mainloop()