import json


class Memory:
    def memory(self, chat):
        file_path = r"C:\PROJECTS\AYRA_\ayra-jarvis\ayra_v3\MEMORY\history.json"

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []

        data.append(chat)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Memory updated!")
