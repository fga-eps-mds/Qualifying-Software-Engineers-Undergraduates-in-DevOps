import json
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'supports':
        sys.exit(0)

context, book = json.load(sys.stdin)


def log(msg, write='a'):
    with open('log.json', write) as f:
        if msg:
            json.dump(msg, f)
        else:
            f.write()


def content_with_estimated_time(content, time_text):
    log(content)
    first_line, remaining_content = content.split('\n', 1)
    if remaining_content.isspace():
        return content
    newline_before_header = '' if remaining_content[1] == '#' else '<br />'
    return f'{first_line}\n{time_text}{newline_before_header}\n{remaining_content}'


def build_span_tag(time):
    return f'<i class="hljs-comment" style="background-color: rgba(0,0,0,0)">Tempo estimado de leitura: {time}min</i>'


def count_time(word_count):
    minutes, seconds = word_count//200, 0.6*(word_count/200)%1
    minutes = minutes if seconds < 30 else minutes+1
    minutes = minutes if minutes else 1
    return minutes


def traverse(list_of_chapters):
    for chapter in list_of_chapters:
        if len(chapter['Chapter']['sub_items']):
            traverse(chapter['Chapter']['sub_items'])
        word_count = len(chapter['Chapter']['content'].split())
        time_text = build_span_tag(count_time(word_count))
        chapter['Chapter']['content'] = content_with_estimated_time(
            chapter['Chapter']['content'], time_text)


# log(None, write='w')
traverse(book['sections'])
json.dump(book, sys.stdout)
