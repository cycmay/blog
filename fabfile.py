from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/cycmay/blogByDjango.git'

env.user = 'root'
env.password = 'Cyc19971215/'

env.hosts = ['123.56.218.23']

env.port = '22'

def deploy():
    source_folder = '/home/cyc/sites/www.helloc.site/blogByDjango/blogproject'

    run('cd %s && git pull % source_folder')
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-123.56.218.23')
    sudo('service nginx reload')
