import pandas as pd
import json

output_fp = r"C:\Users\RAKESH\.PyCharmCE2019.1\config\scratches\New folder\output.csv"
source_json_fp = r'E:\Downloads\New folder\index.json'

new_data = list()

try:
    links_list = list()

    with open(source_json_fp) as f:
        reporting_dict = json.load(f)
        for item in reporting_dict['reporting_structure']:
            for plan_obj in item['reporting_plans']:
                allowed_amount_file = item.get('allowed_amount_file', None)
                if not allowed_amount_file:
                    allowed_amount_file = item.get('in_network_files')[0]
                new_data.append({**plan_obj, **allowed_amount_file})
    if new_data:
        df = pd.DataFrame(new_data)
        col_name_list = ['plan_id', 'plan_id_type', 'plan_market_type', 'plan_name', 'description', 'location']
        df.to_csv(output_fp, columns=col_name_list, index=False)
        links_list = list(set(df['location'].to_list()))
    else:
        print('something went wrong')

except Exception as e:
    print(f'Exceaption: {e}')

if links_list:
    for link in links_list:
        print(link)

import os
os.makedirs('asd', exist_ok=)