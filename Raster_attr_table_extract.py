import os
import pandas as pd
import json
import subprocess
def rasterAttr(dataset_uri):
    #dataset_uri = os.path.join(ecr_folder, raster_name)
    _rat = subprocess.check_output('gdalinfo -json ' + dataset_uri, shell=True)
    data = json.loads(_rat)

    rat = data['rat']['row']
    pval = [i['f'][0] for i in rat]
    aval = [i['f'][2] for i in rat]

    r_table = pd.DataFrame({
        'PixelValue':pval,
        'PixelAttri':aval
    })

    return r_table
