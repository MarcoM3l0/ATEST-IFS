# Documentação do Projeto - ATEST-IFS 📝

Aluno: José Marco Melo Nascimento 👨‍🎓 <br>
Curso: Ciência da Computação - 3° período 🎓<br>
Disciplina: Linguagem de Programação I 🖥️<br>
Projeto: ATEST-IFS - Atestados no IFS 🏥<br>

## Descrição 📄

O projeto "Atestados IFS" tem como objetivo desenvolver um aplicativo console em Python para gerenciar o recebimento de atestados no Instituto Federal de Educação, Ciência e Tecnologia (IFS). O aplicativo visa automatizar o processo de recebimento, registro e acompanhamento dos atestados médicos apresentados pelos estudantes e servidores do IFS.

## Objetivos do Projeto 🎯

- Agilizar o processo de recebimento: o aplicativo deve permitir o recebimento dos atestados, descritos no capítulo III da ROD do IFS, de forma rápida e eficiente, evitando a necessidade de formulários físicos e processos manuais.
- Registrar informações relevantes: o sistema deve armazenar as informações essenciais contidas nos atestados, como nome, data de emissão, diagnóstico, período de afastamento, entre outros.
- Aumentar a eficiência administrativa: ao simplificar e automatizar o processo de recebimento e gerenciamento de atestados, o aplicativo contribuirá para a redução de erros, economia de tempo e recursos administrativos, permitindo que a equipe do IFS possa se concentrar em atividades de maior valor agregado.

## O que foi feito para alcançá-los ✅

Como parte do meu interesse em compreender o processo, busquei informações junto à Coordenadoria de Registros Escolares (CRE) do IFS para entender como é realizado o recebimento de atestados dos estudantes.
O objetivo principal do procedimento é garantir a eficiência e a precisão no recebimento, registro e armazenamento dos atestados, a fim de cumprir as normas e regulamentos do IFS. A CRE desempenha um papel fundamental na supervisão e execução desse processo, assegurando que os atestados sejam tratados de forma adequada e segura.
Essas informações foram úteis para entender o processo e poder desenvolver o sistema com maior fidelidade às normas e regras do IFS. Nesse processo é garantido que o procedimento esteja alinhado com as melhores práticas e requisitos do instituto.

## Documentação do código 📝

### Introdução 🚀

O sistema de pastas do aplicativo é organizado de forma a manter uma estrutura modular e facilitar o desenvolvimento e a manutenção do código. Existem quatro pastas principais que desempenham papéis específicos: "telas", "funcionalidades", "db" e "classes". Cada uma dessas pastas contém arquivos que implementam diferentes aspectos do aplicativo.

### Descrição da estrutura de pastas 📂

1. `main.py`:
   - Este arquivo é o ponto de entrada principal do aplicativo.
   - É responsável por executar o aplicativo e iniciar a interação com o usuário.

2. `telas/`:
   - Essa pasta contém os arquivos responsáveis por implementar as

 telas do aplicativo, onde o usuário interage com o sistema.
   - Cada arquivo representa uma tela específica e contém funções para exibir a tela, obter entrada do usuário e processar ações relacionadas a essa tela.

3. `funcionalidades/`:
   - Nesta pasta estão os arquivos que implementam as funcionalidades do aplicativo.
   - Cada arquivo representa uma funcionalidade específica, como cadastrar um atestado, exibir atestados cadastrados, pesquisar atestados, etc.
   - Esses arquivos contêm funções que são chamadas a partir das telas para executar as ações relacionadas a cada funcionalidade.

4. `db/`:
   - Essa pasta contém os arquivos relacionados ao banco de dados do aplicativo em .json.

5. `classes/`:
   - Esta pasta contém os arquivos que definem as classes do aplicativo.

### Como executar o aplicativo ▶️

Para executar o aplicativo, siga as instruções abaixo:

1. Clone o repositório do projeto para o seu ambiente local.
2. Certifique-se de ter o Python 3 instalado em seu sistema.
3. Navegue até a pasta do projeto no seu terminal.
4. Execute o seguinte comando para iniciar o aplicativo:

```shell
python main.py
```

5. O aplicativo será iniciado e você poderá interagir com ele através das telas e opções apresentadas.

## Conclusão 🎓

O projeto "Atestados IFS" é um aplicativo console desenvolvido em Python que visa automatizar o processo de recebimento, registro e acompanhamento de atestados no Instituto Federal de Educação, Ciência e Tecnologia (IFS). O aplicativo foi projetado para agilizar o processo, reduzir erros e aumentar a eficiência administrativa no tratamento de atestados.

O código fonte do projeto está disponível no repositório GitHub: https://github.com/MarcoM3l0/ATEST-IFS

Espero que esta documentação forneça uma visão geral clara do projeto e de como ele foi implementado. Fico à disposição para qualquer esclarecimento adicional.
