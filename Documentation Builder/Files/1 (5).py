if not __name__ == "__main__":
    print("Started <Pycraft_CharacterDesigner>")
    class GenerateCharacterDesigner:
        def __init__(self):
            pass

        def CharacterDesigner(self):
            try:
                self.Display.fill(self.BackgroundCol) 
                self.mod_Pygame__.display.flip()
                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
                InfoTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)

                TitleFont = MainTitleFont.render("Pycraft", self.aa, self.SecondFontCol)
                TitleWidth = TitleFont.get_width()

                AchievementsFont = InfoTitleFont.render("Character Designer", self.aa, self.FontCol)
                tempFPS = self.FPS

                while True:
                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()

                    if realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                    self.eFPS = self.clock.get_fps()
                    self.aFPS += self.eFPS 
                    self.Iteration += 1
                    
                    tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)

                    for event in self.mod_Pygame__.event.get(): 
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE): 
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None
                        elif event.type == self.mod_Pygame__.KEYDOWN: 
                            if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: 
                                self.Devmode += 1 
                            if event.key == self.mod_Pygame__.K_q:
                                self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)
                            if event.key == self.mod_Pygame__.K_F11:
                                self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)
                            if event.key == self.mod_Pygame__.K_x: 
                                self.Devmode = 1 

                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Character Designer")
                            
                    self.Display.fill(self.BackgroundCol)

                    cover_Rect = self.mod_Pygame__.Rect(0, 0, 1280, 90)
                    self.mod_Pygame__.draw.rect(self.Display, (self.BackgroundCol), cover_Rect)
                    self.Display.blit(TitleFont, ((realWidth-TitleWidth)/2, 0))
                    self.Display.blit(AchievementsFont, (((realWidth-TitleWidth)/2)+55, 50))

                    Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, DataFont)
                    if not Message == None:
                        return Message
                    self.mod_Pygame__.display.flip() 
                    self.clock.tick(tempFPS)
            except Exception as Message:
                return Message
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()