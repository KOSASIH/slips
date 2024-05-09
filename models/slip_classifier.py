# models/slip_classifier.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from typing import List, Dict

class SlipClassifier:
    def __init__(self, max_words: int, max_len: int):
        self.max_words = max_words
        self.max_len = max_len
        self.tokenizer = Tokenizer(num_words=max_words)
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.max_words, 128, input_length=self.max_len),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid")
        ])

        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

        return model

    def train(self, X: List[str], y: List[int], epochs: int, batch_size: int) -> None:
        self.tokenizer.fit_on_texts(X)
        sequences = self.tokenizer.texts_to_sequences(X)
        data = pad_sequences(sequences, maxlen=self.max_len)

        self.model.fit(data, np.array(y), epochs=epochs, batch_size=batch_size)

    def predict(self, X: List[str]) -> List[float]:
        sequences = self.tokenizer.texts_to_sequences(X)
        data = pad_sequences(sequences, maxlen=self.max_len)

        return self.model.predict(data).flatten().tolist()
