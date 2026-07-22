import cv2


#aqui estamos criando o rastreador, vamos tentar o KCF e o CSRT
#rastreador = cv2.TrackerKCF_create()
rastreador = cv2.TrackerCSRT_create()

#aqui estamos abrindo o video que queremos analisar
video = cv2.VideoCapture("race.mp4")

#aqui criamos 2 variaveis, o ok retorna true ou false, se conseguir ler true se n false e a variavel frame é frame
# O video.read aqui estamos fazendo a leitura do primeiro frame do video
ok, frame = video.read()

#primeiro vamos fazer um retangulo pra localizar primeiro
bbox = cv2.selectROI(frame) # regiao de interesse que queremos rastrear

#aqui no print nos vamos selecionar o tamanho no retangulo do objeto queremos identificar no primeiro frame
# assim vamos receber dados desse rastreio eixos e larguras e alturas.

#print(bbox)

ok = rastreador.init(frame, bbox)
#print(ok)

#esse while é para percorrer todo o video e nao apenas o primeiro frame
while True:
    ok, frame = video.read()
    print(ok)
    if not ok:
        break

    ok, bbox = rastreador.update(frame)
    print(bbox)

    if ok :
        (x,y,w,h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), ( 0, 255, 0), 2, 1)
    else:
        cv2.putText(frame, "Erro", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Rastreamento", frame)
    if cv2.waitKey(1) & 0XFF == 27: # esse codigo simboliza "se o usuário clicar na tecla 27/que é a tecla esc
        break
