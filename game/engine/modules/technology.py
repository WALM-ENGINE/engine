def dialog_window_animation(engine_root, iteration_function, font, x_dialog_icon, x_dialog_frame, y_dialog_frame, x_dialog_text, text_seek, dialog_frame, dialog_icon, time, sound):
    global animation_text

    for i in range(1, len(text_seek[0]) + 1):

        if iteration_function() == 'pause':
            return 'pause'

        engine_root.draw(dialog_frame, x_dialog_frame, y_dialog_frame)
        engine_root.draw(dialog_icon, x_dialog_icon, y_dialog_frame + 40)

        engine_root.draw(engine_root.load_text(font, text_seek[0][:i]), x_dialog_text, y_dialog_frame + 40)

        if engine_root.walmen_config.enable_speak == True:
            engine_root.walmen_const.mixer.Sound(sound).play()

        if i == len(text_seek[0]):

            for i in range(1, len(text_seek[1]) + 1):

                if iteration_function() == 'pause':
                    return 'pause'

                engine_root.draw(dialog_frame, x_dialog_frame, y_dialog_frame)
                engine_root.draw(dialog_icon, x_dialog_icon, y_dialog_frame + 40)
                
                engine_root.draw(engine_root.load_text(font, text_seek[0]), x_dialog_text, y_dialog_frame + 40)
                engine_root.draw(engine_root.load_text(font, text_seek[1][:i]), x_dialog_text, y_dialog_frame + 80) 

                if engine_root.walmen_config.enable_speak == True:
                    engine_root.walmen_const.mixer.Sound(sound).play()

                if i == len(text_seek[1]):
                    for i in range(1, len(text_seek[2]) + 1):

                        if iteration_function() == 'pause':
                            return 'pause'

                        engine_root.draw(dialog_frame, x_dialog_frame, y_dialog_frame)
                        engine_root.draw(dialog_icon, x_dialog_icon, y_dialog_frame + 40)
                        
                        engine_root.draw(engine_root.load_text(font, text_seek[0]), x_dialog_text, y_dialog_frame + 40)
                        engine_root.draw(engine_root.load_text(font, text_seek[1]), x_dialog_text, y_dialog_frame + 80)
                        engine_root.draw(engine_root.load_text(font, text_seek[2][:i]), x_dialog_text, y_dialog_frame + 120) 

                        if engine_root.walmen_config.enable_speak == True:
                            engine_root.walmen_const.mixer.Sound(sound).play()

                        if i == len(text_seek[2]):
                            for i in range(1, len(text_seek[3]) + 1):

                                if iteration_function() == 'pause':
                                    return 'pause'

                                engine_root.draw(dialog_frame, x_dialog_frame, y_dialog_frame)
                                engine_root.draw(dialog_icon, x_dialog_icon, y_dialog_frame + 40)
                                
                                engine_root.draw(engine_root.load_text(font, text_seek[0]), x_dialog_text, y_dialog_frame + 40)
                                engine_root.draw(engine_root.load_text(font, text_seek[1]), x_dialog_text, y_dialog_frame + 80)
                                engine_root.draw(engine_root.load_text(font, text_seek[2]), x_dialog_text, y_dialog_frame + 120)
                                engine_root.draw(engine_root.load_text(font, text_seek[3][:i]), x_dialog_text, y_dialog_frame + 160)

                                if engine_root.walmen_config.enable_speak == True:
                                    engine_root.walmen_const.mixer.Sound(sound).play()

                                if i == len(text_seek[3]):
                                    for i in range(1, len(text_seek[4]) + 1):

                                        if iteration_function() == 'pause':
                                            return 'pause'

                                        engine_root.draw(dialog_frame, x_dialog_frame, y_dialog_frame)
                                        engine_root.draw(dialog_icon, x_dialog_icon, y_dialog_frame + 40)
                                        
                                        engine_root.draw(engine_root.load_text(font, text_seek[0]), x_dialog_text, y_dialog_frame + 40)
                                        engine_root.draw(engine_root.load_text(font, text_seek[1]), x_dialog_text, y_dialog_frame + 80)
                                        engine_root.draw(engine_root.load_text(font, text_seek[2]), x_dialog_text, y_dialog_frame + 120)
                                        engine_root.draw(engine_root.load_text(font, text_seek[3]), x_dialog_text, y_dialog_frame + 160)
                                        engine_root.draw(engine_root.load_text(font, text_seek[4][:i]), x_dialog_text, y_dialog_frame + 200)

                                        if engine_root.walmen_config.enable_speak == True:
                                            engine_root.walmen_const.mixer.Sound(sound).play()

                                        if i == len(text_seek[4]):
                                            return True                  

                                        engine_root.walmen_time.sleep(time)
                                        engine_root.update_teck_screen()                    
                                engine_root.walmen_time.sleep(time)
                                engine_root.update_teck_screen()                    
                        engine_root.walmen_time.sleep(time)
                        engine_root.update_teck_screen()                      
                engine_root.walmen_time.sleep(time)
                engine_root.update_teck_screen()
        engine_root.walmen_time.sleep(time)
        engine_root.update_teck_screen()

def adaptive_text(button_x, button_width, font_size, text):
    return (button_x+button_width/2)-((font_size/2)*(len(text)/2))

def self_dialog_window(engine_root, dialog_window, dialog_icon, dialog_font, text):
    engine_root.draw(dialog_window, 37, 400)
    engine_root.draw(dialog_icon, 130, 440)
    engine_root.draw(engine_root.load_text(dialog_font, text[0]), 300, 440)
    engine_root.draw(engine_root.load_text(dialog_font, text[1]), 300, 480) 
    engine_root.draw(engine_root.load_text(dialog_font, text[2]), 300, 520) 
    engine_root.draw(engine_root.load_text(dialog_font, text[3]), 300, 560) 
    engine_root.draw(engine_root.load_text(dialog_font, text[4]), 300, 600) 

    