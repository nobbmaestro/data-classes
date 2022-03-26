def convert_case(input_string: str, case) -> str:
    """Converts the case of the input string.

    Args:
        input_string (str): input of format example "Hello, World."

        case (_type_): 
            camel: camelCase
            snake: snake_case
            kebab: kebab-case
            pascal: PascalCase
            uppercasesnake: UPPERCASE_SNAKE

    Raises:
        TypeError: Args not a string
        ValueError: Improper case setting

    Returns:
        str: coverted string with case setting
    """
    converted_string = ""
    spr = [',', ' ']

    if type(input_string) is not str or type(case) is not str:
        raise TypeError('Args are not of type str')

    elif case.lower() not in ['camel', 'snake', 'kebab', 'pascal', 'uppercasesnake']:
        raise ValueError('Improper case setting')

    else:
        for i in range(len(input_string)):
            if case.lower() == 'camel':
                if input_string[i] not in spr and input_string[i] != ".":
                    if input_string[i-1] not in spr:
                        converted_string += input_string[i].lower()
                    else:
                        converted_string += input_string[i].upper()

            elif case.lower() == 'snake':
                if input_string[i] not in spr and input_string[i] != ".":
                    converted_string += input_string[i].lower()

                elif input_string[i] in spr and converted_string[len(converted_string)-1] != "_":
                    converted_string += '_'

            elif case.lower() == 'kebab':
                if input_string[i] not in spr and input_string[i] != ".":
                    converted_string += input_string[i].lower()

                elif input_string[i] in spr and converted_string[len(converted_string)-1] != "-":
                    converted_string += '-'

            elif case.lower() == 'pascal':
                if input_string[i] not in spr and input_string[i] != ".":
                    if input_string[i-1] not in spr and i != 0:
                        converted_string += input_string[i].lower()
                    else:
                        converted_string += input_string[i].upper()

            elif case.lower() == 'uppercasesnake':
                if input_string[i] not in spr and input_string[i] != ".":
                    converted_string += input_string[i].upper()

                elif input_string[i] in spr and converted_string[len(converted_string)-1] != "_":
                    converted_string += '_'

        return converted_string