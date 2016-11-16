<center>
  <h1>
    Engenharia de Software e Sistemas para
    <br />
    Engenharia da Computação - ESS/EC Cin UFPE
  </h1>
</center>

<br />
<br />

<h2>
  &nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;Plano de Projeto - lembrol
</h2>

<h3>
  Introdução
</h3>	

Uma preocupação constante ao sair de uma residência  é se algo foi esquecido, seja um guarda-chuva, até algo mais grave como um gás ligado. Existem momentos que lembramos logo ao sair, outros em que estamos longe demais para retornar e ficamos preocupados. 

lembrol é um sistema de monitorame-nto residencial que avisa ao usuário algo que ele não lembrou, seja uma ação ou objeto, a fim de minimizar a quantidade de acidentes domésticos.

Baseado na IoT, esse sistema se comunica com sensores dos quais respondem com informações do ambiente, essas informações são comparadas com os dados registrados no momento da instalação, tudo que é fora do padrão é transformado em uma lista de ações que é mandada para o usuário em seu celular. Se o cliente sair de casa sem o dispositivo, um som gerado no lembrol alertará o usuário.	

<h3>
Organização do Projeto
</h3>

<img src="image_0.png" width="90%" heigh="90%" />

<table>
  <tr>
    <td>Área</td>
    <td>Responsabilidades</td>
  </tr>
  <tr>
    <td>Gerente de Projeto</td>
    <td>Definir, coordenar e integrar as atividades executadas para o desenvolvimento do projeto.</td>
  </tr>
  <tr>
    <td>Engenharia de Requisitos</td>
    <td>Determinar, definir e gerenciar o estado e demais aspectos relacionados aos requisitos de software do sistema.</td>
  </tr>
  <tr>
    <td>Arquitetura de Sistemas</td>
    <td>Desenhar e desenvolver a arquitetura dos sistemas.</td>
  </tr>
  <tr>
    <td>Desenvolvimento de Hardware</td>
    <td>Projetar a arquitetura e desenvolver o hardware do projeto realizando os testes pertinentes.</td>
  </tr>
  <tr>
    <td>Desenvolvimento de Software</td>
    <td>Projetar a arquitetura e desenvolver os componentes de software utilizados no projeto, realizando testes sob demanda.</td>
  </tr>
  <tr>
    <td>Gerência de Configuração e Mudanças</td>
    <td>Controlar os artefatos produzidos pelos desenvolvedores e controlar os custos e esforços envolvidos na realização de uma mudança em um sistema.</td>
  </tr>
  <tr>
    <td>Engenharia de Testes</td>
    <td>Criação de estratégias de teste com objetivo de validar os componentes do sistema durante e após seu desenvolvimento.</td>
  </tr>
  <tr>
    <td>User Interface Engineering</td>
    <td>Desenvolver a parte de Interação com o usuário no sistema, para que fique da forma mais acessível o possível.</td>
  </tr>
</table>

<h3>
Análise de Riscos
</h3>

A análise a seguir leva em consideração os riscos identificados e sua categorização através dos valores atribuídos para as variáveis *severidade* e *probabilidade *de ocorrência. Esses atributos podem assumir valores em uma escala definida de 1 a 3, sendo o cálculo do risco dado pela seguinte multiplicação:

RISCO = SEVERIDADE x PROBABILIDADE

Com base nas métricas definidas anteriormente e nos riscos potenciais evidenciados durante a etapa de levantamento foi possível consolidar a seguinte tabela:

