import os
import re
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import plotly.graph_objs as go
import plotly.colors as colors
import streamlit as st
from sklearn.linear_model import LogisticRegression
import joblib
import nltk
import subprocess
from sklearn.preprocessing import LabelEncoder
from wordcloud import WordCloud
from tensorflow import keras
from keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras import layers
from keras.models import Model
from keras.layers import SimpleRNN, LSTM, Bidirectional, GRU
from keras.layers import Input, MultiHeadAttention, Attention, AdditiveAttention
from keras.layers import Embedding, Dense, Dropout, BatchNormalization
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox,Chrome,Edge,Safari
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import torch