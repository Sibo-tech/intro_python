import random


def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')


def get_input():
    return input().lower()


def main():
    keywords_and_response = {'crashed': 'Are the drivers up to date?',
                'blue': 'Ah, the blue screen of death. And then what happened?',
                'hacked': 'You should consider installing anti-virus software.',
                'bluetooth': 'Have you tried mouthwash?',
                'windows': 'Ah, I think I see your problem. What version?',
                'apple': 'You do mean the computer kind?',
                'spam': 'You should see if your mail client can filter messages.',
                'connection': 'Contact Telkom.'}

    welcome()
    query = get_input()
    Keywords = {'crashed', 'blue', 'hacked', 'bluetooth', 'windows', 'apple', 'spam', 'connection'}

    while (not query == 'quit'):
        query_to_list = query.split()
        for i in range(0, (len(query_to_list))):
            if query_to_list[i] in Keywords:
                print(keywords_and_response[query_to_list[i]])
                break
            elif i == (len(query_to_list) - 1):
                print('Curious, tell me more.')

        query = get_input()


if __name__ == '__main__':
    main()