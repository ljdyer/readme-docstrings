import argparse
import re

CONFIG_TAG = r'\[\-\^(.*)\=(.*)'

def func_or_method_match_re(func_or_method_name):
    return re.compile(
        rf""" *# ====================\
[\r\n\s]* def {func_or_method_name}\(\
.*(?:\"\"\").*(?:\"\"\")""",
        re.DOTALL
    )

parser = argparse.ArgumentParser(
    prog = 'README Docstrings',
    description = 'Pull docstrings from Python code files into markdown files'
)
parser.add_argument(
    'source_file',
    metavar='S',
    type=str
)

# ====================
def readme_docstrings():

    args = parser.parse_args()
    with open(args.source_file, 'r', encoding='utf-8') as f:
        template = f.read()

    # Get config tags
    config = {m[0]: m[1] for m in re.findall(CONFIG_TAG, template)}
    template = re.sub(rf'{CONFIG_TAG}\n', '', template)
    assert '[-^' not in template

    # Read .py files
    target = config['TARGET']
    del config['TARGET']
    files = {}
    for fref, fp in config.items():
        with open(fp, 'r', encoding='utf-8') as f:
            files[fref] = f.read()

    # Handle docstring references
    tags = [(m[0], m[1], m[2].split('>'))
            for m in re.findall(r'(\[\-\*(.*) (.*))', template)]
    for tag, cmd, ref in tags:
        if cmd == 'func_or_method':
            file = files[ref[0]]
            func_or_method_re = func_or_method_match_re(ref[-1])
            find = func_or_method_re.findall(file)
            try: 
                assert len(find) == 1
            except:
                raise RuntimeError(f'Error with {ref[-1]}: {len(find)} matches found.')
            template = template.replace(tag, f"```python\n{find[0]}\n```")
    assert '[-*' not in template

    with open(target, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f'Wrote markdown file with docstrings to {target}.')
