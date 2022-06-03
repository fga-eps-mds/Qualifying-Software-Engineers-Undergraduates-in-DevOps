import glob

result = '# Summary\n\n'
visited_folders = set()

for fullpath in sorted(glob.glob("src/**/*.md", recursive=True)):
    tokens = fullpath.split('/')
    print(tokens)
    filename = tokens[-1]
    print(filename)
    name = filename.replace('.md', '').replace('_', '. ').title()
    print('------------------------')
    path = fullpath.split('src/')[-1]
    directory = '/'.join(path.split('/')[:-1])


    for indent, dir in enumerate(directory.split('/')):
        if dir and dir not in visited_folders:
            dir_name = dir.title().replace('_', '. ')
            dir_path = '/'.join(directory.split('/')[:indent+1]).replace(" ", "%20")
            result += f'{" "*((indent)*2)}- [{dir_name}](./{dir_path}/README.md)\n'            
            visited_folders.add(dir)

    if 'SUMMARY' not in fullpath and 'README' not in fullpath:
        indent = (len(tokens)-2)*2
        result += f'{" "*indent}- [{name}](./{path.replace(" ", "%20")})\n'

with open('src/SUMMARY.md', 'w') as file:
    print(result)
    file.write(result)
