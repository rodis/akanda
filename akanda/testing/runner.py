import argparse
import unittest

from akanda.testing import result, testcase, util


JUST_UNIT = 1
JUST_FUNC = 2
BOTH_TYPES = 3


def filter_test_case(test_case, condition, suite):
    is_unit = isinstance(test_case, testcase.UnitTestCase)
    is_func = isinstance(test_case, testcase.FunctionalTestCase)
    is_both = isinstance(test_case, testcase.BaseTestCase)
    unexpected = (isinstance(test_case, unittest.TestCase) and not is_both)
    if unexpected:
        suite.addTest(test_case)
        return False
    elif condition == JUST_FUNC and is_func:
        suite.addTest(test_case)
        return True
    elif condition == JUST_UNIT and is_unit:
        suite.addTest(test_case)
        return True
    elif condition == BOTH_TYPES and is_both:
        suite.addTest(test_case)
        return True
    else:
        return True


def filter_suites(suite_of_suites, condition):
    filtered_suite = unittest.TestSuite()
    # XXX there's *got* to be a better way to do this ...
    for suites in suite_of_suites:
        if not filter_test_case(suites, condition, filtered_suite):
            continue
        for suite in suites:
            if not filter_test_case(suite, condition, filtered_suite):
                continue
            for test_case in suite._tests:
                if not filter_test_case(test_case, condition, filtered_suite):
                    continue
    return filtered_suite


def get_all_tests(condition):
    loader = unittest.TestLoader()
    suites = loader.discover(util.get_top_directory())
    return filter_suites(suites, condition)


def get_specified_tests(names):
    loader = unittest.TestLoader()
    return loader.loadTestsFromNames(names)


def get_suite(args):
    # check for the argparse data to see which ones to filter
    if args.with_functional:
        condition = BOTH_TYPES
    elif args.unit_only:
        condition = JUST_UNIT
    elif args.functional_only:
        condition = JUST_FUNC
    if args.tests:
        return get_specified_tests(args.tests)
    return get_all_tests(condition)


def run_tests(args):
    runner = unittest.TextTestRunner(
        verbosity=2, resultclass=result.CustomTestResult)
    runner.run(get_suite(args))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Akanda Test Runner")
    parser.add_argument(
        "-u", "--unit-only", action="store_true", default=True,
        help="Run only the unit tests (default)")
    parser.add_argument(
        "-f", "--functional-only", action="store_true", default=False,
        help="Run only the functional tests")
    parser.add_argument(
        "-b", "--with-functional", action="store_true", default=False,
        help="Run both unit and functional tests")
    parser.add_argument(
        "tests", metavar="MOD", type=str, nargs="*",
        help="One or more dotted Python namespaces to test")
    args = parser.parse_args()
    if args.functional_only or args.with_functional:
        args.unit_only = False
    run_tests(args)
