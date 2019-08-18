# DFGF Recipes - Milestone 3 Project

The purpose of the the project is too create a recipe database that caters to people that have intolerances to dairy or gluten. The database can have information added, edited and deleted by the user allowing the project to have a more diverse range of recipes. The project is also interactive in the sense that a person can upvote a recipe if they used it and enjoyed it, which in turn allows others to see that it is a popular recipe. 

We believe that this project could create a community for people who have an interest in cooking but have certain food intolerances to come together and share information. We have utilised social media by linking our Instagram page and with the hashtag #DFGF (dairy free, gluten free) we hope to be trending soon. 


## UX
 
In essence this project is an interactive recipe book that allows users to filter recipes based on their dietary requirements. It also allows users to add, update or delete recipes on the site. It provides a platform for people to either publish their own recipes or research and try other peoples. 

The project has been designed with a mobile first approach but it is fully responsive across all devices. This has been achieved by using Materialize a UI component library created with HTML, CSS and Javascript. There is various ways to navigate through the site but we we believe that the majority of people will arrive on the home page and navigate through the recipes using the filters and then the recipe cards. Below is a few different examples of users experience when navigating the site;
- User 1 has arrived on the homepage after searching for cooking recipes on google. They then filter the recipes to show only recipes that are dairy free due to their intolerances. They then see a picture of the Spanish lamb shank casserole and click to view the full recipe straight away as lamb is a family favourite. The user is directed to the full description and cooking instructions where they take a screenshot of the page and go to the shop to buy all of the ingredients.
- User 2 has arrived on the full recipe page of the salmon fishcake after being tagged in one of our posts in Instagram by a friend. When they look through the ingredients and cooking instructions they notice that the potatoes have been missed from the list. They then press the edit button, add the missing potatoes and then save the recipe so that other visitors are able to make the fishcakes correctly.
- User 3 is a returning user who has added multiple recipes to the site previously. It emerged in the news the week before that a common ingredient that the user normally used is in fact not dairy free or gluten free as advertised. The user is able to go through the recipes that they have added which uses this ingredients as a base and delete the recipes so others do not have issues moving forward.
- User 4 has tried a few of the recipes on DFGF previously and enjoyed them, so much so they have clicked that they have used the recipes on their unique pages. The user now wants to add their own recipe to the site. When they open the DFGF homepage on their laptop they proceed to click on new recipe in the navigation bar where they are directed to a page with a form where they can add their recipe, image and their name so that they get the credit for uploading their recipe.
- User 5 is scrolling through the homepage recipes and using the card reveal function to quickly glance at the calories per serving of the recipes as they are trying to reduce their calorie intake. They notice that the scrambled  tofu is only 240 calories per serving, the user then proceeds to the full recipe page to get the ingredients and cooking instructions.

## Features

### Existing Features
- filter - allows the user to split the recipes into categories (dairy free/gluten free) and only show the the ones that are suitable for them
- Card reveal - allows user to browse recipes and read a summary of the recipe while on the homepage
- Add recipe - allows user to add their own recipe to the site  by having them complete a form with specific headings to make sure all recipes have the same format
- Edit recipe - allows user to edit an existing recipe on the site if they spot that it has a mistake
- Delete recipe - allows user to delete a recipe on the site, this could be done if a recipe has been uploaded but is not suitable for the site
- Made this button - allows user to express the fact that they have made specific recipe. This is a counter and the number increase everything it is pressed.
- Object ID - allows user to see all information on a recipe by redirecting them to a unique object_ID for each recipe
- Social media - allows user to follow DFGF across multiple platforms

### Features to be implemented
 - login - this would give users a more personalised experience and also increase the security of the site with regards to editing and deleting recipes
 - Additional filters - As the project grows the types of filters would increase as well, for example a filter to display the recipes with the highest amount of votes on the ‘I made this’ button first
 - Instruction videos - this would provide the user with a more interactive experience where they could make the recipe while following the instructional video

