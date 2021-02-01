--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-1.pgdg16.04+1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-1.pgdg16.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: complexity; Type: TABLE; Schema: public; Owner: misha
--

CREATE TABLE public.complexity (
    complexity character varying(16) NOT NULL
);


ALTER TABLE public.complexity OWNER TO misha;

--
-- Name: professors; Type: TABLE; Schema: public; Owner: misha
--

CREATE TABLE public.professors (
    id integer NOT NULL,
    first_name character varying(16) NOT NULL,
    last_name character varying(16) NOT NULL,
    patronymic character varying(16) NOT NULL
);


ALTER TABLE public.professors OWNER TO misha;

--
-- Name: professors_id_seq; Type: SEQUENCE; Schema: public; Owner: misha
--

CREATE SEQUENCE public.professors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.professors_id_seq OWNER TO misha;

--
-- Name: professors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: misha
--

ALTER SEQUENCE public.professors_id_seq OWNED BY public.professors.id;


--
-- Name: subjects; Type: TABLE; Schema: public; Owner: misha
--

CREATE TABLE public.subjects (
    professor_id integer NOT NULL,
    name character varying(32) NOT NULL
);


ALTER TABLE public.subjects OWNER TO misha;

--
-- Name: tasks; Type: TABLE; Schema: public; Owner: misha
--

CREATE TABLE public.tasks (
    text character varying(256) NOT NULL,
    complexity_id character varying(16) NOT NULL,
    subject_professor_id integer NOT NULL,
    subject_name character varying(32) NOT NULL
);


ALTER TABLE public.tasks OWNER TO misha;

--
-- Name: users; Type: TABLE; Schema: public; Owner: misha
--

CREATE TABLE public.users (
    login character varying(32) NOT NULL,
    password character varying(32) NOT NULL
);


ALTER TABLE public.users OWNER TO misha;

--
-- Name: professors id; Type: DEFAULT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.professors ALTER COLUMN id SET DEFAULT nextval('public.professors_id_seq'::regclass);


--
-- Data for Name: complexity; Type: TABLE DATA; Schema: public; Owner: misha
--

COPY public.complexity (complexity) FROM stdin;
Легкий
Средний
Сложный
\.


--
-- Data for Name: professors; Type: TABLE DATA; Schema: public; Owner: misha
--

COPY public.professors (id, first_name, last_name, patronymic) FROM stdin;
1	Александр	Глускер	Игоревич
2	Владимир	Петросян	Степанович
\.


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: misha
--

COPY public.subjects (professor_id, name) FROM stdin;
1	История
2	Информатика
2	Программирование
1	ОБЖ
\.


--
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: misha
--

