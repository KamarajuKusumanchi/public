import pandas as pd

def get_items_in_fridge():
    # Todo: hard coding for now. Make it generic later.
    df = pd.DataFrame({'items': ['Lettuce', 'Broccoli']})
    return df

def what_to_eat():
    fridge = get_items_in_fridge()
    to_eat = fridge['items'].sample()
    return to_eat

def main():
    to_eat = what_to_eat()
    print(to_eat)

if __name__ == '__main__':
    main()
