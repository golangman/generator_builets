from tkinter import Button, Entry, Frame, StringVar, messagebox, Label
from tkinter.constants import GROOVE
from tkinter.ttk import Combobox

from tkinter.simpledialog import askstring
from utils import config_read, md5
from random import SystemRandom
from collections import Counter
from os import mkdir

import os
import subprocess


class Window:
    def __init__(self, root, database_manager) -> None:
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("255x175+0+0")
        self.database_manager = database_manager

    def main_page_init(self):
        self.root.geometry("330x120+0+0")
        self.root.title("Генератор билетов")
        self.root.eval("tk::PlaceWindow . center")
        self.FrameButtons = Frame(self.root, bg="white")
        self.FrameButtons.place(x=0, y=0)
        self._professors = list()

        professors = self.database_manager.get_all_professors()

        self.professors_combobox_values = list()

        for professor in professors:

            full_name = f"{professor.first_name} {professor.last_name} {professor.patronymic} {professor.id}"

            self.professors_combobox_values.append(full_name)

        self.message_label = Label(
            self.FrameButtons,
            text="Выбери преподавателя из списка",
            font=("times new roman", 20, "bold"),
        )
        self.message_label.grid(row=0, column=0, pady=10, padx=10)

        self.combobox_professor = Combobox(
            self.FrameButtons,
            values=self.professors_combobox_values,
            state="readonly",
            width=30,
        )
        self.combobox_professor.current(0)
        self.combobox_professor.grid(row=1, column=0, padx=10)

        self.button_create = Button(
            self.FrameButtons,
            command=self.create,
            text="Выбрать",
            font=("times new roman", 15, "bold"),
            bg="yellow",
            fg="red",
            width=35,
        )
        self.button_create.grid(row=2, column=0, padx=10)

    def create(self):

        if self.__dict__.get("professors_names") is None:
            self.professors_names = [
                self.combobox_professor.get(),
            ]

            self.combobox_professor.destroy()

            self.professors_combobox_values.remove(self.professors_names[0])

            self.combobox_professor = Combobox(
                self.FrameButtons,
                values=self.professors_combobox_values,
                state="readonly",
                width=30,
            )
            self.combobox_professor.current(0)
            self.combobox_professor.grid(row=1, column=0, padx=10)

            return

        elif len(self.professors_names) == 1 and (
            self.__dict__.get("subjects") is None
        ):
            self.professors_names.append(self.combobox_professor.get())
            self.combobox_professor.destroy()

            professor = self.professors_names.pop(0)
            professor_split = professor.split()
            self._professors.append(
                f"{professor_split[1]} {professor_split[0][:1]}.{professor_split[2][:1]}."
            )
            professor_id = int(professor_split[-1])

            self.message_label.destroy()
            self.message_label = Label(
                self.FrameButtons,
                text=f"{professor_split[1]} {professor_split[0]} {professor_split[2]}",
                font=("times new roman", 20, "bold"),
            )
            self.message_label.grid(row=0, column=0, pady=10, padx=10)

            subjects = self.database_manager.get_subjects_for_professor(
                professor_id=professor_id
            )
            combobox_subjects_values = list()

            for subject in subjects:
                combobox_subjects_values.append(
                    f"{subject.name} {subject.professor_id}"
                )

            self.combobox_subjects = Combobox(
                self.FrameButtons,
                values=combobox_subjects_values,
                state="readonly",
                width=30,
            )
            self.combobox_subjects.current(0)
            self.combobox_subjects.grid(row=1, column=0, padx=10)
            self.subjects = list()
            return

        elif len(self.__dict__.get("subjects")) == 0:
            self.subjects.append(self.combobox_subjects.get())
            self.combobox_subjects.destroy()

            professor = self.professors_names.pop(0)
            professor_split = professor.split()
            self._professors.append(
                f"{professor_split[1]} {professor_split[0][:1]}.{professor_split[2][:1]}."
            )
            professor_id = int(professor_split[-1])

            self.message_label.destroy()
            self.message_label = Label(
                self.FrameButtons,
                text=f"{professor_split[1]} {professor_split[0]} {professor_split[2]}",
                font=("times new roman", 20, "bold"),
            )
            self.message_label.grid(row=0, column=0, pady=10, padx=10)

            subjects = self.database_manager.get_subjects_for_professor(
                professor_id=professor_id
            )
            combobox_subjects_values = list()

            for subject in subjects:
                combobox_subjects_values.append(
                    f"{subject.name} {subject.professor_id}"
                )

            self.combobox_subjects = Combobox(
                self.FrameButtons,
                values=combobox_subjects_values,
                state="readonly",
                width=30,
            )
            self.combobox_subjects.current(0)

            self.combobox_subjects.grid(row=1, column=0, padx=10)

            return

        elif len(self.subjects) == 1:
            self.subjects.append(self.combobox_subjects.get())
            self.combobox_subjects.destroy()
            self.message_label.destroy()

            self.message_label = Label(
                self.FrameButtons,
                text="Выберите кол-во вопросов",
                font=("times new roman", 20, "bold"),
            )
            self.message_label.grid(row=0, column=0, pady=10, padx=10)

            self.combobox_questions_count = Combobox(
                self.FrameButtons, values=[3, 4, 5], state="readonly", width=30,
            )
            self.combobox_questions_count.current(0)

            self.combobox_questions_count.grid(row=1, column=0, padx=10)

            self.questions_count = 0

            return

        elif self.questions_count == 0:
            self.questions_count = int(self.combobox_questions_count.get())

            self.combobox_questions_count.destroy()
            self.message_label.destroy()

            self.is_manually_difficulty = messagebox.askyesno(
                None, "Желаете установить сложность вручную?"
            )
            # * Перемешивание для непостоянства нечётного вопроса
            SystemRandom().shuffle(self.subjects)

            if not self.is_manually_difficulty:
                self.button_create.destroy()
                self.comboboxs_difficulty = []
                questions_count_range = range(self.questions_count)
                difficulties = [
                    _.complexity for _ in self.database_manager.get_all_difficulties()
                ]
                for _ in questions_count_range:
                    combobox_difficulty = Combobox(
                        self.FrameButtons,
                        values=difficulties,
                        state="readonly",
                        width=10,
                    )
                    combobox_difficulty.current(
                        SystemRandom().randint(0, len(difficulties) - 1)
                    )
                    self.comboboxs_difficulty.append((None, combobox_difficulty,))
                self.generate_bilets()
                return  # FIXME: вызов генератора

            self.button_create.destroy()

            self.comboboxs_difficulty = []

            difficulties = [
                _.complexity for _ in self.database_manager.get_all_difficulties()
            ]
            questions_count_range = range(self.questions_count)
            for _ in questions_count_range:
                combobox_difficulty = Combobox(
                    self.FrameButtons, values=difficulties, state="readonly", width=10,
                )

                subject = (
                    self.subjects[0]
                    if _ < (self.questions_count // 2)
                    else self.subjects[1]
                )

                subject = (" ".join(subject.split()[:-1])).strip()

                message_label = Label(
                    self.FrameButtons,
                    text=f"{subject} №{_+1}",
                    font=("times new roman", 20, "bold"),
                    justify="left",
                )

                message_label.grid(row=0 + _, column=0)
                combobox_difficulty.current(0)
                combobox_difficulty.grid(row=0 + _, column=1)

                self.comboboxs_difficulty.append((message_label, combobox_difficulty,))

            self.button_create = Button(
                self.FrameButtons,
                command=self.generate_bilets,
                text="Сгенерировать",
                font=("times new roman", 15, "bold"),
                bg="yellow",
                fg="red",
            )
            self.button_create.grid(
                row=questions_count_range[-1] + 1, column=1,
            )
            self.root.geometry("400x200+0+0")
            self.root.eval("tk::PlaceWindow . center")
            return

    def login_page_init(self) -> None:
        self.Frame = Frame(self.root, bg="white")
        self.Frame.place(x=0, y=0)
        self.username = StringVar()
        self.password = StringVar()

        # *Login entry
        Entry(
            self.Frame, textvariable=self.username, bd=5, relief=GROOVE, font=("", 15),
        ).grid(row=1, column=1, padx=20, pady=10)

        # *Password entry
        Entry(
            self.Frame,
            textvariable=self.password,
            bd=5,
            relief=GROOVE,
            font=("", 15),
            show="*",
        ).grid(row=2, column=1, padx=20)

        # *Sing in button
        Button(
            self.Frame,
            command=self.sign_in,
            text="Sign In",
            width=15,
            font=("times new roman", 15, "bold"),
            bg="yellow",
            fg="red",
        ).grid(row=3, column=1, pady=10)

        # *Sing up button
        Button(
            self.Frame,
            command=self.sign_up,
            text="Sign Up",
            width=15,
            font=("times new roman", 15, "bold"),
            bg="yellow",
            fg="red",
        ).grid(row=4, column=1, pady=10)

    def sign_up(self):
        login, password = self.username.get(), self.password.get()

        result = self.database_manager.sign_up(login, md5(password))
        
        if not result:
            messagebox.showerror("Регистрация", "Ошибка регистрации!", icon="warning")
            return

        messagebox.showinfo("Регистрация", "Пользователь успешно зарегистрирован!")

    def sign_in(self):
        login, password = self.username.get(), self.password.get()
        
        is_sign_in = self.database_manager.sign_in(login, md5(password))

        if is_sign_in:
            # * Очистка фрейма, мусорных атрибутов
            self.Frame.destroy()
            del self.Frame
            del self.username
            del self.password

            # * Инициализация основной страницы
            self.main_page_init()

            return True

        messagebox.showerror(
            "Авторизация", "Логин и/или пароль неверны!", icon="warning"
        )

        return False

    def generate_bilets(self):
        from tkinter.simpledialog import askinteger
        from generator import draw, generate_a4

        config_data = config_read()

        protocol = config_data["default_protocol"]
        specialty = (config_data["default_specialty"],)
        course = config_data["default_course"]
        semester = config_data["default_semester"]
        zam_umr = config_data["default_zam_umr"]
        cicl_comission = config_data["default_cicl_comission"]

        students_count = askinteger(
            None, "Сколько необходимо билетов?", initialvalue="20"
        )

        if not students_count or students_count < 1:
            messagebox.showinfo(
                "Информация",
                "Вы не указали необхомое число студентов!\n\nПовторите попытку!",
            )
            return

        protocol = self.get_string(
            "Введите номер протокола", 410, initialvalue=protocol
        )

        specialty = self.get_string(
            "Введите номер специальности", 440, initialvalue=specialty
        )

        course = self.get_string(
            "Введите номер курса", 220, initialvalue=course, _get_int=True
        )

        semester = self.get_string(
            "Введите номер семестра", 250, initialvalue=semester, _get_int=True
        )

        zam_umr = self.get_string(
            "Введите краткое ФИО заместителя директора по УМР",
            740,
            initialvalue=zam_umr,
        )

        cicl_comission = self.get_string(
            "Введите краткое ФИО председателя цикловой комисси",
            740,
            initialvalue=cicl_comission,
        )

        tasks_difficulty = [combobox[1].get() for combobox in self.comboboxs_difficulty]

        cof = self.questions_count // 2

        first_subject_tasks, last_subject_tasks = (
            tasks_difficulty[:cof],
            tasks_difficulty[cof:],
        )

        first_subject_tasks_count = dict(Counter(first_subject_tasks))
        last_subject_tasks_count = dict(Counter(last_subject_tasks))

        rr = lambda x: list(x.split())

        subjects = list(map(rr, self.subjects))

        first_subject_has = self.database_manager.get_count_tasks(
            list(set(first_subject_tasks)), subjects[0][1], subjects[0][0]
        )
        last_subject_has = self.database_manager.get_count_tasks(
            list(set(last_subject_tasks)), subjects[1][1], subjects[1][0]
        )

        tasks_list = list()

        for comlexity in first_subject_has:
            _tasks_limit = (
                first_subject_tasks_count[comlexity.comlexity] * students_count
            )

            if comlexity.count < _tasks_limit:
                messagebox.showerror(
                    None,
                    f"Необходимо ещё {_tasks_limit-comlexity.count} заданий с сложностью '{comlexity.comlexity}' в предмете {subjects[0][0]} для генерации {students_count} билетов!",
                )
                return

            _tasks_list = self.database_manager.get_tasks(
                complexity=comlexity.comlexity,
                subject_professor_id=subjects[0][1],
                subject_name=subjects[0][0],
                limit=_tasks_limit,
            )
            tasks_list.append(_tasks_list)
        for comlexity in last_subject_has:

            _tasks_limit = (
                last_subject_tasks_count[comlexity.comlexity] * students_count
            )

            if comlexity.count < _tasks_limit:
                messagebox.showerror(
                    None,
                    f"Необходимо ещё {_tasks_limit-comlexity.count} заданий с сложностью '{comlexity.comlexity}' в предмете {subjects[0][0]} для генерации {students_count} билетов!",
                )
                return

            _tasks_list = self.database_manager.get_tasks(
                complexity=comlexity.comlexity,
                subject_professor_id=subjects[1][1],
                subject_name=subjects[1][0],
                limit=_tasks_limit,
            )
            tasks_list.append(_tasks_list)

        builet = None

        from datetime import datetime

        date = datetime.now()

        dirname = f"./results/{students_count} билетов {date.day}.{date.month}.{date.year} {date.hour}:{date.minute}:{date.second}"
        mkdir(dirname)
        students_count_range = range(students_count)
        for task_idx in students_count_range:
            builet_tasks = list()

            _subject_tasks = list(first_subject_tasks_count.items()) + list(
                last_subject_tasks_count.items()
            )

            for idx in range(len(_subject_tasks)):
                _, count = _subject_tasks[idx]
                for _ in range(count):
                    builet_tasks.append(tasks_list[idx].pop(0))

            new_builet = draw(
                str(protocol),
                str(specialty),
                str(course),
                str(semester),
                str(task_idx + 1),
                str(zam_umr),
                str(cicl_comission),
                self._professors,
                [subject[0] for subject in subjects],
                builet_tasks,
            )

            if builet:
                a4 = generate_a4(builet, new_builet)
                a4.save(f"{dirname}/билеты{task_idx}_{task_idx+1}.png")
                builet = None
                continue
            if task_idx == students_count_range[-1]:
                a4 = generate_a4(new_builet, None)
                a4.save(f"{dirname}/билет{task_idx+1}.png")
                break

            builet = new_builet

        from subprocess import Popen

        subprocess.Popen(["open", dirname])
        exit()

    def get_string(
        self, message: str, width: int, initialvalue: str, _get_int: bool = False
    ):
        def check_width(string, width):
            from PIL import ImageFont, ImageDraw, Image

            font = ImageFont.truetype("./docs/font.ttf", 60)
            draw = ImageDraw.Draw(Image.new("RGBA", (1000, 1000,)), "RGBA",)

            _width, _ = draw.textsize(string, font=font)

            return True if _width < width else False

        def get(message):
            result = askstring(None, message, initialvalue=initialvalue)
            
            if not result or not (type(result) is str):
                messagebox.showwarning(None, "Не оставляй поле пустым!")
                return get(message)

            if _get_int and not result.isdigit():
                messagebox.showwarning(None, "Введите число!")
                return get(message)

            return result

        string = get(message)

        if check_width(string, width):
            return string
        messagebox.showwarning(
            None, "Допустимый лимит длинны нарушен, попробуйте что-то покороче!"
        )
        return self.get_string(message, width, initialvalue)
