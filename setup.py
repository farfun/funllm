from funpypi import setup

install_requires = ["funpypi","funfile","requests","tqdm"]

setup(
    name="funwork",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "funget = funget.script:funget",
        ]
    },
    version='0.0.1'
)