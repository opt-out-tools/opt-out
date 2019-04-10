import numpy as np
import os


def save_embeddings(model, word_index):
    """ Writes two files to the current working directory containing the word embeddings and labels.

    Args:
        model (Sequential) : A sequential keras model.
        word_index (dict) : The word to enumeration mapping.
    Returns:
         embeddings.tsv : The word embeddings for the model.
         metadata.tsv : The labels for the word embeddings.
    """

    current_directory = os.getcwd()
    embeddings = model.layers[0].get_weights()[0]
    np.savetxt(current_directory + "/embeddings/embedding.tsv", embeddings, delimiter="\t")

    labels = np.array([key for key in word_index.keys()])
    np.savetxt(current_directory + "/embeddings/metadata.tsv", labels, delimiter="\t", fmt="%s")


