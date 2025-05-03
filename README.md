# Installing a PyMC environment

## For VS Code 
1. Install [pixi](https://pixi.sh/latest/advanced/installation/):
    - Run this in PowerShell:
        - `powershell -ExecutionPolicy ByPass -c "irm -useb <https://pixi.sh/install.ps1> | iex"`
2. Install a git client such as [GitHub Desktop](https://desktop.github.com/download/)
3. Open this repository in GitHub Desktop
    - You open the repository in GitHub and then either:
        - Go to Code → Local → Open with GitHub Desktop
        - Use the URL:
            - Go to Code → Local → Copy the URL
            - Open GitHub Desktop → File → Clone Repository → URL and paste the URL
        - I recommend putting all your repositories in a simple, short directory name in the root directory of a drive. It makes them easier to find.
        - Once the repository is cloned, you can remove the remote
          - In GitHub desktop: `Repository` -> `Remote settings` and then delete the address of this repository
4. Go to GitHub Desktop → Repository → Open in Command Prompt
5. In the command prompt type:
    - In the cloned repository run `pixi install`
        - This will install the environment you need for PyMC
6. Make sure `pixi` extension to VS Code is installed
7. Type `code .` to start VS Code
    - Or click Repository -> Open repository in VS Code in GitHub Desktop
    - VS Code should automatically recognize the environment and suggest it as the default Python environment
8. There are two demo files:
    - Straight python: `pymc_demo.py` 
    - Jupyter notebook: `pymc_demo.ipynb`
  
## For PyCharm
1. Clone this repository into PyCharm
   - When you open PyCharm, choose `Clone a repository`
   - On GitHub, in this repository, go to Code → Local → Copy the URL
   - Paste the URL into PyCharm
   - Once it is cloned, you can remove it in the PyCharm GitHub by clicking Manage Remotes and clicking `-` on this repository
2. Create a new Python environment in PyCharm for your work
   - Go to Settings (gear bar upper right or Ctrl-Alt-S) -> Project -> Python Interpreter
   - Click `add interpreter` -> `add local interpreter`
   - Under Type choose Poetry
     - PyCharm will prompt to install poetery if it is not installed
   - Select `Make a virtual environment for this project`
     - PyCharm will read the `pyproject.toml` file and install all the required packages


3. Your IDE will have different rules for getting it to point to this package:
   - VS Code
     - Install the `pixi` extension to VS Code
     - Type `code .` in the Repositories directory
       - VS Code should automatically recognize the environment and suggest is as the default python environment
   - Spyder
     - Add `pykernels` to this package
       - `pixi add pykernels`
     -
   - PyCharm
     - Open the folder as a project
4. There are two demo files:
   - Straight python: `pymc_demo.py` 
   - Jupyter notebook: `pymc_demo.ipynb`

Now everything should work. Let me know if it does.