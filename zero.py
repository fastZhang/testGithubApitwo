import datetime
import os

# from heavy import special_commit


def modify():
    file = open('zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()
 

def commit():
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')


def set_sys_time(year, month, day):
    os.system('date -s %04d%02d%02d' % (year, month, day))


def trick_commit(year, month, day):
    # set_sys_time(year, month, day)
    os.system('curl -u \'fastZhang\' https://api.github.com/user/repos -d \'{\"name\":\"testGithubApithree\"}\'')
    # modify()
    os.system('git init')
    # os.system('git add .')
    # os.system('git commit -a -m test_github_streak > /dev/null 2>&1')
    # os.system('git remote add origin git@github.com:fastZhang/starttest.git')
    os.system('git push -u origin master')


    






def daily_commit(start_date, end_date):
    # for i in range((end_date - start_date).days + 1):
        # cur_date = start_date + datetime.timedelta(days=i)
    trick_commit(start_date.year, start_date.month, start_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2015, 1, 31), datetime.date(2016, 1, 28))
