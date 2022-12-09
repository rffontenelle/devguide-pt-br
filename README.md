# devguide-pt-br
Brazilian Portuguese translation for the Python developer's guide

## How to set up the environment

1. Clone this repository
```shell
git clone github.com/rffontenelle/devguide-pt-br
```

2. Set up a virtual environment, and activate it 
```shell
python3 -mvenv venv
source venv/bin/activate
```

3. Clone the repository of the devguide
```shell
git clone https://github.com/python/devguide
```

4. Install dependencies
```shell
pip install powrap sphinx-intl -r devguide/requirements.txt
```

Environment is ready, and simply running `python update.py` should
update the translation files
