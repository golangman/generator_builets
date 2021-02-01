from PIL import ImageDraw, Image, ImageFont
from datetime import datetime

months = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]


def draw(
    protocol,
    specialty,
    course,
    semester,
    bilet_number,
    zam_umr,
    cicl_comission,
    professors,
    subjects,
    tasks,
):
    # init block
    font = ImageFont.truetype("./docs/font.ttf", 60)
    font_bold = ImageFont.truetype("./docs/font_bold.ttf", 60)
    bilet = Image.open("./docs/билет.png")
    draw = ImageDraw.Draw(bilet, "RGBA",)
    date = datetime.now()
    # end init block

    # draw dates
    text_date = f"{date.day} {months[date.month-1]} {date.year}г."

    width, _ = draw.textsize(text_date, font=font)

    block_width = 760
    draw.text((block_width - width, 520), text_date, fill="black", font=font)

    block_width = 2460
    draw.text((block_width - width, 450), text_date, fill="black", font=font)

    # draw protocol
    draw.text((2040, 520), protocol, fill="black", font=font)

    # draw specialty
    draw.text((1230, 450), specialty, fill="black", font=font)

    # draw course
    draw.text((930, 520), course, fill="black", font=font)

    # draw semester
    draw.text((1420, 520), semester, fill="black", font=font)

    # draw bilet number
    draw.text((1530, 180), bilet_number, fill="black", font=font)

    # draw zam_umr
    block_width = 760
    width, _ = draw.textsize(zam_umr, font=font)
    draw.text((block_width - width, 450), zam_umr, fill="black", font=font)

    # draw cicl_comission
    block_width = 2450
    _text = f"Председатель цикловой комиссии:{' ' * 42} {cicl_comission}"
    width, _ = draw.textsize(_text, font=font)

    draw.text(
        (block_width - width, 1670), _text, fill="black", font=font,
    )
    # draw professors
    block_width = 2450
    _text = f"Преподаватели:{' ' * 21}{professors[0]}{' ' * 21}{professors[1]}"

    width, _ = draw.textsize(_text, font=font)

    draw.text(
        (block_width - width, 1600), _text, fill="black", font=font,
    )

    # draw subjects
    start_x, start_y = 1260, 260
    is_first_line = True
    line_width = 0
    line_width_max = 380

    subject_len_range = range(len(subjects))
    last_subject_idx = subject_len_range[-1]
    for subject_idx in subject_len_range:
        subject = subjects[subject_idx]

        width, height = draw.textsize(subject + ",  ", font=font)

        if (line_width + width) > line_width_max:
            temp_subject = ""
            while True:
                temp_subject = subject[-1:] + temp_subject
                subject = subject[:-1]

                width, height = draw.textsize(subject, font=font)

                if (line_width + width) > line_width_max:
                    continue

                draw.text(
                    (start_x + line_width, start_y),
                    subject,
                    fill="black",
                    font=font_bold,
                )

                line_width = 0

                start_y += height

                if is_first_line:
                    start_x = 800
                    line_width_max = 860

                draw.text(
                    (start_x + line_width, start_y),
                    temp_subject + (",  " if subject_idx != last_subject_idx else ""),
                    fill="black",
                    font=font_bold,
                )
                temp_subject_width, _ = draw.textsize(temp_subject + ",  ", font=font)

                line_width += temp_subject_width

                break

            continue

        draw.text(
            (start_x + line_width, start_y),
            subject + (",  " if subject_idx != last_subject_idx else ""),
            fill="black",
            font=font_bold,
        )
        line_width += width

    # draw tasks
    row_number = 0
    for task_idx in range(len(tasks)):
        task = tasks[task_idx]

        task = f"{task_idx+1}. {task}"

        width, height = draw.textsize(task, font=font)

        if width > 2400:
            temp_task = ""
            while True:
                temp_task += task[:1]
                task = task[1:]
                width, _ = draw.textsize(temp_task, font=font)
                if width > 2400:

                    task = temp_task[-1:] + task
                    temp_task = temp_task[:-1]

                    draw.text(
                        (30, 600 + (row_number * 60)),
                        temp_task,
                        fill="black",
                        font=font,
                    )
                    temp_task = ""
                    row_number += 1
                elif (temp_task == "") and (task == ""):
                    break
                elif task.strip() == "":
                    draw.text(
                        (30, 600 + (row_number * 60)),
                        temp_task,
                        fill="black",
                        font=font,
                    )
                    temp_task = ""
                    row_number += 1
            continue

        draw.text(
            (30, 600 + (row_number * 60)), task, fill="black", font=font,
        )

        row_number += 1

    return bilet


def generate_a4(first_builet, last_builet):
    a4 = Image.open("./docs/a4.png")

    a4.paste(first_builet, (0, 0))

    if last_builet:
        a4.paste(last_builet, (0, 1750))

    return a4


if __name__ == "__main__":
    builet = draw(
        "272",
        "09.02.03",
        "2",
        "4",
        "30",
        "В. В. Ладынина",
        "Т. В. Доррер",
        ["Галич", "Путен"],
        ["История", "Программирование"],
        [
            "Возникновение и развитие Древнерусского государства (IX – начало ХII в.)",
            "Экономическое и социально-политическое развитие России в начале ХХ в",
            "Политическая раздробленность на Руси. Русь удельная (XII–XIII вв.)",
            "Политическая раздробленность на Руси. Русь удельная (XII–XIII вв.)Политическая раздробленность на Руси. Русь удельная (XII–XIII вв.)Политическая раздробленность на Руси. Русь удельная (XII–XIII вв.)",
            "Культура Древней Руси (Х–ХIII вв.). Значение принятия христианства",
        ],
    )
    builet.show()
    # generate_a4(builet, None)
