Getting Started
===============
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
-----------------
Nectar has two main components: the Nectar API and the Workers. They communicate with each other using RabbitMQ. Additionally, the Nectar API uses MongoDB to store GymEnvironment and Experiment objects. Each of these need to be installed as well as the dependencies for each component.

Python
^^^^^^
First, you will need to download and install Python for running the workers. Some of the dependencies do not have support for Python 3.10 yet so it is strongly advised that you install Python 3.9 instead. Installation instructions for Python 3.9 can be found `here. <https://docs.python.org/3.9/using/index.html>`_

Java
^^^^
Next, you will need to download and install Java 17. Java 17 downloads can be found `here. <https://www.oracle.com/java/technologies/downloads/>`_

Apache Maven
^^^^^^^^^^^^
You will also need to download and install Apache Maven. Instructions can be found `here. <https://maven.apache.org/install.html>`_

MongoDB Community Edition
^^^^^^^^^^^^^^^^^^^^^^^^^
Then, you will need to install and run MongoDB Community Edition. The instructions can be found `here. <https://docs.mongodb.com/manual/administration/install-community/>`_

RabbitMQ
^^^^^^^^
Next, you should install and run RabbitMQ. The instructions can be found `here. <https://www.rabbitmq.com/download.html>`_

Worker Dependencies
^^^^^^^^^^^^^^^^^^^
Now you can install the dependencies for the workers by navigating to the ``workers`` folder in your command line and running: ``pip install -r requirements.txt``

Nectar API Dependencies
^^^^^^^^^^^^^^^^^^^^^^^
Finally, you need to install the Maven dependencies for the Nectar API by navigating to the ``nectar`` folder in your command line and running: ``mvn clean install``

Launching
---------
Before attempting to launch the Nectar API or Workers, ensure that both MongoDB and RabbitMQ are running. Then you can launch the workers in one shell with: ``python ppo_worker.py``

In another shell, you can launch the Nectar API with: ``mvn spring-boot:run``