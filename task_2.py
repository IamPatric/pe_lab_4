
import pickle
from operator import itemgetter

def list_sorting(list_, index=0):
    return sorted(list_, key=itemgetter(index))


class FileProcessing:
    @classmethod
    def make_list_from_file(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
        return [x.split(';') for x in data.split('\n')]

    @classmethod
    def write_csv(self, data, filename, limiter=';'):
        data = '\n'.join([limiter.join(x) for x in data])
        with open(filename, 'w', encoding='utf=8') as f:
            f.write(data)

    @classmethod
    def write_pickle(self, data, filename):
        with open(filename, 'wb') as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def read_pickle(self, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)