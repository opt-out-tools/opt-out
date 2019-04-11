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

# MEASURE SCORE
# df = pd.DataFrame(predicted_sentiment_score, columns = {'score'})
# df.loc[df['score'] >= 0.5, 'label'] = 1
# df.loc[df['score'] < 0.5, 'label'] = 0
# hits_array = np.array(y_test) == np.array(df['label'].values)
# float(np.sum(hits_array)) / len(y_test)
#

# JSON PLAY
#  tweets = []
#    ...: for line in open('Cyber-Trolls.json', 'r'):
#    ...:     tweets.append(json.loads(line))
#    ...:
#    ...: with open('data.json', 'w') as outfile:
#    ...:     json.dump(tweets, outfile)
#
# with open('data.json', encoding='utf-8') as data_file:
#    ...:     data = json.loads(data_file.read())
# test = pd.DataFrame(data)   test.to_csv('dump.csv)