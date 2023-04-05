## Project API automated tests for reqres.in


<!-- Технологии -->

### Used technologies
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/logo_stacks/requests.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo_stacks/tg.png"></code>
</p>


<!-- Тест кейсы -->

### What are we testing
* GET single user
* POST create user
* PUT user
* DELETE user
* POST register user


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo_stacks/jenkins.png"> Running the project in Jenkins.
### [Job](https://jenkins.autotests.cloud/job/api_reqres_qa_guru_python_2/)
##### Clicking on "Build Now" will start the test build and execution process.
![This is an image](images/screenshots/jenkins.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo_stacks/allure_report.png"> Allure report.
##### After the tests have passed, you can view the results in the Allure report, which also contains a link to Jenkins.
![This is an image](images/screenshots/allure_dashboard.png)

##### In the Graphs tab, you can view charts about the test execution, based on their prioritization, execution time, and other parameters.
![This is an image](images/screenshots/allure_graphs.png)

##### In the Suites tab, you can find the collected test cases, which describe the steps.
![This is an image](images/screenshots/allure_suites.png)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"> Allure TestOps Integration.
### [Dashboard](https://allure.autotests.cloud/project/1719/dashboards)
##### Also, all reporting is saved in Allure TestOps, where similar charts are built.
![This is an image](images/screenshots/allure_testops_dashboard.png)

#### In the suites tab, we can:
- Manage all test cases or each one separately
- Restart each test separately from all tests
- Configure integration with Jira
- Add manual tests, etc.

![This is an image](images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/logo_stacks/jira.png"> Jira Integration.
##### By setting up integration with Jira through Allure TestOps, you can pass the test execution results and the list of test cases from Allure to the ticket.

![This is an image](images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo_stacks/tg.png"> Telegram integration.
##### After the tests have passed, a Telegram bot sends a message with a chart and some brief information about the tests.

![This is an image](images/screenshots/tg_bot.png)
