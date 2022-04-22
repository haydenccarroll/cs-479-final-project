import csv
import numpy as np
import matplotlib.pyplot as plt

def read_in_csv(file_name):
    with open(file_name) as csvfile:
        next(csvfile)
        csv_reader = csv.reader(csvfile, delimiter=",")
        return list(csv_reader)

def run_analysis():
    # read in .csv file and convert the types to floats and bools as appropriate
    type_table = "float bool bool float bool float float bool float float bool float bool".split(' ')
    label_table = "age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time,DEATH_EVENT".split(',')
    data = read_in_csv("heart_failure_clinical_records_dataset.csv")
    for rowIndx, row in enumerate(data):
        for colIndx, point in enumerate(row):
            if type_table[colIndx] == "float":
                data[rowIndx][colIndx] = float(point)
            elif type_table[colIndx] == "bool":
                data[rowIndx][colIndx] = float(point)

    without_last_col = np.array([x[:-1] for x in data])


    for colIndx in range(len(data[0])-1):
        fig1, ax1 = plt.subplots()
        ax1.set_title(label_table[colIndx])
        ax1.boxplot(without_last_col[:,colIndx])
        plt.show()

if __name__ == "__main__":
    run_analysis()