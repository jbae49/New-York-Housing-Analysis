# What Affects the most NYC Housing Prices: The number of Starbucks, Whole Foods, Expensive Restaurants, Movie Theaters, or Equinox?

This project aims to analyze the impact of nearby amenities on property prices in New York, using data from a dataset of New York housing. The analysis leverages the Google Maps API to explore how the proximity of Starbucks, Whole Foods, movie theaters, Equinox, and high-rated expensive($$$) / very expensive($$$$) restaurants influences the price per square foot of properties.

## Methodology

The analysis is done by 1000 entries from the dataset to limit the cost of calling Google Map API. Key features included latitude, longitude, price, and property square footage. The `price_per_sqft` was computed for each property alongside its geographical location tuple.

I created a custom Python class, `NearByStoreSearch`, to utilize the Google Maps API for identifying nearby amenities specified by keywords (Starbucks, Whole Foods, movie theaters, Equinox) within a 500-meter radius. This functionality was extended to count good restaurants, defined by a rating above 4 and a price level of 3 or above, suggesting their desirability and potential impact on property values.

## Insights

### Nearby Amenities
The analysis revealed significant variations in the number of high-quality restaurants and popular amenities like Starbucks, Whole Foods, movie theaters, and Equinox near the properties. These amenities were hypothesized to influence the `price_per_sqft` of properties, serving as indicators of a desirable neighborhood.

### Machine Learning Model
A Random Forest Regressor was employed to predict the `price_per_sqft` based on the proximity of amenities and the presence of high-rated restaurants. The model identified Starbucks and the number of good restaurants as significant predictors of property prices, highlighting the value buyers place on nearby dining options and global coffeehouse chains.

### Feature Importance
The model's feature importance analysis underscored the significance of Starbucks, followed by the number of restaurants with a price level of 3, movie theaters, Equinox, restaurants with a price level of 4, and Whole Foods. This ranking reflects the premium that property buyers are willing to pay for convenience and lifestyle amenities.
![feature_importance](/feature_importance.jpeg)

## Conclusion

The findings underscore the considerable impact of nearby amenities on property prices in New York. Specifically, the presence of Starbucks and high-quality restaurants within walking distance significantly boosts the value of properties, demonstrating the importance of location and neighborhood characteristics in real estate valuation. Future research could explore the effects of other amenities and broader geographical areas to further understand the dynamics of urban property prices.
