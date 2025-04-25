Pylint - static code analysis
----------------------------- 

Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. 
It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored and can offer you details about the code's complexity.
Set up is done in the `.pylintrc` file.

In the files `fixtures/conftest.py` and `src/send_email.py`, the following commands were used to disable specific Pylint checks:

- `# pylint: disable=W0611`
- `# pylint: disable=E2502`