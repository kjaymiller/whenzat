# whenzat
A Time-Till menubar app written in python.

Whenzat uses `rumps` and `py2app` to create a simple time-till application. 

Whenzat makes some pretty educated decisions on the time you mean.
Parsed Date (October 6, Oct 6, 10/6)
An Integer will reference the next time that date arrives

## Quick Start
- Clone the Repo
- create virutalenv
- install requirements `pip install -r requirements.txt`
- Update your `when.json` file.
- Run `python whenzat_rumps.py` for the menubar version
- Run `python whenzat.py` for cli version

## Standalone Application
Use `py2app` and `setup.py` to make a standalone application.

## Menubar Mode
- The menubar mode will only 

## CLI Mode
- You can use the cli version of whenzat to quickly get a time until list in your terminal.
Examples:
    ```
    python whenzat.py how-long January 1
    >>> January 1: 1 month 23 days and 16 hours.
    
    python whenzat.py from-file
    >>> Januay 1: 1 month 23 days and 16 hours.
    ```

## Requirements:
- Python 3.6+

## License
Whenzat is licensed with the [MIT License](/LICENSE)
