import re

def get_command_args(regex, match):
    substr = re.sub(regex, r"\1", match.string.replace('*', ''))

    return substr.strip().split(' ')
