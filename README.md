
# Desafio Técnico – Company Hero

## Descrição
Este projeto é um serviço que sugere playlists musicais com base na temperatura atual da cidade fornecida. Utiliza a API do OpenWeatherMap para obter a temperatura e a API do Spotify para recuperar as playlists correspondentes.

## Justificativa para o Padrão de API

Escolhi o padrão REST para a API devido à sua simplicidade e ampla aceitação no mercado. O REST é um padrão de arquitetura que utiliza HTTP para comunicação, facilitando a integração com outros sistemas e serviços. A escolha por REST proporciona uma abordagem intuitiva e fácil de entender para o desenvolvimento de APIs, além de garantir compatibilidade com diversas ferramentas e plataformas.

## Justificativa para a Linguagem de Programação e Frameworks

### Linguagem de Programação: Python
A escolha do Python se deu pela sua simplicidade, legibilidade e vasto ecossistema de bibliotecas. Python é uma linguagem de alto nível que permite o desenvolvimento rápido e eficiente, tornando-a ideal para protótipos e projetos que precisam de flexibilidade e fácil manutenção.

### Framework: FastAPI

Optei por utilizar o FastAPI devido à sua capacidade de criar APIs de alta performance com menos código. FastAPI é um framework moderno que oferece uma excelente experiência de desenvolvimento com suporte nativo para validação de dados, documentação automática e operações assíncronas. Sua natureza enxuta permite adicionar funcionalidades de maneira modular, conforme necessário, facilitando o desenvolvimento e a escalabilidade.

### Ferramenta: Docker
A utilização do Docker foi escolhida para garantir a portabilidade e consistência da aplicação em diferentes ambientes. Com Docker, a aplicação é encapsulada em um contêiner que inclui todas as dependências e configurações necessárias para a execução, o que reduz o risco de problemas relacionados a diferenças entre ambientes de desenvolvimento e produção. Além disso, o Docker facilita o processo de deploy, permitindo que a aplicação seja facilmente movida e executada em diferentes servidores sem a necessidade de ajustes complexos.

## Uso de Serviços de Terceiros

### API do Spotify

A API do Spotify foi escolhida para fornecer playlists musicais baseadas em diferentes gêneros. Ela foi selecionada por ser uma plataforma popular e amplamente usada para serviços de streaming de música, com uma API bem documentada e recursos que atendem às necessidades do projeto.

## API do OpenWeatherMap

A API do OpenWeatherMap foi utilizada para obter a temperatura atual da cidade fornecida. Essa API foi selecionada pela sua abrangência e facilidade de uso, além de oferecer informações climáticas detalhadas com uma documentação clara. O OpenWeatherMap atende às necessidades do projeto de forma eficiente e confiável.
## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/UeresWally/desafio_hero
```

Entre no diretório do projeto

```bash
  cd desafio_hero
```

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`WEATHER_API_KEY=sua_chave_weather`

`SPOTIFY_CLIENT_ID=seu_spotify_client_id`

`SPOTIFY_CLIENT_SECRET=seu_spotify_secret_client`

### Caso sua máquina não consiga rodar o docker.
- Crie um virtual enviroment com python e ative-o

```bash
  virtualenv env
  source /env/bin/activate
```

- Instale as dependencias com o enviroment ativado

```bash
  pip install -r requirements.txt
```
- Execute o seguinte comando para rodar sua aplicação
```bash
  uvicorn app.main:app --reload
```
Pronto sua aplicação estará rodando na porta 8000

### Caso tenha o docker instalado
- Faça o build da sua aplicação
```bash
  docker compose build
```
- Inicie o serviço com
```bash
  docker compose up
