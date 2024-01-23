# txtsplit

[Tortoise TTS](https://github.com/neonbjb/tortoise-tts)'s text splitter, repackaged. All credit goes to the author of Tortoise TTS.

## Installation

```
pip install txtsplit
```

(0 dependencies)

## Usage

```python
from txtsplit import txtsplit
print(txtsplit("Long text", desired_length=100, max_length=200))
```

## License & Credits

Most of the code was taken from [Tortoise TTS](https://github.com/neonbjb/tortoise-tts).

Apache 2.0, like Tortoise TTS.