import os

conf = {
    'zhipu_api_key': os.getenv('ZHIPU_API_KEY', ''),
    'serper_api_key': os.getenv('SERPER_API_KEY', ''),
    'log_dir': './logs',
    'output_base_dir': './output',
    'title_output_path': './title.json',
    'search_result_path': './search_result.json',
    'outline_output_path': './outline.json',
    'paragraph_dir': './paragraph',
    'output_html_path': './news.html',
}

conf['title_output_path'] = os.path.normpath(os.path.join(conf['output_base_dir'], conf['title_output_path']))
conf['search_result_path'] = os.path.normpath(os.path.join(conf['output_base_dir'], conf['search_result_path']))
conf['outline_output_path'] = os.path.normpath(os.path.join(conf['output_base_dir'], conf['outline_output_path']))
conf['paragraph_dir'] = os.path.normpath(os.path.join(conf['output_base_dir'], conf['paragraph_dir']))
conf['output_html_path'] = os.path.normpath(os.path.join(conf['output_base_dir'], conf['output_html_path']))
