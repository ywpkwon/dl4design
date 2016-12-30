# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import zipfile

import numpy as np
import tensorflow as tf

# Step 1: Download the data.

def zip_string(mystring, dest_file):
  with zipfile.ZipFile(dest_file, 'w') as zf:
    zf.writestr('000.txt', mystring)
    zf.close()

# Read the data into a list of strings.
def read_data(filename):
  """Extract the first file enclosed in a zip file as a list of words"""
  with zipfile.ZipFile(filename) as f:
    data = tf.compat.as_str(f.read(f.namelist()[0])).split()
  return data

# Prepare input file (string -> zip)
mystring = "I went to the school where MR. White teaches."
dest_file = 'tester.zip'
zip_string(mystring, dest_file)

# Read (zip -> words)
words = read_data(dest_file)
print('Data size', len(words))
print(words)

