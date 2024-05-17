from PIL import Image
import os

def gif_to_png(gif_path, output_folder):
    gif = Image.open(gif_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frame = 0
    while True:
        try:
            gif.seek(frame)
            frame_path = os.path.join(output_folder, f'{frame}.png')
            gif.save(frame_path, 'PNG')
            print(f'Saved {frame_path}')
            frame += 1
        except EOFError:
            break

gif_path = input('Gif Path: ')
output_folder = 'output_frames'
gif_to_png(gif_path, output_folder)