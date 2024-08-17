from tqdm import tqdm
import time

for i in tqdm(range(50), desc='Processing', ascii=True, ncols=100, unit='item'):
    time.sleep(0.05)

# ==========================================================================================
# from tqdm import tqdm
# from multiprocessing import Pool

# def process_item(x):
#     time.sleep(0.1)  # Simulate some work
#     return x**2

# items = range(100)
# with Pool(4) as p:
#     results = list(tqdm(p.imap(process_item, items), total=len(items)))
# ==========================================================================================
# ==========================================================================================
# ==========================================================================================

import pandas as pd
from tqdm import tqdm
tqdm.pandas()

# Example with DataFrame apply
df = pd.DataFrame({'a': range(100)})
df['b'] = df['a'].progress_apply(lambda x: x**2)

# ==========================================================================================

from tqdm import tqdm
import time

# Example with list comprehension
results = [x**2 for x in tqdm(range(100))]
# Using tqdm with pandas
# ==========================================================================================

# Nested Progress Bars
# tqdm supports nested progress bars for loops within loops:

print("*********************")

from tqdm import tqdm
import time

for i in tqdm(range(5), desc='Outer loop'):
    for j in tqdm(range(100), desc='Inner loop', leave=False):
        time.sleep(0.01)
# ==========================================================================================
