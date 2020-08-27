# AskTheAI

## Introdução

A respostas e perguntas (QA) é um campo dentro do processamento de linguagem natural focado no projeto de sistemas que podem responder a perguntas. Entre os sistemas de resposta a perguntas mais famosos está o Watson, o computador IBM que competiu (e venceu) no Jeopardy! Um sistema de respostas e perguntas da precisão do Watson requer uma enorme complexidade e grandes quantidades de dados, mas neste problema, iremos projetar um sistema de resposta a perguntas muito simples com base na frequência inversa de documentos.

Nosso sistema de respostas e perguntas realizará duas tarefas: recuperação de documentos e recuperação de passagens. Nosso sistema terá acesso a um corpus de documentos de texto. Quando apresentada uma consulta (uma pergunta em inglês feita pelo usuário), a recuperação do documento identificará primeiro quais documentos são mais relevantes para a consulta. Assim que os principais documentos forem encontrados, o(s) documento(s) principal(is) serão subdivididos em passagens (neste caso, sentenças) para que a passagem mais relevante para a questão possa ser determinada.

Como encontramos os documentos e passagens mais relevantes? Para encontrar os documentos mais relevantes, usaremos tf-idf para classificar documentos com base na frequência de termo para palavras na consulta, bem como frequência inversa de documento para palavras na consulta. Depois de encontrar os documentos mais relevantes, há muitas métricas possíveis para as passagens de pontuação, mas usaremos uma combinação de frequência de documento inversa e uma medida de densidade de termo de consulta.

## Como usar

### pip install -r requirements

e 

### python questions.py corpus

## Projeto original

Projeto 6 do Curso: [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/weeks/6/)