## Technologies Used
For this singles page application there was a number of programming languages, frameworks and libraries that were used. These are stated below with an explanation as to why they were used;
- HTML - The markup language is used as the building blocks allowing text to be displayed on the project
- CSS - This is used to style the website making the HTML more appealing to the user
- Javascript - This is used to add interactive functionality to the project such as the card reveal, mobile nav bar and collapsable buttons (https://www.javascript.com)
- Python - This is used as the language provides increased functionality over HTML/CSS. . A vital part of the project is the front end being able to display, read, input, edit and delete information stored on the mongoDB back end database, Python was used to do this (https://www.python.org/)

- Materialize - This framework is used to enable the site to be responsive on all users devices. It also has features that are (https://materializecss.com/)
- jQuery - This was used to manipulate the DOM and reduce the amount of code required compared to using javascript alone, shortening the development time (https://jquery.com/)
- Flask - this framework is used with the Python language to navigate the site by binding the URLs to certain functions. The functions also retrieve and send data to mongoDB using PyMongo (https://flask.palletsprojects.com/en/1.0.x/)
- mongoDB - this non relational database is used to store the data that can be read, edited and deleted by the user (https://www.mongodb.com/)
- PyMongo - this is used as a driver to allow the Python based project to use mongoDB (https://api.mongodb.com/python/current/)
- BSON - this is used as mongoDB stores data in a binary code JSON format (http://bsonspec.org/)

## Testing
### Manual Testing

1. Accessing and navigating the site
    1. Accessing the site on different browsers to make sure that it is accessible. This has been tested on chrome, safari and internet explorer browsers
    2. Scrolling up and down the homepage on both desktop and mobile to make sure that it works on different devices. This has been tested on a MacBook Pro, iPad and Galaxy Samsung S9+
2. Filtering recipes on the homepage
    1. Clicking on the filter button and selecting the different options making sure that the recipe that are showing have been filtered correctly
3. Adding a recipe to the site
    1. Selecting the add recipe option in the navigation bar when on the home screen
    2. Completing the required fields and selecting if the recipe is dairy free or gluten free
    3. Clicking add recipe at the bottom of the page after all the information is correct
    4. Returning to the homepage, finding and selecting the recipe that has just been created, selecting to see the full recipe details and checking that all the information that had been input is showing
4. Editing a recipe
    1. Selecting the view full recipe and instructions link on a recipe already created
    2. Selecting the edit recipe button
    3. Proceeding to change some of the cooking instructions and saving the recipe
    4. Returning to the homepage, finding the recipe that has just been edited and making sure that the changes made have been saved
5. Deleting a recipe
    1. Selecting the view full recipe and instructions link on a recipe already created
    2. Selecting the delete recipe button
    3. Returning to the homepage to confirm that that the recipe has been deleted
6. Voting to say that we made the recipe
    1. Selecting the view full recipe and instructions link on a recipe already created
    2. Pressing the I made this button and ensuring that the number increases by one 
7. Checking social media links
    1. Pressing the Instagram link to ensure that it opens in a new window on the correct profile
8. Overall site navigation
    1. Selecting all links and making sure all pages load correctly and there is not any dead links

### Automated Testing
- All HTML code was tested using the W3C HTML tool validator ( https://validator.w3.org). The validator did not recognise the Django template extender which resulted in it flagging up multiple errors
- All CSS code was tested using the W3C CSS tool validator (https://jigsaw.w3.org/css-validator/). No errors were found

## Issues Faced

While creating the data centric project there were several issues that were encountered that have been explained in detail below
- During the design stage of the project a login function and dedicated page was going to be incorporated. This was attempted and a lot of time was spent trying to create a flask based login system. It seemed to have been successful to the point that it all worked but it would not remember any usernames that were created. For this reason I toke the code out of the project as It was not working properly. When looking for solutions on Slack I found that there would be a section in the next module covering login systems so I have added this into the features to be implemented section.
- Materialize was used as a framework to make the site responsive. This was used as an alternative to Bootstrap, having used Materialize for a smaller project previously I liked the functionality of it. When building the project I noticed that Materialize was quite limited in what it could do. Due to this I tried to use Bootstrap as well but could not get basic things like a responsive nav bar to work. After researching on StackOverflow it was apparent that there was known issues when trying to use the two frameworks together. This resulted in me taking out the Bootstrap code as materialize had been used from the beginning.
- While creating this project the platform CLoud9 that was used to write the code was acquired by Amazon therefore the project had to be migrated over to AWS Cloud. This caused many problems for this project in particular for instance I had to create a new Git repository as I could not access the initial one, I have since found a solution on how to do this on other projects. The requirements.txt file included a lot of packages that I did not download and this was preventing the project being deployed to Heroku, after researching the issue seems that the command being used stated all package in AWS Cloud and not just the local packages that I installed. This was solved with help from the users on Slack.

## Development and Deployment
- The project was developed using Cloud9 and then AWS IDE Cloud as Cloud9 was disabled. 
- Github  was used as a code repository to ensure any changes were saved, https://github.com/zanderm73/milestone-3. The entire project can be cloned form the Github repository and can be then be run locally. For a cloned site to work the same as this project ensure that that the MongoDB database that is created has the same headings and the Mongo_URI is changed to the new database that you create.
- The project has been deployed using Heroku where the config vars have been set to ‘IP - 0.0.0.0’ and ‘PORT - 5000’. Heroku has been linked to GitHub and it has been setup so that Heroku deploys the master branch of the GitHub repository.


## Credits
- This project was designed by Alexander Miller for the purpose of completing Milestone 3 data centric development module. The guidelines of the project were set by Code Institute.

### Content
- At the time of deployment the recipes instructions, ingredients and images were all taken from either Great British Chefs (https://www.greatbritishchefs.com) and Tesco (https://realfood.tesco.com/recipes.html).
- As the project encourages users to add their own recipes and images there will be content sourced user that isn’t referenced

### Acknowledgements
- Stack Overflow, and Slack were useful when problems were encountered during the project development