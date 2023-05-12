"""pip install SpeechRecognition and pip install pyAudio"""
import speech_recognition as sr
from pydub import AudioSegment


"""Преобразует все типы файла, которые поддерживает ffmpeg"""
def convertFileToWav(file_name, file_type):
    try:
        sound = AudioSegment.from_file(f"{file_name}.{file_type}", f"{file_type}")
        # Можно оставить, чтобы постоянно был один файл, так память меньше будет чище
        sound.export("new_file.wav", format="wav")
        # Или если нам надо сохранять все файлы, то можно оставить такое же название
        # sound.export(f"{file_name}.wav", format="wav")
    except Exception as e:
        print(e)


"""Основная функция"""
def main(file_name, language_file):
    sound = f'{file_name}.wav'
    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print('Преобразую аудиофайл в текс...')
        audio = r.listen(source)

        """Проверка на ошибки"""
        try:
            print(f"Текс из аудиофайла: {r.recognize_google(audio, language=f'{language_file}')}")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    convertFileToWav('test_name', 'mp3') # Указать имя файла и его тип
    main('new_file', 'ru-RU') # Указать имя файла, если у нас один файл, который сам себя переписывает и язык





