from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)

        label.config(text="Work", fg=GREEN)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global marks
    mins = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    if count >= 0:
        global timer
        canvas.itemconfig(canvas_text, text=f"{mins}:{seconds}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔️"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.config(bg=YELLOW)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
start = Button(text="Start", command=start_timer, font=(FONT_NAME, 12, "bold"))
restart = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 12, "bold"))
start.grid(column=1, row=3)
restart.grid(column=3, row=3)
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 42, "bold"), bg=YELLOW)
label.grid(column=2, row=1)
checkmark = Label(fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
checkmark.grid(column=2, row=4)




window.mainloop()

