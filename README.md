# Language Translator model
### This is a language translation application developed during the proposal submission round of GSOC 2024 for the  organization City of Boston. The project idea has been taken from the list of ideas of the organization itself. ###
### Working ###
This application uses MarianMTModel which is a family of neural machine translation models trained on the OPUS dataset. This model is designed for translating text between multiple languages. Further model is  accessed through REST APIs developed using Flask.<br><br>

### This model can translate the below language. ### 


<li><a href="" target="_blank"><img src="assets/language translator.gif"width="500" height="500"></a></li>



### Below is the flow diagram of the application. ###

<li><a href="" target="_blank"><img src="assets/flow_chart.png"></a></li>

### To test this model , description of one pothole reporting has been copied from the 311-app ,and passed as the request body of RESTAPIs and below are the response in different languages.

### Request body ###

    curl --location --request GET 'http://127.0.0.1:5000/translation/ar' \
    --header 'Content-Type: text/plain' \
    --data '"close to the mbta station | Where exactly on the pavement is the pothole: [On Roadway] What is the approximate size of the pothole: [2ft] Date when pothole noticed: [03/31/2024] Time when pothole noticed: [10:09]"


### Response in Arabic ###

    "Language - arabic  \"على مقربة من محطة Mbta حيث بالضبط على الرصيف هو حفرة الفتحة: [على الطريق] ما هو الحجم التقريبي للحفرة: [[ft] التاريخ الذي لاحظت فيه الحفرة: [03/31/2024]"
### Response in French ###

    
### Response in Russian ###



