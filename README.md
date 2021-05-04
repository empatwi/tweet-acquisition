# Empatwi

## Tweet acquisition

Esse repositório contém o script necessário para a coleta de dados do Twitter utilizando Python 3.8 e a biblioteca Tweepy para manipulação da API do Twitter. 

Os dados coletados serão classificados posteriormente com a ajuda da nossa ferramenta de Crowdsourcing.

## Sobre

Primeiramente, foi necessário entrar em contato com o [suporte de desenvolvedor do Twitter](https://developer.twitter.com/) e solicitar uma conta com privilégios de desenvolvedor. Isso porque, apenas com esse nível de conta é possível acessar o Portal de Desenvolvedor do Twitter.
Após a solicitação ser aprovada, foi criado um projeto de aplicativo que gerou as chaves de API e os tokens de acesso mandatórios para a manipulação da API via código. No caso desse repositório, foram utilizadas a linguagem Python na versão 3.8 e a biblioteca [Tweepy](https://www.tweepy.org/).

## Estrutura

Dentro da pasta `src/twitter` encontram-se:

- O arquivo `settings.py` contém todas as variáveis de configuração e também possui acesso ao arquivo `.env` local, que abriga os valores das variáveis de ambiente sensiveis, como as chaves e os tokens utilizados para acessar a API do Twitter. Foi adicionada também nesse arquivo uma lista chamada `TRACKED_TOPICS` cujos valores são os tópicos desejados para filtrar a coleta de tweets;
- O arquivo `tweet_acquisition.py`, onde é feita a autenticação com a API do Twitter e são instanciados os objetos necessários para que a coleta de tweets seja realizada. Aqui os parâmetros de filtragem dos tweets também são especificados, onde os tweets devem conter pelo menos uma das palavras-chave definidas na lista `TRACKED_TOPICS` e devem ser em português;
- E o último, o arquivo `stream_listener.py` que abriga todas as regras de negócio da coleta de dados e montagem do csv. Esse script cria, abre e escreve no arquivo `files/raw_stream_output.csv` o conteúdo de tweets sem URLs, vídeos, GIFs (ou qualquer outro tipo de mídia), a data e hora em que foram postados, a localização do usuário que postou e as entidades do tweet (como menções, hashtags, etc).

Dentro da pasta `files` encontram-se:

- O primeiro arquivo com dados coletados não tratados, o `raw_stream_output.csv`;
- O arquivo Jupyter Notebook onde o csv raiz é tratado (remoção de tweets repetidos) e o novo DataFrame é salvo no próximo e último arquivo;
- O arquivo `filtered_stream_output.csv` que contém os dados coletados e tratados.

## Instruções

É necessário possuir Python 3.x, `pip` e qualquer gerenciador de ambiente virtual instalados para rodar o script.

1. Primeiramente, crie o ambiente virtual com o comando `python -m venv venv` no terminal.
2. Em seguida, ative o ambiente com o comando `venv\scripts\activate` (Windows) ou `source venv/bin/activate` (Linux).
3. Instale as dependências necessárias com o comando `pip install -r requirements.txt`.
4. Para rodar o script, navegue até a pasta `twitter` com `cd src/twitter` e execute o comando `python tweet_acquisition.py`.
5. Você pode interromper o streaming manualmente utilizando `Ctrl+C` no terminal.
6. O arquivo `raw_stream_output.csv` será gerado no diretório `files`.
7. Execute o notebook `csv_treatment.ipynb` para remover os tweets repetidos e gerar o novo arquivo `filtered_stream_output.py`.

## Desenvolvido por:
- [Fabiana Masini Garcia](https://www.linkedin.com/in/fabianamasini/)
- [Letícia Vigna Modenese Silva](https://www.linkedin.com/in/leticia-vigna/)
