import pandas as pd
class House:
    # open the first file, go through houses
    file = pd.read_csv("wijk1_huizen.csv")
    frame = pd.DataFrame(file)

    def __init__(self, x, y, output, connection):
        self.x = x 
        self.y = y 
        self.output = output
        self.connection = connection # (bool)
        
    # def coordinaten(self):
    #     file = pd.read_csv("wijk1_huizen.csv")
    #     frame = pd.DataFrame(file)
    #     X_axis = frame["x"]
    #     Y_axis = frame["y"]
        
    #     print(X_axis)
    #     for x in X_axis:
    #         self.X_coordinate = X_axis[x]
        
    #     for y in Y_axis:
    #         self.Y_coordinate = Y_axis[y]
    #     coordinate = [self.X_coordinate, self.Y_coordinate]
    #     return coordinate


    def X(self):


        file = pd.read_csv("wijk1_huizen.csv")
        frame = pd.DataFrame(file)
        # print(frame)
        X_axis = frame["x"]
        print(X_axis)
        for x in X_axis:
            X_coordinate = x
            print(X_coordinate)
        return X_coordinate


    def Y(self):
        file = pd.read_csv("wijk1_huizen.csv")
        frame = pd.DataFrame(file)
        Y_axis = frame["y"]
        for y in Y_axis:
            Y_coordinate = y
        return Y_coordinate


    def Output(self):
        file = pd.read_csv("wijk1_huizen.csv")
        frame = pd.DataFrame(file)
        max_output = frame["max. output"]

        for z in max_output:
            output = z
        return output
         