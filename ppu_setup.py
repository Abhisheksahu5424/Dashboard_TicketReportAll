import os
import subprocess


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out.decode(), err.decode()


# Step 1: Download and Install Python 3.9
python_version = "3.9.1"
python_tarball_url = f"https://www.python.org/ftp/python/{python_version}/Python-{python_version}.tgz"

run_command(f"sudo apt update")
run_command(
    f"sudo apt install libffi-dev libsqlite3-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev build-essential libreadline-dev wget libbz2-dev")
run_command(f"cd /home/parkzap/")
run_command(f"wget {python_tarball_url}")
run_command(f"tar -xzvf Python-{python_version}.tgz")
run_command(f"cd Python-{python_version} && ./configure && make && sudo make install")
run_command(f"python3 --version")

# Step 2: Clone the Repo
run_command(f"cd /opt/ && mkdir ppu")
run_command(f"git clone https://ppu_vijayawada:AMTEcP1CvejncwB-88EK@gl.stackfusion.io/jeet/ppu-api.git")
run_command(f"cd /opt/ppu/ppu-api/")

# Step 3: Create Virtual Environment
run_command(f"python3.9 -m pip install --user virtualenv")
run_command(f"cd /opt/ppu && python3.9 -m venv env && source env/bin/activate && git checkout staging_primary")

# Step 4: Install Requirements
run_command(f"pip install -r ppu/requirement.txt")
run_command(f"pip install psycopg2==2.9.1")

# Step 5: Create Database
run_command(f"sudo -i -u postgres")
run_command(f"createdb -O dev-django1 postgress_db2")
run_command(f"psql --dbname=postgress_db2 && CREATE EXTENSION pg_trgm; CREATE EXTENSION hstore;")

# Step 6: Migrations and Static Files
run_command(f"python3 manage.py makemigrations")
run_command(f"python3 manage.py migrate")
run_command(f"python3 manage.py collectstatic")

# Step 7: Create Supervisor
supervisor_config = """
[program:run_ppu_uvicorn_server]
directory=/opt/p/ppu-api/ppu
command=/opt/ppu/env/bin/python3.9 -m gunicorn --workers=9 --threads=8 -b 0.0.0.0:5000 ppu.asgi:application -k uvicorn.workers.UvicornWorker
user=dev-django1
stdout_logfile=/var/log/jetson/run_ppu_server.out.log
stderr_logfile=/var/log/jetson/run_ppu_server.err.log
redirect_stderr=false
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
stdout_logfile_backups=0
stderr_logfile_backups=0
stderr_logfile_maxbytes=5MB
stdout_logfile_maxbytes=5MB
environment=PATH="/opt/ppu/env/bin/"
"""

with open("/etc/supervisor/conf.d/server_setup.conf", "w") as supervisor_file:
    supervisor_file.write(supervisor_config)

# Step 8: Install Nginx and Configure
run_command(f"sudo apt install nginx")
nginx_config = """
# Copy the nginx configuration present in /opt/ppu-api/ppu/scripts/Nginx/ngnix_configration.conf into this file.
"""

with open("/etc/nginx/sites-enabled/ngnix_configration.conf", "w") as nginx_file:
    nginx_file.write(nginx_config)

run_command(f"sudo nginx -t")
run_command(f"sudo systemctl restart nginx")
