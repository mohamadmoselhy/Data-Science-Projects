from src.utils import save_model_and_scaler,prepare_and_train_knn_model,drop_columns,read_csv_file,calculate_regression_metrics



DataSetPath="D:\My drive\Course\Data Science\Models Testing\Data-Science-Projects\KNN\Iris DateSet\2\Iris.csv"

df=read_csv_file(DataSetPath)

df=drop_columns(df,'id')


x=drop_columns(df,'species')
y=df['species']

MyScaler, KNNModel, x_train, x_test, y_train, y_test=prepare_and_train_knn_model(x,y,shuffle=True, random_state=0, n_neighbors=5)

y_pred = KNNModel.predict(MyScaler.transform(x_test))

mse, mae, r2=calculate_regression_metrics(y_test,y_pred)