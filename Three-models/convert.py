import os
import shutil
from zipfile import ZipFile

# Код который конвертирует все .csv файлы с решением, лежащие в папке 'submissions',
# в требуемый .zip формат в папке 'send'

for filename in os.listdir('./submissions'):
    if filename.startswith('submission') and filename.endswith('.csv'):
        name = filename.split('.')[0]
        path = os.path.join('./send', name)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(f'./send/{name}')
        shutil.copy(os.path.join('./submissions', filename), os.path.join(path, filename))
        os.rename(os.path.join('./send', name, filename), os.path.join(path, '01.out'))
        with ZipFile(os.path.join(path, 'output.zip'), 'w') as mz:
            mz.write(os.path.join(path, '01.out'), '01.out')
        os.remove(os.path.join(path, '01.out'))
