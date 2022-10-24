import random as rand
import string

def create_state_key(size):
    return ''.join(rand.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))