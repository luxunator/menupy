# menupy
[![MIT License](https://img.shields.io/badge/license-MIT-red.svg)](https://github.com/luxunator/menupy/blob/master/LICENSE)

Interactive Python Menu

**About**

CLI Menu creation with easy, fast, flexible usage for the programmer, and a clean layout for their users.

# Examples
**Option Menu**
```python
import menupy

NewMenu = menupy.OptionMenu("Title", title_color="cyan")
NewMenu.add_option("Option Selection #1")
NewMenu.add_option("Option Selection #2", color="red")
NewMenu.add_option("Option Selection #3", color="green")
result = NewMenu.run()
```
![](http://i67.tinypic.com/344ys60.jpg)

**Input Menu**
```python
import menupy

NewMenu = menupy.InputMenu("Title", title_color="cyan")
NewMenu.add_input("Input #1")
NewMenu.add_input("Input #2", color="magenta")
NewMenu.add_input("Input #3", color="yellow", input_text="default", input_color="blue")
result = NewMenu.run()
```
![](http://i63.tinypic.com/rgwgvs.jpg)

## License
This project is licensed under the terms of the [MIT License](https://github.com/luxunator/menupy/blob/master/LICENSE).
