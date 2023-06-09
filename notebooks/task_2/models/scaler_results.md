## Random Forest Regression

```
MSE:  0.3415060152178885
R2:  0.7366485041956597
{'max_depth': 25, 'n_estimators': 200}
->ohne Scaler
```
```
MSE:  0.35709841978096335
R2:  0.7193981094281223
{'max_depth': 20, 'n_estimators': 200}
->MinMax
```
```
MSE:  0.357762175879315
R2:  0.717488958426777
{'max_depth': 25, 'n_estimators': 200}
->Standard
```
```
MSE:  0.3372681959325651
R2:  0.7298443058051178
{'max_depth': 20, 'n_estimators': 200}
->Robust
```
```
MSE:  0.34514472704662297
R2:  0.716287649665585
-> Poly Features (3 Minuten)
```
```
MSE:  0.34565108185658344
R2:  0.7272876940493196
-> Poly Features MinMax (3 Minuten)
```

---

## KNN:

```
MSE:  1.2464098055790362
R2:  -0.029882830719510478
{'n_neighbors': 13}
-> ohne Scaler
```
```
MSE:  0.5958068047337279
R2:  0.5343633465598645
{'n_neighbors': 13}
-> MinMax
```

```
MSE:  1.0402754920634922
R2:  0.1691220939345931
{'n_neighbors': 15}
-> Standard
```
```
MSE:  0.9655073789846516
R2:  0.2527045293432342
{'n_neighbors': 11}
-> Robust
```
---
## ANN:

```
MSE:  1.2462236282315282
R2:  -0.0011535453292645936
{'activation': 'logistic', 'alpha': 0.001, 'hidden_layer_sizes': (100, 100, 100), 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'solver': 'adam'}
-> ohne scaling
```
```
MSE:  0.5938111433862567
R2:  0.5264538651048809
{'activation': 'logistic', 'alpha': 0.001, 'hidden_layer_sizes': (100, 100, 100), 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'solver': 'adam'}
-> MinMax
```

---
## Linear Regression:

```
MSE:  0.5589966117844319
R2:  0.5484320861062658
{'copy_X': True, 'fit_intercept': False}
-> ohne scaling
```
```
MSE:  0.5586754117369863
R2:  0.5478887874799423
{'copy_X': True, 'fit_intercept': False}
-> MinMax
```
```
MSE:  0.5555778104781455
R2:  0.5564765906560103
{'copy_X': True, 'fit_intercept': False}
-> Standard
```
---
## Gradient Boosting Regression:

```
MSE:  0.3507348790261811
R2:  0.7174755601050784
{'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 400}
-> ohne scaling (3 Min)
```
```
MSE:  0.36897346792489594
R2:  0.696033195149695
{'learning_rate': 0.05, 'max_depth': 5, 'n_estimators': 500}
-> MinMax (3 Min)
```

---

## SVM Regression:
```
MSE:  615.3567419525039759
R2:  -405.1517312735693753
-> ohne scaling (nach 32 Minuten abgebrochen)
-> ohne scaling ohne gridseach und linear (4 Minuten)
```
```
MSE:  0.5250335674199759
R2:  0.5693751517312733
{'C': 100, 'gamma': 0.1, 'kernel': 'poly'}
-> MinMax (12 Sekunden)
```
---

# Results
Scaling is useful and necessary for following models: 
- KNN
- ANN
- SVM

Scaling is not useful or improves results significantly for following models:
- Random Forest
- Gradient Boosting
- Linear Regression


### Results without scaling vs with best scaling method:
| Model | MSE | R² |
| ----------- | ----------- | ----------- |
| Random Forest | -1.46% | +1.1% |
| Gradient Boosting | +4.8% | -2.9% |
| Linear Regression | -0.5% | +1.5% |
| KNN* | -∞ | +∞ |
| ANN* | -∞ | +∞ |
| SVM* | -∞ | +∞ |


*all had Error > 1 and R² < 0

\
The different scaling methods have no significant impact on the results for most models. 


But for KNN, MinMaxScaler outperformed the other scalers.

### MSE:
```
MinMaxScaler:   0%
StandardScaler: +74.5%
RobustScaler:   +62,1%
```
### R²:
```
MinMaxScaler:   0%
StandardScaler: -68.4%
RobustScaler:   -52.6%
```
**MinMaxScaler** is reliable and fast, so it is the best choice for scaling.

SVM's without scaling the data are not usable, because the training takes too long.

Polinomial feature transformation did not improve the results.
Deviation to best result:\
`+1.16% MSE (Random Forest)`\
`-1.24% R2 (Random Forest)`