<table>
  <tr>
    <td>Código</td>
    <td>Descrição</td>
    <td>Severidade</td>
    <td>Probabilidade</td>
    <td>Risco</td>
  </tr>
  <tr>
    <td>R1</td>
    <td>Problemas com a integração da central com os diferentes módulos do projeto</td>
    <td>3</td>
    <td>2</td>
    <td>6</td>
  </tr>
  <tr>
    <td>R2</td>
    <td>Atrasos relacionados ao aprendizado das diferentes tecnologias envolvidas.</td>
    <td>2</td>
    <td>3</td>
    <td>6</td>
  </tr>
  <tr>
    <td>R3</td>
    <td>Atrasos na entrega dos dispositivos de hardware solicitados / adquiridos.</td>
    <td>3</td>
    <td>1</td>
    <td>3</td>
  </tr>
  <tr>
    <td>R4</td>
    <td>Mudança de requisitos de software / hardware envolvidos no projeto.</td>
    <td>2</td>
    <td>2</td>
    <td>4</td>
  </tr>
  <tr>
    <td>R5</td>
    <td>Abandono de integrante devido a desistência de participação no projeto</td>
    <td>2</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>R6</td>
    <td>Integrante ficar doente</td>
    <td>3</td>
    <td>2</td>
    <td>6</td>
  </tr>
</table>


A seguir será apresentada uma breve descrição a respeito de possíveis ações associadas a cada um desses riscos. O objetivo é descrever as principais medidas para  mitigá-los e como agir no caso da ocorrência de um incidente.

*R1 - Problemas com a integração dos diferentes componentes de hardware e software.*

* Como mitigar o risco: A equipe deve procurar escolher tecnologias conhecidas para evitar erros causados pela falta de conhecimento nas plataformas de desenvolvimento. Além disso, é importante ficar atento a possíveis incompatibilidades que possam impactar e inviabilizar o desenvolvimento do projeto.

* Ocorrência do incidente: Inicialmente pode-se alocar mais desenvolvedores para tentar resolver o problema de integração. Caso as dificuldades persistam, deve-se partir para tentar encontrar outras alternativas, como por exemplo, alterar os componentes de software ou de hardware e realizar ajustes.

*R2 - Atrasos relacionados ao aprendizado das diferentes tecnologias envolvidas.*

* Como mitigar o risco: Escolher pessoas qualificadas para cada tarefa e que tenham engajamento dentro da sua área de atuação. Além disso, deve-se buscar ferramentas que proporcionem agilidade ao desenvolvimento garantindo que as atividades sejam cumpridas no tempo estimado.

* Ocorrência do incidente: Deve-se alocar mais desenvolvedores para ajudar na tarefa e/ou auxiliar o desenvolvedor que está com dificuldades. Caso o problema persista, pode-se realocar o desenvolvedor com dificuldades para trabalhar em uma atividade diferente, que envolva uma tecnologia a qual ele está mais bem ambientado.

*R3 - Atrasos na entrega dos dispositivos de hardware / software solicitados.*

* Como mitigar o risco: Realizar a decisão e pedido dos dispositivos com antecedência, minimizando assim eventuais riscos de atraso.  Além disso, deve-se buscar alternativas na concepção inicial do projeto de modo a minimizar a dependência de um hardware específico, criando alternativas e maximizando o número de fornecedores.

* Ocorrência do incidente: Buscar dentre as alternativas existentes um outro fornecedor, com disponibilidade de entrega imediata. Deve-se ainda adaptar, conforme necessário, os requisitos de hardware utilizados na concepção inicial do projeto.

*R4 - Mudança de requisitos de software / hardware envolvidos no projeto.*

* Como mitigar o risco: Realizar uma pesquisa exaustiva durante o período inicial do projeto com foco na definição de requisitos sólidos, minimizando dessa forma a ocorrência de eventuais incompatibilidades durante a etapa de desenvolvimento.

* Ocorrência do incidente: Certificar-se que a mudança é realmente necessária e definir corretamente o novo requisito, mapeando adequadamente o impacto nos demais requisitos do projeto e minimizando o risco de alterações futuras.

*R5 - Abandono de integrante devido a desistência de participação no projeto.*

* Como mitigar o risco: Realizar um acompanhamento periódico das atividades realizadas, certificando-se que todos os membros da equipe tenham acesso ao material e o suporte necessário durante todo o desenvolvimento do projeto.

* Ocorrência do incidente: Minimizar o impacto a partir da alocação de um outro desenvolvedor para área desfalcada. Negociar com o membro desistente a transferência do conhecimento e das responsabilidades envolvidas.

