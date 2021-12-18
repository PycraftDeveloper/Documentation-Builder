if not __name__ == "__main__":
    print("Started <Pycraft_StartupAnimation>")
    class GenerateStartupScreen:
        def __init__(self):
            pass
                        
        def Start(self):
            try:
                self.Display.fill(self.BackgroundCol)
                self.mod_Pygame__.display.flip()
                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Welcome")
                PresentsFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                PycraftFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                NameFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 45)

                NameText = NameFont.render("Tom Jebbo", True, self.FontCol)
                NameTextWidth = NameText.get_width()
                NameTextHeight = NameText.get_height()

                PresentsText = PresentsFont.render("presents", True, self.FontCol)

                PycraftText = PycraftFont.render("Pycraft", True, self.FontCol)
                PycraftTextWidth = PycraftText.get_width()
                PycraftTextHeight = PycraftText.get_height()

                iteration = 0
                clock = self.mod_Pygame__.time.Clock()
                if self.RunFullStartup == True:
                    while iteration <= (60*3):
                        self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()
                        self.Display.fill(self.BackgroundCol)
                        self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))
                        iteration += 1

                        if self.realWidth < 1280:
                            self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                        if self.realHeight < 720:
                            self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)
                        
                        self.mod_Pygame__.display.flip()
                        clock.tick(60)
                        for event in self.mod_Pygame__.event.get():
                            if event.type == self.mod_Pygame__.QUIT:
                                self.Stop_Thread_Event.set()

                                self.Thread_StartLongThread.join()
                                self.Thread_AdaptiveMode.join()
                                self.Thread_StartLongThread.join()
                                self.mod_Pygame__.quit()
                                self.mod_Sys__.exit("Thanks for playing")
                                quit()
                    iteration = 0

                    while iteration <= (60*2):
                        self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()
                        self.Display.fill(self.BackgroundCol)
                        self.Display.blit(NameText, ((self.realWidth-NameTextWidth)/2, (self.realHeight-NameTextHeight)/2))
                        self.Display.blit(PresentsText, ((((self.realWidth-NameTextWidth)/2)+120), ((self.realHeight-NameTextHeight)/2)+30))
                        iteration += 1

                        if self.realWidth < 1280:
                            self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                        if self.realHeight < 720:
                            self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                        self.mod_Pygame__.display.flip()
                        clock.tick(60)
                        for event in self.mod_Pygame__.event.get():
                            if event.type == self.mod_Pygame__.QUIT:
                                self.Stop_Thread_Event.set()

                                self.Thread_StartLongThread.join()
                                self.Thread_AdaptiveMode.join()
                                self.Thread_StartLongThread.join()
                                self.mod_Pygame__.quit()
                                self.mod_Sys__.exit("Thanks for playing")
                                quit()

                    iteration = 0

                while iteration <= (60*3):
                    self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()
                    self.Display.fill(self.BackgroundCol)
                    self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, (self.realHeight-PycraftTextHeight)/2))
                    iteration += 1

                    if self.realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if self.realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                    self.mod_Pygame__.display.flip()
                    clock.tick(60)
                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT:
                            self.Stop_Thread_Event.set()

                            self.Thread_StartLongThread.join()
                            self.Thread_AdaptiveMode.join()
                            self.Thread_StartLongThread.join()

                            self.mod_Pygame__.quit()
                            self.mod_Sys__.exit("Thanks for playing")
                            quit()

                y = 0
                while True:
                    self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()
                    self.Display.fill(self.BackgroundCol)
                    self.Display.blit(PycraftText, ((self.realWidth-PycraftTextWidth)/2, ((self.realHeight-PycraftTextHeight)/2)-y))
                    y += 2

                    if self.realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if self.realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                    self.mod_Pygame__.display.flip()
                    clock.tick(60)
                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT:
                            self.Stop_Thread_Event.set()

                            self.Thread_StartLongThread.join()
                            self.Thread_AdaptiveMode.join()
                            self.Thread_StartLongThread.join()

                            self.mod_Pygame__.quit()
                            self.mod_Sys__.exit("Thanks for playing")
                            quit()
                    if ((self.realHeight-PycraftTextHeight)/2)-y <= 0:
                        self.RunFullStartup = False
                        return None
            except Exception as Message:
                self.RunFullStartup = False
                return Message
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()