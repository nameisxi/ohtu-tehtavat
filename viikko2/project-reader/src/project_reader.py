from urllib import request
from project import Project

import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_data = toml.loads(content)['tool']['poetry']

        # print(toml_data['tool']['poetry'])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deps = toml_data['dependencies'].keys()
        dev_deps = toml_data['dev-dependencies'].keys()

        return Project(toml_data['name'], toml_data['description'], deps, dev_deps)
