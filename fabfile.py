from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO =  'https://github.com/IPandaaaaa/django-blog.git'

env.user = 'panda'
env.password = 'ls6836211'

env.hosts = ['47.101.128.154',]

env.port = '22'

def deploy():
    source_folder = '/home/panda/sites/blank/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd{}&&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-panda')
    sudo('service nginx reload')