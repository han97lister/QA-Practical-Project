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
  * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-end Design](#front-end-design)
  * [Known Issues](#known-issues)
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


### **Author**
Hannah Lister-Sims

[erd]:https://i.imgur.com/pXvji8l.png?1
[services]:https://i.imgur.com/QDP3UB6.png
[trello]:https://i.imgur.com/Spu1E0m.png
[risk]:https://i.imgur.com/2WIr8rm.png
