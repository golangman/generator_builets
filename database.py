from _database import *
from utils import _AutoInit


class _Professor(_AutoInit):
    pass


class _Subject(_AutoInit):
    pass


class _Difficulty(_AutoInit):
    pass


class _TaskCount(_AutoInit):
    pass


class DatabaseManager:
    def __init__(self) -> None:
        self.driver = database

    def sign_in(self, login: str, password: str) -> bool or Exception:
        cursor = database.execute_sql(
            f"SELECT * from users where users.login='{login}' and users.password='{password}';"
        )

        user = cursor.fetchone()

        if not user:
            return False

        return user

    def get_subjects_for_professor(self, professor_id: int) -> list:
        cursor = database.execute_sql(
            f"SELECT name from subjects where professor_id={professor_id};"
        )

        subjects = list()

        for row in cursor.fetchall():
            subjects.append(_Subject(professor_id=professor_id, name=row[0],))

        return subjects

    def get_all_professors(self) -> list:
        cursor = database.execute_sql(
            f"SELECT id, first_name, last_name, patronymic from professors;"
        )

        professors = list()

        for row in cursor.fetchall():
            professors.append(
                _Professor(
                    id=row[0], first_name=row[1], last_name=row[2], patronymic=row[3],
                )
            )

        return professors

    def get_all_difficulties(self) -> list:
        cursor = database.execute_sql(f"SELECT complexity from complexity;")

        difficulties = list()

        for row in cursor.fetchall():
            difficulties.append(_Difficulty(complexity=row[0],))

        return difficulties

    # def get_tasks(complexity) -> dict:
    #     cursor = database.execute_sql(f"SELECT complexity from complexity;")

    #     tasks = list()

    #     for row in cursor.fetchall():
    #         difficulties.append(_Difficulty(complexity=row[0],))

    #     return difficulties

    def get_count_tasks(self, comlexity_list, subject_professor_id, subject_name):
        comlexity_list_str = "".join(
            [f"'{comlexity}'," for comlexity in comlexity_list]
        )[:-1]
        cursor = database.execute_sql(
            f"select tasks.complexity_id, count(tasks.text) from tasks where tasks.complexity_id in ({comlexity_list_str}) and tasks.subject_professor_id = {subject_professor_id} and subject_name = '{subject_name}' group by tasks.complexity_id;"
        )

        tasks = list()

        for row in cursor.fetchall():
            tasks.append(_TaskCount(comlexity=row[0], count=row[1]))
            comlexity_list.remove(row[0])

        for comlexity in comlexity_list:
            tasks.append(_TaskCount(comlexity=comlexity, count=0))

        return tasks

    def get_tasks(self, complexity, subject_professor_id, subject_name, limit):
        cursor = database.execute_sql(
            f"""select tasks.text from tasks
where tasks.complexity_id = '{complexity}'
and tasks.subject_professor_id = {subject_professor_id}
and tasks.subject_name = '{subject_name}'
LIMIT {limit};"""
        )

        tasks = list()

        for row in cursor.fetchall():
            tasks.append(row[0].strip())

        return tasks


if __name__ == "__main__":
    db = DatabaseManager()

    result = db.get_count_tasks(
        comlexity_list=("Легкий", "Средний", "Сложный"),
        subject_professor_id=2,
        subject_name="Программирование",
    )
    print(result)

