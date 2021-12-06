# Project2
this repo is my files for my QA 2021 devops second project

## Contents:
* [Project Brief](#Project-Brief)
* [App Design](#App-Design)
* [CI/CD Pipeline](#CI/CD-Pipeline)
* [Known Issues](#Known-Issues)
* [What i'd add in the future](#What-i'd-add-in-the-future)



## Project Brief
For this project I was required to produce an application consisting of 4 microservices, 2 of these must interact with one another to produce another result, this would then all be displayed on the 4th service. This app was then to be produced and maintained on a fully automated CI/CD pipeline, therefore it needed project tracking, version control, containerisation tools, ochestration tools, config managements, a CI server and a load balancer/reverse proxy. To achieve this I needed to use tools such as Jira, Git, Docker, Ansible, Jenkins and Nginx.

To illustrate some of the brief and the risks involved, I put together a risk assessment from some of the possible outcomes and their severity. I also included possible mitigations.

![risk](https://github.com/bradfield7/Project2/blob/main/projscreenshots/riskassessment.png)

## App Design
Following the brief, and deciding to carry on from my first project, I decided to go with a football theme. My idea is to produce a "who will your child support?" generator, this would go as follows:
* Name API : This service will generate a random name from a list of 24 names using the random.choice() function. It will use a HTTP GET request to receive the information.
* League API: This service will generate a random League from one of the 4 football leagues, like the name it will also use random.choice() and use a HTTP request.
* Club API: This service will use a HTTP POST request to receive data from the first 2 API's, from there it will access 4 dictionaries, 1 for each League. Within each League I will have a name assigned to a team already, so it will get a league from the league API, pick the dictionary, get the name from the name API and then pick the matching club. This info will then be fed back.
* Front-end: This is where I will display my data, this will be the "homepage" of the site and will show the data in a sentence that looks presentable, it will also show the previous 5 results if they are available as they will be stored in a database.

I will also use NGINX as a reverse proxy, this will listen on port 80 on the host machine and direct the traffic to port 5000, where the front-end container is located. This offers a layer of protection to the app and data.

This is a diagram of the layout of my app and the basics of how it will work/be directed
![ERD](https://github.com/bradfield7/Project2/blob/main/projscreenshots/service.png)

This is my app in action
![app](https://github.com/bradfield7/Project2/blob/main/projscreenshots/workingapp2.png)


## CI/CD Pipeline:
This project uses a full CI/CD pipeline, therefore it can test, build, deploy and maintain an app. Like I mentioned earlier, this includes project tracking, version control, development, CI servers and deployment.

this is the link https://bradfield.atlassian.net/jira/software/projects/PR2/boards/4 to my Jira where I used a scrum board for my tracking

Git was used for version control and github was used to store my repository. i used a dev branch and a feature branch in my work so I had more room for freedom without risk of bugs and errors making it to the main branch while I was developing, here is a rundown of my branches throughout the project:

![branches](https://github.com/bradfield7/Project2/blob/main/projscreenshots/networkgraph.png)

The development environment I used was an ubuntu VM, using Google cloud platform.

For the CI server I used jenkins, jenkins would clone down my github repo and peform the script from the 'Jenkinsfile', this included testing, building/pushing images and deploying the app. For the testing I had to include mocking, which simulates the idea of randomness but allows you to say what you want the input to be, this allows you to check specific actions as, although not impossible, it could possibly not come up during tests.
I didn't manage to find a way to get the clearest results possible from my tests but here are images of my coverage:
![test1](https://github.com/bradfield7/Project2/blob/main/projscreenshots/nameGenTests.png)

![test2](https://github.com/bradfield7/Project2/blob/main/projscreenshots/leagueGenTests.png)

![test3](https://github.com/bradfield7/Project2/blob/main/projscreenshots/clubGenTests.png)

![test4](https://github.com/bradfield7/Project2/blob/main/projscreenshots/front-endTests.png)

as you can see it is including some python files which is bringing down my total coverage, even though they should be excluded. the files that matter though all have great coverage

If jenkins decides that all the tests have passed then it will proceed to the build/push images stage. It will take the docker credentials stored in the secret files and matched with variables in the jenkinsfile and then it will push the images to that docker account.

Following this, it moves on to the deploy stage. the scp command will send the docker-compose and the nginx.conf over to the manager VM, then the ansible playbook will run the defined roles. In my case I have Docker, Swarm-manager and swarm-worker. Docker will install the docker requirements and nginx, it will add jenkins to the docker group. Swarn-manager will initiate the swarm and deploy the app from the docker-compose.yaml. docker-worker will simply use the join token to join the swarm as a worker and take on some of the replicas.

After the ansible playbook has ran through all its roles and tasks it will look similar to this:

![ansible](https://github.com/bradfield7/Project2/blob/main/projscreenshots/ansibleworking.png)
Ideally it would show a lot more as yellow "changed" but I ran into multiple errors so had to go through step by step. it its been processed already in a previous step it will show as a green "ok" so it doesn't waste time building again.

this is what the same playbook looks like when it has ran through jenkins:
![jenkinsplay](https://github.com/bradfield7/Project2/blob/main/projscreenshots/jenkinsfinish.png)

Jenkins also shows a nice feature for the jenkinsfile, with checkpoints for each "stage" in the file:

![jenk](https://github.com/bradfield7/Project2/blob/main/projscreenshots/jenkinstable.png)

as you can see from the image, it failed at the last stage on a couple of previous builds, but on the third try it succeeded and built successfully.

## Known Issues
Due to me using a sqlite database, data isnt persistent between uses.
Ansible had a lot of issues to originally work so there may be some instability between VM shut downs. This hasn't been tested at the time of writing.

## What I'd add in the future
In an ideal environment I would make more time to make improvements to the HTML, to make it look cleaner/more professional. With more experience I may add a nexus repository which would be locally hosted, this would elimate the need for docker credentials and would help keep the images/data private.
