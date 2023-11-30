



# SAPB1
  
Com este módulo você pode automatizar SAP Business One.  

*Read this in other languages: [English](Manual_SAPB1.md), [Português](Manual_SAPB1.pr.md), [Español](Manual_SAPB1.es.md)*
  
![banner](imgs/Banner_SAPB1.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

Para podermos executar os comandos, devemos ter em mente que os objectos que encontramos no SAP B1, sejam eles inputs, botões ou menus, são diferenciados por IDs, e alguns deles são encontrados dentro de linhas e colunas. Para conhecer estes dados, devemos activar a opção "Informação do sistema" encontrada no menu Exibir, ou premir a combinação de teclas Ctrl + Shift + I. Depois, no canto inferior esquerdo, podemos ver os dados do objecto. É importante ter isto em conta ao automatizar, pois será necessário ter o ID do Formulário e o ID do Item, bem como a coluna e linha, se aplicável.
## Descrição do comando

### Conecte-se ao SAP B1
  
Conecte-se ao SAP B1. O aplicativo deve estar aberto no momento de executar o comando.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável|Nome da variável para armazenar o resultado|res|

### Entrar no SAP B1
  
Entrar no SAP B1
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Usuário||manager|
|Senha||password|
|Nome do banco de dados (Opcional)||DBSociety01|
|Sociedade (Opcional)||2|

### Click
  
Faça um clique em um item
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Forma||form|
|Item||item|
|Linha||row|
|Coluna||column|
|Modelo|||
|Clique no seletor|Clique no mecanismo de busca de objetos, aplicável no caso de objetos do Edição de Texto|checkbox|

### Selecione
  
Selecione um item
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Forma||form|
|Item||item|
|Linha||row|
|Coluna||column|
|Type|||
|Parâmetro||Value/Index|

### Ativar item de menu
  
Ativar item de menu
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Item do menu||3392|

### Enviar texto ou tecla
  
Enviar texto ou tecla a uma entrada de texto. Se deixar em branco o texto, a tecla será enviada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto||Hello World!|
|Enviar tecla||ENTER|

### Obter texto
  
Obtém o texto de um item
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Forma||form|
|Item||item|
|Linha||row|
|Coluna||column|
|Atribuir resultado a uma variável|Nome da variável para armazenar o resultado|result|

### Clique no pop-up
  
Clique na janela pop-up
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável|Nome da variável para armazenar o resultado|item|

### Obtenha formulários visíveis e dados de menus
  
Get data of forms and menus. The data will be about visible forms and menus at the moment of the execution.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a uma variável|Nome da variável para armazenar o resultado|data|

### Obter dados de matriz visíveis
  
Obter dados de matriz. A matriz deve estar visível no momento da execução.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Forma||form|
|Item||item|
|Atribuir resultado a uma variável|Nome da variável para armazenar o resultado|result|
