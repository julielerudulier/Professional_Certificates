-- Keep a log of any SQL queries you execute as you solve the mystery.

-- First, I want to see what information I can get from the crime_scene_reports table.
SELECT *
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = 'Humphrey Street';

-- CRIME ID = 295

-- That query gives us the time of the crime which is 10:15am, and the exact location of the event which is the Humphrey Street bakery.
-- We also learn that interviews were conducted the same day with three witnesses, all of which mention the bakery.
-- Let's have a look at these interviews:
SELECT *
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE '%bakery%';

-- Thanks to the transcripts of the interviews, we learn that the thief drove away within 10 minutes of the theft.
-- We also learn that they withdraw money at the ATM that's on Leggett Street some time before the theft.
-- Finally, we learn that the thief called someone while leaving the bakery. They spoke for less than a minute.
-- The thief was planning to take the earliest flight out of Fiftyville tomorrow and asked the person on the phone to purchase the flight ticket.

-- Let's start by looking at security logs from the bakery:
SELECT *
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute BETWEEN 15 AND 30;

-- We see here that 8 cars exited the bakery's parking lot within 10 minutes of the theft.
-- As we now know what their licence_plate is, we can run a query from the people database and get their names:
SELECT *
FROM people
WHERE license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute BETWEEN 15 AND 24);

-- This query provides us with names, phone numbers and passport numbers.
-- We can thus cross reference these results with the information contained in the atm_transactions and bank_accounts tables, as we know the thief withdraw money earlier that day.
SELECT person_id, name, phone_number, passport_number
FROM atm_transactions AS a, bank_accounts AS b, people AS c
WHERE a.account_number = b.account_number
AND b.person_id = c.id
AND a.transaction_type = 'withdraw'
AND a.atm_location = 'Leggett Street'
AND a.year = 2021
AND a.month = 7
AND a.day = 28
AND c.license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute BETWEEN 15 AND 24);

-- This query helps us narrow down our list of suspects to 4 potential thieves instead of 8 previously.
-- We're now going to look at the airports, flights and passengers tables, as we know the thief wanted to leave town the next day:
SELECT *
FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
AND origin_airport_id =
    (SELECT id
    FROM airports
    WHERE city = 'Fiftyville')
ORDER BY hour, minute;

-- We now know that the earliest flight to fly out of Fiftyville on July 29th took off at 8:20am and its flight id is 36.
-- By running a query from the passengers table and matching this new piece of information with the name of the passengers, we should find out who our thief is:
SELECT name, phone_number
FROM people AS pe, passengers AS pa, flights AS fl
WHERE pe.passport_number = pa.passport_number
AND pa.passport_number IN
    (SELECT passport_number
    FROM atm_transactions AS a, bank_accounts AS b, people AS c
    WHERE a.account_number = b.account_number
    AND b.person_id = c.id
    AND a.transaction_type = 'withdraw'
    AND a.atm_location = 'Leggett Street'
    AND a.year = 2021
    AND a.month = 7
    AND a.day = 28)
AND pe.license_plate IN
    (SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute BETWEEN 15 AND 24)
AND pa.flight_id =
    (SELECT id
    FROM flights
    WHERE year = 2021
    AND month = 7
    AND day = 29
    AND origin_airport_id =
        (SELECT id
        FROM airports
        WHERE city = 'Fiftyville')
    ORDER BY hour, minute
    LIMIT 1)
GROUP BY name;

-- We still have 2 suspects: Bruce and Luca.
-- The last thing we need to do to find out who our thief is is to look for a match between Luca and Bruce's phone numbers and the phone numbers logged in the phone_calls table:
SELECT name
FROM people
WHERE phone_number =
    (SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration <= 60
    AND caller IN
        (SELECT phone_number
        FROM people AS pe, passengers AS pa, flights AS fl
        WHERE pe.passport_number = pa.passport_number
        AND pa.passport_number IN
            (SELECT passport_number
            FROM atm_transactions AS a, bank_accounts AS b, people AS c
            WHERE a.account_number = b.account_number
            AND b.person_id = c.id
            AND a.transaction_type = 'withdraw'
            AND a.atm_location = 'Leggett Street'
            AND a.year = 2021
            AND a.month = 7
            AND a.day = 28)
        AND pe.license_plate IN
            (SELECT license_plate
            FROM bakery_security_logs
            WHERE year = 2021
            AND month = 7
            AND day = 28
            AND hour = 10
            AND minute BETWEEN 15 AND 24)
        AND pa.flight_id =
            (SELECT id
            FROM flights
            WHERE year = 2021
            AND month = 7
            AND day = 29
            AND origin_airport_id =
                (SELECT id
                FROM airports
                WHERE city = 'Fiftyville')
            ORDER BY hour, minute LIMIT 1)
        GROUP BY name));

-- And the thief is Bruce!
-- We can now find out where he escaped to:
SELECT city, full_name
FROM airports
WHERE id =
    (SELECT destination_airport_id
    FROM flights
    WHERE year = 2021
    AND month = 7
    AND day = 29
    AND origin_airport_id =
        (SELECT id
        FROM airports
        WHERE city = 'Fiftyville')
    ORDER BY hour, minute
    LIMIT 1);

-- Bruce escaped to New York City flying out to LaGuardia Airport!
-- And lastly, his accomplice was:
SELECT name
FROM people
WHERE phone_number =
    (SELECT receiver
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration <= 60
    AND caller IN
        (SELECT phone_number
        FROM people AS pe, passengers AS pa, flights AS fl
        WHERE pe.passport_number = pa.passport_number
        AND pa.passport_number IN
            (SELECT passport_number
            FROM atm_transactions AS a, bank_accounts AS b, people AS c
            WHERE a.account_number = b.account_number
            AND b.person_id = c.id
            AND a.transaction_type = 'withdraw'
            AND a.atm_location = 'Leggett Street'
            AND a.year = 2021
            AND a.month = 7
            AND a.day = 28)
        AND pe.license_plate IN
            (SELECT license_plate
            FROM bakery_security_logs
            WHERE year = 2021
            AND month = 7
            AND day = 28
            AND hour = 10
            AND minute BETWEEN 15 AND 24)
        AND pa.flight_id =
            (SELECT id
            FROM flights
            WHERE year = 2021
            AND month = 7
            AND day = 29
            AND origin_airport_id =
                (SELECT id
                FROM airports
                WHERE city = 'Fiftyville')
            ORDER BY hour, minute LIMIT 1)
        GROUP BY name));

-- Bruce's accomplice was Robin!
-- Mystery solved :)
