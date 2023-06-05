import pickle


class PickleOperations:

    def load_data(self, filename):
        try:
            with open(filename, "rb") as file:
                data = file.read()
        except FileNotFoundError:
            data = None
        return data

    def save_data(self, data, filename="data.pkl"):
        current_data = self.load_data(filename)
        if current_data:
            data = current_data + data
        with open(filename, "wb") as file:
            file.write(data)
        return True
