import Dataset
import ModelPool
from Tasks import TaskData
import MLPipeline as mlp

# Initialize ML pipeline
pipeline = mlp.Pipeline()

# Define models that are to be included in the ML Pipeline
@pipeline.Model("catboostv1","This model will be trained using CatBoost classifier " +
        " with 5-Fold CV. Predictions will be evaluated based on AUC metric.")
def CatBoost_v1():
    return ModelPool.CatBoost_v1("catboostv1")

@pipeline.Model("lightbgmv1","This model will be trained using LightGBM classifier " +
        " with 5-Fold CV. Predictions will be evaluated based on AUC metric.")
def LisghtGBM_v1():
    return ModelPool.LightGBM_v1("lightbgmv1")


# Define datasets that are to be included in the ML Pipeline
@pipeline.Dataset("allDatav2","This dataset has been generated from Application dataset" +
        " downloaded from Kaggle HomeCredit competition.")
def AllData_v2():
    return TaskData(Dataset.Load("AllData_v2"), "allDatav2")

@pipeline.Dataset("allDatav3","This dataset has been generated from Application dataset" +
        " downloaded from Kaggle HomeCredit competition.")
def AllData_v3():
    return TaskData(Dataset.Load("AllData_v3"), "allDatav3")

@pipeline.Dataset("applicationburo","This dataset has been generated from ApplicationBuro dataset" +
        " downloaded from Kaggle HomeCredit competition.")
def ApplicationBuro():
    return TaskData(Dataset.Load("ApplicationBuro"), "applicationburo")

@pipeline.Dataset("applicationonly","This dataset has been generated from ApplicationOnly dataset" +
        " downloaded from Kaggle HomeCredit competition.")
def ApplicationOnly():
    return TaskData(Dataset.Load("ApplicationOnly"), "applicationonly")