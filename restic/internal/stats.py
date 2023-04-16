import json

from restic.internal import command_executor


def run(restic_base_command,
        mode=None,
        repository=None,
        password_file=None):
    cmd = restic_base_command + ['stats']

    if mode:
        cmd.extend(['--mode', mode])

    if repository:
        cmd.extend(['--repo', repository])

    if password_file:
        cmd.extend(['--password-file', password_file])

    return json.loads(command_executor.execute(cmd))
