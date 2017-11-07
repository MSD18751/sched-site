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
                                   'res_sched\\sched_lib\\src' +
                                   '\\ojModel.py')
    logger.info(filepath)
    _ms = ModelSolver(filepath)
    _ms.load_data(f)
    _ms.solve()
    return _ms._vars
