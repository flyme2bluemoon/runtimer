# Runtimer
A Python Command Line Tool used calculate the runtime of a program.

## Installation

If your system is running ZSH:
```zsh
git clone https://github.com/flyme2bluemoon/runtimer.git
cd runtimer
echo "alias runtimer=\"python3 $PWD/runtimer.py\"" >> ~/.zsh
```

If your system is running BASH:
```bash
git clone https://github.com/flyme2bluemoon/runtimer.git
cd runtimer
echo "alias runtimer=\"python3 $PWD/runtimer.py\"" $PWD >> ~/.bashrc
```

## Usage

```sh
runtimer program_name program_args
```
Where `program_name` is the program you would like to calculate the time of and `program_args` are the optional arguments that will be passed to the program.

## License

[MIT License](https://github.com/flyme2bluemoon/runtimer/blob/main/LICENSE)
