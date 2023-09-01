import nox


@nox.session
def tests(session):
    session.run("mkdir", "-p", ".pytest_report", external=True)
    session.run("rm", "-rf", ".pytest_report/*", external=True)
    session.run(
        "coverage",
        "run",
        "-m",
        "pytest",
        "--junitxml=.pytest_report/report.xml",
        "--html=.pytest_report/report.html",
        "--self-contained-html",
        "--ds=src.settings",
        "--log-cli-level=DEBUG",
        "--log-file=pytest.log",
        "--log-file-level=DEBUG",
        external=True,
    )


@nox.session
def coverage(session):
    session.run("mkdir", "-p", ".coverage_report", external=True)
    session.run("rm", "-rf", ".coverage_report/*", external=True)
    session.run("coverage", "html", external=True)


@nox.session
def lint(session):
    session.run(
        "ruff",
        "domain",
        "tests",
        external=True,
    )