*R5 - Integrante ficar doente*

* Como mitigar o risco: Evitar comidas estragadas, usar repelente, ser mais higiênico.

* Ocorrência do incidente: Minimizar o impacto a partir da alocação de um outro desenvolvedor para área desfalcada. Pedir ao membro doente a transferência do conhecimento e das responsabilidades envolvidas.

<h3>
Requisitos de recursos de hardware e software
</h3>

Foram mapeados os seguintes requisitos com relação aos recursos mínimos de hardware e software necessários para o desenvolvimento das atividades do projeto.

* Raspberry Pi: Será utilizada uma Raspberry Pi para atuar como coração do HUB..

* Arduino Nano: Serão necessários dois Arduinos Nano para efetuar o processamento de dados necessário em cada módulo.

* Resistores e Jumpers: Utilizados no desenvolvimento do circuito montado na protoboard. Necessários para efetuar a automação e o controle dos sensores que irão monitorar o ambiente.

* Sensor de gás: Utilizado para detecção de vazamento de  gás. Capta o nível de gás no ar, transformando em uma leitura analógica.

* Piezzo elétrico : Reconhece quando há ou não há um peso acima do mesmo. Necessário para saber se o objeto importante está no lugar desejado ou não.

* Swift: Linguagem open source utilizada para desenvolvimento em plataformas da Apple de fácil legibilidade e redigibilidade. Necessária para programação do aplicativo iOS. 

* Firebase : Serviço de nuvem para banco de dados em tempo real, com API para diversas linguagens, permite que mudanças no banco de dados possam ser acompanhadas de forma simples

* Python : Linguagem open source conhecida por ser extremamente simples e fácil de entender. Necessária para programação da Raspberry Pi.

* Baterias Lipo : Baterias para funcionamento do sistema em modo remoto. Necessárias para garantir autonomia do sistema.

* ESP8266 : Módulo WiFi para conexão de internet para Arduino. Necessário para passagem de dados entre o HUB e os módulos.

<h3>
Estrutura Analítica
</h3>

Com base nas reuniões efetuadas para discussão sobre o processo de divisão de atividades foram identificadas as seguintes estruturas analíticas para o projeto.

*T1 - Fazer requisitos*

Detalhar os requisitos de serviços funcionais e não funcionais, de forma, detalhada e registrar todos os requisitos.

*T2 - Montar os casos de uso*

Descrever os casos de uso para serem consultados durante todo o desenvolvimento.

*T3 - Montar a arquitetura do HUB*

Arquitetar o HUB, arquitetura deve conter todo o sistema do HUB que será o centro do serviço e deve se conectar com todos os componentes e usuários do sistema. A sua arquitetura deve ser bem montada para sua comunicação.

*T4 - Modelar comunicação do HUB*

Modelar a comunicação do HUB com módulos e aplicativos, para uma comunicação efetiva e sem atrasos, feita com diversos testes no sistema

*T5 - Modelar banco de dados do HUB*

Modelar o banco de dados onde os estados dos sensores vão ser armazenados para em seguida serem enviadas para o aplicativo e serem visualizados pelo usuário.

*T6 - Desenvolver aplicativo*

Desenvolver aplicativo de gerenciamento do sistema pelo usuário, o aplicativo deverá informar ao usuário o estado dos sensores, se comunicar com o HUB e seu banco de dados além de informar ao HUB sua localização para análise de esquecimento do dispositivo.

*T7 - Montar hardware do módulo de objetos importantes*

Desenvolver módulo de localização para hardware que será colocado em objetos que possuem grande importância e não poderão ser esquecidos pelo usuário.

O módulo deve estar anexado ao objeto e o usuário deve ser alertado caso saia de sua residência e esqueça o objeto, no caso do celular a sua posição será feita pelo aplicativo.

*T8 - Desenvolver o software do módulo de objetos importantes*

Desenvolver software de comunicação do módulo com o HUB, leitura de dados e envio para o HUB, que armazenará seu estado em seu banco de dados.