COPY public.tasks (text, complexity_id, subject_professor_id, subject_name) FROM stdin;
Сколько лет Путину?	Легкий	2	Информатика
Возникновение и развитие Древнерусского государства (IX – начало ХII в.)	Легкий	1	История
Экономическое и социально-политическое развитие России в начале ХХ в	Легкий	1	История
Культура Древней Руси (Х–ХIII вв.). Значение принятия христианства	Легкий	1	История
Революция 1905–1907 гг.: причины, этапы, значение.	Средний	1	История
Борьба Руси против внешних вторжений в ХIII в	Средний	1	История
Реформы П.А. Столыпина. Направления, итоги и значение аграрной реформы.	Средний	1	История
Объединение русских земель вокруг Москвы и становление единого Российского государства в ХIV–XV вв.	Средний	1	История
Культура России в начале ХХ в. (1900–1917 гг.), ее вклад в мировую культуру	Средний	1	История
Московская Русь в эпоху Ивана Грозного	Сложный	1	История
Участие России в Первой мировой войне: причины, роль Восточного фронта, последствия	Сложный	1	История
Основные направления внешней политики и расширение территории Российского государства в ХV–XVI вв.	Сложный	1	История
1917 год в России (основные события, их характер и значение).	Сложный	1	История
Культура и духовная жизнь Руси в ХIV–XV вв	Сложный	1	История
Сколько мне лет?	Сложный	2	Информатика
Внешняя политика России в конце XIX – начале ХХ в. Русско-японская война: причины, ход военных действий, итоги и последствия.	Легкий	1	История
Политическая раздробленность на Руси. Русь удельная (XII–XIII вв.)	Легкий	1	История
Образование государства Киевская Русь: предпосылки, причины, точки зрения на эту проблемы в историографии.	Легкий	1	История
«Норманнская теория» и антинорманнизм в российской исторической науке.	Легкий	1	История
Важнейшие причины принятия христианства Руcью.\n	Легкий	1	История
Проблема возникновения феодализма в России. Агрессия немецких и шведских феодалов. Ледовое побоище.	Легкий	1	История
Походы Батыя на Северо-Восточную и Южную Русь. Влияние татаро-монгольского нашествия и ига на развитие русских земель.	Легкий	1	История
Особенности объединительного процесса на Руси.	Легкий	1	История
Становление самодержавия в России.\n	Легкий	1	История
Внутренняя политика Московской Руси во второй половине XVI века.	Легкий	1	История
Причины, сущность и последствия Смуты. Проблема царской власти в период Смуты.	Легкий	1	История
Особенности политического развития России во второй половине XVII века. Становление абсолютизма.\n	Легкий	1	История
Сущность и последствия церковной реформы и Раскола в России в XVII века.	Легкий	1	История
Особенности «просвещенного абсолютизма» в Западной Европе и в России.	Легкий	1	История
Основные направления и влияние на развитие страны реформ Петра I.	Легкий	1	История
Начало модернизации в России и ее особенности.	Легкий	1	История
Основные направления внутренней и внешней политика России при Екатерине II.	Легкий	1	История
Особенности социально-экономического и политического развития России в первой половине XIX века.  Сущность «правительственного либерализма»	Средний	1	История
Основные направления развития войны 1812 года и заграничных походов российской армии.\n	Средний	1	История
Декабристы и их влияние на развитые страны.\n	Средний	1	История
Основные направления развития общественной мысли в 30-50-е годы XIX века.\n	Средний	1	История
Крымская война и е влияние на развитые страны.\n	Средний	1	История
Сущность второй промышленной революции и ее влияние на мировое развитие.\n	Средний	1	История
Содержание «Великих реформ» в России. Соотношение либерального и консервативного курсов в правительственной политике Александра II.\n	Средний	1	История
Внешняя политика России во второй половине XIX – начале XX вв.\n	Средний	1	История
Народническое движение.\n	Средний	1	История
Цель и значение реформ С.Ю.Витте.\n	Средний	1	История
Особенности внутренней  политики правительства Александра III.\n	Средний	1	История
Причины и следствия революции 1905 – 1907 гг. в России.\n	Средний	1	История
Особенности российского парламентаризма.\n	Средний	1	История
Крестьянская община в России: ее достоинства и недостатки.\n	Средний	1	История
Цели и содержание реформ П.Столыпина.\n	Средний	1	История
Предпосылки и итоги Первой мировой войны. Влияние войны на внутреннее положение России.\n	Средний	1	История
Особенности российского либерализма. Либеральные партии в России.\n	Средний	1	История
Цели и программные положения революционных партий России.\n	Средний	1	История
Цели и программные положения консервативных партий в России.\n	Сложный	1	История
Причины и особенности революции в 1917 году в России.\n	Сложный	1	История
Представления о будущей государственности у большевиков до 1917 и их реальная политика в 1917-1918 гг.\n	Сложный	1	История
Причины и следствия гражданской войны в России.\n	Сложный	1	История
Основные черты политики «военного коммунизма».\n	Сложный	1	История
Новая экономическая политика: причины, сущность, следствия.\n	Сложный	1	История
Основные тенденции мирового развития СССР в 20-е – 30-е гг.\n	Сложный	1	История
Причины зарождения фашизма в Европе.\n	Сложный	1	История
Особенности международной ситуации в 30 – 40-х гг. XX в. и внешняя политика СССР.\n	Сложный	1	История
Великая Отечественная война, ее основные этапы, итоги и уроки.  Проблемы изучения Второй мировой войны в историографии.\n	Сложный	1	История
Основные тенденции развития СССР в 1950 – 1980-е гг.\n	Сложный	1	История
Сущность третьей научно-технической революции, постиндустриальной цивилизации.\n	Сложный	1	История
Основные тенденции мирового развития на современном этапе.\n	Сложный	1	История
Особенности развития СССР в период «перестройки».\n	Сложный	1	История
Распад СССР и его последствия.\n	Сложный	1	История
Внутренняя политика России в 1991 – 2011 гг.\n	Сложный	1	История
Внешняя политика СССР и РФ 1985 – 2011 гг.\n	Сложный	1	История
Объекты	Средний	2	Программирование
Основы алгоритмизации и программирования. Алгоритмы: свойства, способы, описания.	Средний	2	Программирование
Виды алгоритмов и основные принципы составления.	Средний	2	Программирование
Основные положения и методы использования базовых алгоритмических структур.	Средний	2	Программирование
Введение в программирование.	Средний	2	Программирование
Инструменты программирования.	Средний	2	Программирование
Языки программирования.	Средний	2	Программирование
Трансляторы	Средний	2	Программирование
Языки программирования: эволюция, классификация.	Средний	2	Программирование
Основные элементы языка. Идентификаторы	Средний	2	Программирование
Структура программы	Средний	2	Программирование
Типы данных в программе: целые типы, вещественные типы, логический тип, символьный тип.	Средний	2	Программирование
Типы данных в программе: строковый тип данных.	Средний	2	Программирование
Выражения и арифметические операции.	Средний	2	Программирование
Оператор присваивания, оператор ввода и оператор вывода.	Сложный	2	Программирование
Основные алгоритмические конструкции. Линейный оператор. Приведите пример.	Сложный	2	Программирование
Основные алгоритмические конструкции. Оператор ветвления. Приведите пример.	Сложный	2	Программирование
Основные алгоритмические конструкции. Оператор выбора. Приведите пример.	Сложный	2	Программирование
Основные алгоритмические конструкции. Оператор цикла с параметром. Приведите пример.	Сложный	2	Программирование
Понятие подпрограммы. Достоинства подпрограмм. 	Сложный	2	Программирование
Графические средства QBasic: графические режимы окна, цвет фона и цвет рисунка.	Сложный	2	Программирование
Графические средства QBasic: графические примитивы, закраски и заполнения.	Сложный	2	Программирование
Символьные строки QBasic: основные функции. Примеры.	Сложный	2	Программирование
Структурированный тип данных: одномерные массивы. Приведите пример.	Сложный	2	Программирование
Структурированный тип данных: двумерные массивы. Приведите пример	Сложный	2	Программирование
Основные понятия ООП	Сложный	2	Программирование
Классы объектов	Средний	2	Программирование
Свойства	Средний	2	Программирование
Метод	Средний	2	Программирование
События	Средний	2	Программирование
Инкапсуляция	Средний	2	Программирование
Наследование	Средний	2	Программирование
Полиморфизм	Средний	2	Программирование
Визуальное проектирование интерфейса\t	Средний	2	Программирование
Этапы разработки приложения	Средний	2	Программирование
Структура проекта VB	Легкий	2	Программирование
Среда разработки VB	Легкий	2	Программирование
Переменные	Легкий	2	Программирование
Константы	Легкий	2	Программирование
Функция InputBox	Легкий	2	Программирование
Функция MsgBox	Легкий	2	Программирование
Ввод и вывод данных в VB	Легкий	2	Программирование
Вывод результатов	Легкий	2	Программирование
Математические функции и функции преобразования данных	Легкий	2	Программирование
Функция Format	Легкий	2	Программирование
Условные операторы	Легкий	2	Программирование
Циклы	Легкий	2	Программирование
Циклы с параметром	Легкий	2	Программирование
Методы графики в VB\t	Легкий	2	Программирование
Задание цвета\t	Легкий	2	Программирование
Свойства объектов, влияющих на графические методы	Легкий	2	Программирование
Применение метода Scale	Легкий	2	Программирование
Объект управления Shape (Фигура)	Легкий	2	Программирование
Объект управления Timer	Легкий	2	Программирование
Объект управления ProgressBar\t	Легкий	2	Программирование
Объект управления Slider (Движок)	Легкий	2	Программирование
Объект управления CheckBox (Флажок)	Легкий	2	Программирование
Объект управления OptionButton (Переключатель)	Легкий	2	Программирование
Работа с несколькими формами	Легкий	2	Программирование
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: misha
--

