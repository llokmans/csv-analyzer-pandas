# csv-analyzer-pandas

A login security report built with pandas. It reads a CSV of login attempts and answers the questions a security analyst asks first.

## What it reports

- Total number of logins
- Breakdown of successful vs failed attempts
- Failed logins grouped by IP address, to spot likely attackers
- The usernames attackers target most

## Data

`logins.csv` has four columns: `timestamp`, `ip`, `username`, `status`.

## Tech

Python · pandas (filtering, `value_counts`)

## Run it

```
pip install pandas
python analyze.py
```