*T9 - Integração do módulo de objetos importantes com o HUB*

Integração do módulo e com o HUB deve ser feita de forma com que o módulo possa ser facilmente removido e adicionado. Sua comunicação deve ser feita para uma interação rápida e deve ser amplamente testada.

*T10 - Montar o módulo de gás*

Desenvolver o módulo de gás e sua comunicação com o HUB, suas funcionalidades e suas conexões

*T11 -  Desenvolver o software do módulo de gás*

*Desenvolver software de leitura, análise e envio de dados do módulo.*

*T12 -  Integrar o módulo de gás com o HUB*

Conectar o módulo com o HUB, testar funcionalidades e comunicação entre HUB e módulos.

<h3>
Cronograma do Projeto
</h3>

Com base nas estruturas analíticas do projeto foi estabelecido o seguinte cronograma.

<table>
  <tr>
    <td>Atividade</td>
    <td>Entrega</td>
    <td>Responsáveis</td>
    <td>Dependências</td>
  </tr>
  <tr>
    <td>T1</td>
    <td>12/10/2016</td>
    <td>hcf2</td>
    <td>-</td>
  </tr>
  <tr>
    <td>T2</td>
    <td>12/10/2016</td>
    <td>hcf2</td>
    <td>T1</td>
  </tr>
  <tr>
    <td>T3</td>
    <td>26/10/2016</td>
    <td>mpmr,jnolj</td>
    <td>T2</td>
  </tr>
  <tr>
    <td>T4</td>
    <td>26/10/2016</td>
    <td>mpmr,jnolj</td>
    <td>T3</td>
  </tr>
  <tr>
    <td>T5</td>
    <td>26/10/2016</td>
    <td>mpmr,jnolj</td>
    <td>T3</td>
  </tr>
  <tr>
    <td>T6</td>
    <td>14/11/2016</td>
    <td>jnolj</td>
    <td>T5</td>
  </tr>
  <tr>
    <td>T7</td>
    <td>21/11/2016</td>
    <td>dapd,mapa</td>
    <td>T1</td>
  </tr>
  <tr>
    <td>T8</td>
    <td>21/11/2016</td>
    <td>dapd,mapa,jnolj,mpmr</td>
    <td>T7</td>
  </tr>
  <tr>
    <td>T9</td>
    <td>21/11/2016</td>
    <td>dapd,mapa,jnolj,mpmr</td>
    <td>T8</td>
  </tr>
  <tr>
    <td>T10</td>
    <td>05/12/2016</td>
    <td>dapd,mapa</td>
    <td>T1</td>
  </tr>
  <tr>
    <td>T11</td>
    <td>05/12/2016</td>
    <td>dapd,mapa,jnolj,mpmr</td>
    <td>T10</td>
  </tr>
  <tr>
    <td>T12</td>
    <td>05/12/2016</td>
    <td>dapd,mapa,jnolj,mpmr</td>
    <td>T11</td>
  </tr>
</table>

<h3>
  Mecanismos de monitoramento e elaboração de relatórios
</h3>

Ao longo do processo de desenvolvimento serão disponibilizados relatórios gerenciais para refletir o nível atual de progresso e andamento das atividades através de métricas bem definidas. Esses relatórios serão consolidados em cada milestone e servirão de instrumento fundamental para o acompanhamento do projeto pelas partes interessadas.

Com base no cronograma apresentado serão definidas atividades elementares para representar as etapas de desenvolvimento necessárias para alcançar os milestones definidos. Cada atividade terá uma prioridade para execução, uma estimativa de esforço, além de um responsável pelo desenvolvimento.

O registro global dessas atividades com relação ao progresso e a rastreabilidade serão efetuados através de ferramentas auxiliares, notadamente o Trello [1] e o GitHub [2]. A primeira proporciona uma visão gerencial dando indicativos claros a respeito do progresso efetuado, enquanto a segunda permite um acompanhamento operacional, fornecendo indicadores essenciais que orientam o processo de gestão de mudanças.

Referências

[1] http://www.trello.com

[2] https://github.com/

