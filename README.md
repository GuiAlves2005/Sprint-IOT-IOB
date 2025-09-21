# Projeto de Detecção Facial em Tempo Real (IOT & IOB)

## 1. Objetivo

Este projeto consiste em uma aplicação local (desktop) desenvolvida em Python que utiliza a biblioteca OpenCV e o classificador Haar Cascade para realizar a detecção facial de um usuário em tempo real através da webcam. O objetivo é demonstrar o funcionamento da tecnologia e o impacto de seus parâmetros no resultado final.

## 2. Como Executar

**Pré-requisitos:**
* Python 3.x
* Biblioteca OpenCV

**Instalação das Dependências:**
Abra seu terminal e instale a única dependência necessária com o seguinte comando:
```bash
pip install opencv-python
```

**Execução:**
1.  Clone este repositório.
2.  Navegue até a pasta do projeto pelo terminal.
3.  Certifique-se de que os arquivos `detector_facial.py` e `haarcascade_frontalface_default.xml` estão no mesmo diretório.
4.  Execute o script com o comando:
```bash
python detector_facial.py
```
5.  Uma janela com a imagem da sua webcam será aberta, mostrando os retângulos de detecção. Pressione a tecla 'q' para fechar a aplicação.

## 3. Parâmetros Ajustáveis

O script utiliza a função `detectMultiScale` do OpenCV, que possui parâmetros chave para ajustar a precisão e a velocidade da detecção. Os dois principais demonstrados são:

* `scaleFactor`: Este parâmetro define o quanto a imagem é redimensionada em cada passo da busca por faces. Um valor como **1.05** (mais próximo de 1) cria mais "camadas" de busca, aumentando a chance de encontrar faces, mas torna o processo mais lento. Um valor maior, como **1.3**, acelera a detecção, mas pode não detectar faces que estejam entre os "saltos" de escala.

* `minNeighbors`: Este parâmetro determina a qualidade da detecção. Ele especifica quantos retângulos vizinhos um candidato a face deve ter para ser considerado uma detecção válida. Um valor baixo (ex: **3**) pode gerar muitos "falsos positivos". Um valor mais alto (ex: **10**) exige uma confirmação mais forte, resultando em detecções mais confiáveis, mas pode ignorar faces reais.

## 4. Nota Ética Sobre o Uso de Dados Faciais

A tecnologia de reconhecimento facial é poderosa e carrega responsabilidades éticas significativas. O uso de dados faciais deve sempre priorizar a privacidade, o consentimento e a segurança do indivíduo. É crucial estar ciente dos vieses que podem existir em algoritmos pré-treinados, que muitas vezes apresentam menor precisão para certos grupos demográficos. Este projeto é estritamente educacional e não armazena nenhuma imagem ou dado biométrico.

## Link do vídeo
https://youtu.be/2r7o9fS36F4

## Integrantes do Grupo
Bruno Venturi Lopes Vieira - 99431
Guilherme Alves de Lima - 550433
Pedro Guerra - 99526
Leonardo de Oliveira Ruiz - 98901
