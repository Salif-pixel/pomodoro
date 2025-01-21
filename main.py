import tkinter

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


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0 and reps < 8:
        count_down(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
       global timer
       timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        label_check.config(text="✅" * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=1, row=0)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = tkinter.Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)
label_check = tkinter.Label( padx=50, pady=20, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_check.grid(column=1, row=3)
button_reset = tkinter.Button(text="Reset" , command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
