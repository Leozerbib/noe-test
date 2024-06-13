import os
import til

import pandas as pd

HOME = os.path.dirname(os.path.abspath(__file__))
DATALAKE_ROOT_FOLDER = HOME + "/datalake/"


def convert_raw_to_formatted(file_name, source,entity):
   path = til.getPath(True,source,entity) 
   newPath = til.getPath(False,source,entity)
   if not os.path.exists(newPath):
       os.makedirs(newPath)
   df = pd.read_json(path + file_name)
   parquet_file_name = file_name.replace(".json", ".snappy.parquet")
   final_df = pd.DataFrame(data=df)
   final_df.to_parquet(newPath + parquet_file_name)


   

