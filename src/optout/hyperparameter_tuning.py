from hyperopt import Trials, STATUS_OK, tpe, rand
from hyperas import optim
from hyperas.distributions import choice
import keras
import numpy as np
import pandas as pd
import os
from .model import Model as m

def create_model(train_data):
    """Returns the sentiment of the parsed sentence.

    Args:
        train_data (df) : The data the model is to be built from.
        save_word_embeddings (bool) : If true, will save the embedding data.
        save_model (bool) : If true, will save the model.

    Returns
        model : The sentiment analyser model, fit to the training data.
    """
    global corpus_vocabulary

    X_train = train_data['content']
    y_train = train_data['label']

    vocab_size = 10000  # TODO automatic

    train_sequences = corpus_vocabulary.texts_to_sequences(X_train.values)
    padded_train = keras.preprocessing.sequence.pad_sequences(train_sequences, padding='post',
                                                              maxlen=140)
    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 40))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense({{choice([np.power(2, 5), np.power(2, 6), np.power(2, 7)])}}, input_shape=(140,)))
    model.add(keras.layers.Dense({{choice([np.power(2, 5), np.power(2, 6), np.power(2, 7)])}}, input_shape=(140,)))

    model.summary()

    split = int(len(X_train) / 4)  # number of comments halved

    x_val = padded_train[:split]
    partial_x_train = padded_train[split:]

    y_val = y_train[:split]
    partial_y_train = y_train[split:]

    from keras import callbacks

    reduce_lr = callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                                            patience=5, min_lr=0.001)

    model.compile(optimizer={{choice(['rmsprop', 'adam', 'sgd'])}},
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(X_train,
              y_train,
              epochs={{choice([25, 50, 75, 100])}},
              batch_size={{choice([16, 32, 64])}},
              validation_data=(x_val, y_val),
              callbacks=[reduce_lr])

    score, acc = model.evaluate(x_val, y_val, verbose=0)
    print('Test accuracy:', acc)
    return {'loss': -acc, 'status': STATUS_OK, 'model': model}
    return model


if __name__ == '__main__':
    data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
    corpus_vocabulary = m.create_dictionary(data['content'], 10000)

    train, test = m.split(data, 18000)

    best_run, best_model = optim.minimize(model=create_model,
                                          data=train,
                                          algo=tpe.suggest,
                                          max_evals=15,
                                          trials=Trials())

    print("Evalutation of best performing model:")
    print(best_model.evaluate(test['content'], test['label']))
    print("Best performing model chosen hyper-parameters:")
    print(best_run)
