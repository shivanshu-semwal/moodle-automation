# Moodle Utilities

This script can be used with [Moodle LMS](https://moodle.org/).

## Requirements

- `python3` - download [here](https://www.python.org/downloads/)
- `beautiful soup` (`pip install bs4`)
- `selenium` (`pip install selenium`)
- `selenium-driver` (either mozilla one or chrome one)
  - [get driver for mozilla firefox](https://github.com/mozilla/geckodriver/releases)
  - [get driver for google chrome](https://chromedriver.chromium.org/downloads)

## How to use

- satisfy all the requirements needed above
- either clone `git clone https://github.com/shivanshu-semwal/moodle-automation` or [download this repo](https://github.com/shivanshu-semwal/moodle-automation/archive/refs/heads/master.zip) and extract it.
- copy the `selenium-driver` to the cloned directory
- open `terminal/cmd` and navigate to the directory
- run `python3 ./main.py` if you want output in terminal
- or store to a `markdown` file `python3 ./main.py > moodle.md`, open `moodle.md` in you 
favorite markdown editor

## Configuration

- modify these option in  `config.json` file

```json
{
    "useChrome": true,
    "driverPath": "./chromedriver",
    "loginPage": "http://url",
    "loginData": [
        "username",
        "password"
    ],
    "showCompleted": false,
    "markAllComplete": false,
    "getRedirectedLinks": false,
    "showSectionHeadings": false,
    "showBrowser": true
}
```

[MIT License](./LICENSE)