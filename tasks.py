from invoke import task, Context

@task
def start(ctx: Context):
    ctx.run("python3 src/main.py", pty=True)

@task
def build(ctx: Context):
    ctx.run("python3 src/init_database.py", pty=True)

@task
def test(ctx: Context):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx: Context):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx: Context):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx: Context):
    ctx.run("pylint src", pty=True)

@task
def format(ctx: Context):
    ctx.run("autopep8 --in-place --recursive src", pty=True)