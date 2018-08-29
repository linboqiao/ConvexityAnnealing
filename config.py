"""
Date: August 28, 2018
Author: Eric Cotner, UCLA Dept. of Physics and Astronomy

Base configuration class which contains all the useful information important to the configuration of the experiment.
"""

class Config(object):
    """
    Configuration class; contains all relevant information to the experiment configuration.
    """
    # Name of the experiment and seed
    NAME = "Baseline"
    SEED = 0

    # Specify hyperparameters
    MAX_EPOCHS = 1
    VAL_SPLIT = 0.05        # Fraction of training set to use for validation
    BATCH_SIZE = 32
    USE_PARALLELISM = False # Whether to use parallel threads (set to False for 100% reproducibility)

    # Shape of input
    INPUT_SHAPE = [28, 28, 1]     # MNIST input shape - 28x28 greyscale images

    # Shape of output
    OUTPUT_SHAPE = 10                   # 10 MNIST classes
    OUTPUT_ACTIVATION = "softmax"

    # Specify optimizer, loss to optimize, and metrics to track
    OPTIMIZER = "adam"
    LOSS = "categorical_crossentropy"
    METRICS = ["accuracy"]


    # Specification of hidden layer architecture
    ARCHITECTURE = [("conv2d", {"filters":16, "kernel_size":(4,4), "strides":1, "padding":"valid", "activation":"relu"}),
                    ("conv2d", {"filters":16, "kernel_size":(3,3), "strides":1, "padding":"valid", "activation":"relu"}),
                    ("conv2d", {"filters":16, "kernel_size":(3,3), "strides":1, "padding":"valid", "activation":"relu"})]