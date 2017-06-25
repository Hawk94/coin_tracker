from django.core.files.storage import default_storage

import json


def model_to_json(models):
    final_json = {}

    for model in models:
        qs = model.objects.all()
        to_json = {}
        if model.__name__ == 'Rate':
            for instance in qs:
                to_json.update({instance.date.strftime('%Y-%m-%d'): {'usd_rate': 1, 'gbp_rate': float(instance.gbp_rate), 'eur_rate': float(instance.eur_rate)}})
            
        else:
            for instance in qs:
                to_json.update({instance.date.strftime('%Y-%m-%d'): float(instance.price)})

        final_json.update({model.__name__: to_json})

    json_file = json.dumps(final_json)
    return json_file


def save_to_s3(file_name, body):
    new_file = default_storage.open(file_name, 'w')
    new_file.write(body)
    new_file.close()
    return default_storage.exists(file_name)