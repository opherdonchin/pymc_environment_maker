# Installing a PyMC environment

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
4. Go to GitHub Desktop → Repository → Open in Command Prompt
5. In the command prompt type:
    - In the cloned repository run `pixi install`
        - This will install the environment you need for PyMC
6. Your IDE will have different rules for getting it to point to this package:
   - VS Code
     - Install the `pixi` extension to VS Code
     - Type `code .` in the Repositories directory
       - VS Code should automatically recognize the environment and suggest is as the default python environment
   - Spyder
     - Add `pykernels` to this package
       - `pixi add pykernels`
     -
   - PyCharm
7. There are two demo files:
   - Straight python: `pymc_demo.py` 
   - Jupyter notebook: `pymc_demo.ipynb`

Now everything should work. Let me know if it does.