def my_model(img_size=64,channels=1):
    model = Sequential()
    input_shape = (img_size,img_size,channels)
    
    model.add(Conv2D(32, (3, 3), input_shape=input_shape,activation='relu', padding='same'))
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
    #model.add(Dropout(0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3),activation='relu',padding='same'))
    model.add(Conv2D(64, (3, 3),activation='relu',padding='same'))
    #model.add(Dropout(0.2))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    #model.add(Conv2D(128, (3, 3),activation='relu',padding='same'))
    #model.add(Dropout(0.2))
    #model.add(MaxPooling2D(pool_size=(2, 2)))
   
    model.add(Flatten())
    
    model.add(Dense(128,activation='relu'))
    model.add(Dropout(0.5))
    
    #model.add(Dense(128,activation='relu'))
    #model.add(Dropout(0.5))
    
    model.add(Dense(10))
    model.add(Activation('softmax'))
    
    from keras import optimizers
    #sgd = optimizers.SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'],optimizer='adam')
    return model
  
model=my_model()