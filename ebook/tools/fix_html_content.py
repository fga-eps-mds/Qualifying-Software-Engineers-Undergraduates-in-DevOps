import glob

pattern = '<pre><code class="language-bash">$ '
fixed_pattern = pattern.replace('$ ', '<span style="user-select: none">$ </span>')


def fix_dollar_sign(content):
    return content.replace(pattern, fixed_pattern)


def fix_newline_after_estimated_time(content):
    return content.replace('<br /></p>', '</p><br />')


for f in glob.glob("**/*.html", recursive=True):
    fixed_content = ''

    with open(f, 'r') as file:
        content = file.read()
        fixed_content = fix_dollar_sign(content)
        fixed_content = fix_newline_after_estimated_time(fixed_content)       

    with open(f, 'w') as file:
        file.write(fixed_content)
