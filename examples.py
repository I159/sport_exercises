import collections
import math
import string


def find_uniq(arr):
    """Find a unique number."""
    count = collections.Counter(arr)
    n = [k for (k, v) in count.items() if v == 1][0]
    return n  # n: unique integer in the array


def mormons(s, r, t, m=0):
    """The Mormons are trying to find new followers and in order to do that they embark on missions.
    Each time they go on a mission, every Mormons converts a fixed number of people (reach) into followers.
    This continues and every freshly converted Mormon as well as every original Mormon go on another mission and convert the same fixed number of people each. The process continues until they reach a predefined target number of followers (target).
    Converted Mormons are unique so that there's no duplication amongst them.
    Complete the function that calculates how many missions Mormons need to embark on, in order to reach their
    target. While each correct solution will pass, for more fun try to make a recursive function.
    All inputs are valid positive integers.
    """
    return mormons(s + s * r, r, t, m + 1) if s < t else m


def combinations(n):
    lst = str(n)
    ln = len(lst)

    for i in range(ln):
        tmp = lst[:i] + lst[i + 1 :]
        for j in range(ln):
            print(tmp[:j] + lst[i] + tmp[j:])
            yield [int(tmp[:j] + lst[i] + tmp[j:]), i, j]


def smallest(n):
    """You have a positive number n consisting of digits. You can do at most one operation:
      Choosing the index of a digit in the number, remove this digit at that index and insert
      it back to another or at the same place in the number in order to find the smallest number you can get.
    Task:
    Return an array or a tuple or a string depending on the language (see "Sample Tests") with
    the smallest number you got
    the index i of the digit d you took, i as small as possible
    the index j (as small as possible) where you insert this digit d to have the smallest number.
    Examples:
    smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
    126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0
    smallest(209917) --> [29917, 0, 1] or ...
    [29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than
    index `i` in [29917, 0, 1].
    29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave
    029917 which is the number 29917.
    smallest(1000000) --> [1, 0, 6] or ..."""
    return min(combinations(n))


def sieve(n):
    S = range(n)
    S[1] = False
    for k in range(2, int(math.sqrt(n))):
        if S[k]:
            for l in xrange(k**2, n, k):
                S[l] = False
        k += 1
    return filter(lambda x: x is not False, S)


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_emirp(n):
    """If you reverse the word "emirp" you will have the word "prime". That idea is
        related with the purpose of this kata: we should select all the primes that when reversed
        are a different prime (so palindromic primes should be discarded).
    For example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also
    primes, so 13 and 17 are "emirps". But primes 757, 787, 797 are palindromic primes, meaning that
    the reversed number is the same as the original, so they are not considered as "emirps" and should be discarded.
    The emirps sequence is registered in OEIS as A006567
    Your task
    Create a function that receives one argument n, as an upper limit, and the return the following array:
    [number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n]
    """
    revs = (int(str(i)[::-1]) for i in sieve(n) if str(i) != str(i)[::-1])
    empirps = [i for i in revs if is_prime(i)]
    empirps += [int(str(i)[::-1]) for i in empirps]
    empirps = filter(lambda x: x <= n, set(empirps))
    if empirps:
        return [len(empirps), max(empirps), sum(empirps)]
    return [0, 0, 0]


abc = string.ascii_lowercase


def encrypt(offset):
    def get_letter(letter):
        if letter.lower() in abc:
            encripted = abc[(abc.index(letter.lower()) + offset) % 26]
            letter = encripted.upper() if letter.isupper() else encripted
        return letter

    return get_letter


def encryptor(key, message):
    """Caesar Ciphers are one of the most basic forms of encryption. It consists of a
        message and a key, and it shifts the letters of the message for the value of the key.
    Read more about it here: https://en.wikipedia.org/wiki/Caesar_cipher
    Your task
    Your task is to create a function encryptor that takes 2 arguments - key and message - and
    returns the encrypted message.
    Make sure to only shift letters, and be sure to keep the cases of the letters the same. All
    punctuation, numbers, spaces, and so on should remain the same.
    Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!"""
    return "".join(map(encrypt(key), message))
