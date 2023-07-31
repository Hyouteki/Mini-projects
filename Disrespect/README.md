# Disrespect
A python framework with a hint of **disrespect** to python syntax and logic.<br>
Use `#define` command to rename anything to anything...

## Examples
- ``` python
  #define 2 3
  print(1+2)
  ```
  Output: `4`<br><br>
- ``` python
  #define hello moto
  def say():
      print("hello")
  say()
  ```
  Output: `moto`<br><br>
- ``` python
  #define ;
  print("disrespect");
  ```
  Output: `disrespect`<br><br>
- ``` python
  #define push append
  #define vector list
  #define new
  #define <int>
  array = new vector<int>()
  array.push(1)
  array.push(1)
  ```
## How to use #define command
There are two types of commands you can put;
> `#define` commands do not override other `#define` commands.
1. `#define <old> <new>`<br>
  Replaces every instance of `<old>` with `<new>` in every command after this.
2. `#define <old>`<br>
   Deletes every instance of `<old>` in every command after this.
   
## How to compile Disrepect code 
`python disrespect-compiler.py <file-name>`
