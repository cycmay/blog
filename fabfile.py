#coding = utf-8
from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = "https://github.com/cycmay/blog.git"

env.user = 'root'
env.password = 'Cyc19971215/'

env.hosts = ['123.56.218.23']

env.port = '22'

def deploy():
    source_folder = '/home/cyc/sites/www.helloc.site/blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('sudo systemctl start helloc')
    sudo('service nginx reload')
