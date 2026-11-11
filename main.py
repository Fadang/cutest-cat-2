"""Cutest cat entry (2nd shot): copy the bundled cat picture to /output/entry.png.

Deterministic: the same bytes are written on every run. No network,
no randomness, standard library only.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

os.makedirs("/output", exist_ok=True)
shutil.copyfile(os.path.join(HERE, "cat.png"), "/output/entry.png")
