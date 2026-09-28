<h2>Danh sách sinh viên</h2>
<div id="status"></div>
<table border="1" cellpadding="6" style="border-collapse:collapse">
  <thead><tr><th>#</th><th>Tên</th><th>Money</th></tr></thead>
  <tbody id="dssv"></tbody>
</table>

<script>
  // Gọi API /api/tacke (nginx chuyển sang Node-RED)
  fetch("/api/tacke")
    .then(res => res.json())
    .then(data => {
      if (data.ok !== 1) {
        document.getElementById("status").textContent = "Lỗi: " + data.msg;
        return;
      }
      document.getElementById("status").textContent = data.msg + " - tổng: " + data.tong;

      const tbody = document.getElementById("dssv");
      data.dssv.forEach((sv, i) => {
        const tr = document.createElement("tr");
        tr.innerHTML = "<td>" + (i + 1) + "</td><td></td><td>" + sv.money + "</td>";
        tr.children[1].textContent = sv.name;   // tránh chèn HTML từ dữ liệu
        tbody.appendChild(tr);
      });
    })
    .catch(err => {
      document.getElementById("status").textContent = "Không gọi được API: " + err.message;
    });
</script>
