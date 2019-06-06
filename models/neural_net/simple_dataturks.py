import os

import pandas as pd
from keras.preprocessing.text import Tokenizer
from tensorflow import keras
from keras.models import load_model

class Model:

    def create_dictionary(self, data, n_words):
        """Prepares the corpus for the model and returns the Tokenizer object.
        Args:
            data (pandas series) : The column of text to be classified.
            n_words (int) : This argument will keep the most frequent n_words in the training data.

        Returns:
            tokenizer (Tokenizer) :
        """
        tokenizer = Tokenizer(num_words=n_words)
        tokenizer.fit_on_texts(data)
        return tokenizer

    def predict(self, sentence, path_to_model, path_to_data, text_column_name, vocab_size):
        """Returns a sentiment score.

        Args:
            sentence (str) : The sentence to be analised.
            path_to_model (str) : The path to the model from the current directory.
            path_to_data (str) : The path to the dataset from the current directory.
            text_column_name (str) : The name of the column of the dataset with the text to be classified
            vocab_size (int) : The size of dictionary of the most frequent n_words in the corpus.

        Returns:
            score (float) : The sentiment score of the sentence. 1 - cyber abusive, 0 - not cyber abusive.
        """

        model = load_model(path_to_model)

        data = pd.read_csv(os.getcwd() + path_to_data)

        corpus_vocabulary = self.create_dictionary(data[text_column_name], vocab_size)

        parsed_test = pd.DataFrame({"content": pd.Series(sentence)})
        X_test = parsed_test['content']

        test_sequences = corpus_vocabulary.texts_to_sequences(X_test.values)

        padded_test = keras.preprocessing.sequence.pad_sequences(test_sequences, padding='post', maxlen=140)

        sentiment_score = round(model.predict(padded_test).item(0))

        print(f"This sentence has a sentiment score of: {sentiment_score}")

        return sentiment_score
