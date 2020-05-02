[![webMonitoringBot Homepage](https://img.shields.io/badge/webMonitoringBot-develop-orange.svg)](https://github.com/davidvelascogarcia/webMonitoringBot/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/webMonitoringBot.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/webMonitoringBot/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/webMonitoringBot.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/webMonitoringBot)

# Web Monitoring Bot: webMonitoringBot (Python API)

- [Introduction](#introduction)
- [Running Software](#running-software)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`webMonitoringBot` module use `BeautifulSoup` in `python`. This module analyze and monitor website and send notification message to computer if website has changed or specific element in there. `webMonitoringBot` allow select website blocks to analyze. Also have support to send push notifications with `Pushbullet` API.


## Running Software

`webMonitoringBot` requires website `url` like input. Also need specific elements of `HTML` website to specific analysis, like `id` or other element like `div`, `section`, `h1` ... with their respective `class` name.
The process to running the program:

1. Execute [programs/webMonitoringBot.py](./programs), to start de program.
```python
python webMonitoringBot.py
```
2. Introduce your `url` and config analysis.

NOTE:

If use `Pushbullet` service configure `authentication.ini` with your token.

## Requirements

`webMonitoringBot` requires:

* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install requests:

```bash
pip install requests
```
* Install BeautifulSoup4:

```bash
pip install beautifulsoup4
```

* Install ConfigParser:

```bash
pip install configparser
```

**Microsoft Windows:**

* Install Win10Toast:

```bash
pip install win10toast
```

**Linux:**

* Install Notify2:

```bash
sudo apt-get install python3-notify2
```

**Optional:**

* Install Pushbullet:

```bash
pip install pushbullet.py
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/webMonitoringBot.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/webMonitoringBot)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/webMonitoringBot.svg?label=Issues)](https://github.com/davidvelascogarcia/webMonitoringBot/issues)

## Related projects

* [Web Scraping: docs](https://realpython.com/beautiful-soup-web-scraper-python/)

