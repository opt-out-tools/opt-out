import copy

import numpy as np


def random_labelling(y_test):
    """Returns the proportion of samples that would be labelled correctly if totally random.

    Args:
        Series : The labels for the test data.

    Returns:
        float : The proportion that would correctly labelled if the process were totally random.

    """
    y_test.index = range(0, len(y_test))
    test_labels_copy = copy.copy(y_test)
    np.random.shuffle(test_labels_copy)
    hits_array = np.array(y_test) == np.array(test_labels_copy)
    return float(np.sum(hits_array)) / len(y_test)
