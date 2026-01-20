from pydantic import BaseModel

class HouseFeatures(BaseModel):
    bedrooms: int
    bathrooms:int
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: int
    view: int
    condition: int
    sqft_above: int
    sqft_basement: int
    age_of_house: int
    has_been_renovated: int
