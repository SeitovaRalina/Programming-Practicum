from model.token_model import TokenModel


valid_data = [TokenModel('admin', 'password123')]
valid_ids = ['Valid username and password']

invalid_data = [
    TokenModel('', 'password123'),
    TokenModel('admin', ''), 
    TokenModel('invalidUser', 'wrongPassword'),
    TokenModel('', ''),             
    TokenModel(0, 1),
    TokenModel(True, False),       
    TokenModel(password='password123'),      
    TokenModel(username='admin'),             
    TokenModel(),                          
]
invalid_ids = [
    'Empty username',
    'Empty password',
    'Both parameters are invalid strings',
    'Both parameters are empty',
    'Both parameters are invalid integers',
    'Both parameters are invalid booleans',
    'Missing username',
    'Missing password',
    'Both parameters are missing',
]
