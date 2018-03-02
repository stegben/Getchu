import pickle as pkl

from tqdm import tqdm
from getchu import URL, Getchu


def main():
    getchu = Getchu()
    images = []
    with open('erogame_list.tsv', 'r') as f:
        f.readline()
        for line in tqdm(f):
            data = line.rstrip().split()
            try:
                item = getchu.item('http://' + data[-1])
                if 'image' in item:
                    images = images + item['image']
                    # print(item)
            except:
                print(data[-1])
    import ipdb; ipdb.set_trace()
    with open('eroge_character_imglist.pkl', 'wb') as fw:
        pkl.dump(images, fw)
    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()
