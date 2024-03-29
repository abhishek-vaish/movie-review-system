# 🎬Movie Review System
Movie Review System is based on the Natural Processing Language or NLP Model
that takes the review from the user and predict the review as a `positive` or `negative`.
Model is train using the TensorFlow and TensorFlow API called Keras. This application predict 
the output with the accuracy level i.e. how much confident the model is on that particular prediction.

## What you get at the end?

If you successfully complete all the steps than you get an application which looks something like this.

![screenshot.png](/image/screenshot.JPG)
![screenshot-1.jpg](/image/screenshot-1.JPG)

## Let's get started 🤝
Okay!! I'm in. What I need to get this application running on my own browser?

`You need to follow these 5 simple steps to get this application.`

### Step1: Clone this repository in your own system
```
$ git clone https://www.github.com/abhishekv5055/movie-review-system.git
```

### Step2: Install the pipenv enviornment
Lets install the virtual environment so that we cannot mess up with the configuration of our own system.

> Note: Before moving forward make sure you must have a python==3.5+ installed in your system.

```
$ pip install pipenv
```

### Step3: Lets install the required modules
```
$ cd app \
  && pipenv install
```
This will download all the modules that are required for this application in the virtual enviornment.

### Step4: Activate the Enviornment
```
$ cd app \ 
  && pipenv shell
```
This will activate the environment. Now you can access all your modules that you had downloaded in the above step.

### Step5: Run the application
```
$ cd app \
  && streamlit run app.py
```
This will open up the new tab of your default browser and launch the application on the localhost:8501.

Congratulations!!! 🎉 You have successfully run your Machine Learning Application in the easy 5 Steps. Now you can deploy it in any free cloud service provider like, Heroku, Netlify, etc.

## Wanna Deploy! ☁
So far we have launch the application on the local system. Now, making the one step forward, we deploy the application on the `Heroku` Platform using the containerize serive called Docker. **But before that you must have a docker and heroku cli installed on your system.**

> You can download the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).

So, we are making the `Movie Review System` live. Are you ready?

### Step1: Login to Heroku.
```
$ heroku login
```
Enter your heroku credentials to login into the Heroku.

### Step2: Login to Heroku Container.
```
$ heroku container login
```

### Step3: Create Heroku App.
```
$ heroku create -a <APP-NAME>
```
This will create an application to your heroku account.

### Step4: Build the `docker-compose.yml` file.
```
$ heroku container:push web -a <APP-NAME>
```
This will build your dockerfile and install all the required requirement.

### Step5: Release your application
```
$ heroku container:release web -a <APP-NAME>
```

### Step6: Open your application
```
$ heroku open
```

Congratulations!!! 🎉 You have successfully deploy your application on Heroku in just 6 easy steps. Share your application on social network and do tag me on [LinkedIn](https://www.linkedin.com/in/abhishek-vaish)



## Developer
You can connect with me on my [LinkedIn](https://www.linkedin.com/in/abhishek-vaish) or on my [Twitter](https://www.twitter.com/abhishek_vaish_). ❤

