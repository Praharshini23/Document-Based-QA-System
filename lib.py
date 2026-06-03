import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2
import os
from transformers import pipeline

nltk.download("punkt")
