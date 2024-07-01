from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))
    
    multiplied_int = my_int1 * my_int2
    
    return [Output(multiplied_int, "multiplied_output", party1)]

