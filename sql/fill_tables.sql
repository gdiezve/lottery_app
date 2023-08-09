INSERT INTO "lottery_participant" (name, surname, national_id_card, age)
VALUES ('Gina', 'Díez', '12345678A', 30)
     , ('Fran', 'Alonso', '87654321B', 32)
     , ('Anna', 'Casablanca', '347892134C', 67)
     , ('Jordi', 'Valles', '895436773D', 52)
     , ('Raquel', 'García', '453927562G', 42)
     ;

INSERT INTO "lottery_ballot" (number, participant_id, lottery_date)
VALUES (0, 1, '2023-08-07')
     , (1, 1, '2023-08-07')
     , (2, 2, '2023-08-07')
     , (3, 3, '2023-08-07')
     , (4, 2, '2023-08-07')
     , (5, 5, '2023-08-07')
     , (6, 4, '2023-08-07')
     , (7, 3, '2023-08-07')
     , (8, 4, '2023-08-07')
     , (9, 2, '2023-08-07')
     , (10, 5, '2023-08-07')
     ;

INSERT INTO "lottery_lottery" (lottery_date)
VALUES ('2023-08-07')
     , ('2023-08-08')
     ;
