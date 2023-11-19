# 5sim.net API Handler

Este projeto oferece um handler em Python para interações com a API do site 5sim.net. Ele facilita a verificação de compras, a leitura de mensagens SMS e o cancelamento de pedidos se não houver recebimento de mensagens por 3 minutos.

## Instalação

Para utilizar este handler, siga estas etapas:

1. Clone este repositório:

    ```bash
    git clone https://github.com/darkmathew/nome-do-repositorio.git
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

O handler 5sim.net permite interações por meio de diversos serviços e países. Abaixo estão listados os países e serviços disponíveis:

### Lista de Países

- afghanistan - Afghanistan
- albania - Albania
- algeria - Algeria
- ... [(Lista completa dos países disponíveis)](https://5sim.net/docs/?python#countries-list)

### Serviços Disponíveis

- 1688
- 23red
- 32red
- 99app
- Ace2Three
- ... [(Lista completa dos serviços disponíveis)](https://5sim.net/docs/?python#products-list)

### Utilização

Primeiramente você deve configurar suas informações corretamente.

- **token**: O seu [token](https://5sim.net/settings/security) da plataforma.
- **country**: O país do número
- **product**: O serviço a ser adquirido

```python
if __name__ == "__main__":
    token = 'token'
    country = 'brazil'
    operator = 'any'
    product = 'telegram'

    api_client = APIClient(token)
    activation_handler = ActivationHandler(api_client)
    activation_handler.buy_and_check_activation(country, operator, product)

```

Rode a aplicação:

```bash
python main.py
```

## Créditos

Este projeto foi autorado por [Matheus Santos/darkmathew](https://github.com/darkmathew/)
