# F-test
![F-Test](/images/f-test_img.png)

F-test is a simple web app test that handles a register format to send data into a MariaDB Database made with Flask. This simple project is made to learn Flask in a nutshell.

## Frontend
It uses JavaScript, HTML and CSS. You can install Node [here](https://nodejs.dev/en/download/).

## Backend
It uses [Flask](https://flask.palletsprojects.com/en/2.3.x/) as a modern framework to build minimal and scalable applications, as well as [jinja](https://palletsprojects.com/p/jinja/) for HTML rendering. F-test is being set up with environment variables, as well as app.py script to deploy the app. F-test already has it's enviroment deployed but you need to install the proper package itself.
```bash
$ pip install flask
```

## Local
If you wanna store F-test in your local, you can type the following commands with [git](https://git-scm.com/).
```shell
$ git clone https://www.github.com/Its-Yayo/f-test.git
$ cd f-test
```

If you wanna update all changes of F-test, you can type the following command.
```shell
$ git pull
```

# Updates
- Note, [vulnerability](https://github.com/advisories/GHSA-h5c8-rqwp-cp95) in Jinja template which allows users to inject arbitrary code, known as XSS (Cross-Site Scripting) in a HTML Jinja template. Low moderate severity. Id: [CVE-2024-22195](https://nvd.nist.gov/vuln/detail/CVE-2024-22195)

# Releases
- v2023-beta.1.0: Updates in UI interface for client. DB remotely set up for data handling
- v2023-beta.2.0: Updates in code set and data error handlings. DB remotely set up for data handling

## License
This project is under the [MiT](https://opensource.org/license/mit/) License

