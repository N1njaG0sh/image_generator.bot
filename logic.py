import http.client
from config import API
from deep_translator import MyMemoryTranslator

def generate_image(promt, image_path = 'downloaded_file.jpg', height = 1024, width = 1024, seed = 0, quality = 'medium'):
    promt = MyMemoryTranslator(source='ru-RU', target='en-GB').translate(promt)
    conn = http.client.HTTPSConnection("gen.pollinations.ai")

    headers = {
    "Authorization": f"Bearer {API}"
    }

    conn.request(
        "GET",
        f"/image/{promt.replace(' ','%20')}?model=tongyi-mai%2Fz-image-turbo&width={width}&height={height}&seed={seed}&quality={quality}",
        headers=headers,
    )

    response = conn.getresponse()
    with open(image_path, "wb") as f:  # Укажите правильное расширение файла
        f.write(response.read())
    print("Файл успешно сохранен!")

    conn.close()
    return image_path

if __name__ == '__main__':
    generate_image('закат в японии на горе фудзи')