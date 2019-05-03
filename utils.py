import argparse
import json
import os
import sys

import numpy as np
import pandas as pd
import pytest

current_directory = os.getcwd()


def save_embeddings(model, word_index):
    """Writes two files to the current working directory containing the word embeddings and labels.

    Args:
        model (Sequential) : A sequential Keras model.
        word_index (dict) : The word to enumeration mapping.
    Returns:
         embeddings.tsv : The word embeddings for the model.
         metadata.tsv : The labels for the word embeddings.
    """

    embeddings = model.layers[0].get_weights()[0]
    np.savetxt(current_directory + "/saved_model_data/embeddings/embedding.tsv", embeddings, delimiter="\t")

    labels = np.array([key for key in word_index.keys()])
    np.savetxt(current_directory + "/saved_model_data/embeddings/metadata.tsv", labels, delimiter="\t", fmt="%s")


def is_correctly_labelled(scores, target_labels):
    """Returns the percentage of the test data that was correctly labelled.

    Args:
        scores (np.ndarray) : The predicted scores from the sentiment analyser.
        target_labels (np.ndarray) : The desired labelling from the sentiment analysers.

    Returns:
        float : The percentage of correctly labelled comments.
    """
    df = pd.DataFrame(scores, columns={'score'})

    df.loc[df['score'] >= 0.5, 'label'] = 1
    df.loc[df['score'] < 0.5, 'label'] = 0

    hits_array = np.array(target_labels) == np.array(df['label'].values)

    return round(float(np.sum(hits_array)) / len(target_labels) * 100, 2)


def test_is_cyber_bullying():
    score = np.array([0.6], dtype=float)
    target = np.array([1.0], dtype=float)
    assert is_correctly_labelled(score, target) == 100


def test_is_not_cyber_bullying():
    score = np.array([0.49], dtype=float)
    target = np.array([0.0], dtype=float)
    assert is_correctly_labelled(score, target) == 100


def test_boundary_test():
    score = np.array([0.5], dtype=float)
    target = np.array([1.0], dtype=float)
    assert is_correctly_labelled(score, target) == 100


def convert_json_to_csv(read_filename, write_filename):
    """Converts a list of jsons which are not in correct list format, into the correct format and writes them to csv."""
    tweets = []
    for line in open(read_filename, 'r'):
        tweets.append(json.loads(line))

    with open('tmp.json', 'w') as outfile:
        json.dump(tweets, outfile)

    with open('tmp.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    tmp = pd.DataFrame(data)
    tmp.to_csv(write_filename)


class ParseArgs:

    def __init__(self):
        parser = argparse.ArgumentParser(description='Runs the neural net.', usage='python model.py <command> [<args>]')
        parser.add_argument("command", help="Subcommand of run.")
        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def build(self):
        parser = argparse.ArgumentParser(
            description='Trains and builds the neural net')

        parser.add_argument('--batch_size', action='store', type=int)
        parser.add_argument('--epoch', action='store', type=int)
        parser.add_argument('--verbose', action='store', type=int)
        parser.add_argument('--callbacks', action='store', type=int)
        parser.add_argument('--validation_split', action='store', type=int)
        parser.add_argument('--validation_data', action='store', type=int)
        parser.add_argument('--class_weight', action='store', type=int)
        parser.add_argument('--sample_weight', action='store', type=int)
        parser.add_argument('--initial_epoch', action='store', type=int)
        parser.add_argument('--steps_per_epoch', action='store', type=int)
        parser.add_argument('--validation_steps', action='store', type=int)

        args = parser.parse_args(sys.argv[2:])
        epoch = args.epoch
        print(f'Building neural net, epoch={epoch}')

    def predict(self):
        parser = argparse.ArgumentParser(
            description='Predicts the sentiment of the sentence')

        print(f'Predicting sentiment, score=')


def test_parseargs_help_message_correct(capsys):
    sys.argv.pop()  # used to because sys.argv ordering different using pytest
    sys.argv.append('-h')
    with pytest.raises(SystemExit):
        ParseArgs()
    out, err = capsys.readouterr()
    assert "Runs the neural net." in out


def test_parseargs_unknown_command(capsys):
    sys.argv.pop()  # used to because sys.argv ordering different using pytest
    sys.argv.append('whatever')
    with pytest.raises(SystemExit):
        ParseArgs()
    out, err = capsys.readouterr()
    assert "Unrecognized command" in out


def test_parseargs_build_message_correct(capsys):
    sys.argv.pop()
    sys.argv.append('build')
    ParseArgs()
    out, err = capsys.readouterr()
    assert "Building neural net" in out

def test_parseargs_epoch(capsys):
    sys.argv.pop()
    sys.argv.append('build')
    sys.argv.append('--epoch')
    sys.argv.append('1')
    ParseArgs()
    out, err = capsys.readouterr()
    assert "epoch=1" in out



# if __name__ == '__main__':
#     ParseArgs()
