# eshop_proejct

## [preview]
![Uploading _-GoogleChrome2024-06-0917-02-00-ezgif.com-video-to-gif-converter.gif…]()

## Running the Project Locally

0. First, clone the repository to your local machine:
```bash
https://github.com/mehdi-shoqeyb/eshop_proejct.git
cd eshop_proejct
```

1. Ideally, create a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) and install the projects dependencies:
```bash
python3 -m venv env
source env/bin/activate
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Init database and runserver
```bash
./manage.py migrate
./manage.py runserver
```
