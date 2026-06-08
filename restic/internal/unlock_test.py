import unittest
from unittest import mock

import restic
from restic.internal import init


class InitTest(unittest.TestCase):

    @mock.patch.object(init.command_executor, 'execute')
    def test_unlock_with_no_parameters(self, mock_execute):
        restic.unlock()
        mock_execute.assert_called_with(['restic', '--json', 'unlock'])

    @mock.patch.object(init.command_executor, 'execute')
    def test_unlock_with_repository_and_password_file(self, mock_execute):
        restic.unlock(repository='/dummy/repo/path',
                      password_file='secret-pw.txt')
        mock_execute.assert_called_with([
            'restic', '--json', 'unlock', '--repo', '/dummy/repo/path',
            '--password-file', 'secret-pw.txt'
        ])
