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

### **Architecture**
#### **Architecture Plan**
Architecture plans are useful as they allow you to initially visualise your end project without going into much detail. As my project progressed, my architecture plan changed slightly and evolved into my final end structure. Below you can see the evolution:    

#### **ERD**
I have used an Entity Relationship Diagram (ERD) to illustrate the table within my database.  
![erd][erd]  
As you can see I only have the one table but this table stores each ticket with it's allocated prize and gives it an identity number so that it stays unique. Both the ERD and architecture plans are component diagrams as they describe my project and wiring of some physical components in the system. I found they helped model implementation details and  allowed me to follow the system's structure which was required in order to cover the brief; more so with the architecture plan. 


### **Author**
Hannah Lister-Sims

[erd]:https://i.imgur.com/pXvji8l.png?1
