from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements


class Iris(BaseModel):
    sepal_length: float
    petal_length: float
    sepal_width: float
    petal_width: float
