from models import Base

def list_models_and_table_names():
    model_info = []
    for model in Base.__subclasses__():
        model_name = model.__name__
        table_name = model.__tablename__ if hasattr(model, '__tablename__') else 'No table name'
        model_info.append((model_name, table_name))
    return model_info

if __name__ == "__main__":
    model_info = list_models_and_table_names()
    for model_name, table_name in model_info:
        print(f"Model Name: {model_name}, Table Name: {table_name}")

