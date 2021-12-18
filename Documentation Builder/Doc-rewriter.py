import json
Unknown = 0
AutoFilled = 0
with open("ENTRIES.json", "r") as Input:
    Stored = {}
    readDATA = json.load(Input)
    Stored.update(readDATA)
    with open("OUTPUT.txt", "w") as Output:
        Output.write("")
        for h in range(len(Stored)):
            for i in range(26): # 26 = num of files
                with open(fr"Files\1 ({i+1}).py", "r") as file:
                    data = file.readlines()

                counter = 0
                Indent = False
                int_indent = 7
                
                Skippy = 0

                Indent = 0
                for j in range(len(data)):
                    Indent = 0
                    Doc = ""
                    for i in range(len(data[Skippy])):
                        if data[Skippy][i] == " ":
                            Indent += 1
                        else:
                            break
                    Indent = Indent/4
                    try:
                        if data[Skippy].strip() == "":
                            Output.write("")
                        else:
                            counter += 1
                            temp = data[Skippy].strip()
                                
                            if data[Skippy][:len('if not __name__ == "__main__":')].strip() == 'if not __name__ == "__main__":':
                                Output.write("\n\n.. note::\n")
                                Output.write("   For information on this consult the above guide\n")
                                Output.write("\n        "+str(counter)+": ``"+str(temp)+"``\n")
                                #print("\n        "+str(counter)+": ``"+str(temp)+"``\n")
                                AutoFilled += 1
                                if data[Skippy+1][:len('    print("Started <Pycraft_')].strip() == 'print("Started <Pycraft_':
                                    temp = data[Skippy+1].strip()
                                    counter += 1
                                    #print("\n        "+str(counter)+": ``¬ "+str(temp)+"``\n")
                                    Output.write("\n        "+str(counter)+": ``"+str(temp)+"``\n")
                                    AutoFilled += 1
                                    if data[Skippy+2][:len('    class ')].strip() == 'class':
                                        temp = data[Skippy+2].strip()
                                        counter += 1
                                        Output.write("\n        "+str(counter)+": ``¬ "+str(temp)+"``\n")
                                        #print("\n        "+str(counter)+": ``"+str(temp)+"``\n")
                                        AutoFilled += 1
                                        if data[Skippy+3][:len('        def __init__(self):')].strip() == 'def __init__(self):':
                                            temp = data[Skippy+3].strip()
                                            counter += 1
                                            Output.write("\n        "+str(counter)+": ``¬ ¬ "+str(temp)+"``\n")
                                            #print("\n        "+str(counter)+": ``"+str(temp)+"``\n")
                                            AutoFilled += 1
                                            if data[Skippy+4][:len('            pass')].strip() == 'pass':
                                                temp = data[Skippy+4].strip()
                                                counter += 1
                                                Output.write("\n        "+str(counter)+": ``¬ ¬ ¬ "+str(temp)+f"``\n")
                                                #print("\n        "+str(counter)+": ``¬ ¬ ¬ "+str(temp)+"``\n")
                                                Skippy += 4
                                                AutoFilled += 1
                                                
                            elif data[Skippy+1][:len('       print("You need to run this as part of Pycraft")')].strip() == 'print("You need to run this as part of Pycraft")':
                                Output.write("\n\n.. note::\n")
                                Output.write("   For information on this consult the above guide\n")
                                Output.write(f'\n        {counter}: ``else:``\n\n        {counter+1}: ``¬ print("You need to run this as part of Pycraft")``\n\n        {counter+2}: ``¬ import tkinter as tk``\n\n        {counter+3}: ``¬ from tkinter import messagebox``\n\n        {counter+4}: ``¬ root = tk.Tk()``\n\n        {counter+5}: ``¬ root.withdraw()``\n\n        {counter+6}: ``¬ messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the \'main.py\' file")``\n\n        {counter+7}: ``¬ quit()``\n\n')
                                AutoFilled += 8
                                break
                            else:
                                try:
                                    EOL = Stored[temp]
                                    AutoFilled += 1
                                except Exception as Message:
                                    Unknown += 1
                                    INPUT = str(input(f"< | > {temp} < | > UNKNOWN; Enter documentation here: "))
                                    Stored.update({temp: INPUT})
                                    with open("ENTRIES.json", "w") as lib:
                                        json.dump(Stored, lib)
                                        
                                Tabs = "¬ "*int(Indent)
                                Output.write(str(counter)+": ``"+Tabs+str(temp)+f"`` {EOL}\n")
                        int_indent -= 1
                        Skippy += 1
                        Output.write("\n")
                    except Exception as error:
                        print(error)
            Output.write("\n")

print(Unknown, "Lines are unknown at present")
print("Autofilled:", AutoFilled, f"lines, so ~{int((100/(Unknown+AutoFilled))*AutoFilled)}% complete")

