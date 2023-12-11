import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.model import Sequential
from keras.layer import Dense

dataset = np.loadtxt('data.csv', delimiter=',')

x = dataset[:,0:8] # input features
y = dataset[:,8]    # output

scaler = StandardScaler()
x = scaler.fit_transform(x)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense( input_dim=8, activation='relu'))
model.add(Dense( 8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=100, batch_size=10)

loss, accuracy = model.evaluate(X_test, Y_test)