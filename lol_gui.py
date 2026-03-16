import tkinter as tk
from tkinter import scrolledtext, font
import random
import time
import sys
import datetime
import pyfiglet
import winsound
import threading

# Словник перекладів
LANG = {
    "uk": {
        "title": "FASTIV OS - Головний термінал",
        "btn_matrix": "1. Matrix дощ",
        "btn_hack": "2. Хак NASA",
        "btn_joke": "3. Жарт",
        "btn_guess": "4. Вгадай число",
        "btn_rps": "5. Камінь/Ножиці",
        "btn_weather": "6. Погода",
        "btn_ai": "7. AI Чат",
        "btn_exit": "8. Вихід",
        "btn_submit": "ВІДПРАВИТИ",
        "init": "ІНІЦІАЛІЗАЦІЯ СИСТЕМИ...",
        "ask_lang": "Оберіть мову / Choose language:\n[1] Українська\n[2] English",
        "ask_name": "Введіть ваше ім'я для авторизації:",
        "access_granted": "Вітаю, {name}! Доступ дозволено.",
        "choose_prog": "\nОберіть програму з меню нижче...",
        "matrix_start": "Запуск Matrix дощу...",
        "matrix_done": "Матриця стабілізована.",
        "hack_start": "Ініціація операції...",
        "hack_steps": [
            "Підключення до серверів NASA...", "Обхід firewall...", 
            "Сканування портів...", "Злам супутникового каналу...", 
            "Дешифрування даних...", "Отримання ROOT-доступу..."
        ],
        "hack_done": "ДОСТУП НАДАНО",
        "jokes": [
            "Є 10 типів людей: ті хто знає двійкову систему і ті хто ні.",
            "Мій код працює... і я боюсь його чіпати.",
            "Ctrl + C / Ctrl + V — найкращий алгоритм.",
            "Я не лінивий. Я просто кешую енергію."
        ],
        "weather": "Погода у місті: {temp}°C, {status}",
        "weather_status": ["Ясно ☀️", "Хмарно ☁️", "Кодний дощ 🌧", "Матричний туман 🌫"],
        "guess_start": "🎲 Я загадав число від 1 до 20. У тебе 5 спроб.\nВведи число в поле нижче:",
        "guess_win": "🏆 Спроба {att}: Ти вгадав! Це {secret}!",
        "guess_more": "📈 Спроба {att}: Більше! (Залишилось {left})",
        "guess_less": "📉 Спроба {att}: Менше! (Залишилось {left})",
        "guess_lose": "💀 Ти програв. Було число {secret}",
        "guess_err": "⚠️ Введи число!",
        "rps_start": "⚔️ Гра: Камінь, Ножиці, Папір\nВведи свій вибір у поле нижче (камінь/ножиці/папір):",
        "rps_err": "⚠️ Введи: камінь, ножиці або папір",
        "rps_bot": "🤖 Бот вибрав: {bot}",
        "rps_draw": "🤝 Нічия",
        "rps_win": "🏆 Ти виграв!",
        "rps_lose": "💀 Бот переміг",
        "rps_choices": {"камінь": "камінь", "ножиці": "ножиці", "папір": "папір"},
        "ai_hello": "🤖 [AI-CHAT]: Привіт, {name}. Я самонавчальний алгоритм.",
        "ai_q": [
            "Який твій улюблений фреймворк?", 
            "Ти готовий зламати систему сьогодні?", 
            "Кава чи енергетик для кодування?"
        ],
        "ai_ans": "🤖 [AI-CHAT]: Запис завершено. NASA здивовані... 🤔",
        "secret_act": "🔓 СЕКРЕТНИЙ РЕЖИМ АКТИВОВАНО!",
        "secret_done": "⚡️ Система розігнана до 1.21 Гіга-LOL! ⚡️"
    },
    "en": {
        "title": "FASTIV OS - Mainframe",
        "btn_matrix": "1. Matrix Rain",
        "btn_hack": "2. Hack NASA",
        "btn_joke": "3. IT Joke",
        "btn_guess": "4. Guess Number",
        "btn_rps": "5. Rock/Paper",
        "btn_weather": "6. Weather",
        "btn_ai": "7. AI Chat",
        "btn_exit": "8. Exit",
        "btn_submit": "SUBMIT",
        "init": "SYSTEM INITIALIZATION...",
        "ask_lang": "Оберіть мову / Choose language:\n[1] Українська\n[2] English",
        "ask_name": "Enter your name for authorization:",
        "access_granted": "Welcome, {name}! Access granted.",
        "choose_prog": "\nSelect a program from the menu below...",
        "matrix_start": "Starting Matrix rain...",
        "matrix_done": "Matrix stabilized.",
        "hack_start": "Initiating operation...",
        "hack_steps": [
            "Connecting to NASA servers...", "Bypassing firewall...", 
            "Scanning ports...", "Hacking satellite uplink...", 
            "Decrypting data...", "Gaining ROOT access..."
        ],
        "hack_done": "ACCESS GRANTED",
        "jokes": [
            "There are 10 types of people: those who understand binary, and those who don't.",
            "My code works... and I have no idea why.",
            "Ctrl + C / Ctrl + V — the best algorithm.",
            "I'm not lazy. I'm just caching my energy."
        ],
        "weather": "Local weather: {temp}°C, {status}",
        "weather_status": ["Clear ☀️", "Cloudy ☁️", "Code rain 🌧", "Matrix fog 🌫"],
        "guess_start": "🎲 I have a number from 1 to 20. You have 5 tries.\nEnter number below:",
        "guess_win": "🏆 Try {att}: You won! It was {secret}!",
        "guess_more": "📈 Try {att}: Higher! ({left} left)",
        "guess_less": "📉 Try {att}: Lower! ({left} left)",
        "guess_lose": "💀 You lost. The number was {secret}",
        "guess_err": "⚠️ Enter a valid number!",
        "rps_start": "⚔️ Rock, Paper, Scissors\nEnter your choice below (rock/paper/scissors):",
        "rps_err": "⚠️ Enter: rock, paper, or scissors",
        "rps_bot": "🤖 Bot chose: {bot}",
        "rps_draw": "🤝 Draw",
        "rps_win": "🏆 You won!",
        "rps_lose": "💀 Bot wins",
        "rps_choices": {"rock": "rock", "paper": "paper", "scissors": "scissors", "камінь": "rock", "ножиці": "scissors", "папір": "paper"},
        "ai_hello": "🤖 [AI-CHAT]: Hello, {name}. I am a self-learning algorithm.",
        "ai_q": [
            "What's your favorite framework?", 
            "Are you ready to hack the system today?", 
            "Coffee or energy drink for coding?"
        ],
        "ai_ans": "🤖 [AI-CHAT]: Log saved. NASA is surprised... 🤔",
        "secret_act": "🔓 SECRET OVERDRIVE ACTIVATED!",
        "secret_done": "⚡️ System overclocked to 1.21 Giga-LOL! ⚡️"
    }
}

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
        
        # Змінні стану
        self.current_state = "ASK_LANGUAGE" # ASK_LANGUAGE, ASK_NAME, MENU, GUESS, RPS, AI_CHAT
        self.game_data = {}
        self.user_name = "Гість"
        self.lang = "uk" # Default

        self.root.title(LANG[self.lang]["title"])

        self.btn_send = tk.Button(
            self.frame_input, text=LANG[self.lang]["btn_submit"], bg="#333333", fg="#00FF00",
            font=self.button_font, command=lambda: self.handle_input(None)
        )
        self.btn_send.pack(side=tk.RIGHT)

        # Контейнер для кнопок меню
        self.frame_buttons = tk.Frame(root, bg="black")
        self.frame_buttons.pack(padx=10, pady=10, fill=tk.X)

        self.menu_buttons = [
            (LANG[self.lang]["btn_matrix"], self.run_matrix),
            (LANG[self.lang]["btn_hack"], self.run_hack),
            (LANG[self.lang]["btn_joke"], self.run_joke),
            (LANG[self.lang]["btn_guess"], self.start_guess_game),
            (LANG[self.lang]["btn_rps"], self.start_rps_game),
            (LANG[self.lang]["btn_weather"], self.run_weather),
            (LANG[self.lang]["btn_ai"], self.start_ai_chat),
            (LANG[self.lang]["btn_exit"], self.root.quit)
        ]

        # Розміщення кнопок у 2 ряди
        self.btn_widgets = []
        for i, (text, cmd) in enumerate(self.menu_buttons):
            btn = tk.Button(
                self.frame_buttons, text=text, bg="#222222", fg="#00FF00",
                font=self.button_font, activebackground="#00FF00",
                activeforeground="black", command=cmd, height=2
            )
            btn.grid(row=i//4, column=i%4, sticky="nsew", padx=3, pady=3)
            self.btn_widgets.append(btn)

        # Налаштування колонок кнопок
        for col in range(4):
            self.frame_buttons.columnconfigure(col, weight=1)

        # Запуск вітання
        self.ask_for_language()

    def update_ui_language(self):
        self.root.title(LANG[self.lang]["title"])
        self.btn_send.config(text=LANG[self.lang]["btn_submit"])
        
        new_texts = [
            LANG[self.lang]["btn_matrix"], LANG[self.lang]["btn_hack"], 
            LANG[self.lang]["btn_joke"], LANG[self.lang]["btn_guess"], 
            LANG[self.lang]["btn_rps"], LANG[self.lang]["btn_weather"], 
            LANG[self.lang]["btn_ai"], LANG[self.lang]["btn_exit"]
        ]
        for i, btn in enumerate(self.btn_widgets):
            btn.config(text=new_texts[i])

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

    def ask_for_language(self):
        self.clear_console()
        self.disable_buttons()
        self.print_to_console(LANG["uk"]["init"], color="#00FF00")
        self.print_to_console(LANG["uk"]["ask_lang"], color="#00FFFF")
        self.entry_field.focus()

    def ask_for_name(self):
        self.clear_console()
        self.update_ui_language()
        self.print_to_console(LANG[self.lang]["ask_name"], color="#00FFFF")
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
        
        if self.current_state == "ASK_LANGUAGE":
            if user_text == "1":
                self.lang = "uk"
                self.current_state = "ASK_NAME"
                self.ask_for_name()
            elif user_text == "2":
                self.lang = "en"
                self.current_state = "ASK_NAME"
                self.ask_for_name()
            else:
                self.print_to_console("⚠️ 1 or 2!")
        elif self.current_state == "ASK_NAME":
            self.user_name = user_text
            self.current_state = "MENU"
            msg = LANG[self.lang]["access_granted"].format(name=self.user_name)
            self.print_to_console(msg, color="#00FFFF")
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
        self.sys_log("MAINFRAME ONLINE")
        self.print_to_console(LANG[self.lang]["choose_prog"], color="#AAAAAA")

    def matrix_rain_task(self):
        self.clear_console()
        chars = "01ABCDEF"
        self.sys_log(LANG[self.lang]["matrix_start"], "INFO")
        for _ in range(25):
            line = "".join(random.choice(chars) for _ in range(70))
            self.print_to_console(line)
            time.sleep(0.04)
        self.sys_log(LANG[self.lang]["matrix_done"])

    def run_matrix(self):
        self.run_in_thread(self.matrix_rain_task)

    def fake_hack_task(self):
        self.clear_console()
        steps = LANG[self.lang]["hack_steps"]
        self.sys_log(LANG[self.lang]["hack_start"], "HACK")
        for step in steps:
            self.typewriter(step, 0.03, "💻")
            time.sleep(random.uniform(0.3, 0.7))
        self.sys_log(LANG[self.lang]["hack_done"], "HACK")
        self.sound_success()

    def run_hack(self):
        self.run_in_thread(self.fake_hack_task)

    def run_joke(self):
        self.clear_console()
        jokes = LANG[self.lang]["jokes"]
        self.run_in_thread(lambda: self.typewriter(random.choice(jokes), 0.03, "🃏"))

    def run_weather(self):
        self.clear_console()
        temp = random.randint(18, 25)
        status = random.choice(LANG[self.lang]["weather_status"])
        msg = LANG[self.lang]["weather"].format(temp=temp, status=status)
        self.sys_log(msg)

    # --- Інтерактивні ігри ---
    def start_guess_game(self):
        self.clear_console()
        self.current_state = "GUESS"
        self.game_data = {
            "secret": random.randint(1, 20),
            "attempts": 5,
            "current": 0
        }
        self.print_to_console(LANG[self.lang]["guess_start"])

    def process_guess(self, user_text):
        try:
            guess = int(user_text)
            self.game_data["current"] += 1
            att = self.game_data["current"]
            max_att = self.game_data["attempts"]
            secret = self.game_data["secret"]
            left = max_att - att
            
            if guess == secret:
                msg = LANG[self.lang]["guess_win"].format(att=att, secret=secret)
                self.print_to_console(msg)
                self.sound_success()
                self.current_state = "MENU"
            elif guess < secret:
                msg = LANG[self.lang]["guess_more"].format(att=att, left=left)
                self.print_to_console(msg)
            else:
                msg = LANG[self.lang]["guess_less"].format(att=att, left=left)
                self.print_to_console(msg)
                
            if guess != secret and att >= max_att:
                msg = LANG[self.lang]["guess_lose"].format(secret=secret)
                self.print_to_console(msg)
                self.sound_fail()
                self.current_state = "MENU"
                
        except ValueError:
            self.print_to_console(LANG[self.lang]["guess_err"])

    def start_rps_game(self):
        self.clear_console()
        self.current_state = "RPS"
        self.print_to_console(LANG[self.lang]["rps_start"])

    def process_rps(self, user_text):
        avail_choices = LANG[self.lang]["rps_choices"]
        player_raw = user_text.lower()
        
        if player_raw not in avail_choices:
            self.print_to_console(LANG[self.lang]["rps_err"])
            return
            
        player = avail_choices[player_raw]
        bot = random.choice(["rock", "paper", "scissors"])
        # Перекладаємо хід бота на поточну мову візуально (через пошук ключа по значенню)
        bot_display = [k for k, v in avail_choices.items() if v == bot][0] if self.lang == "uk" else bot
        
        msg = LANG[self.lang]["rps_bot"].format(bot=bot_display)
        self.print_to_console(msg)

        if player == bot:
            self.print_to_console(LANG[self.lang]["rps_draw"])
        elif (player == "rock" and bot == "scissors") or \
             (player == "scissors" and bot == "paper") or \
             (player == "paper" and bot == "rock"):
            self.print_to_console(LANG[self.lang]["rps_win"])
            self.sound_success()
        else:
            self.print_to_console(LANG[self.lang]["rps_lose"])
            self.sound_fail()
            
        self.current_state = "MENU"

    def start_ai_chat(self):
        self.clear_console()
        self.current_state = "AI_CHAT"
        msg = LANG[self.lang]["ai_hello"].format(name=self.user_name)
        self.print_to_console(msg)
        
        q = random.choice(LANG[self.lang]["ai_q"])
        self.print_to_console(f"🤖 [AI-CHAT]: {q}")

    def process_ai_chat(self, user_text):
        self.current_state = "MENU"
        ans = LANG[self.lang]["ai_ans"]
        self.run_in_thread(lambda: self.typewriter(ans))

    def secret_mode_task(self):
        self.clear_console()
        self.print_to_console("\n" + "🔥" * 30)
        self.print_to_console(LANG[self.lang]["secret_act"])
        self.print_to_console("🔥" * 30 + "\n")
        
        for _ in range(12):
            line = "".join(random.choice(["L","O","L","!","7"]) for _ in range(70))
            self.print_to_console(line)
            time.sleep(0.05)

        self.sound_success()
        self.print_to_console("\n" + LANG[self.lang]["secret_done"])

    def run_secret(self):
        self.run_in_thread(self.secret_mode_task)

if __name__ == "__main__":
    root = tk.Tk()
    app = FastivOSApp(root)
    root.mainloop()
