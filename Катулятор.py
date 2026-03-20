import tkinter as tk
from tkinter import messagebox


# ——— тема ———
COL_BG = "#eef2f6"
COL_CARD = "#ffffff"
COL_BORDER = "#d8dee9"
COL_TEXT = "#1a1d26"
COL_MUTED = "#5c6370"
COL_ACCENT = "#3b5bdb"
COL_ACCENT_ACTIVE = "#2f4ac4"
COL_ACCENT_TEXT = "#ffffff"
COL_DANGER = "#c92a2a"
COL_DANGER_HOVER = "#a61e1e"
COL_RESULT_BG = "#f8fafc"


def parse_float(value: str) -> float:
    value = value.strip().replace(",", ".")
    if not value:
        raise ValueError("empty")
    return float(value)


def format_number(x: float) -> str:
    if x != x:  # NaN
        return "—"
    if x == int(x):
        return str(int(x))
    s = f"{x:.12g}"
    return s


def main() -> None:
    window = tk.Tk()
    window.title("Калькулятор")
    window.configure(bg=COL_BG)
    window.minsize(600, 600)
    window.geometry("420x440")

    state: dict[str, str] = {"op": "+"}
    op_symbols = {"+": "+", "-": "−", "*": "×", "/": "÷"}

    result_var = tk.StringVar(value="0")
    expr_var = tk.StringVar(value="Оберіть дію або натисніть Enter")

    def set_button_hover(btn: tk.Button, normal: str, hover: str) -> None:
        def on_enter(_: object) -> None:
            if btn["state"] == tk.NORMAL:
                btn.configure(bg=hover)

        def on_leave(_: object) -> None:
            btn.configure(bg=normal)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def calculate(op: str | None = None) -> None:
        use = op if op is not None else state["op"]
        state["op"] = use
        try:
            num1 = parse_float(entry1.get())
            num2 = parse_float(entry2.get())
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректні числа в обидва поля.")
            return

        if use == "+":
            result = num1 + num2
        elif use == "-":
            result = num1 - num2
        elif use == "*":
            result = num1 * num2
        else:
            if num2 == 0:
                messagebox.showwarning("Увага", "Ділення на нуль неможливе.")
                return
            result = num1 / num2

        sym = op_symbols.get(use, use)
        expr_var.set(f"{format_number(num1)} {sym} {format_number(num2)} =")
        result_var.set(format_number(result))

    def clear_all() -> None:
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        result_var.set("0")
        expr_var.set("Оберіть дію або натисніть Enter")
        entry1.focus_set()

    def copy_result() -> None:
        text = result_var.get()
        if text and text != "0":
            window.clipboard_clear()
            window.clipboard_append(text)
            window.update()

    def accent_button(parent: tk.Widget, text: str, op: str) -> tk.Button:
        b = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=COL_ACCENT,
            fg=COL_ACCENT_TEXT,
            activebackground=COL_ACCENT_ACTIVE,
            activeforeground=COL_ACCENT_TEXT,
            relief=tk.FLAT,
            cursor="hand2",
            padx=8,
            pady=10,
            command=lambda: calculate(op),
        )
        set_button_hover(b, COL_ACCENT, COL_ACCENT_ACTIVE)
        return b

    def ghost_button(parent: tk.Widget, text: str, command, danger: bool = False) -> tk.Button:
        bg = COL_CARD
        fg = COL_DANGER if danger else COL_MUTED
        hover = "#fff5f5" if danger else "#f1f5f9"
        b = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 9),
            bg=bg,
            fg=fg,
            activebackground=hover,
            activeforeground=fg,
            relief=tk.FLAT,
            cursor="hand2",
            padx=12,
            pady=6,
            command=command,
        )
        set_button_hover(b, bg, hover)
        return b

    # ——— верхня «картка» з результатом ———
    outer = tk.Frame(window, bg=COL_BG)
    outer.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    card = tk.Frame(outer, bg=COL_CARD, highlightbackground=COL_BORDER, highlightthickness=1)
    card.pack(fill=tk.BOTH, expand=True)

    inner = tk.Frame(card, bg=COL_CARD)
    inner.pack(fill=tk.BOTH, expand=True, padx=18, pady=18)

    tk.Label(
        inner,
        text="Калькулятор",
        font=("Segoe UI", 18, "bold"),
        fg=COL_TEXT,
        bg=COL_CARD,
    ).pack(anchor="w")

    tk.Label(
        inner,
        textvariable=expr_var,
        font=("Segoe UI", 10),
        fg=COL_MUTED,
        bg=COL_CARD,
    ).pack(anchor="w", pady=(4, 12))

    result_frame = tk.Frame(inner, bg=COL_RESULT_BG, highlightbackground=COL_BORDER, highlightthickness=1)
    result_frame.pack(fill=tk.X, pady=(0, 16))
    tk.Label(
        result_frame,
        textvariable=result_var,
        font=("Consolas", 22, "bold"),
        fg=COL_TEXT,
        bg=COL_RESULT_BG,
        anchor="e",
    ).pack(fill=tk.X, padx=14, pady=14)

    row_copy = tk.Frame(inner, bg=COL_CARD)
    row_copy.pack(fill=tk.X, pady=(0, 8))
    ghost_button(row_copy, "Копіювати результат", copy_result).pack(side=tk.RIGHT)

    # ——— поля вводу ———
    def labeled_entry(label: str) -> tk.Entry:
        f = tk.Frame(inner, bg=COL_CARD)
        f.pack(fill=tk.X, pady=(0, 10))
        tk.Label(f, text=label, font=("Segoe UI", 10), fg=COL_MUTED, bg=COL_CARD, width=14, anchor="w").pack(
            side=tk.LEFT
        )
        e = tk.Entry(
            f,
            font=("Segoe UI", 12),
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground=COL_BORDER,
            highlightcolor=COL_ACCENT,
            insertbackground=COL_TEXT,
            fg=COL_TEXT,
            bg="#fafbfc",
        )
        e.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, ipadx=8)
        return e

    entry1 = labeled_entry("Перше число")
    entry2 = labeled_entry("Друге число")

    # ——— кнопки операцій ———
    tk.Label(inner, text="Операції", font=("Segoe UI", 9, "bold"), fg=COL_MUTED, bg=COL_CARD).pack(
        anchor="w", pady=(8, 6)
    )

    grid = tk.Frame(inner, bg=COL_CARD)
    grid.pack(fill=tk.X)

    ops = [
        ("Додати", "+"),
        ("Відняти", "−"),
        ("Помножити", "×"),
        ("Поділити", "÷"),
    ]
    # Map display symbol back to internal op
    display_to_op = {"−": "-", "×": "*", "÷": "/"}

    for i, (name, sym) in enumerate(ops):
        internal = display_to_op.get(sym, sym)
        r, c = divmod(i, 2)
        b = accent_button(grid, f"{name}\n({sym})", internal)
        b.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")
    grid.columnconfigure(0, weight=1)
    grid.columnconfigure(1, weight=1)

    # ——— низ: очистити та вихід ———
    bottom = tk.Frame(inner, bg=COL_CARD)
    bottom.pack(fill=tk.X, pady=(16, 0))

    ghost_button(bottom, "Очистити все", clear_all).pack(side=tk.LEFT)
    ghost_button(bottom, "Вихід", window.destroy, danger=True).pack(side=tk.RIGHT)

    # ——— клавіатура ———
    window.bind("<Return>", lambda _: calculate())
    window.bind("<Escape>", lambda _: clear_all())

    entry1.focus_set()
    window.mainloop()


if __name__ == "__main__":
    main()
