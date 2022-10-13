# Git Fork Me

A simple application to fork this repository into your GitHub account.

## Design decisions

Given the time constraint to hand in this assignment the framework of choice was Django. With more time, a micro framework would have made more sense. Something without all the extra overhead and boilerplate like FastAPI or Flask. However, the second reason to go down the Django route was that Social Auth was necessary to meet the assignments requirements.

An all backend approach was chosen to tackle the call to GitHubs API to fork the repository. A more UI friendly decision would have been to handle the request with AJAX on the front end side and alter the DOM to present the results. Django Templating language was used instead and once the fork button is pressed the user is presented with another view and a message indicating that the repository is being forked and a link to his/her own GitHub page.

Docker, together with Docker Compose, for the DB service, was used to develop this App locally. This has the benefit of allowing for a uniform development environment across different machines and smoothens the deployment process. It also allows us to make sure we're using Python. In this case the lightweight "slim-buster" image for the latest 3.7 release.

For dependency management, the project was started on barebones pip installs and updating a requirements.txt file. However, this approach was soon scrapped in favor of Poetry, which, in the author's opinion, is the best modern dependency manager for Python. And it does a lot more than just that.

Things that could be improved upon:
* The first and foremost, testing. This assignment clearly fails on the TDD side of things. However, TDD is not about speed and was, therefore, consciously abandoned for this assignment.
* UI. The user login page after clicking on the Log In through GitHub button needs work. In it's current state, it's functional but far from pretty.
* Verify that all other means of registering but using GitHub are completely deactivated.


## Setting up project after forking

This project was dockerized with the intention of being run on any machine without issues.
Before running building the App, please create an .env file (you can use the .env.example file in this repository as a starter).
The `CLIENT_SECRET` and `CLIENT_ID` variables are set when creating an OAuth App in GitHub.

To do so, head over to https://github.com/settings/developers.
Click on "OAuth Apps" and then on "New OAuth App". The application name can be whatever you desire, though I'd advise keeping it in line with the name of the app.
If you start the project with the docker configuration in this repository enter the following.

* `Homepage URL=http://0.0.0.0:8000`
* `Authorization Callback URL=http://0.0.0.0:8000/accounts/github/login/callback`

Once these steps are complete we are ready to build the App.
Run `docker-compose up -d --build` in any shell of your liking. When it is completed you'll need to run migrations to create all the necessary tables in the DB.

To do so, run `docker-compose exec web python manage.py migrate`.
With this, you are in a position to start using the App.

[Optional] You can also create a superuser to access the admin panel like so `docker-compose exec web python manage.py createsuperuser` if you desire to view the users that have registered and forked the repo.

Last but not least, this App is fully prepared to be hosted on Heroku. Taking advantage of the free tier that's coming to an end on November.

## Live App

With that said, if you want know what the App looks like and how it behaves without setting it up locally, you can head over to https://git-fork-me.herokuapp.com/home/
