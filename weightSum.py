def weight_sum():
    print("The sum of alpha and beta must be 1.0.")
    alphaValue = float(input('input alpha weight value: '))
    betaValue = float(input('input bata weight value: '))
    if alphaValue + betaValue != 1:
        return weight_sum()
    elif alphaValue + betaValue == 1:
        return alphaValue, betaValue