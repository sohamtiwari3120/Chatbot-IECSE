import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
# import tflearn
import tensorflow as tf
import json
import random
import keras
import sklearn

stemmer = LancasterStemmer()

with open("intents.json") as file:
    data = json.load(file)

print(data)