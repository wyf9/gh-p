# coding: utf-8
# Fork / clone to modify (maybe) useless config

import typing as t

pr_branch_format: str = 'gh-pull-{number}'
'''
Controls local branch prefix\n
Placeholder: `{number}`\n
e.g. `gh-pull-{number}` -> `gh-pull-125`
'''

pr_branch_matches: list[tuple[str, bool]] = [
    (pr_branch_format, True),
    ('gh-{number}', False),
    ('pull-{number}', False),
    ('pr-{number}', False)
]
'''
Controls how to extract PR number from local branch name\n
Format: `(pattern: str, strict: bool)`\n
`pattern`: regex / string contains `{number}` / string contains `*`\n
`strict`: Controls full-match mode / contain mode\n
Placeholder: `{number}`
'''

temp_remote_name: str = 'gh-pull-temp'
'''
Control remote name (for temp use)
'''

remote_url: str = 'https://github.com/{owner}/{repo}.git'
'''
Custom remote url\n
Placeholder: `{owner}`, `{repo}`\n
HTTPS: `https://github.com/{owner}/{repo}.git`\n
SSH: `git@github.com:{owner}/{repo}.git`
'''

aliases: dict[t.Literal[
    'checkout',
    'push',
    'delete' # TODO
], list[str]] = {
    'checkout': [
        'checkout',
        'check'
        'chk',
        'co',
        'c'
    ],
    'push': [
        'push',
        'ps',
        'p'
    ]
}
