# Run Selenium Tests With pytest On LambdaTest

## Table Of Contents

* [Pre-requisites](#pre-requisites)
* [Run Your First Test](#run-your-first-test)
* [Local Testing With pytest](#testing-locally-hosted-or-privately-hosted-projects)
## Prerequisites

Before you can start performing **Python 3** automation testing using **pytest**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Download the latest **Selenium Client** and its **WebDriver bindings** from the [official website](https://www.selenium.dev/downloads/). Latest versions of **Selenium Client** and **WebDriver** are ideal for running your automation script on LambdaTest Selenium cloud grid.
* Install **virtualenv** which is the recommended way to run your tests. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules.

```bash
pip install virtualenv
```
### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s pytest-selenium-sample repository and navigate to the code directory as shown below:
```bash
git clone https://github.com/rohitbinmile/lambda-test.git
cd lambda-test
```
**Step 2:** Create a virtual environment in your project folder the environment name is arbitrary.
```bash
virtualenv venv
```
**Step 3:** Activate the environment.
```bash
source venv/bin/activate
```
**Step 4:** Install the [required packages](https://github.com/LambdaTest/pytest-selenium-sample/blob/master/requirements.txt) from the cloned project directory:
```bash
pip install -r requirements.txt
```

### Setting Up Your Authentication

Make sure you have your LambdaTest credentials with you to run test automation scripts. You can get these credentials from the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build/?utm_source=github&utm_medium=repo&utm_campaign=pytest-selenium-sample) or by your [LambdaTest Profile](https://accounts.lambdatest.com/login/?utm_source=github&utm_medium=repo&utm_campaign=pytest-selenium-sample).

**Step 5:** Set LambdaTest **Username** and **Access Key** in environment variables.

* For **Linux/macOS**:
  
  ```bash
  export LT_USERNAME="YOUR_USERNAME" 
  export LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```
  * For **Windows**:
  ```bash
  set LT_USERNAME="YOUR_USERNAME" 
  set LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```

## Run Your First Test

>**Test Scenario**: The [main.py](https://github.com/LambdaTest/pytest-selenium-sample/blob/master/main.py) sample script tests a simple to-do application with basic functionalities like mark items as done, add items in a list, calculate total pending items etc.

### Executing The Test

**Step 6:** You would need to execute the below command in your terminal/cmd.

```bash
pytest -s main.py
```
Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on LambdaTest automation dashboard. [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build/?utm_source=github&utm_medium=repo&utm_campaign=pytest-selenium-sample) will help you view all your text logs, screenshots and video recording for your entire automation tests.

## Run Your Parallel Tests Using PyTest Framework

To run parallel tests using PyTest, we would have to execute the below command in the terminal:

```bash
pytest --workers 2 -s main.py
```

## Testing Locally Hosted Or Privately Hosted Projects

You can test your locally hosted or privately hosted projects with LambdaTest Selenium grid using LambdaTest Tunnel. All you would have to do is set up an SSH tunnel using tunnel and pass toggle `tunnel = True` via desired capabilities. LambdaTest Tunnel establishes a secure SSH protocol based tunnel that allows you in testing your locally hosted or privately hosted pages, even before they are live.

Refer our [LambdaTest Tunnel documentation](https://www.lambdatest.com/support/docs/testing-locally-hosted-pages/) for more information.

Here’s how you can establish LambdaTest Tunnel.

Download the binary file of:
* [LambdaTest Tunnel for Windows](https://downloads.lambdatest.com/tunnel/v3/windows/64bit/LT_Windows.zip)
* [LambdaTest Tunnel for macOS](https://downloads.lambdatest.com/tunnel/v3/mac/64bit/LT_Mac.zip)
* [LambdaTest Tunnel for Linux](https://downloads.lambdatest.com/tunnel/v3/linux/64bit/LT_Linux.zip)

Open command prompt and navigate to the binary folder.

Run the following command:

```bash
LT -user {user’s login email} -key {user’s access key}
```
So if your user name is lambdatest@example.com and key is 123456, the command would be:

```bash
LT -user lambdatest@example.com -key 123456
```
Once you are able to connect **LambdaTest Tunnel** successfully, you would just have to pass on tunnel capabilities in the code shown below :

**Tunnel Capability**

```
"tunnel" = true
```