class ClassifierResult:
    def __init__(self, result, confidence):
        self.__result = result
        self.__confidence = confidence

    @property
    def result(self) -> str:
        return self.__result

    @property
    def confidence(self) -> float:
        return self.__confidence

    @property
    def to_dict(self):
        return {
            'result': self.__result,
            'confidence': self.__confidence
        }

    @classmethod
    def from_dict(cls, dct) -> 'ClassifierResult':
        for field in ['result', 'confidence']:
            if field not in dct:
                raise ValueError("field '{0}' not in dict".format(field))

        return cls(dct['result'], dct['confidence'])
