.. _how_to_run_tests:

TESTING
=======

.. note::

    All commands are executed from the root directory of the project.

Pytest BDD
----------

To execute BDD tests, run the following command:

.. code:: text

    pytest bdd_tests/login_logout_test.py

    pytest bdd_tests/send_email_test.py  

To execute BDD tests and generate an HTML report stored in a specific folder, run the following command:

.. code:: text

    pytest bdd_tests/login_logout_test.py --html=reports/bdd_reports/report.html

.. hint::

    Test reports are stored in the ``reports/bdd_reports`` folder and can be checked by your favorit browser by opening the ``report.html`` file.

.. _how_to_run_robot:

Robot Framework
---------------

To execute Robot Framework tests, run the following command:

.. code:: text

    robot robot_framework/login_logout.robot

To execute Robot Framework tests and generate an HTML report stored in a specific folder, run the following command:

.. code:: text

    robot --outputdir reports/robot_framework robot_framework/login_logout.robot

BDD Coverage test
-----------------

.. code:: text
    
    pytest --cov=src --cov-report=html:reports/coverage bdd_tests/login_logout_test.py bdd_tests/send_email_test.py
