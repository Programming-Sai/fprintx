# fprintx

**fprintx** is a minimal Python utility for clean, aligned debug printing — especially useful in coding contests or complex loops where output readability matters.

---

## Why fprintx?

When debugging in competitive programming or trying to inspect multiple values in a loop, messy spacing can make it hard to quickly see what’s happening. You might print values like this:

```python
for i in range(3):
    print(i, i * 10, i ** 2)
```

And get:

```
0 0 0
1 10 1
2 20 4
```

That’s fine… until the values start getting uneven:

```
10 100 100
100 1000 10000
```

That’s where **fprintx** helps — it aligns and formats each value clearly, so you can visually track changes without squinting.

---

## Features

- Align multiple values (left, center, right)
- Set custom widths for better visual layout
- Apply styles like bold, italic, or underline (optional)
- Optional truncation of long strings
- Return as string if you don’t want to print immediately

---

## Quick Example

```python
from fprintx import printx

for i in range(3):
    printx("i:", i, "i*10:", i*10, "i^2:", i**2, widths=[3, 4, 6, 5, 4])
```

Sample output:

```
i:  0    i*10:    0   i^2:  0
i:  1    i*10:   10   i^2:  1
i:  2    i*10:   20   i^2:  4
```

---

## Installation

To install fprintx directly via pip, simply run:

```bash
pip install git+https://github.com/Programming-Sai/fprintx.git
```

If you'd like to test, contribute, or run it locally, you can also clone the repository:

```bash
git clone https://github.com/Programming-Sai/fprintx.git

cd fprintx
```

---

## Options

| Parameter       | Description                                    |
| --------------- | ---------------------------------------------- |
| `widths`        | List of widths per value                       |
| `alignments`    | List of alignments (`<`, `>`, `^`)             |
| `styles`        | List of styles (`bold`, `italic`, `underline`) |
| `truncate`      | Truncate values that overflow width            |
| `return_as_str` | Return the result instead of printing          |

---

## Testing

```bash
python -m unittest discover -s tests
```

---

## Project Structure

```ftt
./fprintx/*
        ├─ fprintx/*
        |       ├─ core.py
        |       └─ __init__.py
        ├─ tests/*
        |       └─ test_fprintx.py
        ├─ .fttignore
        ├─ .gitignore
        ├─ LICENSE
        ├─ README.md
        └─ setup.py
```

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Programming-Sai/fprintx/issues) for any ideas or to report bugs.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
