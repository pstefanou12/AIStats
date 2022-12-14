"""
Default parameters for running algorithms in delphi.ai.
"""

from typing import Iterable

from AIStats.helpers import has_attr


# CONSTANTS
REQ = 'required'


TRAINER_DEFAULTS = { 
    'epochs': (int, 20),
    'trials': (int, 3),
    'tol': (float, 1e-3),
    'early_stopping': (bool, False), 
    'n_iter_no_change': (int, 5),
    'verbose': (bool, False),
    'disable_no_grad': (bool, False), 
    'epoch_step': (bool, False)
}

DATASET_DEFAULTS = {
        'workers': (int, 1), 
        'batch_size': (int, 100), 
        'val': (float, .2), 
        'normalize': (bool, False),
}

DEFAULTS = { 
    #'alpha': (float, REQ), 
    'lr': (float, 1e-1), 
    'step_lr': (int, 100),
    'step_lr_gamma': (float, .9), 
    'custom_lr_multiplier': (str, None), 
    'momentum': (float, 0.0), 
    'weight_decay': (float, 0.0), 
    'device': (str, 'cpu')
}


def check_and_fill_args(args, defaults): 
        '''
        Checks args (algorithm hyperparameters) and makes sure that all required parameters are 
        given.
        '''
        # assign all of the default arguments and check that all necessary arguments are provided
        for arg_name, (arg_type, arg_default) in defaults.items():
            if has_attr(args, arg_name):
                # check to make sure that hyperparameter inputs are the same type
                if isinstance(arg_type, Iterable):
                    if args.__getattr__(arg_name) in arg_type: continue 
                    raise ValueError('arg: {} is not correct type: {}. fix hyperparameters and run again.'.format(arg_name, arg_type))
                if isinstance(args.__getattr__(arg_name), arg_type): continue
                raise ValueError('arg: {} is not correct type: {}. fix hyperparameters and run again.'.format(arg_name, arg_type))
            if arg_default == REQ: raise ValueError(f"{arg_name} required")
            elif arg_default is not None: 
                # use default arugment
                setattr(args, arg_name, arg_default)
        
        return args

