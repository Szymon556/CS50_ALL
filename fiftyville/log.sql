-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10  AND minute = 16);--sprawdzamy dokogo należy podejrzana rejesracja

SELECT * FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 221103);

SELECT * FROM people WHERE phone_number IN(SELECT receiver FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 221103) AND year = 2021 AND month = 7 AND day = 28);

SELECT * FROM people WHERE phone_number IN(SELECT caller FROM phone_calls WHERE receiver IN (SELECT phone_number FROM people WHERE id = 221103) AND year = 2021 AND month = 7 AND day = 28);--sprawdzam od kogo odebrała tego dnia telofn Vanessa

SELECT * FROM people WHERE phone_number IN(SELECT receiver FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 632023) AND year = 2021 AND month = 7 AND day = 28);--sprawdzamy do kogo dzwoniłą Amanda tego dnia i okazuje się że do nikogo nie dzwoniła
SELECT * FROM bank_accounts WHERE person_id = 632023;

SELECT * FROM atm_transactions WHERE day = 28 AND month = 7  AND year = 2021 AND atm_location = "Leggett Street";

SELECT * FROM atm_transactions WHERE account_number IN (SELECT account_number FROM bank_accounts WHERE person_id = 632023); --Szukamy kto zrobił wypłate z ATM i to nie Amanda

SELECT * FROM atm_transactions WHERE account_number IN (SELECT account_number FROM bank_accounts WHERE person_id IN (SELECT id FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE license_plate IN (SELECT license_plate FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)) AND year = 2021 AND day = 28 AND month = 7 AND hour = 10) )); -- szukamy kto zrobił wypłate z atm oraz jest na pokłądzie samolotu oraz było widać jego rejestracje w momencie kradzieży

SELECT MIN(hour),origin_airport_id,id FROM flights WHERE year = 2021 AND day = 29;

SELECT * FROM passengers WHERE flight_id = 36;

SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36) AND phone_number IN(SELECT receiver FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 221103) AND year = 2021 AND month = 7 AND day = 28);--wychodzi na to że nie ma żadnego posiadacza odebranego telefonu na pokładzie

SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36) AND phone_number IN(SELECT caller FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id = 221103) AND year = 2021 AND month = 7 AND day = 28);

SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7  AND year = 2021 AND atm_location = "Leggett Street" AND account_number IN (SELECT account_number FROM bank_accounts WHERE person_id IN (SELECT id FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)));--sprawdzamy jacy pasażerowanie tego lotu robili wypłąty tego dnia na Legget Street

SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7  AND year = 2021 AND atm_location = "Leggett Street" AND transaction_type = "withdraw" AND account_number IN (SELECT account_number FROM bank_accounts WHERE person_id IN (SELECT id FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)))));--mamy 4 podejrzanych którzy w dniu kradzieży wypłacali z ATM i są na pokładzie

SELECT * FROM phone_calls WHERE day = 28 AND year = 2021 AND month = 7 AND receiver IN ( SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7  AND year = 2021 AND atm_location = "Leggett Street" AND account_number IN (SELECT account_number FROM bank_accounts WHERE person_id IN (SELECT id FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36))))));-- sprawdzamy który z pasażerów odebrał telefon tego dnia oraz wypłącał pieniądze mamy 1 podejrzanego

SELECT * FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE id = 227);--obydwa telefony odebrała Luca teraz czas sprawdzić od kogo
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE id = 227);--dłuższy od jakiego Waltera
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE id = 234);--krótszy od jakiejś Kathryn

SELECT * FROM people WHERE phone_number IN ( SELECT caller  FROM phone_calls WHERE receiver IN (SELECT caller FROM phone_calls WHERE id = 234) AND year = 2021 AND month = 7);--sprawdzamy wszystkich do których dzowniła Kathryn w tych dniach potwierdza że w dniu wylotu dzwniłą do Lucy
-- czas zobaczyć czy auto któregoś z pasażerów było widać pod piekarnią

SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE license_plate IN (SELECT license_plate FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)) AND year = 2021 AND day = 28 AND month = 7);--sprawdzamy wszystkich ludzi których auto było pod piekarnią w dniu kradzieży oraz lecą tym samolotem

SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE license_plate IN (SELECT license_plate FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)) AND year = 2021 AND day = 28 AND month = 7 AND hour = 10);

SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE id = 246));--LUCA
SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE id = 266 ));--Taylor
SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE id = 267));--Bruce

SELECT * FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE id = 266))) AND year = 2021 AND month = 7 AND day = 28;-- wszystkie telefony jakie wykonał Taylor w dniu kradzieży

SELECT * FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE id = 267))) AND year = 2021 AND month = 7 AND day = 28 AND duration < 60;-- to samo dla Bruce

SELECT * FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE id = 267))) AND year = 2021 AND month = 7 AND day = 28 AND duration < 60); --sprawdzamy podejrzany telefon od Bruca

SELECT * FROM airports where id = 4;