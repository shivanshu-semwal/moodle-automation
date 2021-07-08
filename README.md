# Moodle Utilities

This script can be used with [Moodle LMS](https://moodle.org/).

## Requirements

- `python3`
- `beautiful soup` (`pip install bs4`)
- `selenium` (`pip install selenium`)
- selenium-driver (either mozilla one or chrome one) - download and copy the driver in the directory in which the file
  - [get driver for mozilla firefox](https://github.com/mozilla/geckodriver/releases)
  - [get driver for google chrome](https://chromedriver.chromium.org/downloads)

## How to use

- either clone or download the repo
- to run `python3 ./main.py`
- or store to a `markdown` file `python3 ./main.py > moodle.md`

## Configuration

- modify these option in  `main.py` script

```py
# use chrome, if set to false firefox will be used
useChrome = True

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