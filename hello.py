def get_number(prompt):
    """사용자로부터 숫자를 입력받고, 유효한 숫자인지 검사하여 반환합니다."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:

            print("오류: 유효한 숫자만 입력해 주세요.")

def get_operator():
    """사용자로부터 유효한 연산자를 입력받아 반환합니다."""
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("수행할 연산을 선택하세요 (+, -, *, /): ")
        if op in valid_operators:
            return op
        else:
            print("오류: 지원하지 않는 연산자입니다. 다시 입력해 주세요.")

def calculate_result(num1, operator, num2):
    """입력받은 숫자와 연산자로 실제 계산을 수행하고 결과를 반환합니다."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:

            print("오류: 0으로 나눌 수 없습니다!")
            return None
        return num1 / num2

    return None

def run_calculator():


    while True:

        num1 = get_number("첫 번째 숫자를 입력하세요: ")


        operator = get_operator()


        num2 = get_number("두 번째 숫자를 입력하세요: ")


        result = calculate_result(num1, operator, num2)

        if result is not None:

            print(f"\n 계산 결과: {num1} {operator} {num2} = {result}\n")


        continue_calc = input("계속 계산하시겠습니까? (Y/N): ").strip().upper()
        
        if continue_calc != 'Y':
            print("계산기를 종료합니다. 이용해 주셔서 감사합니다!")
            break

# 계산기 프로그램 시작
if __name__ == "__main__":
    run_calculator()
