import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

"""Чтение данных из датафрейма"""
frame = pd.read_csv('titanic.csv', header=0, sep=',')
"""Оставляем в выборке четыре класса"""
x_labels = ['Pclass', 'Fare', 'Age', 'Sex']
X = frame.loc[:, x_labels] # Пробегает по всей таблице и оставляет только x_labels
"""Обратите внимание, что признак Sex имеет строковые значения"""
X['Sex'] = X['Sex'].map(lambda sex: 1 if sex == 'male' else 0)
"""Выделите целевую переменную - она записана в признаке Survived"""
y = frame['Survived']
"""Удалите объекты с пропущенными признаками (NaN)"""
X = X.dropna()
y = y[X.index.values]
"""Обучите решающее дерево с параметром random_state=241"""
clf = DecisionTreeClassifier(random_state=241)
clf.fit(np.array(X.values), np.array(y.values))
"""Вычислите важности признаков и найдите два признака с наибольшей важностью"""
importances = pd.Series(clf.feature_importances_, index=x_labels)
print(importances)