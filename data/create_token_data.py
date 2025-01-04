from model.token_model import TokenModel


valid_data = (TokenModel('admin', 'password123'),)

invalid_data = (TokenModel('бобр', 'курва'), TokenModel(0, 1))
