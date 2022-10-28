



# SAPB1
  
Módulo para automatizar o SAP Business One.  
  
![banner](imgs/Banner_SAPB1.png)

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  

## Como usar este módulo

Para podermos executar os comandos, devemos ter em mente que os objectos que encontramos no SAP B1, sejam eles inputs, botões ou menus, são diferenciados por IDs, e alguns deles são encontrados dentro de linhas e colunas. Para conhecer estes dados, devemos activar a opção "Informação do sistema" encontrada no menu Exibir, ou premir a combinação de teclas Ctrl + Shift + I. Depois, no canto inferior esquerdo, podemos ver os dados do objecto. É importante ter isto em conta ao automatizar, pois será necessário ter o ID do Formulário e o ID do Item, bem como a coluna e linha, se aplicável.

## Descrição do comando

### Conectar ao SAP B1
  
Conectar ao SAP B1
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável||result|

### Iniciar sessão no SAP B1
  
Iniciar sessão no SAP B1
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Utilizador||manager|
|Senha||password|
|Nome da base de dados||DBSociety01|
|Empresa||2|

### Click
  
Clique sobre um item
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Formulário||form|
|Item||item|
|Linha||row|
|Coluna||column|
|Tipo|||

### Activar item do menu
  
Activar item do menu
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Item do menu||3392|

### Enviar texto
  
Enviar texto para uma entrada de texto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto||Hello World!|

### Obter texto
  
Obtém o texto de um item
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Formulário||form|
|Item||item|
|Linha||row|
|Coluna||column|
|Atribuir resultado a uma variável||result|

### Clique na janela pop-up
  
Clique na janela pop-up
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Item||item|

### Obter dados a partir de formulários e menus visíveis
  
Obter dados a partir de formulários e menus. Os dados serão sobre os formulários e menus visíveis no momento da 
execução.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável||result|

### Obter dados de matriz visíveis
  
Obter dados matriciais. A Matriz seleccionada deve ser visível no momento da execução.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Formulário||form|
|item||item|
|Atribuir resultado a uma variável||result|
