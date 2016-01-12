from unipath import Path
import os
BASE_DIR = Path(os.path.abspath(__file__)).ancestor(3)
print(BASE_DIR)
