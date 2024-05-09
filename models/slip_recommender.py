# models/slip_recommender.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from typing import List, Dict

class SlipRecommender:
    def __init__(self, max_words: int, max_len: int):
        self.max_words = max_words
        self.max_len = max_len
        self.tokenizer = Tokenizer(num_words=max_words)
        self.model = self.build_model()

    def build_model(self):
        input_layer = tf.keras.layers.Input(shape=(self.max_len,))
        embedding_layer = tf.keras.layers.Embedding(self.max_words, 128)(input_layer)
        lstm_layer = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64))(embedding_layer)
        dense_layer = tf.keras.layers.Dense(64, activation="relu")(lstm_layer)
        output_layer = tf.keras.layers.Dense(1, activation="sigmoid")(dense_layer)

        model = tf.keras.Model(inputs=input_layer, outputs=output_layer)

        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

        return model

    def train(self, X: List[str], y: List[int], epochs: int, batch_size: int) -> None:
        self.tokenizer.fit_on_texts(X)
        sequences = self.tokenizer.texts_to_sequences(X)
        data = pad_sequences(sequences, maxlen=self.max_len)

        self.model.fit(data, np.array(y), epochs=epochs, batch_size=batch_size)

    def recommend(self, X: List[str], top_n: int) -> List[Dict]:
        sequences = self.tokenizer.texts_to_sequences(X)
        data = pad_sequences(sequences, maxlen=self.max_len)

        scores = self.model.predict(data).flatten()
        sorted_indices = np.argsort(scores)[::-1]

        recommended_slips = []
        for i in sorted_indices[:top_n]:
            slip_id = i + 1
            recommended_slips.append(self.get_slip(slip_id))

        return recommended_slips

    def get_slip(self, slip_id: int) -> Dict:
        # Implement this method to fetch the SLIP data from a database or other data source.
        pass
