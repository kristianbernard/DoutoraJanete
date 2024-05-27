# Doutora Janete

Este é um sistema simples de gerenciamento de pacientes e consultas médicas desenvolvido em Python. O sistema permite cadastrar, alterar, excluir e listar pacientes e consultas.

## Funcionalidades

1. **Cadastrar Pacientes**: Permite adicionar novos pacientes ao sistema.
2. **Cadastrar Consultas**: Permite marcar consultas para pacientes cadastrados.
3. **Alterar Paciente**: Permite alterar o nome de um paciente cadastrado.
4. **Alterar Consulta**: Permite alterar a data e hora de uma consulta marcada.
5. **Excluir Paciente**: Permite excluir um paciente e todas as suas consultas associadas.
6. **Listar Pacientes**: Exibe a lista de pacientes cadastrados.
7. **Listar Consultas**: Exibe a lista de consultas marcadas.
8. **Sair**: Encerra o sistema.

## Requisitos

- Python 3.x

## Como Executar

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```

3. Execute o script principal:
    ```bash
    python nome_do_script.py
    ```

## Estrutura do Código

- `Paciente`: Classe que representa um paciente.
- `Consulta`: Classe que representa uma consulta médica.
- `MAX`: Constante que define o número máximo de registros (não está sendo utilizada no código atual).
- `pacientes`: Lista que armazena os pacientes cadastrados.
- `consultas`: Lista que armazena as consultas marcadas.

### Funções

- `cliente_existe(codigo)`: Verifica se um paciente existe pelo código.
- `consulta_existe(data, hora)`: Verifica se uma consulta já está marcada para a data e hora fornecidas.
- `cadastrar_paciente()`: Adiciona um novo paciente ao sistema.
- `cadastrar_consulta()`: Marca uma nova consulta para um paciente existente.
- `alterar_paciente()`: Altera o nome de um paciente existente.
- `alterar_consulta()`: Altera a data e hora de uma consulta existente.
- `excluir_paciente()`: Exclui um paciente e todas as suas consultas associadas.
- `listar_pacientes()`: Lista todos os pacientes cadastrados.
- `listar_consultas()`: Lista todas as consultas marcadas.
- `main()`: Função principal que exibe o menu e gerencia as opções selecionadas pelo usuário.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature ou correção de bug (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -am 'Adicionar nova feature'`).
4. Faça um push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações, entre em contato através do email: kristiandasilva46@gmail.com

---

**Nota**: Este README é um modelo básico. Você pode personalizá-lo conforme necessário para incluir informações adicionais, como capturas de tela, exemplos de uso, ou qualquer outra informação relevante para o seu projeto.
