
def balanceParethesis(string):
    if len(string) == 0:
        return

    count = 0
    partialResult = ""
    
    for ch in string:
        if ch == "(":
            count += 1
            partialResult += ch
        elif ch == ")":
            if count <= 0:
                continue
            count -= 1
            partialResult += ch
        else:
            partialResult += ch

    reversedPartialResult = partialResult[::-1]
    # print(partialResult)

    count = 0
    finalResult = ""
    for ch in reversedPartialResult:
        if ch == "(":
            if count <= 0:
                continue
            count -= 1
            finalResult += ch
        elif ch == ")":
            count += 1
            finalResult += ch
        else:
            finalResult += ch

    reversedFinalResult = finalResult[::-1]
    return reversedFinalResult


if __name__ == "__main__":
    print(balanceParethesis("a(b)c)("))
    print(balanceParethesis("a(a(a)b)b"))
    print(balanceParethesis("()"))
    print(balanceParethesis(")("))
    print(balanceParethesis("(((((("))
    print(balanceParethesis(")))))"))
    print(balanceParethesis("))))))))))(((((("))
    print(balanceParethesis("(()()("))
    print(balanceParethesis(")(())("))
    print(balanceParethesis(")())(()()("))
    print(balanceParethesis("(())())"))
    print(balanceParethesis("(ab)"))
    print(balanceParethesis("a(b)c)"))
    print(balanceParethesis("a(b(c)))"))
