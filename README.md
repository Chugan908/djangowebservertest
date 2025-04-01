# Dažādu tīmekļa serveru Django tīmekļa lietotnes ātrdarbības ietekme

## Abstract
  Performance Impact of Different Web Servers on Django Web App. The authors of the paper are Gļebs Cvetkovs and Maksims Rubins, the supervisor is Aleksandrs Korņijenko. 

  The main goal of this work is to investigate how different web servers can affect the speed of a Django web app. For the research, a Django web app was created that includes various tests, the execution speed of which was measured on selected web servers.

  Analysis of the test results allows us to conclude that in the context of simple operations, the web server Gunicorn shows the fastest performance. However, in more complex cases, the web server Nginx showed the best performance.

## Testu rezultāti ar 1 lietotāju
Testēšanas paraugs: `wrk -t1 -c750 -d600s http://192.168.0.164/database`

![asd](https://github.com/user-attachments/assets/a89d25aa-501c-4e62-a295-0e40da726db5)
![ghfh](https://github.com/user-attachments/assets/c4f76b24-dc97-47f0-9678-20621cd57599)
![dgf](https://github.com/user-attachments/assets/eb3c373f-870c-4100-81b5-7383142dd593)


## Testu rezultāti ar vairākiem lietotājiem
Testēšanas paraugs: `wrk -t12 -c400 -d600s http://192.168.0.164/database`

![sadasd](https://github.com/user-attachments/assets/1462998f-a9e2-474a-954f-4fe58d352034)
![asdsads](https://github.com/user-attachments/assets/8e44c807-46b2-4be0-8ccc-89dea364b99d)
![bvnv](https://github.com/user-attachments/assets/a16c2665-7bc5-491f-81d7-633e35505cb8)

