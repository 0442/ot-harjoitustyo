from invoke import task, Context

@task
def start(ctx: Context):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx: Context):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx: Context):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx: Context):
    ctx.run("coverage html", pty=True)