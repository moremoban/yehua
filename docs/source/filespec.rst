Example yehua file
================================================================================

Here is the sample startup file::

    configuration:
	  - template_path: ./relative_path_to_this_file
	  - static_path: ./relative_path_to_this_file
    questions:
      - simple_keyword: "Simple Question?"
      - complex_question:
        - question: "The actual question?"
          "1. Answser":
            - follow_up_keyword: "Follow up question?"
          "2. Answer": "N/A"
    mobans:
      - 'mobans': 'this is optional'
    layout:
      - tests
      - docs:
        - source
      - .moban.d:
        - tests
        - docs:
          - source
    templates:
      - "{{project_name}}.yml": project.yml
      - .moban.yml: .moban.yml
    static:
      - ".moban.d/README.rst": "README.rst"
      - "{{project_src}}/__init__.py": __init__.py.jj2
    post-moban:
      git-repo-files:
      - "this_is_optional"
