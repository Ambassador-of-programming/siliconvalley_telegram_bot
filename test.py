# процентный рандом, значит что с вероятностью % выведет значение

import random
if random.randint(0,100) < 20:
    print("bad")
else: print("good")