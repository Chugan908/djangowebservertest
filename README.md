# :globe_with_meridians: Dažādu tīmekļa serveru Django tīmekļa lietotnes ātrdarbības ietekme

---

## :rocket: Performance Impact of Different Web Servers on Django Web App

The authors of the study are Gļebs Cvetkovs and Maksims Rubins, the supervisor is Aleksandrs Korņijenko.

The main goal of this research is to analyze how different web servers impact the performance of a Django web application. A Django app was created to run multiple tests, and the execution speeds were measured on selected web servers.

:sparkles: **Key Findings:**
- For simple operations, **Gunicorn** demonstrates the fastest performance.
- For more complex scenarios, **Nginx** outperforms other servers.

:key: **Keywords:** `Django`, `Python`, `Web Server`

---

## :bar_chart: Testu rezultāti ar 1 lietotāju

Testēšanas paraugs: 
```bash
wrk -t1 -c750 -d600s http://192.168.0.164/database
```

---

<p align="center">
<img src="https://github.com/user-attachments/assets/a89d25aa-501c-4e62-a295-0e40da726db5" width="750" height="450">
</p>

---

<p align="center">
<img src="https://github.com/user-attachments/assets/c4f76b24-dc97-47f0-9678-20621cd57599" width="750" height="450">
</p>

---

<p align="center">
<img src="https://github.com/user-attachments/assets/eb3c373f-870c-4100-81b5-7383142dd593" width="750" height="450">
</p>



## :bar_chart: Testu rezultāti ar 1 lietotāju

Testēšanas paraugs: 
```bash
wrk -t12 -c400 -d600s http://192.168.0.164/database
```
---

<p align="center">
<img src="https://github.com/user-attachments/assets/1462998f-a9e2-474a-954f-4fe58d352034" width="750" height="450">
</p>

---

<p align="center">
<img src="https://github.com/user-attachments/assets/8e44c807-46b2-4be0-8ccc-89dea364b99d" width="750" height="450">
</p>

---

<p align="center">
<img src="https://github.com/user-attachments/assets/a16c2665-7bc5-491f-81d7-633e35505cb8" width="750" height="450">
</p>

