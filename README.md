# lập trình web
## 1. giả lập linux os ubuntu trên vmware
- Truy cập trang chủ của Ubuntu (ubuntu.com/download) và tải về file .iso.
- Tải vmware tạo máy ảo mới rồi gắn file iso ubuntu vào.
  
  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/8ccbb613-66ca-4d81-a50f-37360089369e" />
## 2. cài đặt docker compose 
- Trên Ubuntu, bạn có thể cài đặt Docker trực tiếp từ kho lưu trữ mặc định bằng lệnh: sudo apt install docker.io -y
- Cấp quyền cho User sử dụng Docker không cần "sudo": sudo usermod -aG docker ${USER}
- Kiểm tra xem bạn đã chạy được Docker chưa bằng cách gõ:docker version
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/32d44aeb-c463-45a3-a9c1-7fec90cd6bca" />

- cài đặt docker compose bằng lệnh: sudo apt install docker-compose-v2 -y
<img width="1912" height="482" alt="image" src="https://github.com/user-attachments/assets/cea38e35-a0ba-41f2-bf47-28881248e85d" />

## 3. cài đặt docker compose : các dịch vụ: nginx, nodered, mariadb, phpmyadmin, cloudflared

- Tạo file docker-compose.yml
- chạy các dịch vụ: nginx, nodered, mariadb, phpmyadmin, cloudflared
<img width="1920" height="1080" alt="Screenshot 2026-09-27 140304" src="https://github.com/user-attachments/assets/a9a122fd-5c08-478d-8d9b-055fa25060aa" />

<img width="1920" height="1080" alt="Screenshot 2026-09-27 140314" src="https://github.com/user-attachments/assets/02dd8f36-5102-416d-b733-19033050b465" />
- Tạo đường hầm tới cloudflared
<img width="1920" height="1080" alt="Screenshot 2026-09-28 002408" src="https://github.com/user-attachments/assets/acb46e5c-fad6-4ef9-b517-a1ae77f60286" />
- Khởi chạy 2 trang web thử nghiệm chạy trên 2 domain khác nhau
<img width="1920" height="1080" alt="Screenshot 2026-09-28 002527" src="https://github.com/user-attachments/assets/53d754f5-ab6f-4876-be88-65862f79a7de" />

<img width="1920" height="1080" alt="Screenshot 2026-09-28 002531" src="https://github.com/user-attachments/assets/7dd2673d-bbc4-49b2-a113-90c05d4d6d79" />
