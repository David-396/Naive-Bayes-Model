from static import get_max_classify_from_csv


class TestAccuracy:
    def __init__(self, classifier):
        self.classifier = classifier            # the object that will be used for classify the data

    def test_accuracy(self, data_for_test):
        correct_classes = data_for_test.iloc[:,-1]
        res = self.classifier.csv_classified(data_for_test)

        if res:
            count_res = len(res)
            res_class_from_model = get_max_classify_from_csv(res)
            count_correct = 0

            for i in range(len(correct_classes)):
                if correct_classes.iloc[i] == res_class_from_model[i]:
                    count_correct += 1
            return (count_correct / count_res) * 100

        print('--- wrong input ---')
        return None
