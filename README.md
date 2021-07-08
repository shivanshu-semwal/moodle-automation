# Moodle Utilities

This script can be used with [Moodle LMS](https://moodle.org/).

## Requirements

- `python3`
- `beautiful soup` (`pip install bs4`)
- `selenium` (`pip install selenium`)
- `selenium-driver` (either mozilla one or chrome one)
  - [get driver for mozilla firefox](https://github.com/mozilla/geckodriver/releases)
  - [get driver for google chrome](https://chromedriver.chromium.org/downloads)

## How to use

- satisfy all the requirements needed above
- either clone `git clone https://github.com/shivanshu-semwal/moodle-automation` or download this repo
- copy the `selenium-driver` to the cloned directory
- open `terminal/cmd` and navigate to the directory
- run `python3 ./main.py` if you want output in terminal
- or store to a `markdown` file `python3 ./main.py > moodle.md`, open `moodle.md` in you 
favorite markdown editor

## Configuration

- modify these option in  `main.py` script

```py
# use chrome, if set to false firefox will be used
useChrome = True

# path for the driver including the file name
driverPath = "./chromedriver"
# driverPath = "./geckodriver"
# driverPath = "./chromedriver.exe"
# driverPath = "./geckodriver.exe"

# moodle link
loginPage = "http://url"

# username and password
loginData = ["username", "password"]

# show completed topics too
showCompleted = True

# mark all topics complete
markAllComplete = True
```

[MIT License](./LICENSE)