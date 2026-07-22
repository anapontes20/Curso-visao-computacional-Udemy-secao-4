Rastreamento de objetos é diferente de detecção de objetos. Vamos entender a diferença entre os dois.

## RASTREAMENTO × DETECÇÃO

**RASTREAMENTO:** Nessa técnica, identificamos e rastreamos um alvo específico. Um exemplo é acompanhar o percurso que um determinado jogador fez durante uma partida de futebol. O algoritmo de rastreamento utiliza as informações dos frames anteriores do vídeo para continuar acompanhando o mesmo objeto ao longo do tempo.

**DETECÇÃO:** É a técnica utilizada para identificar um determinado objeto em uma imagem. Por exemplo, detectar carros em uma cena que também contém ônibus, caminhões e outros veículos. O algoritmo de detecção analisa cada frame do vídeo de forma independente, desde o primeiro frame.

As duas técnicas podem trabalhar em conjunto: primeiro a detecção identifica o objeto e, em seguida, o rastreamento acompanha seu movimento ao longo dos frames.

Outra coisa interessante sobre isso é que um algoritmo de detecção tem grandes chances de não reconhecer um rosto se tiver um objeto na frente dele, como uma mão por exemplo.
Mas o de rastreamento tem grandes chances de conseguir identificar mesmo com algo tampando uma parte da face.

#

## Algoritmos KCF e CSRT importantes na area de rastreamento de objetos.

**KCF(KERNEL CORRELATION FILTERS):**
Nesse algoritmo, o rastreamento é iniciado a partir de um retângulo que delimita o objeto de interesse.

Por exemplo, no primeiro frame do vídeo, o algoritmo identifica um objeto, como um rosto, e desenha um retângulo ao seu redor. A partir dos próximos frames, o KCF utiliza essa região como referência para acompanhar a movimentação do objeto ao longo do vídeo.

No entanto, esse algoritmo não é muito eficiente em vídeos com movimentos muito rápidos, mudanças bruscas de direção ou quando o objeto fica oculto, pois pode perder a referência do objeto e interromper o rastreamento.

**CSRT(DISCRIMINATIVE CORRELATION FILTER WITH CHANNELA ND SPATIAL RELIABILITY):**
Esse algoritmo é mais avançado que o KCF, porem consome mais processamento pois ele é mais lento que o KCF. A forma como ele acompanha o objeto é igual ao KCF mas ele é mais lento e complexo.