```

# Deployment

## 1. Documentação do Processo de Deployment

### 1.1 Preparar a Instância EC2

#### Criar Instância EC2

1. Acesse o AWS Management Console.
2. Vá para o serviço EC2 e inicie uma nova instância.
3. Escolha uma Amazon Machine Image (AMI), como a Amazon Linux 2 ou Ubuntu.
4. Selecione o tipo de instância apropriado com base nas necessidades de sua aplicação (por exemplo, t2.micro para testes).

#### Configurar o Grupo de Segurança

1. Configure o grupo de segurança da instância para permitir tráfego nas portas 80 (HTTP) e 443 (HTTPS).
2. Adicione uma regra para permitir SSH na porta 22.

### 1.2 Configurar o Servidor

#### Conectar à Instância via SSH

Pelo console da AWS você pode acessar o terminal da sua maquina EC2

#### Instalar e Configurar Docker

Para instalar o docker na sua maquina você pode acompanhar o passo a passo pelo link a seguir

https://docs.docker.com/engine/install/ubuntu/

#### Instalar e configurar nginx

Primeiro, atualize a lista de pacotes e o sistema:

```bash
sudo apt update
sudo apt upgrade
```
Instale o NGINX usando o gerenciador de pacotes apt:

```
sudo apt install nginx
```

Verifique o status do nginx:

```sudo systemctl status nginx ```

Configure o nginx para o seu sistema criando uma configuração com o seguinte comando:

``` sudo nano /etc/nginx/sites-available/meusite ```

e adicione a seguinte configuração

``` 
server {
        listen 80;
        server_name endereço ipv4_sua_maquina;
        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
        }
}
```
Reinicie o NGINX para aplicar as mudanças:

``` 
sudo systemctl restart nginx
```

### Rodando a aplicação no Servidor

clone o projeto para dentro da sua máquina

``` git clone https://github.com/UeresWally/desafio_hero.git```

Acesse o repositório baixado e configure o .env conforme a instrução para executar o projeto no seu ambiente local

build e rode sua aplicação com os comandos:

```
docker compose build
docker compose up -d
```

Para Testar se funcionou acesse:

http://endereço_ipv4_sua_maquina:docs

## Justificativa Tecnologias

### 2.1 Amazon EC2
- **Flexibilidade e Controle**: EC2 fornece um ambiente flexível e escalável para executar sua aplicação, permitindo que você escolha a AMI e o tipo de instância adequados para suas necessidades.
- **Custo**: O EC2 oferece várias opções de preços, incluindo instâncias gratuitas e pagas conforme o uso.

### 2.2 Nginx
- **Serviço de Proxy Reverso**: Nginx atua como um proxy reverso, roteando o tráfego HTTP/HTTPS para sua aplicação FastAPI que está rodando em uma porta diferente. Isso é útil para separar as preocupações de tráfego da aplicação e melhorar a segurança.
- **Desempenho e Escalabilidade**: Nginx é conhecido por sua alta performance e capacidade de lidar com um grande número de conexões simultâneas.
- **Configuração de SSL/TLS**: Facilita a configuração de SSL/TLS para fornecer acesso seguro via HTTPS.

### 2.3 Docker (Opcional)
- **Portabilidade**: O Docker permite que você empacote sua aplicação e suas dependências em um contêiner, garantindo que funcione de maneira consistente em qualquer ambiente.
- **Isolamento**: Ajuda a manter sua aplicação isolada do sistema operacional subjacente, facilitando o gerenciamento e a atualização.

## 3. Justificativa das Tecnologias

### 3.1 Padrão de API
- **Escolha**: REST
- **Justificativa**: REST é um padrão amplamente utilizado e compreendido para a construção de APIs. Ele permite a criação de serviços escaláveis e de fácil manutenção.

### 3.2 Linguagem de Programação e Framework
- **Escolha**: Python e FastAPI
- **Justificativa**: Python foi escolhido pela sua simplicidade e a ampla gama de bibliotecas disponíveis. FastAPI é um framework moderno que é rápido e fácil de usar, permitindo a adição gradual de funcionalidades conforme necessário.

### 3.3 Serviços de Terceiros
- **APIs Utilizadas**: API do Spotify e OpenWeatherMap
- **Justificativa**: Estas APIs foram selecionadas com base na recomendação do desafio e na facilidade de uso. A documentação das APIs foi revisada para garantir que não haveria dificuldades significativas em sua implementação.

