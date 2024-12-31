import os
import json

class BaseDB:
    def __init__(self):
        self.basepath = 'data'
        self.filepath = '/'.join((self.basepath, self.filename))

    # def read(self):
    #     if not os.path.exists(self.filepath):
    #         print(f"File {self.filepath} is not available")
    #         return False
        
    #     with open(self.filepath, 'r') as file:
    #         raw = file.readline()
        
    #     if len(raw) > 0:
    #         data = json.loads(raw)
    #     else:
    #         data = []
    #     return data
    
    # def write(self,item):
    #     data = self.read()

    #     if data:
    #         data = data + item
    #     else:
    #         data = item
        
    #     with open(self.filepath, "w+") as file:
    #         file.write(json.dumps(data))

    def read(self):
        if not os.path.exists(self.filepath):
            print(f"File {self.filepath} is not available")
            return False

        data = []  # Initialize an empty list to store the JSON objects

        with open(self.filepath, 'r') as file:
            for line in file:  # Read the file line by line
                line = line.strip()  # Remove any leading/trailing whitespace

                if not line:
                    continue  # Check if the line is not empty
                try:
                    data.append(json.loads(line))  # Parse the JSON and add to the list
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e} - Line: {line}")

        return data
    
    def write(self,data):
        json_data = json.dumps(data)
        with open(self.filepath, "a") as file:
            file.write(json_data + "\n")



class BlockchainDB(BaseDB):
    def __init__(self):
        self.filename = 'blockchain'
        super().__init__()
    
    def lastBlock(self):
        data = self.read()
        
        if data:
            return data[-1]