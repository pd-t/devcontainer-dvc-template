import dvc.api
import 

def prepare(dataset: Dataset, **kwargs):
    splitted_dataset = train_test_split(
        dataset, 
        **params['data']
    )
    metrics = get_metrics(splitted_dataset, **params['data'])
    return splitted_dataset, metrics

if __name__ == '__main__':
    Path('data/prepare.dir').mkdir(parents=True, exist_ok=True)
    
    params = dvc.api.params_show(stages=['prepare'])

    loaded_dataset = load_from_disk("data/load.dir/dataset")
    prepared_dataset, prepared_metrics = prepare(loaded_dataset, **params['data'])
    prepared_dataset.save_to_disk("data/prepare.dir/dataset")

    write_json("data/" + params['data']['logging_file'], prepared_metrics)