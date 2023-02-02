# pylint: disable=missing-module-docstring
from crontab import CronTab

#init cron
cron   = CronTab()

#add new cron job
job  = cron.new(command='python ${file_path}/morning_message.py')

#job settings
job.hour.every(24)
cron.write()

# uncomment below to write this cron to your user only (UNIX only)
#cron.write_to_user( user=True )
