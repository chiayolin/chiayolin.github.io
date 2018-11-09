from jinja2 import FileSystemLoader as load_files
from jinja2 import Environment
from markdown2 import markdown

import os, sys, shutil

"""
site configs
"""
TITLE = 'chiayolin.org'
SITE_PREFIX = '/'
POSTS_PREFIX = 'blog/'

"""
symbolic constants
"""
OUTPUT_DIR = '_output/'
STATIC_DIR = '_static/'
PAGES_DIR = '_pages/'
POSTS_DIR = '_posts/'
TEMPLATES = 'templates/'

def read_file(path):
    """
    returns file content specified by path.
    """

    with open(path, 'rb') as f:
        content = f.read().decode('utf-8', 'ignore')

    return content

def write_file(path, content):
    """
    returns None, writes content to file specified by path.
    """

    with open(path, 'w') as f:
        f.write(content)

    return

def list_dir(path):
    """
    returns list of everything under path exclusing the hidden files
    """

    return [*filter(lambda x: x[0] != '.', os.listdir(path))]

def kigenize(date):
    l = date.split('-')
    y = '紀元 ' + str(int(l[0]) + 660) + ' 年 '
    m = l[1] + ' 月 '
    d = l[2] + ' 日'

    return y + m + d

def render_pages(j2_env, metadata = {}):
    """
    returns None, renders pages in src_dir, write to out_dir.

    This functions takes two arguments, j2_env and metadata. Second is a
    mapping which can be passed for special pages to render. An example of a
    of a special page can be 'index.html', where it displays a list of posts
    And to display these posts, a mapping of { 'posts' : [...] } will be
    passed to the function where [...] is an array of post metadata.

    Futhemore, these special pages shall not be rendered with the default
    template, since the default one is just HTML subsititution where the
    content is not rendered. Therefore, this function matches page's file-
    name against existing ones in TEMPLATES. If the page's filename is same
    with a template's filename, then that template is used to render instead
    of the default one.

    A pound sign '#' is used to indicate file hierarchy for the output of the
    page rendered. E.G. page named 'blog#index.html under PAGES_DIR will be
    rendered with 'blog#index.html' under TEMPLATES, this behavior is described
    above. However, the rendered file will be at OUTPUT_DIR/blog/index.html
    instead since a pound sign indicates a slash '/' which is a representation
    of the file hierarchy.
    """

    src_dir = PAGES_DIR
    out_dir = OUTPUT_DIR
    tmp_dir = j2_env.loader.searchpath[0] + '/'

    for raw_page in list_dir(src_dir):
        # render special pages: if page's filename is the same as the one in
        # template, use that template to render instead.
        print(raw_page + ': processing page...')
        if raw_page in list_dir(tmp_dir):
            j2_temp = j2_env.get_template(raw_page)
            print(raw_page + ': special case template')
        else:
            j2_temp = j2_env.get_template('page.html')

        raw_html = read_file(src_dir + raw_page)
        rendered = j2_temp.render(html = raw_html, **metadata)

        # engineer and write to correct output path
        fullpath = raw_page.replace('#', '/')
        basename = os.path.basename(fullpath)
        dirname = os.path.dirname(fullpath)
        if dirname:
            os.makedirs(out_dir + dirname, exist_ok=True)

        write_file(out_dir + fullpath, rendered + '\n')
        print('wrote to ' + out_dir + fullpath)

    return

def render_posts(j2_env, metadata, path_prefix=POSTS_PREFIX):
    """
    returns list of post meta, renders posts in src_dir, write to out_dir.

    This function by default outputs the rendered file under POST_DIR to
    OUTPUT_DIR/POSTS_PREFIX/FILE.html. Futhemore, it returns a collection
    of metadata of the posts it rendered.
    """

    src_dir = POSTS_DIR
    out_dir = OUTPUT_DIR

    md_extr = ['metadata', 'footnotes', 'code-friendly', 'fenced-code-blocks']
    j2_temp = j2_env.get_template('post.html')

    _metadata = []
    for raw_post in list_dir(src_dir):
        print(raw_post + ': processing post...')
        raw_data = read_file(src_dir + raw_post)
        raw_html = markdown(raw_data, extras=md_extr)
        metadata = raw_html.metadata

        # add path name to file
        filename = os.path.splitext(raw_post)[0] + '.html'
        metadata.update({ 'filename' : filename })

        # update date format
        metadata['date'] = kigenize(metadata['date'])
        if 'modified' in metadata:
            metadata['modified'] = kigenize(metadata['modified'])

        _metadata.append(metadata) # append to accumula. list
        rendered = j2_temp.render(html = raw_html, **metadata)
        write_file(out_dir + path_prefix + filename, rendered + '\n')
        print('wrote to ' + out_dir + path_prefix + filename)

    # sort _metadata with each dict's datetime created and then
    # return the reverse because latest should go first
    sorted_metadata = sorted(_metadata, key=lambda kv: kv['date'])
    return [*reversed(sorted_metadata)]

def main():
    """
    returns None, program's main entry.
    """

    # output preprocessing: remove the existing OUTPUT_DIR if presented.
    # copytree() creates a new directory if not yet presented, things
    # under STATIC_DIR will just be copied to OUTPUT_DIR without rednering.
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    shutil.copytree(STATIC_DIR, OUTPUT_DIR, ignore=shutil.ignore_patterns('.*'))

    os.mkdir(OUTPUT_DIR + POSTS_PREFIX)

    # load jinja2 template
    j2_env = Environment(loader = load_files(TEMPLATES))

    metadata = { 'site' : {
        'title' : TITLE,
        'prefix' : SITE_PREFIX,
        'posts_prefix' : POSTS_PREFIX,
        }
    }

    # render posts and pages
    posts = render_posts(j2_env, metadata)
    metadata.update({ 'posts' : posts })
    render_pages(j2_env, metadata)

    print('\n' + str(metadata))

    return

__name__ == '__main__' and main()
