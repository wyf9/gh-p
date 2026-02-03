# coding: utf-8
# Fork / clone to modify (maybe) useless config

import typing as t
from pathlib import Path
from json import load as load_json
from sys import argv

import log as l

# region define


class Config:
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
        'push'
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

# endregion define

# region load

for v in argv:
    if v == '-v' or v == '--verbose':
        l.is_verbose = True

PATHS = [
    Path.home() / '.wyf9' / 'gh-p.json',
    Path.home() / '.wyf9' / 'gh-p' / 'config.json',
    Path.home() / '.config' / 'gh-p.json',
    Path.home() / '.config' / 'gh-p' / 'config.json',
]


def load_config() -> dict:
    for p in PATHS:
        if p.exists() and p.is_file():
            l.verbose(f'[config] try path {p}')
            try:
                with p.open('r', encoding='utf-8') as f:
                    return load_json(f)
            except Exception as e:
                l.warning(f'Load config file {p} failed: {e}')
    return {}


config = Config()
loaded_config = load_config()
l.verbose(f'[config] loaded json: {loaded_config}')

for k, v in loaded_config.items():
    i = getattr(config, k, None)
    if i:
        t1 = type(i)
        t2 = type(v)
        if t1 == t2:
            setattr(config, k, v)
            l.verbose(f'[config] item set: {k} ({t1.__name__}) : {v}')
        else:
            l.warning(f'Type of config item {k} is expected {t1.__name__}, but got {t2.__name__}')


# endregion load
