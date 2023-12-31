# registro:
import pandas as pd


def load_db():
    file_path = 'users.csv'
    try:
        print('csv loaded successfully!')
        df = pd.read_csv(file_path)
    except:
        print('Creating the csv file...')
        data = {
            'User': [],
            'Password': []
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        df = pd.read_csv(file_path)
    return df


def create_user():
    df = load_db()
    dictionary = df.to_dict(orient='records')
    # INTENTO CREAR USUARIO
    user_name = input('Create your username:')
    # CHECKEO SI EL USUARIO EXISTE EN MI DB
    for users in dictionary:
        if users.get('User') == user_name:
            print('This username already exists')
            return
    user_password = input('Create your password:')
    # ALMACENO EL USUARIO
    new_user = {
        'User': user_name,
        'Password': user_password,
    }
    new_user_df = pd.DataFrame([new_user])
    df = pd.concat([df, new_user_df], ignore_index=True)
    df.to_csv('users.csv', index=False)
    print('User created successfully!')
    return df
    # print(db)


def login():
    df = load_db()
    user_name = input('Enter your username:')
    dictionary = df.to_dict(orient='records')
    for users in dictionary:
        if users.get('User') == user_name:
            user_password = input('Enter your password:')
            if users.get('Password') == user_password:
                print('You have logged in successfully!')
            else:
                print('Invalid password')
            return
    else:
        print('User not found')
    return


def run_program():
    while True:
        selector = int(input('0: Create a new user\n 1: Log in\n 2: Exit \n'))
        if selector > 2:
            print('Not allowed. Please be sure to type the correct number')
        if selector == 0:
            create_user()
        if selector == 1:
            login()
        if selector == 2:
            print('Exiting the program...')
            return False


run_program()
