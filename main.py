import random
import string
import pymysql
from config import host, user, password, db_name
from faker import Faker
random.seed(10000)

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
    try:
        def generate_random_string(length):#рандомная строка
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for k in range(length))
            return rand_string
        def generate_pw(lenght):#рандомный пароль
            pas = ''
            for x in range(lenght):
                pas = pas + random.choice(list(
                    '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
            return pas
        def fake_companymail():               #почта для компаний
            fake = Faker()
            return fake.company_email()
        def fake_mail():                      #дефолтная почта работяги
            fake = Faker()
            return fake.ascii_free_email()
        def fake_text(lenght):                #рандомный текст
            fake = Faker('ru_RU')
            return fake.sentence(nb_words = lenght)
        def fake_phone():                     #рандомный номер телефона, Но перед этим заходим в папку venv/Lib/site-packages/faker/providers/phone_number/ru_RU  и открываем __init__, а в formats удаляем список и вставляем эти значение  "7##########","380#########","375#########","373#########"
            fake = Faker('ru_RU')
            return fake.phone_number()
        def fake_date():                      #случайная дата за последние 2 года
            fake = Faker()
            return fake.date_this_decade()
        def fake_date_bth():                  #случайная дата рождение, диапазон возрастов можно указать ниже
            fake = Faker()
            return fake.date_of_birth(None,1,30)#   1 - min_age, 30 - max_age (can change) None - лучше оставить;)
        def fake_city():                      #cлучайный город, село и т.д в Украине  пример: місто Зоринськ, селище Алушта,село Корець и т.д.Но перед этим заходим в папку venv/Lib/site-packages/faker/providers/address/uk_UA и открываем __init__, ищем через ctrl+f кавычки ( ' ) и удаляем их.
            fake = Faker('uk_UA')
            return fake.city()
        def fake_price():                     #случайная цена в float
            price = random.randint(5,100000)/100
            return price
        def fake_streetaddress():             #случайный адресс пример: узвіз Городня, буд. 35 кв. 3,сквер Капітана Гаврікова, буд. 7 кв. 7,узвіз Раїси Сергієнко, буд. 34 кв. 527 и т.д
            fake = Faker('uk_UA')
            return fake.street_address()
        def fake_company():                   #случайное название компании пример: ЗАО «Крылова»,ОАО «Григорьева, Рыбаков и Бирюков»,Холдинг Транспортные компоненты, ООО «Овчинников-Матвеева» и т.д
            fake = Faker('ru_RU')
            return fake.company()
        def fake_word():                      #случайное слово
            fake = Faker('ru_RU')
            return fake.word()

        for i in range(0, 700):               #500 - количество записей
                        with connection.cursor() as cursor:
                            mail = ["@gmail.com", "@mail.ru", "@yandex.ru", "@ui.ua", "@nure.ua", "@rambler.com",
                                    "@outlook.com", "@aval.ua", "@yahoo.com", ]
                            l = ["Олексій", "Максим", "Марина", "Аліна", "Олена", "Владислав", "Борислав", "Олександр",
                                 "Валерія", "Звенимир", "Захар", "Устим",
                                 "Сергій", "Федір", "Йосеф", "Юхим", "Радослав", "Юрій", "Йосип", "Іван", "Артур",
                                 "Гліб", "Еміль", "Панас", "Георгій", "Мартин",
                                 "Славомир", "Едуард", "Ігор", "Ян", "Роман", "Любава", "Юнія", "Яна", "Наталія",
                                 "Капитолина", "Дарина", "Либідь", "Ярослава",
                                 "Євгенія", "Евеліна", "Адріана", "Таїсія", "Карина", "Уляна", "Злата", "Любов",
                                 "Марта", "Ждана", "Елвіна", "Іванна", "Інна",
                                 "Белла", "Елла", "Ярина", "Сарра", "Ірма", "Орися", "Ладислава", "Устина", "Мстислава",
                                 "Людмила", ]
                            female = ["Черінько", "Чернобай", "Хаварівська", "Сивокінь", "Семків", "Семеніхіна",
                                      "Свиридовська", "Плешкан", "Пласконіс",
                                      "Атаманенко", "Овчаренко", "Михальчук", "Лубківська", "Литовченко", "Лашкевичі",
                                      "Кулинич", "Крітенко", "Кротюк",
                                      "Коханенко", "Коробчинська", "Коломиєць", "Кирієнко", "Качур", "Затула",
                                      "Жоравки", "Жаботинська", "Дмитрів", "Гребінь",
                                      "Говорун", "Гайдученко", "Гаврилишин", "Вітовська", "Візиренко", "Волянська",
                                      "Васянович", "Бабанська"]
                            male = ["Мелещенко", "Корольчук", "Сіренко", "Головінський", "Копитко", "Рудницький",
                                    "Ярошинський", "Мочурад", "Щоголів",
                                    "Довгань", "Ковалів", "Головенко", "Кобець", "Недря", "Ісаєвич", "Чабан",
                                    "Сереженко", "Дудик", "Марценюк", "Дерегус",
                                    "Линник", "Свашенко", "Мілютенко", "Сокуренко", "Овдовіченко", "Вербило",
                                    "Ленкевич", "Чекалюк", "Вороновський",
                                    "Ястремський", "Турянський", "Чаплинський", "Данканич", "Сердюк", "Павленко",
                                    "Демидась", ]
                            fname = l[random.randint(0, 61)]

                            if fname[len(fname) - 1:] == "а" or fname[len(fname) - 1:] == "я":
                                sname = female[random.randint(0, 35)]
                            else:
                                sname = male[random.randint(0, 35)]
                                status_id = random.randint(1,2)

                        


                            insert_query = "INSERT INTO `user` (email, password, name, second_name, `phone number`,status_id, about, created,total_spent)" " VALUES ('" \
                                           +fake_mail()+"',"+generate_pw(random.randint(6,15))+",'"+str(fname)+"' ,'"+str(sname)+"',,'"+str(fake_phone())+"','"+str(status_id)+"','"+str(fake_text(20))+"','"+str(fake_date())+"'," \
                                           +(str(fake_price()) if status_id == 1 else "NULL")+");"
                            cursor.execute(insert_query)
                            connection.commit()




                                                                
                            # create table
                            # with connection.cursor() as cursor:
                            #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
                            #                          " name varchar(32)," \
                            #                          " password varchar(32)," \
                            #                          " email varchar(32), PRIMARY KEY (id));"
                            #     cursor.execute(create_table_query)
                            #     print("Table created successfully")

                            # insert data
                            # with connection.cursor() as cursor:
                            #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Anna', 'qwerty', 'anna@gmail.com');"
                            #     cursor.execute(insert_query)
                            #     connection.commit()

                            # with connection.cursor() as cursor:
                            #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
                            #     cursor.execute(insert_query)
                            #     connection.commit()
                            #
                            # with connection.cursor() as cursor:
                            #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
                            #     cursor.execute(insert_query)
                            #     connection.commit()

                            # with connection.cursor() as cursor:
                            #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
                            #     cursor.execute(insert_query)
                            #     connection.commit()
                            #
                            # with connection.cursor() as cursor:
                            #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
                            #     cursor.execute(insert_query)
                            #     connection.commit()

                            # update data
                            # with connection.cursor() as cursor:
                            #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
                            #     cursor.execute(update_query)
                            #     connection.commit()

                            # delete data
                            # with connection.cursor() as cursor:
                            #     delete_query = "DELETE FROM `users` WHERE id = 5;"
                            #     cursor.execute(delete_query)
                            #     connection.commit()

                            # drop table
                            # with connection.cursor() as cursor:
                            #     drop_table_query = "DROP TABLE `users`;"
                            #     cursor.execute(drop_table_query)

                            # select all data from table
                            #with connection.cursor() as cursor:
                            #    select_all_rows = "SELECT * FROM `users`"
                            #    cursor.execute(select_all_rows)
                            #    # cursor.execute("SELECT * FROM `users`")
                            #    rows = cursor.fetchall()
                            #    for row in rows:
                            #        print(row)
                            #    print("#" * 20)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)