# 🌐 Dažādu tīmekļa serveru Django tīmekļa lietotnes ātrdarbības ietekme

---

## 🚀 Performance Impact of Different Web Servers on Django Web App

The main goal of this research is to analyze how different web servers impact the performance of a Django web application. A Django app was created to run multiple tests, and the execution speeds were measured on selected web servers.

✨ **Key Findings:**
- For simple operations, **Gunicorn** demonstrates the fastest performance.
- For more complex scenarios, **Nginx** outperforms other servers.

🔑 **Keywords:** `Django`, `Python`, `Web Server`

---

## 📊 Testu rezultāti ar 1 lietotāju

Testēšanas paraugs: 
```bash
wrk -t1 -c750 -d600s http://192.168.0.164/database
```

---
<div style="display: flex; flex-wrap: wrap; gap: 20px; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
  <img src="https://github.com/user-attachments/assets/a89d25aa-501c-4e62-a295-0e40da726db5" alt="Performance Chart 1" style="width: 30%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="https://github.com/user-attachments/assets/c4f76b24-dc97-47f0-9678-20621cd57599" alt="Performance Chart 2" style="width: 30%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="https://github.com/user-attachments/assets/eb3c373f-870c-4100-81b5-7383142dd593" alt="Performance Chart 3" style="width: 30%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
</div>

## 📊 Testu rezultāti ar 1 lietotāju

Testēšanas paraugs: 
```bash
wrk -t12 -c400 -d600s http://192.168.0.164/database
```
---
<div style="display: flex; flex-wrap: wrap; gap: 20px; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
  <img src="/mnt/data/image.png" alt="Performance Chart 4" style="width: 30%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="/mnt/data/image.png" alt="Performance Chart 5" style="width: 30%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
  <img src="/mnt/data/image.png" alt="Performance Chart 6" style="width: 30%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
</div>
---



