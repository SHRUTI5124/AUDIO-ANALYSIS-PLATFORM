import librosa
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def classifications():            # Load the audio files and extract features
    audio_files = []
    genres = []
    moods = []
    for file_path in [r'static\audios\sunrise-anna-li-sky-wav-8476.mp3']:
        for file_path in [r'result.wav']:
            audio_files.append(librosa.load(file_path, duration=30)[0])
            genre = file_path.split('\\')[-2]
            mood = file_path.split('\\')[-1].split('_')[0]
            genres.append(genre)
            moods.append(mood)

    features = []
    for audio_file in audio_files:
        feature = librosa.feature.mfcc(y=audio_file, sr=22050)
        features.append(feature)

    # Encode the genre and mood labels
    genre_encoder = LabelEncoder()
    genre_labels = genre_encoder.fit_transform(genres)

    mood_encoder = LabelEncoder()
    mood_labels = mood_encoder.fit_transform(moods)

    # Scale the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(np.array(features))

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(scaled_features, genre_labels, test_size=0.2)

    # Build the model
    model = Sequential()
    model.add(Dense(256, input_shape=(scaled_features.shape[1],)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(genre_encoder.classes_)))
    model.add(Activation('softmax'))

    model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(lr=0.0001), metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, batch_size=32, epochs=50, validation_data=(X_test, y_test))

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    print('Test loss:', loss)
    print('Test accuracy:', accuracy)

    # Predict the genre and mood labels for new audio files
    new_audio_file = librosa.load('path/to/new_audio.wav', duration=30)[0]
    new_feature = librosa.feature.mfcc(y=new_audio_file, sr=22050)
    new_scaled_feature = scaler.transform(np.array([new_feature]))
    predicted_genre = genre_encoder.inverse_transform(model.predict_classes(new_scaled_feature))
    predicted_mood = mood_encoder.inverse_transform(model.predict_classes(new_scaled_feature))

    print('Predicted genre:', predicted_genre[0])
    print('Predicted mood:', predicted_mood[0])

if __name__=='__main__':
    classifications()
