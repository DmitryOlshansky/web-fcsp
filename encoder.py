from celery import Celery
from celery.utils.log import get_task_logger
import subprocess

logger = get_task_logger(__name__)
app = Celery('tasks', broker='amqp://guest@localhost//', backend='rpc://')

def encode(mol):
	proc = subprocess.Popen("fcss-2a".split(),
    	stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	return proc.communicate(mol)[0]

@app.task(name='tasks.encode_mols', serializer='json')
def encode_mols(mols):
	total = sum(map(lambda x: len(x), mols))
	logger.info("Encoding %s MOL files, total size = %s"%  (len(mols), total))
	result = map(encode, mols)
	return result
