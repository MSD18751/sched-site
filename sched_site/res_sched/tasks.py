from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from .sched_lib.src.sched_api import ModelSolver
import os

logger = get_task_logger(__name__)


@shared_task(name="beep")
def solveit(f):
    filepath = os.path.join(settings.BASE_DIR,
                            "res_sched/sched_lib/src/residents.py")
    _ms = ModelSolver(filepath)
    _ms.load_data(f)
    _ms.solve()

    results = {}
    results["vars"] = str(_ms._vars)
    results["params"] = str(_ms._params)
    results["sets"] = str(_ms._sets)
    results["objectives"] = str(_ms._objectives)
    results["constraints"] = str(_ms._constraints)
    return results

    #return str(_ms._vars) + str(_ms._params) + str(_ms._sets) + str(_ms._objectives) + str(_ms._constraints)