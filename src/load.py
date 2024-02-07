import dvc.api
import json
from pathlib import Path

def load(params):
    data = {'seed': params['data']['seed']}
    return data

if __name__ == '__main__':
    Path('data/load.dir').mkdir(parents=True, exist_ok=True)
    params = dvc.api.params_show(stages=['load'])
    loaded_data = load(params)

    with open('data/load.dir/data.json', 'w') as f:
        json.dump(loaded_data, f)



