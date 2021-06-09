## Test data for converting GAL/EQJ

This directory contains data generated by the [JPL Horizons](https://ssd.jpl.nasa.gov/horizons.cgi)
online tool with example conversions between equatorial J2000 (EQJ)
and galactic (GAL) coordinates.

Here are the steps to reproduce this test data on JPL Horizons:

1. Ephemeris Type = OBSERVER
2. Target Body = Mars (499)
3. Observer Location = Geocentric (500)
4. Time Span: Start=2021-06-06, Stop=2031-06-06, Step=100 days
5. Table Settings: check boxes 1 (Astrometric RA, DEC) and 33 (Galactic lon, lat).
6. Also on Table Settings, change angle format to decimal degrees;
   airless (no refraction); enable extra precision.
7. Set Display Output to plain text.
8. Generate the data, Ctrl+A, Ctrl+C to copy to clipboard.
   Paste into editor. Add an extra blank line at the end, and save.

Here are the equivalent "batch file" settings:

```
!$$SOF
COMMAND= '499'
CENTER= '500@399'
MAKE_EPHEM= 'YES'
TABLE_TYPE= 'OBSERVER'
START_TIME= '2021-06-06'
STOP_TIME= '2031-06-06'
STEP_SIZE= '100 d'
CAL_FORMAT= 'CAL'
TIME_DIGITS= 'MINUTES'
ANG_FORMAT= 'DEG'
OUT_UNITS= 'KM-S'
RANGE_UNITS= 'AU'
APPARENT= 'AIRLESS'
SUPPRESS_RANGE_RATE= 'NO'
SKIP_DAYLT= 'NO'
EXTRA_PREC= 'YES'
R_T_S_ONLY= 'NO'
REF_SYSTEM= 'J2000'
CSV_FORMAT= 'NO'
OBJ_DATA= 'YES'
QUANTITIES= '1,33'
!$$EOF
```