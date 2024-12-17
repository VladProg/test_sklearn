import os

best = """
CalibratedClassifierCV
LogisticRegressionCV
PassiveAggressiveClassifier
Perceptron
RidgeClassifier
RidgeClassifierCV
SGDClassifier
ComplementNB
GaussianNB
MLPClassifier
LinearSVC
""".split()

for file in os.listdir():
    if file.startswith('stats'):
        open(file.replace('stats', 'best'), 'w').writelines(
            line for i, line in enumerate(open(file))
            if not i or any(item in line for item in best)
        )
