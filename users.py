import os
import pwd
import subprocess
from time import sleep

# Create ncbackup if it does not exists.
username = ['ncbackup1','ncadmin1']
password = 'The0Pass'
import subprocess
from time import sleep

PASSWD_CMD='/usr/bin/passwd'

def set_password(user, password):
    cmd = [PASSWD_CMD, user]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    p.stdin.write(u'%(p)s\n%(p)s\n' % { 'p': password })
    p.stdin.flush()
    # Give `passwd` cmd 1 second to finish and kill it otherwise.
    for x in range(0, 10):
        if p.poll() is not None:
            break
        sleep(0.1)
    else:
        p.terminate()
        sleep(1)
        p.kill()
        raise RuntimeError('Setting password failed. '
                '`passwd` process did not terminate.')
    if p.returncode != 0:
        raise RuntimeError('`passwd` failed: %d' % p.returncode)

for user in username:
    print '************************************'
    print '* Creating ' + user + ' user...'
    print '************************************'
    try:
        pwd.getpwnam(user)
        print 'The user already exists; no need to create it'
    except KeyError:
        os.system('useradd -m %s -s /sbin/nologin' % user)
        if user == 'ncadmin':
             set_password(user, password)
        print 'Done.'


