Logistic Regression
F1 Score: 0.5142478462557986
              precision    recall  f1-score   support

          no       0.93      0.97      0.95     36548
         yes       0.67      0.42      0.51      4640

    accuracy                           0.91     41188
   macro avg       0.80      0.70      0.73     41188
weighted avg       0.90      0.91      0.90     41188

Decision Tree
[[10571   397]
 [  676   713]]
              precision    recall  f1-score   support

           0       0.94      0.96      0.95     10968
           1       0.64      0.51      0.57      1389

    accuracy                           0.91     12357
   macro avg       0.79      0.74      0.76     12357
weighted avg       0.91      0.91      0.91     12357

random forest
              precision    recall  f1-score   support

          no       0.93      0.97      0.95      7289
         yes       0.68      0.48      0.56       949

    accuracy                           0.91      8238
   macro avg       0.81      0.72      0.76      8238
weighted avg       0.91      0.91      0.91      8238


random forest 2
Best Params: {'max_depth': 19, 'max_features': 'log2', 'min_samples_leaf': 1, 'n_estimators': 157}
              precision    recall  f1-score   support

           0       0.96      0.93      0.95      7303
           1       0.57      0.72      0.64       935

    accuracy                           0.91      8238
   macro avg       0.77      0.83      0.79      8238
weighted avg       0.92      0.91      0.91      8238

principle component analysis
              age  avg_duration  avg_campaign  avg_emp_var_rate  \
cluster                                                            
0        41.459948    304.700258      1.801034         -2.108269   
1        39.685106    259.285372      2.089096         -1.595160   
2        40.140953    258.974201      2.921408          1.291440   

         avg_cons_conf  avg_euribor3m  avg_nr_employed     %_yes          job  \
cluster                                                                         
0           -38.088372       1.002044      5032.541602  0.607235       admin.   
1           -42.981809       1.852965      5104.980691  0.160106       admin.   
2           -39.035862       4.919255      5215.590894  0.049718  blue-collar   

                 education  marital housing loan  
cluster                                           
0        university.degree  married     yes   no  
1        university.degree  married     yes   no  
2        university.degree  married     yes   no 