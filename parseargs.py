import argparse
import sys

import pytest


class ParseArgs:

    def __init__(self, component):
        self.component = component

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

        parser.add_argument('--path_to_data', action='store', type=str, required=True)
        parser.add_argument('--text_column_name', action='store', type=str, required=True)
        parser.add_argument('--label_column_name', action='store', type=str, required=True)

        parser.add_argument('--vocab_size', action='store', type=int, default=10000)
        parser.add_argument('--batch_size', action='store', type=int, default=512)
        parser.add_argument('--epoch', action='store', type=int, default=150)
        parser.add_argument('--verbose', action='store', type=int, default=1)
        parser.add_argument('--callbacks', action='store', type=list, default=None)
        parser.add_argument('--validation_split', action='store', type=int, default=None)
        parser.add_argument('--class_weight', action='store', type=dict)
        parser.add_argument('--sample_weight', action='store')
        parser.add_argument('--initial_epoch', action='store', type=int, default=None)
        parser.add_argument('--steps_per_epoch', action='store', type=int, default=None)
        parser.add_argument('--validation_steps', action='store', type=int, default=None)

        parser.add_argument('--save_word_embeddings', action='store', default=False, type=bool)
        parser.add_argument('--save_model', action='store', default=False, type=bool)

        args = parser.parse_args(sys.argv[2:])

        hyperparameters = {"vocab_size": args.vocab_size, "batch_size": args.batch_size,
                           "epoch": args.epoch, "verbose": args.verbose}

        self.component.build(args.path_to_data, args.text_column_name, args.label_column_name, hyperparameters,
                             args.save_word_embeddings, args.save_model)

        print(f"Building neural net, epoch={hyperparameters['epoch']}, batch_size={hyperparameters['batch_size']}")

    def predict(self):
        parser = argparse.ArgumentParser(
            description='Predicts the sentiment of the sentence')

        parser.add_argument('--sentence', action='store', type=str, required=True)
        parser.add_argument('--path_to_model', action='store', type=str, required=True)

        parser.add_argument('--path_to_data', action='store', type=str, required=True)
        parser.add_argument('--text_column_name', action='store', type=str, required=True)
        parser.add_argument('--vocab_size', action='store', type=int, default=10000)


        args = parser.parse_args(sys.argv[2:])

        self.component.predict(args.sentence, args.path_to_model, args.path_to_data, args.text_column_name, args.vocab_size)
        print(f'Predicting sentiment')


@pytest.fixture(scope='function')
def sys_args():
    sys.argv = ['parseargs.py']  # used to because sys.argv ordering different using pytest
    return sys.argv


@pytest.fixture(scope='function')
def model():
    from model import Model
    return Model()


def test_help_message_correct(capsys, sys_args, model):
    sys_args.append('-h')
    with pytest.raises(SystemExit):
        ParseArgs(model)
    out, err = capsys.readouterr()
    assert "Runs the neural net." in out


def test_unknown_command(capsys, sys_args, model):
    sys_args.append('whatever')
    with pytest.raises(SystemExit):
        ParseArgs(model)
    out, err = capsys.readouterr()
    assert "Unrecognized command" in out


def test_build_message_correct(capsys, sys_args, model):
    sys_args.append('build')
    mandatory_sys_args(sys_args)

    ParseArgs(model)
    out, err = capsys.readouterr()
    assert "Building neural net" in out


def mandatory_sys_args(sys_args):
    sys_args.append('--path_to_data')
    sys_args.append("/data/DataTurks/dump.csv")
    sys_args.append('--text_column_name')
    sys_args.append("content")
    sys_args.append('--label_column_name')
    sys_args.append("label")
    sys_args.append('--epoch')
    sys_args.append('1')


def test_predict(capsys, sys_args):
    sys_args.append('predict')
    ParseArgs(model)
    out, err = capsys.readouterr()
    assert "Predicting sentiment" in out


def test_two_arguments(capsys, sys_args, model):
    sys_args.append('build')
    mandatory_sys_args(sys_args)
    sys_args.append('--batch_size')
    sys_args.append('100')
    ParseArgs(model)
    out, err = capsys.readouterr()
    assert "batch_size=100" in out
    assert "epoch=1" in out

# TODO write parameterized test in pytest
