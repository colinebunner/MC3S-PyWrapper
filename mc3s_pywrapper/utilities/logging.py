import datetime

def multidimensional_error(var_name, probability=False):
    
    '''
        I write a ridiculously verbose message to the logs when a multidimensional input
        is mis-specified. The reason multidimensional inputs are harder to handle here is
        I explicitly track each variable in the array for precise logging. For example,
        the changeLog will tell you if only the second entry of an array of values is
        changed. This message explains how to properly set these variables.

        Input:
            var_name [str]: Name of variable
            probability [bool]: Is this number required to be less than 1.0?

        Output:
            message [str]: The error message slightly adjusted for specific use case.
    '''

    message = (
        f"To properly set {var_name} you have a few options. You can always pass it as a "
        f" python list (e.g. mySim.$module.{var_name} = [1.0, 1.0])."
        " This will automatically convert to the special oneDimArray used by the code."
        " You can also set it as a oneDimArray object yourself, but this is far more "
        " tedious and you need to be careful that the errorLog, changeLog, location, "
        " and variable flags are set properly, which involves passing the right "
        " reference. Note that single values can be passed as a float/int, but they "
    )

    if probability:
        message += (
            " must be probabilities (number less than 1.0, can be negative for "
            "numerical reasons)."
        )
    else:
        message += " must be real, positive numbers."

    return message

def changelog_entry(location, variable, success, previous, new, errorMessage=None):

    '''
        This is what every "changeLog" entry needs to look like. It's important to
        keep the same structure so that someone 20 years later can easily search
        your logs.

        Input:
            location [str]: module location (e.g. Sim.simple)
            variable [str]: variable name (e.g. pmtra)
            success [bool]: Was the variable successfully changed?
            previous [str]: repr of previous value
            new [str]: repr of (attempted) new value
            errorMessage[Union[str, None]]: If success is False, what errorMessage 
                was generated?
    '''

    return {
        'Date': datetime.datetime.now(), 'Location': location, 'Variable': variable,
        'Success': success, 'Previous': previous, 'New': new,
        'ErrorMessage': errorMessage
    }

def errorlog_entry(errorType, errorMessage=None):

    '''
        This is what every "errorLog" entry needs to look like. It's important to
        keep the same structure so that someone 20 years later can easily search
        your logs.

        Input:
            errorType [str]: What type of error is this (i.e. a "Setter" or "slurm" error)
            errorMessage[Union[str, None]]: If success is False, what errorMessage 
                was generated?
    '''

    return {
        'Date': datetime.datetime.now(), 'Type': errorType, 'ErrorMessage': errorMessage
    }