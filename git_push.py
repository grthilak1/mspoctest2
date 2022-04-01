import subprocess

def execute_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, universal_newlines=True)
    stdout,stderr = process.communicate()
    print("output: {}".format(stdout))
    print("error:".format(stderr))

execute_cmd('git init')
execute_cmd('git add .')
execute_cmd('git commit -m "updated"')
execute_cmd('git remote add origin https://github.com/grthilak1/mspoctest.git')
execute_cmd('git branch -M main')
execute_cmd('git push https://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@github.com/grthilak1/mspoctest.git')