COPY public.users (login, password) FROM stdin;
@dmin	@dmin
\.


--
-- Name: professors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: misha
--

SELECT pg_catalog.setval('public.professors_id_seq', 3, true);


--
-- Name: complexity complexity_pkey; Type: CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.complexity
    ADD CONSTRAINT complexity_pkey PRIMARY KEY (complexity);


--
-- Name: professors professors_pkey; Type: CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_pkey PRIMARY KEY (id);


--
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (professor_id, name);


--
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (text);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (login);


--
-- Name: subjects_professor_id; Type: INDEX; Schema: public; Owner: misha
--

CREATE INDEX subjects_professor_id ON public.subjects USING btree (professor_id);


--
-- Name: tasks_complexity_id; Type: INDEX; Schema: public; Owner: misha
--

CREATE INDEX tasks_complexity_id ON public.tasks USING btree (complexity_id);


--
-- Name: tasks_subject_professor_id; Type: INDEX; Schema: public; Owner: misha
--

CREATE INDEX tasks_subject_professor_id ON public.tasks USING btree (subject_professor_id);


--
-- Name: subjects subjects_professor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professors(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: tasks tasks_complexity_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_complexity_id_fkey FOREIGN KEY (complexity_id) REFERENCES public.complexity(complexity);


--
-- Name: tasks tasks_subject_professor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_subject_professor_id_fkey FOREIGN KEY (subject_professor_id) REFERENCES public.professors(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: tasks tasks_subject_professor_id_subject_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: misha
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_subject_professor_id_subject_name_fkey FOREIGN KEY (subject_professor_id, subject_name) REFERENCES public.subjects(professor_id, name);


--
-- PostgreSQL database dump complete
--

