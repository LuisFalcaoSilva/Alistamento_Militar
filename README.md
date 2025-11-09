🪖 ASCE - Sistema de Alistamento Militar

Este projeto foi desenvolvido como parte de um desafio acadêmico, com o propósito de disponibilizar informações preliminares sobre o alistamento militar do usuário, com base em seu ano de nascimento e sexo.
Dessa vez, o sistema ganhou uma interface gráfica interativa (GUI) desenvolvida com Tkinter, e todos os dados são armazenados em um banco de dados SQLite.

👨‍💻 Sobre Mim

Sou uma pessoa que presta muita atenção aos detalhes e busca sempre unir funcionalidade e estética.
Para deixar o projeto mais envolvente, criei um robô chamado ASCE, que atua como um assistente simpático no processo de alistamento.
Na versão anterior, ele conversava com o usuário via terminal. Agora, ASCE tem um ambiente visual próprio, organizado e intuitivo — uma evolução natural do projeto original.

🧩 Desafios e Aprendizados

O maior desafio neste projeto foi unir lógica de programação, interface gráfica e banco de dados de forma harmônica.
Foi preciso compreender a estrutura e o comportamento do Tkinter, especialmente na parte de atualização de tabelas (Treeview) e no gerenciamento das transações SQLite.

Outro aprendizado valioso foi sobre tratamento de dados e validação de entradas, garantindo que o sistema responda de maneira adequada a erros comuns, como campos vazios ou valores inválidos.

O algoritmo em si é simples, mas a preocupação principal foi com a organização do código e a experiência do usuário — desde o fluxo de cadastros até o feedback visual das operações (como exclusão, limpeza ou inserção de registros).

🚀 O Que Vem Por Aí

Nas próximas versões, pretendo:

Adicionar autenticação de usuários (login e senha);

Permitir exportar relatórios em PDF ou Excel;

Criar uma versão web utilizando Flask ou Django;

Aprimorar o design com temas customizados e ícones.

Atualmente, estou estudando HTML, CSS, JavaScript e Flask, com o objetivo de levar este projeto para a web e transformar o ASCE em um assistente militar digital completo.

⚠️ Observações Importantes

O programa já possui uma interface gráfica (diferente da primeira versão, que rodava apenas no terminal).

Os dados são armazenados automaticamente em um arquivo SQLite (alistamento.db), criado na primeira execução.

Para rodar o programa, basta ter o Python 3 instalado e executar o arquivo principal (main.py ou equivalente).

Todos os registros inseridos podem ser visualizados, excluídos ou limpos diretamente na interface.

📑 Tabela de Conteúdos

Arquitetura

Características

Como Executar o Projeto

Contribua com o Projeto

Extra

🏗️ Arquitetura

A estrutura do projeto segue uma organização simples, porém eficiente:

📁 ASCE/
├── main.py                 # Arquivo principal (interface + lógica)
├── alistamento.db          # Banco de dados SQLite (criado automaticamente)
└── README.md               # Documentação do projeto

Principais Componentes

Tkinter e ttk → Responsáveis pela interface gráfica (janelas, botões, campos e tabela).

SQLite3 → Armazena os dados de alistamento (nome, sexo, ano, situação e multa).

Datetime → Registra automaticamente a data da conversa/registro.

Fluxo de Execução

O usuário insere Nome, Sexo e Ano de Nascimento.

O sistema calcula a idade, a situação de alistamento e, se necessário, a multa por atraso.

Os dados são salvos no banco SQLite e exibidos em uma tabela visual.

O usuário pode excluir registros, limpar o histórico ou atualizar a tabela em tempo real.

💡 Características

Interface gráfica amigável com Tkinter

Armazenamento persistente em SQLite

Cálculo automático da idade, situação e multa

Botões intuitivos para Adicionar, Excluir, Limpar e Atualizar

Sistema responsivo e adaptável a diferentes resoluções

Mensagens informativas e de erro para melhor usabilidade

⚙️ Como Executar o Projeto
🔧 Pré-requisitos

Python 3.10+ instalado

Nenhuma dependência externa (somente bibliotecas padrão: tkinter, sqlite3, datetime)

▶️ Execução

Baixe ou clone o repositório:

git clone https://github.com/seuusuario/ASCE.git
cd ASCE


Execute o projeto:

python main.py


A interface será aberta, e o ASCE estará pronto para começar os cadastros!

🤝 Contribua com o Projeto

O projeto está aberto a contribuições!
Se você tiver ideias para novas funcionalidades ou melhorias, fique à vontade para abrir um pull request ou enviar uma mensagem com sugestões.

Toda colaboração será reconhecida com créditos na documentação e divulgação da sua versão aprimorada.

✨ Extra

A ideia principal do projeto é humanizar a interação com o usuário, tornando o processo de consulta de alistamento mais acessível e didático.
Espero que este projeto inspire outros estudantes a explorarem o poder do Tkinter e do SQLite — tecnologias simples, mas extremamente úteis em aplicações reais.

“A melhor forma de aprender é transformar lógica em experiência.”

🕓 Codado entre cafés e madrugadas inspiradas.
💻 Desenvolvido com dedicação e curiosidade.
