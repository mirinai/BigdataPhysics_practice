#에라토스테네스의 체를 쓰기
def getting_prime_num(n):
    primes = []
    isPrimes = [False, False]  # 0과 1은 소수가 아님

    for _ in range(2, n + 1):
        isPrimes.append(True)

    for i in range(2, int(n**0.5) + 1):
        if isPrimes[i]:
            for j in range(i * i, n + 1, i):
                isPrimes[j] = False

    for i in range(2, n + 1):
        if isPrimes[i]:
            primes.append(i)
    return primes

def output_spacebar(lst):
    print("prime number:", end=" ")
    for i in lst:
        print("%d" % i, end=" ")

n = int(input("숫자입력: "))
result = getting_prime_num(n)
output_spacebar(result)
