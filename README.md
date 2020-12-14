# QA-Practical-Project
## **Lottery App**

### **Resources**

* Presentation:
* Trello Board:https://trello.com/b/JbWnQiQF/qa-practical-project
* Website: 

### **Contents**
* [Brief](#brief)
* [My Approach](#my-approach)
* [Architecture](#architecture)
  * [Architecture Plan](#architecture-plan)
  * [ERD](#erd)
  * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-end Design](#front-end-design)
* [Future Improvements](#future-improvements)
* [Author](#author)

### **Brief**
For this project, I had the objective of creating a service-orientated application that is composed of four services which all communicate with each other. I also needed to implement changes to each service without disrupting the user experience in order to show automated updates. A key focus to this project was the deployment using containerisation and an orchestration tool; which enables applications to go up to the service level, allowing scalability and thus better handle more traffic.

### **My Approach**
I decided to create a Lottery Ticket and Prize Generator application that allows users to win a prize based on what lottery ticket they are given. My first service is the main API and the front-end which is what users see, it is also where I will render my Jinja2 templates and persist data into MySQL. As the main API, it is responsible for communicating with the other 3 services and it does this by allowing get and post requests. This application will display a lottery ticket with the allocated prize and the option to play again with the use of a refresh button which will generate a new lottery ticket for the user.  

The second service generates a random object which is the first half of the user's lottery ticket and a combination of three uppercase letters selected from a list. Once generated it will pass the letters back onto service 1. The third service also generates a random object; except this application will be a selection of randomly chosen 5-digit numbers. Similar to service 2, it will be passed back to service 1 where it combines both the letters and numbers in order to create the lottery ticket.

The fourth service takes both get and post requests as it creates an object based upon the results of service 2 and 3. Once it has received the lottery ticket from service 1, it will allocate a prize and post the object back to service 1 for the user to see.  

Here is a visual representation of the relationship between my services:  
![services][services]

### **Architecture**
#### **Architecture Plan**
Architecture plans are useful as they allow you to initially visualise your end project without going into much detail. As my project progressed, my architecture plan changed slightly and evolved into my final end structure. Below you can see the evolution:  
![arch1][arch1]  
Initially I thought my load balancer (NGINX) would be containerised and included within my Docker-Swarm, however, I soon realised it would need to be seperate in order to deligate the user traffic to each machine. Here is an updated plan I created:  
![arch1-2][arch1-2]  
After completing this design, I wasn't convinced with the placement of my Jenkins box and thus how it lead to the load balancer. I was happy with my Docker-Swarm image so created a design that would give a clear overview of my architecture:  
![arch2][arch2]  
I was pleased with this final architecture plan as it simply shows that the load balancer is used to deal with traffic and balance it between my swarm cluster which are made up of replica nodes that are all created as part of my Jenkins Pipeline. Below is a screenshot of my Jenkins Pipeline successfully deploying my application:  
![jenkins][jenkins]  

#### **ERD**
I have used an Entity Relationship Diagram (ERD) to illustrate the table within my database.  
![erd][erd]  
As you can see I only have the one table but this table stores each ticket with it's allocated prize and gives it an identity number so that it stays unique. Both the ERD and architecture plans are component diagrams as they describe my project and wiring of some physical components in the system. I found they helped model implementation details and  allowed me to follow the system's structure which was required in order to cover the brief; more so with the architecture plan.  

### **Project Tracking**
I chose to track my project using Trello and have attached a snapshot below:  
![trello][trello]  
Trello is very useful as it allows you to label your tasks in order to keep a clear methodology whilst working through projects. As this project required 4 services all working together, I thought it would be helpful seperating my tasks into each service and then using my product backlog to keep general tasks needed for all services; in an order that would be efficient in completion. I colour co-orindated my labels with a simple to-do (red), doing (yellow) and done (green) system so that at a quick glance it was clear to gage my progress within the project. In order to follow agile methods, I also included user stories within my trello board. User stories are really useful as they allow you stay focused on the end goal and keep in mind the user's experience throughout.

### **Risk Assessment**
Risk assessments are essential when completing a project as they allow you to mitigate certain risks and prepare responses for others that me out of your control. Below I have attached a screenshot of the risk assessment I completed and underneath that image is a link to the full version:  
![risk][risk]  
https://docs.google.com/spreadsheets/d/1lqB149AnvSHusWHYlMSmQc1Qp5mM6y4bi0fCFFa7N3E/edit?usp=sharing  
Components of a risk include the cause, event and effect and I have assessed these risks based on the probability of them occuring, the impact they will have and proximity in order to try mitigate risks as much as possible. Once I identified some risks, I was able to strengthen my application by enforcing proposed mitigations assessed earlier on. Therefore, I have included a column in my register in order to document updates I have made throughout my project to combat some risks.  

### **Testing**
I completed unit-tests using Pytest and I did this for each service. These tests were written so that I knew each application was created and thus outputted what I expected. For service 1, I used the unittest mock method called patch. This allowed me to adjust the functionality of my app for testing purposes by allowing mock responses. For example, I was able input a return value for both the GET and POST requests my application completed and the correct response for that data. Here is the coverage report for my service 1 application:  
![test1][test1]  
This is a snapshot of the pytest I completed when my application code was all within the app.py file and the line not accounted for is the code "if __name__=='__main__':" which I am unable to test for. Therefore, in terms of my service 1 app I have gained 100% successful coverage for what I expect the app to do and display for users. Since I have developed my application further by connecting a Mysql database, the structure of this application has changed. However, as I was able to deploy my whole application through Gunicorn in Jenkins, Jenkins completed this same test with the correct file structure and thus coverage.  

When testing service 2, I didn't use the patch method as I simply tested that my app retrieved letters from the list provided in the url 'letters' and responsed with a 200 status code which would mean it had no errors. Here is a snapshot of the pytest result:  
![test2][test2]  
As you can see there is only one line of code not accounted for and this is the same issue found with service 1 in terms of preventing 100% test coverage. Therefore, I am happy with this result as it confirms the output of this service is in the correct format.  

Service 3 was very similar to service 2 in terms of testing with the only difference being which list it retrieved data from. Service 3 was responsible for providing numbers to the lottery ticket and so it got data from the url 'get_number' and had a 200 status code response. Below is the screenshot of my pytest coverage report for service 3:  
![test3][test3]  
Similar to the previous pytest reports for other applications, I am only not testing the one line of code and so would consider this a fully successful test coverage as it proves my application has no errors and outputs expected data.  

Service 4 required tests for POST requests as this was the application responsible for returning the prize to the user. Therefore, I wanted to test that each possible prize was accounted for depending on the user's ticket and here is the coverage report:  
![test4][test4]  
This report has the same missing term for tests as the other services but looking past that, it is clear my appliation outputs what I expect with no errors.  

Initially, I ran these tests in my virtual machine and gained a coverage report in order to monitor the success; as my project progressed I was then able to containerise these tests have Jenkins run them and report the results in the configuration analysis, however when I analysed this it did not show what I expected or the high coverage I have shown above. The reason for this is unknown to me and so I would definitely like to look into this in the future.

### **Front-end Design**
To help you visulise my application, I have included screenshots of it functioning with the full deployment pipeline automated through Jenkins. This design meets the minimum requirements for this project, however I would definitely like to improve the HTML features in order to have the application looking more applealing for the user. Here is a screenshot of the application where the user would be awarded the highest prize offered:  
![prize1][prize1]  
Here is a screenshot of another lottery ticket example with a different prize awarded:  
![prize2][prize2]  
Finally, here is a screenshot of a lottery ticket where the user unfortunately wins nothing:  
![prize3][prize3]  
Fortunately, the user has the option to try again for a prize by clicking on the refresh button. The refresh button will output a different lottery ticket and potentially a different prize!

### **Future Improvements**
When considering future improvements, I would first look at addressing the known issues, some of which mentioned previously, and then consider ways in which I could both improve the user experience and update more risks in my risk registry. These would include:  
* Investigate the issue with the test reports in my Jenkins configuration output
* Implement tests for the change branch I merged during the presentation demonstration
* Improve the general visulisation of my application
* Implement more proposed mitigations that have been addressed in my risk assessment

### **Author**
Hannah Lister-Sims

[arch1]:https://i.imgur.com/SYzcwBi.png
[arch1-2]:https://i.imgur.com/KlUfYb7.png
[arch2]:https://i.imgur.com/m2mjZbz.png
[jenkins]:https://i.imgur.com/i2KZ3eQ.png
[erd]:https://i.imgur.com/pXvji8l.png?1
[services]:https://i.imgur.com/QDP3UB6.png
[trello]:https://i.imgur.com/Spu1E0m.png
[risk]:https://i.imgur.com/2WIr8rm.png
[test1]:https://i.imgur.com/96ivknO.png
[test2]:https://i.imgur.com/lDbn1z1.png
[test3]:https://i.imgur.com/QU9kWin.png
[test4]:https://i.imgur.com/IEjREsv.png
[prize1]:https://i.imgur.com/eo207Px.png
[prize2]:https://i.imgur.com/neD0Unz.png
[prize3]:https://i.imgur.com/MtT6b8U.png
