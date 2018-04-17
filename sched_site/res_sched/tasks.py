from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from .sched_lib.src.sched_api import ModelSolver

import datetime
import os

logger = get_task_logger(__name__)


@shared_task(name="beep")
def solveit(uid, filename):
    filepath = os.path.join(settings.BASE_DIR,
                            "res_sched/sched_lib/src/residents.py")
    f = os.path.join(settings.BASE_DIR, "users/%s/data/%s" % (uid, filename))
    logger.info(f)
    ms = ModelSolver(filepath)
    ms.load_data(f)
    ms.solve()
    results = ms.post_process()
    now = datetime.datetime.now()
    stamp = "%4d-%02d-%02d-%02d-%02d-%02d" % (now.year, now.month, now.day,
                                             now.hour, now.minute, now.second)
    bname = os.path.basename(f).split(".")[0]
    sched_file = "users/%s/schedules/%s-%s" % (uid, bname, stamp)
    tmp_name = sched_file + ".json"
    cnt = 1
    while os.path.isfile(tmp_name):
        tmp_name = sched_file + ("(%d)" % cnt) + ".json"
        cnt += 1

    with open(tmp_name, "w") as f:
        f.write(results)

    return tmp_name