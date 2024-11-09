class Univariate:
    def QuanQual(dataset):
        Quan = []
        Qual = []
        for columnName in dataset.columns:
            if dataset[columnName].dtypes == 'O':
                Qual.append(columnName)
            else:
                Quan.append(columnName)
        return Quan, Qual
