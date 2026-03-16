import random
import time
import sys
import datetime
import pyfiglet
import winsound

# --- Утиліти ---
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def sys_log(message, level="INFO"):
    colors = {"INFO": "🔵", "WARN": "⚠️", "CRIT": "💀", "HACK": "🏴‍☠️"}
    print(f"[{get_time()}] {colors.get(level, '⚪️')} {message}")

def typewriter(text, speed=0.04, label="[INFO]"):
    print(f"{label} ", end="", flush=True)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# --- ASCII банер ---
def banner():
    ascii_art = pyfiglet.figlet_format("FASTIV OS")
    print("\033[96m" + ascii_art + "\033[0m")

# --- Звуки ---
def sound_success():
    winsound.Beep(1000, 200)
    winsound.Beep(1500, 200)

def sound_fail():
    winsound.Beep(400, 300)
    winsound.Beep(300, 300)

# --- Matrix ефект ---
def matrix_rain():
    chars = "01ABCDEF"
    sys_log("Запуск Matrix дощу...", "INFO")

    for _ in range(25):
        line = "".join(random.choice(chars) for _ in range(60))
        print("\033[92m" + line + "\033[0m")
        time.sleep(0.03)

# --- Фейковий хак ---
def fake_hack():
    steps = [
        "Підключення до серверів NASA...",
        "Обхід firewall...",
        "Сканування портів...",
        "Злам супутникового каналу...",
        "Дешифрування даних...",
        "Отримання ROOT-доступу..."
    ]

    sys_log("Ініціація операції...", "HACK")

    for step in steps:
        typewriter(step, 0.03, "💻")
        time.sleep(random.uniform(0.3, 0.7))

    sys_log("ACCESS GRANTED", "HACK")
    sound_success()

# --- Жарт програміста ---
def programmer_joke():
    jokes = [
        "Є 10 типів людей: ті хто знає двійкову систему і ті хто ні.",
        "Мій код працює... і я боюсь його чіпати.",
        "Ctrl + C / Ctrl + V — найкращий алгоритм.",
        "Я не лінивий. Я просто кешую енергію."
    ]

    typewriter(random.choice(jokes), 0.03, "🃏")

# --- Гра: Вгадай число ---
def guess_game():
    secret = random.randint(1, 20)
    attempts = 5

    typewriter("Я загадав число від 1 до 20.", 0.03, "🎲")

    for i in range(attempts):
        try:
            guess = int(input(f"Спроба {i+1}: "))
            if guess == secret:
                print("🏆 Ти вгадав!")
                sound_success()
                return
            elif guess < secret:
                print("📈 Більше")
            else:
                print("📉 Менше")
        except ValueError:
            print("⚠️ Введи число!")

    print(f"💀 Ти програв. Було число {secret}")
    sound_fail()

# --- Камінь ножиці папір ---
def rps_game():
    choices = ["камінь", "ножиці", "папір"]
    player = input("Твій вибір (камінь/ножиці/папір): ").lower()
    bot = random.choice(choices)

    print(f"🤖 Бот вибрав: {bot}")

    if player == bot:
        print("🤝 Нічия")
    elif (player == "камінь" and bot == "ножиці") or \
         (player == "ножиці" and bot == "папір") or \
         (player == "папір" and bot == "камінь"):
        print("🏆 Ти виграв!")
        sound_success()
    else:
        print("💀 Бот переміг")
        sound_fail()

# --- Фейковий прогноз ---
def fastiv_weather():
    temp = random.randint(18, 25)
    status = random.choice([
        "Ясно ☀️",
        "Хмарно ☁️",
        "Кодний дощ 🌧",
        "Матричний туман 🌫"
    ])
    sys_log(f"Погода у Фастові: {temp}°C, {status}")

# --- AI чат ---
def ai_chat_simulation():
    print("\n🤖 [AI-CHAT]: Привіт, Ростиславе. Я самонавчальний алгоритм Фастова.")

    questions = [
        "Який твій улюблений фреймворк?",
        "Ти готовий зламати систему сьогодні?",
        "Кава чи енергетик для кодування?"
    ]

    input(f"🤖 [AI-CHAT]: {random.choice(questions)} ")

    typewriter("🤖 [AI-CHAT]: Запис завершено. NASA здивовані... 🤔")

# --- Секретний режим ---
def secret_mode():
    print("\n" + "🔥" * 30)
    print("🔓 SECRET OVERDRIVE ACTIVATED!")
    print("🔥" * 30)
    for _ in range(12):
        line = "".join(random.choice(["L","O","L","!","7"]) for _ in range(60))
        print("\033[91m" + line + "\033[0m")
        time.sleep(0.05)

    sound_success()
    print("⚡️ Система розігнана до 1.21 Гіга-LOL! ⚡️\n")

# --- Меню ---
def menu():
    banner()

    sys_log("FASTIV MAINFRAME ONLINE")

    while True:
        print("\n🟡 === FASTIV MAINFRAME МЕНЮ ===")
        print("1️⃣  Matrix дощ")
        print("2️⃣  Фейковий хак NASA")
        print("3️⃣  Жарт програміста")
        print("4️⃣  Гра: Вгадай число")
        print("5️⃣  ⚔️ Камінь/Ножиці/Папір")
        print("6️⃣  🌦 Погода у Фастові")
        print("7️⃣  🤖 Чат з AI")
        print("8️⃣  🚪 Вихід")

        choice = input("\n🎮 Обери (1-8): ").strip()

        if choice == "1":
            matrix_rain()

        elif choice == "2":
            fake_hack()

        elif choice == "3":
            programmer_joke()

        elif choice == "4":
            guess_game()

        elif choice == "5":
            rps_game()

        elif choice == "6":
            fastiv_weather()

        elif choice == "7":
            ai_chat_simulation()

        elif choice == "8":
            typewriter("👋 Сесія завершена. Ростислав, повертайся швидше! 🚀")
            sound_success()
            break

        elif choice == "404":
            secret_mode()

        else:
            sys_log("Некоректний запит. Спробуй ще раз.", "WARN")
            sound_fail()

if __name__ == "__main__":
    menu()