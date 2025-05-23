from critical_hit import *

run_cases = [
    (2, 5, 30),
    (3, 15, 120),
    (4, 30, 300),
    (0, 1, 0),
]

submit_cases = run_cases + [
    (1, 0, 0),
    (5, 50, 600),
    (7, 105, 1680),
    (10, 225, 4950),
    (15, 525, 16800),
    (20, 950, 39900),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Num attacks: {input1} Base damage: {input2}")
    print(f"Expecting: {expected_output} damage")
    result = calculate_flurry_crit(input1, input2)
    print(f"Actual: {result} damage")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
