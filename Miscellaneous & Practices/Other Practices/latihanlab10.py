import typing as t
import tkinter as tk
from tkinter import messagebox
import random


def generate_question(num_ops: int):
    # Angka pertama sudah pregenerated
    cmds: t.List[str] = [str(random.randint(1, 10))]

    # Generate sebanyak n operator dan operand
    for _ in range(num_ops):
        cmds.append(random.choice(["+", "-", "*"]))
        cmds.append(str(random.randint(1, 10)))

    qstr = " ".join(cmds)
    # NOTE: **Jangan gunakan eval() di dunia nyata!!**
    #       eval() dapat saja melakukan eksekusi code APAPUN.
    # https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
    val: int = eval(qstr)
    return qstr, val


def generate_options(answer: int):
    opts = []

    # Generate 3 jawaban yang salah
    for _ in range(3):
        num = int(random.random() * 20 * random.choice([1, -1])) + answer

        # Guard agar jawaban tidak duplikat dan tidak sama dengan jawaban
        while num in opts or num == answer:
            num = int(random.random() * 20 * random.choice([1, -1])) + answer
        opts.append(num)

    # Set posisi jawaban benar
    correct_idx = random.randint(0, 3)
    opts.insert(correct_idx, answer)
    return opts


class GameConfig(t.TypedDict):
    max_questions: int
    max_ops: int


class SettingsWindow(tk.Toplevel):
    def __init__(
        self,
        on_save: t.Callable[[GameConfig], None],
        current_config: GameConfig,
        master: tk.Misc = None,
    ):
        super().__init__(master)
        self.geometry("300x100")

        # Set agar lebih responsif
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.on_save = on_save
        self.current_config = current_config

        self.wm_title("Pengaturan")
        self.create_widgets()

    def on_btn_click(self):
        # Ambil data, asumsi input benar
        max_questions = int(self.questions_inp.get())
        max_ops = int(self.ops_inp.get())

        # Panggil on_save dan keluar
        self.on_save(
            {
                "max_questions": max_questions,
                "max_ops": max_ops,
            }
        )
        messagebox.showinfo("MathQuiz", "Pengaturan tersimpan!")
        self.destroy()

    def create_widgets(self):
        # Definisi widgets
        self.questions_lbl = tk.Label(self, text="Jumlah Pertanyaan")
        self.questions_inp = tk.Entry(self)
        self.questions_inp.insert(0, str(self.current_config["max_questions"]))

        self.ops_lbl = tk.Label(self, text="Jumlah Operator")
        self.ops_inp = tk.Entry(self)
        self.ops_inp.insert(0, str(self.current_config["max_ops"]))

        self.submit_btn = tk.Button(
            self,
            text="Simpan",
            command=self.on_btn_click,
        )

        # Posisi widgets
        self.questions_lbl.grid(row=0, column=0, padx=2, pady=2)
        self.questions_inp.grid(row=0, column=1, padx=2, pady=2)
        self.ops_lbl.grid(row=1, column=0, padx=2, pady=2)
        self.ops_inp.grid(row=1, column=1, padx=2, pady=2)
        self.submit_btn.grid(row=2, column=1, pady=2)


class LevelWindow(tk.Toplevel):
    def __init__(
        self,
        question_num: int,
        question: str,
        answer: int,
        options: t.Tuple[int, int, int, int],
        master: tk.Misc = None,
    ):
        super().__init__(master)
        self.geometry("300x100")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.question_num = question_num
        self.answer = answer
        self.question = question
        self.options = options

        self.draw_level()

    def on_options_click(self, opt: int):
        # Cek apabila opsi yang dipilih merupakan nilai yang benar
        # opt adalah index dari options
        if self.options[opt] == self.answer:
            messagebox.showinfo("MathQuiz", "Jawaban kamu benar!")
            self.destroy()
        else:
            messagebox.showerror("MathQuiz", "Jawaban kamu salah!")

    def draw_level(self):
        # Definisi widgets
        self.q_label = tk.Label(
            self,
            text=self.question,
            wraplength=300,
            justify=tk.CENTER,
        )

        # Dalam options, pasti akan ada 4 elemen, sehingga
        # set masing-masing untuk menjadi button jawaban dengan indexnya.
        self.opt_a = tk.Button(
            self,
            text=str(self.options[0]),
            command=lambda: self.on_options_click(0),
        )
        self.opt_b = tk.Button(
            self,
            text=str(self.options[1]),
            command=lambda: self.on_options_click(1),
        )
        self.opt_c = tk.Button(
            self,
            text=str(self.options[2]),
            command=lambda: self.on_options_click(2),
        )
        self.opt_d = tk.Button(
            self,
            text=str(self.options[3]),
            command=lambda: self.on_options_click(3),
        )

        # Posisi widgets
        self.q_label.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.opt_a.grid(row=1, column=0, sticky="ew", padx=2, pady=2)
        self.opt_b.grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        self.opt_c.grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        self.opt_d.grid(row=2, column=1, sticky="ew", padx=2, pady=2)


class MainWindow(tk.Frame):
    def __init__(self, master: tk.Misc = None):
        super().__init__(master)
        self.master.title("MathQuiz")  # type: ignore
        self.master.geometry("400x100")  # type: ignore

        # Set default config
        self.__game_config: GameConfig = {
            "max_questions": 5,
            "max_ops": 5,
        }

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Definisi widgets
        self.label = tk.Label(self, text="Selamat datang di MathQuiz!")
        self.btn_start = tk.Button(
            self,
            text="Mulai",
            command=self.start_game,
        )
        self.btn_settings = tk.Button(
            self,
            text="Pengaturan",
            command=self.open_settings,
        )
        self.btn_exit = tk.Button(
            self,
            text="Keluar",
            command=self.master.destroy,
        )

        # Posisi widgets
        self.label.pack(pady=10)
        self.btn_start.pack(side=tk.LEFT, pady=5)
        self.btn_settings.pack(side=tk.LEFT, padx=5)
        self.btn_exit.pack(side=tk.LEFT, pady=5)

    def start_game(self):
        for i in range(self.__game_config["max_questions"]):
            q, ans = generate_question(self.__game_config["max_ops"])
            opts = generate_options(ans)

            self.wait_window(
                LevelWindow(
                    question_num=i,
                    question=q,
                    answer=ans,
                    options=opts,
                )
            )

    def set_config(self, config: GameConfig):
        self.__game_config = config

    def open_settings(self):
        SettingsWindow(self.set_config, self.__game_config)


if __name__ == "__main__":
    m = MainWindow()
    m.master.mainloop()
