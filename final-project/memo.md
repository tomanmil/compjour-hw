*Quick pitch*

We will find out the inspection grades, history and other information about Santa Clara Restaurants, as many people have no idea where to start to find this.

*The old way*

1) Think of the name of a restaurant 
2) Enter that information and see if a search pops up and returns information or even figuring out which exact restaurant you’re searching for. 
3) Click on a link to get more details. You may need to click on a link to get a google map or to view the inspection history. Or we may need to consult Yelp separately.

*The new way*

People will use this project to find the latest scores the restaurant received. We could potentially limit searches and have a drop down list of cities. We could add in the average Yelp rating and Yelp reviews. We propose having the user choose from a drop down list of cities, scores and average number of stars from Yelp. Users could choose any or all of those options. The project could also delve into inspection history by including an option that says 'no past inspection problems.'  This would be more of a one-stop shopping for both inspection and reviews.

*Where does the data come from? How is it collected?*

The data comes from Santa Clara County and from Yelp (using the API).

*What data-cleaning/processing needs to be done?*

The data-cleaning will involve sorting, parsing HTML from the SCC website and parsing HTML from the inspection history. We will also add information from the Yelp API.

*How will the data be stored?*

We will store the data locally as a csv file.

*Who else has done it and how is your attempt better?*

Santa Clara is making this data available. There is a SafeEats app that does something similar to what we are trying to do, but it's only applicable to New York City.

*Pre-mortem:*

The big task (and most difficult part of the project) is parsing search results from Santa Clara. I have to collect inspection
histories and lists of violations. Some lists of violations are in html. Others are in pdf format. Another difficulty is in integrating all parts of our display, crafting a good application view that may include an area map, lists of violations, and information about the restaurant and past inspections all in an aesthetically pleasing way.
