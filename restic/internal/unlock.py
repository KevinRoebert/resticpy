from restic.internal import command_executor


def run(restic_base_command,
        repository=None,
        password_file=None):
    cmd = restic_base_command + ['unlock']

    if repository:
        cmd.extend(['--repo', repository])

    if password_file:
        cmd.extend(['--password-file', password_file])

    return command_executor.execute(cmd)
