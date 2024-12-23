
import pandas as pd
import numpy as np
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import confusion_matrix, classification_report,roc_auc_score
from sklearn.model_selection import train_test_split,cross_val_score,KFold
data = pd.read_csv('Final_data.csv',encoding= 'unicode_escape')
x_train,x_test,y_train,y_test = train_test_split(data.drop('Target', axis = 1).values,data['Target'].values,test_size = 0.25,random_state = 100)
rf_tune = RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=10, max_features='sqrt',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=2, min_samples_split=10,
                       min_weight_fraction_leaf=0.0, n_estimators=100,
                       n_jobs=None, oob_score=True, random_state=None,
                       verbose=0, warm_start=False)
model = rf_tune.fit(x_train, y_train)
y_pred = model.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))
print(roc_auc_score(y_test,y_pred))
[[16695  3635]
 [10277 14521]]
              precision    recall  f1-score   support

           0       0.62      0.82      0.71     20330
           1       0.80      0.59      0.68     24798

    accuracy                           0.69     45128
   macro avg       0.71      0.70      0.69     45128
weighted avg       0.72      0.69      0.69     45128

0.7033858069016642
rf_tune.feature_importances_
array([0.01616426, 0.01498899, 0.90362862, 0.01465726, 0.01747873,
       0.03308215])
xgb = XGBClassifier(base_score=0.5, booster=None, colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=0.8, gamma=0.1, gpu_id=-1,
              importance_type='gain', interaction_constraints=None,
              learning_rate=0.1, max_delta_step=0, max_depth=5,
              min_child_weight=1, monotone_constraints=None,
              n_estimators=140, n_jobs=4, nthread=4, num_parallel_tree=1,
              objective='binary:logistic', random_state=27, reg_alpha=0,
              reg_lambda=1, scale_pos_weight=1, seed=27, subsample=0.8,
              tree_method=None, validate_parameters=False, verbosity=None)
model = xgb.fit(x_train,y_train)
y_pred = model.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)
print(classification_report(y_test,y_pred))
print(roc_auc_score(y_test,y_pred))
[[17474  2856]
 [10866 13932]]
              precision    recall  f1-score   support

           0       0.62      0.86      0.72     20330
           1       0.83      0.56      0.67     24798

    accuracy                           0.70     45128
   macro avg       0.72      0.71      0.69     45128
weighted avg       0.73      0.70      0.69     45128

0.7106687276678098
xgb.feature_importances_
array([0.02989238, 0.02548258, 0.82316405, 0.02658245, 0.03221522,
       0.06266331], dtype=float32)
