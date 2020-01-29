import sys
from behave import __main__ as runnerfile

if __name__ == '__main__':
    sys.stdout.flush()
    report_generation = "-f allure_behave.formatter:AllureFormatter -o allure/results "
    command_line_args = ' --no-capture'
    runnerfile.main(report_generation + command_line_args)