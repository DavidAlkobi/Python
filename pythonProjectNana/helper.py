def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == 'hours':
        return f"{num_of_days} days are {num_of_days * 24} hours"
    if conversion_unit == 'minutes':
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    if conversion_unit == 'seconds':
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return 'unsupported unit'


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary['days'])
        conversion_unit = days_and_unit_dictionary['unit']
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, conversion_unit)
            print(calculated_value)
        else:
            print('you entered zero or a negative number, please try again later because you are stupid..')
    except ValueError:
        print('you piece of shit')


user_input_message = "Hey there, please enter number of days and conversion unit!\n"
