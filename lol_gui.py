import tkinter as tk
from tkinter import scrolledtext, font
import random
import time
import sys
import datetime
import pyfiglet
import winsound
import threading

class FastivOSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FASTIV OS - Mainframe")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Налаштування шрифтів
        self.terminal_font = font.Font(family="Consolas", size=11)
        self.button_font = font.Font(family="Consolas", size=10, weight="bold")

        # Основний екран виведення
        self.console = scrolledtext.ScrolledText(
            root, bg="black", fg="#00FF00", font=self.terminal_font,
            wrap=tk.WORD, state=tk.DISABLED
        )
        self.console.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Контейнер для вводу (для ігор)
        self.frame_input = tk.Frame(root, bg="black")
        self.frame_input.pack(padx=10, pady=(0, 5), fill=tk.X)
        
        self.input_var = tk.StringVar()
        self.entry_field = tk.Entry(
            self.frame_input, textvariable=self.input_var,
            font=self.terminal_font, bg="#111111", fg="#00FF00",
            insertbackground="#00FF00"
        )
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry_field.bind("<Return>", self.handle_input)
        
        self.btn_send = tk.Button(
            self.frame_input, text="SUBMIT", bg="#333333", fg="#00FF00",
            font=self.button_font, command=lambda: self.handle_input(None)
        )
        self.btn_send.pack(side=tk.RIGHT)

        # Контейнер для кнопок меню
        self.frame_buttons = tk.Frame(root, bg="black")
        self.frame_buttons.pack(padx=10, pady=10, fill=tk.X)

        buttons = [
            ("1. Matrix дощ", self.run_matrix),
            ("2. Хак NASA", self.run_hack),
            ("3. Жарт", self.run_joke),
            ("4. Вгадай число", self.start_guess_game),
            ("5. Камінь/Ножиці", self.start_rps_game),
            ("6. Погода", self.run_weather),
            ("7. AI Чат", self.start_ai_chat),
            ("8. Вихід", self.root.quit)
        ]

        # Розміщення кнопок у 2 ряди
        for i, (text, cmd) in enumerate(buttons):
            btn = tk.Button(
                self.frame_buttons, text=text, bg="#222222", fg="#00FF00",
                font=self.button_font, activebackground="#00FF00",
                activeforeground="black", command=cmd, height=2
            )
            btn.grid(row=i//4, column=i%4, sticky="nsew", padx=3, pady=3)

        # Налаштування колонок кнопок
        for col in range(4):
            self.frame_buttons.columnconfigure(col, weight=1)

        # Змінні стану для інтерактивних ігор
        self.current_state = "ASK_NAME" # ASK_NAME, MENU, GUESS, RPS, AI_CHAT
        self.game_data = {}
        self.user_name = "Гість"

        # Запуск вітання
        self.ask_for_name()

    # --- Утиліти вікна ---
    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def print_to_console(self, text, color="#00FF00", end="\n"):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, text + end)
        self.console.see(tk.END)
        self.console.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def clear_console(self):
        self.console.config(state=tk.NORMAL)
        self.console.delete(1.0, tk.END)
        self.console.config(state=tk.DISABLED)

    def sys_log(self, message, level="INFO"):
        colors = {"INFO": "🔵", "WARN": "⚠️", "CRIT": "💀", "HACK": "🏴‍☠️"}
        prefix = f"[{self.get_time()}] {colors.get(level, '⚪️')} "
        self.print_to_console(prefix + message)

    def typewriter(self, text, speed=0.04, label="[INFO]"):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, f"{label} ")
        self.console.see(tk.END)
        self.root.update_idletasks()
        
        for char in text:
            self.console.insert(tk.END, char)
            self.console.see(tk.END)
            self.root.update_idletasks()
            time.sleep(speed)
            
        self.console.insert(tk.END, "\n")
        self.console.config(state=tk.DISABLED)

    def run_in_thread(self, func):
        def wrapper():
            self.disable_buttons()
            func()
            self.enable_buttons()
        threading.Thread(target=wrapper, daemon=True).start()

    def disable_buttons(self):
        for widget in self.frame_buttons.winfo_children():
            widget.config(state=tk.DISABLED)

    def enable_buttons(self):
        for widget in self.frame_buttons.winfo_children():
            widget.config(state=tk.NORMAL)

    def ask_for_name(self):
        self.clear_console()
        self.disable_buttons()
        self.print_to_console("ІНІЦІАЛІЗАЦІЯ СИСТЕМИ...", color="#00FF00")
        self.print_to_console("Введіть ваше ім'я для авторизації:", color="#00FFFF")
        self.entry_field.focus()

    # --- Звуки ---
    def sound_success(self):
        threading.Thread(target=lambda: (winsound.Beep(1000, 200), winsound.Beep(1500, 200)), daemon=True).start()

    def sound_fail(self):
        threading.Thread(target=lambda: (winsound.Beep(400, 300), winsound.Beep(300, 300)), daemon=True).start()

    # --- Обробка вводу ---
    def handle_input(self, event):
        user_text = self.input_var.get().strip()
        if not user_text:
            return
            
        self.input_var.set("")

        if user_text == "404":
            self.print_to_console(f"\n> 404", color="#FFFFFF")
            self.run_secret()
            return

        self.print_to_console(f"\n> {user_text}", color="#FFFFFF")
        
        if self.current_state == "ASK_NAME":
            self.user_name = user_text
            self.current_state = "MENU"
            self.print_to_console(f"Вітаю, {self.user_name}! Доступ дозволено.", color="#00FFFF")
            self.enable_buttons()
            self.sound_success()
            self.root.after(1500, self.show_banner)
        elif self.current_state == "GUESS":
            self.process_guess(user_text)
        elif self.current_state == "RPS":
            self.process_rps(user_text)
        elif self.current_state == "AI_CHAT":
            self.process_ai_chat(user_text)

    # --- Логіка додатків ---
    def show_banner(self):
        self.clear_console()
        ascii_art = pyfiglet.figlet_format("FASTIV OS")
        self.print_to_console(ascii_art, color="#00FFFF")
        self.sys_log("FASTIV MAINFRAME ONLINE")
        self.print_to_console("\nОберіть програму з меню нижче...", color="#AAAAAA")

    def matrix_rain_task(self):
        self.clear_console()
        chars = "01ABCDEF"
        self.sys_log("Запуск Matrix дощу...", "INFO")
        for _ in range(25):
            line = "".join(random.choice(chars) for _ in range(70))
            self.print_to_console(line)
            time.sleep(0.04)
        self.sys_log("Матриця стабілізована.")

    def run_matrix(self):
        self.run_in_thread(self.matrix_rain_task)

    def fake_hack_task(self):
        self.clear_console()
        steps = [
            "Підключення до серверів NASA...",
            "Обхід firewall...",
            "Сканування портів...",
            "Злам супутникового каналу...",
            "Дешифрування даних...",
            "Отримання ROOT-доступу..."
        ]
        self.sys_log("Ініціація операції...", "HACK")
        for step in steps:
            self.typewriter(step, 0.03, "💻")
            time.sleep(random.uniform(0.3, 0.7))
        self.sys_log("ACCESS GRANTED", "HACK")
        self.sound_success()

    def run_hack(self):
        self.run_in_thread(self.fake_hack_task)

    def run_joke(self):
        self.clear_console()
        jokes = [
            "Є 10 типів людей: ті хто знає двійкову систему і ті хто ні.",
            "Мій код працює... і я боюсь його чіпати.",
            "Ctrl + C / Ctrl + V — найкращий алгоритм.",
            "Я не лінивий. Я просто кешую енергію."
        ]
        self.run_in_thread(lambda: self.typewriter(random.choice(jokes), 0.03, "🃏"))

    def run_weather(self):
        self.clear_console()
        temp = random.randint(18, 25)
        status = random.choice(["Ясно ☀️", "Хмарно ☁️", "Кодний дощ 🌧", "Матричний туман 🌫"])
        self.sys_log(f"Погода у Фастові: {temp}°C, {status}")

    # --- Інтерактивні ігри ---
    def start_guess_game(self):
        self.clear_console()
        self.current_state = "GUESS"
        self.game_data = {
            "secret": random.randint(1, 20),
            "attempts": 5,
            "current": 0
        }
        self.print_to_console("🎲 Я загадав число від 1 до 20. У тебе 5 спроб.")
        self.print_to_console("Введи число в поле нижче:")

    def process_guess(self, user_text):
        try:
            guess = int(user_text)
            self.game_data["current"] += 1
            att = self.game_data["current"]
            max_att = self.game_data["attempts"]
            secret = self.game_data["secret"]
            
            if guess == secret:
                self.print_to_console(f"🏆 Спроба {att}: Ти вгадав! Це {secret}!")
                self.sound_success()
                self.current_state = "MENU"
            elif guess < secret:
                self.print_to_console(f"📈 Спроба {att}: Більше! (Залишилось {max_att - att})")
            else:
                self.print_to_console(f"📉 Спроба {att}: Менше! (Залишилось {max_att - att})")
                
            if guess != secret and att >= max_att:
                self.print_to_console(f"💀 Ти програв. Було число {secret}")
                self.sound_fail()
                self.current_state = "MENU"
                
        except ValueError:
            self.print_to_console("⚠️ Введи число!")

    def start_rps_game(self):
        self.clear_console()
        self.current_state = "RPS"
        self.print_to_console("⚔️ Гра: Камінь, Ножиці, Папір")
        self.print_to_console("Введи свій вибір у поле нижче:")

    def process_rps(self, user_text):
        choices = ["камінь", "ножиці", "папір"]
        player = user_text.lower()
        
        if player not in choices:
            self.print_to_console("⚠️ Введи: камінь, ножиці або папір")
            return
            
        bot = random.choice(choices)
        self.print_to_console(f"🤖 Бот вибрав: {bot}")

        if player == bot:
            self.print_to_console("🤝 Нічия")
        elif (player == "камінь" and bot == "ножиці") or \
             (player == "ножиці" and bot == "папір") or \
             (player == "папір" and bot == "камінь"):
            self.print_to_console("🏆 Ти виграв!")
            self.sound_success()
        else:
            self.print_to_console("💀 Бот переміг")
            self.sound_fail()
            
        self.current_state = "MENU"

    def start_ai_chat(self):
        self.clear_console()
        self.current_state = "AI_CHAT"
        self.print_to_console(f"🤖 [AI-CHAT]: Привіт, {self.user_name}. Я самонавчальний алгоритм Фастова.")
        
        questions = [
            "Який твій улюблений фреймворк?",
            "Ти готовий зламати систему сьогодні?",
            "Кава чи енергетик для кодування?"
        ]
        q = random.choice(questions)
        self.print_to_console(f"🤖 [AI-CHAT]: {q}")

    def process_ai_chat(self, user_text):
        self.current_state = "MENU"
        self.run_in_thread(lambda: self.typewriter("🤖 [AI-CHAT]: Запис завершено. NASA здивовані... 🤔"))

    def secret_mode_task(self):
        self.clear_console()
        self.print_to_console("\n" + "🔥" * 30)
        self.print_to_console("🔓 SECRET OVERDRIVE ACTIVATED!")
        self.print_to_console("🔥" * 30 + "\n")
        
        for _ in range(12):
            line = "".join(random.choice(["L","O","L","!","7"]) for _ in range(70))
            self.print_to_console(line)
            time.sleep(0.05)

        self.sound_success()
        self.print_to_console("\n⚡️ Система розігнана до 1.21 Гіга-LOL! ⚡️")

    def run_secret(self):
        self.run_in_thread(self.secret_mode_task)

if __name__ == "__main__":
    root = tk.Tk()
    app = FastivOSApp(root)
    root.mainloop()
