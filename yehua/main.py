from yehua.project import Project


def main():
    project = Project()
    project.create_all_directories()
    project.templating()
    project.copy_static_files()
