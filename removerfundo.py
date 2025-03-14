import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Definir caminhos das pastas
input_path = "input/imagem.png"  # Caminho da imagem de entrada
output_path = "output/imagem_sem_fundo.png"  # Caminho para salvar a imagem processada

# Criar a pasta de saída se não existir
os.makedirs("output", exist_ok=True)

# Carregar a imagem
imagem = cv2.imread(input_path)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converter para RGB

# Criar uma máscara inicial
mask = np.zeros(imagem.shape[:2], np.uint8)

# Criar os modelos de fundo e frente exigidos pelo GrabCut
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Definir a área do primeiro plano manualmente (ajuste conforme necessário)
rect = (50, 50, imagem.shape[1] - 100, imagem.shape[0] - 100)  # (x, y, largura, altura)

# Aplicar o GrabCut
cv2.grabCut(imagem, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Criar uma máscara onde o fundo é 0 e o primeiro plano é 1
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Aplicar a máscara na imagem original
imagem_resultado = imagem_rgb * mask2[:, :, np.newaxis]

# Salvar a imagem processada sem fundo
cv2.imwrite(output_path, cv2.cvtColor(imagem_resultado, cv2.COLOR_RGB2BGR))

print(f"Imagem salva em: {output_path}")

# Mostrar a imagem resultante (opcional)
plt.figure(figsize=(10, 5))
plt.imshow(imagem_resultado)
plt.axis("off")
plt.show()
