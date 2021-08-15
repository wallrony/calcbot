import re
from errbot import BotPlugin, re_botcmd

from lib import utils, calculator_helper

CALCULE_SUM = r"^sum (.+)$"
CALCULE_SUB = r"^sub (.+)$"
CALCULE_MULT = r"^mult (.+)$"
CALCULE_DIV = r"^div (.+)$"
SHOW_SUM_RESULT_LIST = r"^show sum results$"
SHOW_SUB_RESULT_LIST = r"^show sub results$"
SHOW_MULT_RESULT_LIST = r"^show mult results$"
SHOW_DIV_RESULT_LIST = r"^show div results$"

class CalcBot(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    def __init__(self):
        super.__init__(self)
        print("Hello, i'm the CalcBot.\n")
        print("I have some rules like: don't give me numbers that the result is repeated.\n\n")
        print("So, if you give me 3 and 2 and 2 and 3 after, i won't say to you the result because it's repeated and i hate to answer repeated results...\n\n")
        print("Other thing is to don't give zero value in logic results. You know that 0 x 5 is ZERO, so, don't pretent to not know.")

    @re_botcmd(pattern=CALCULE_SUM, flags=re.IGNORECASE, prefixed=False, re_cmd_name_help="Calculate the sum of two numbers", name="calc_sum")
    def calcule_sum(self, message, match):
        args = utils.get_command_args(CALCULE_SUM, match)

        if len(args) < 2 or len(args) > 2:
            yield 'I work only with 2 numbers. No more or less than that!'
            return

        yield from self.get_calculator_helper().sum(args[0], args[1])
        return
    
    @re_botcmd(pattern=CALCULE_SUB, flags=re.IGNORECASE, prefixed=False, re_cmd_name_help="Calculate the subtraction of two numbers", name="calc_sub")
    def calcule_sub(self, message, match):
        args = utils.get_command_args(CALCULE_SUB, match)

        if len(args) < 2 or len(args) > 2:
            yield 'I work only with 2 numbers. No more or less than that!'
            return

        yield from self.get_calculator_helper().sub(args[0], args[1])
        return
    
    @re_botcmd(pattern=CALCULE_MULT, flags=re.IGNORECASE, prefixed=False, re_cmd_name_help="Calculate the multiplication of two numbers", name="calc_mult")
    def calcule_mult(self, message, match):
        args = utils.get_command_args(CALCULE_MULT, match)

        if len(args) < 2 or len(args) > 2:
            yield 'I work only with 2 numbers. No more or less than that!'
            return

        yield from self.get_calculator_helper().mult(args[0], args[1])
        return
    
    @re_botcmd(pattern=CALCULE_DIV, flags=re.IGNORECASE, prefixed=False, re_cmd_name_help="Calculate the division of two numbers", name="calc_div")
    def calcule_div(self, message, match):
        args = utils.get_command_args(CALCULE_DIV, match)

        if len(args) < 2 or len(args) > 2:
            yield 'I work only with 2 numbers. No more or less than that!'
            return

        yield from self.get_calculator_helper().div(args[0], args[1])
        return
    
    @re_botcmd(pattern=SHOW_SUM_RESULT_LIST, flags=re.IGNORECASE, prefixed=False)
    def show_sum_result_list(self, message, match):
        yield from self.get_calculator_helper().show_results('sum')
        return
    
    @re_botcmd(pattern=SHOW_SUB_RESULT_LIST, flags=re.IGNORECASE, prefixed=False)
    def show_sub_result_list(self, message, match):
        yield from self.get_calculator_helper().show_results('sub')
        return
    
    @re_botcmd(pattern=SHOW_MULT_RESULT_LIST, flags=re.IGNORECASE, prefixed=False)
    def show_mult_result_list(self, message, match):
        yield from self.get_calculator_helper().show_results('mult')
        return
    
    @re_botcmd(pattern=SHOW_DIV_RESULT_LIST, flags=re.IGNORECASE, prefixed=False)
    def show_div_result_list(self, message, match):
        yield from self.get_calculator_helper().show_results('div')
        return

    def get_calculator_helper(self):
        return calculator_helper.CalculatorHelper(self)
