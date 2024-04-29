import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_repos_info():
    """Information about Python repos on Github."""
    # Check the response from the API call.
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars" 
    r = requests.get(url)
    return r

def get_repo_dicts(response):
    """Convert response object into a dictionary."""
    response_dict = response.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_names_plot_dicts(repo_dicts):
    """Getting data from repository dicts."""
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        description = repo_dict['description']
        if not description:
            description = 'No description provided.'
        
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': description,
            'xlink': repo_dict['html_url']
            }
        plot_dicts.append(plot_dict)
    return names, plot_dicts

def make_visualization(names, plot_dicts):
    """Visualization of most popular repos."""
    chart_style = LS('#086CA5', base_style=LCS)
    chart_config = pygal.Config()
    chart_config.x_label_rotation=45
    chart_config.show_legend=False
    chart_config.title_font_size = 30
    chart_config.label_font_size = 16
    chart_config.major_label_font_size = 24
    chart_config.show_y_guides = False
    chart_config.width =1000

    chart = pygal.Bar(chart_config, style= chart_style)
    chart.title = 'Most starred Python projects on Github'
    chart.x_labels = names

    chart.add(' ', plot_dicts)
    chart.render_to_file('python_repos_def.svg')

response = get_repos_info()
repo_dicts = get_repo_dicts(response)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)
    