from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .sched_lib.src.sched_api import ModelSolver


@shared_task(name="beep")
def solveit(f):
    _ms = ModelSolver(os.path.join(BASE_DIR, '\\sched_site\\sched_site\\'
                                   'sched_lib\\src\\ojModel.py'))
    _ms.load_data(f)
    _ms.solve()
    _ms._instance.display()
