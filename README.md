# eshop_proejct

## Running the Project Locally

0. First, clone the repository to your local machine:
```bash
git clone https://github.com/suhailvs/django-whatsapp
cd django-whatsapp
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

4. Optional: Install and Start Redis Server
```bash
sudo add-apt-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get install redis
redis-server
```
