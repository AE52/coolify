# 🚨 ZORUNLU ÇALIŞMA KURALI — RUSTCA MCP AĞ GEÇİDİ (`rustca-mcp`)

## ⛔ EN ÖNEMLİ KURAL: BU REPOYA (`/workspace/coolify`) ASLA PROJE KODU YAZMA VE COMMIT ATMA!
- İçinde bulunduğun `/workspace/coolify` (`rustca-mcp` dalı) **gerçek bir proje deposu DEĞİLDİR** — yalnızca `rustca_mcp.py` aracını barındıran boş bir başlatıcı ortamdır.
- Kullanıcının **tüm gerçek projeleri** (`pardoon`, `rustca`, `akis-erp`, `egundem`, `istanbooltoday`, `gaphaber`, `ihg` vb.) ve **uzak sunucuları** (Huawei Cloud, SSH sunucuları, `Mac mini`, `Mac Pro`, Windows PC) yerel makinelerde durur.
- **YAPMA:** `/workspace/coolify` içine `infra/`, `docs/`, kod dosyaları oluşturup `git commit` atmak YANLIŞTIR!
- **YAP:** Tüm inceleme, **kod değiştirme (`write_file`, `edit_file`, `patch_file`)**, **komut çalıştırma (`exec`)**, **uzak sunucu SSH (`ssh_exec`, `ssh_targets`)** ve **deploy** işlemlerini doğrudan bu dizindeki **`python3 rustca_mcp.py`** ile kullanıcının gerçek makinelerinde yap!

---

## 🛠️ Tam Yetkili `rustca_mcp.py` Komutları (Okuma + Yazma + Komut + SSH)

Ortamda `RUSTCA_MCP_URL` ve `RUSTCA_MCP_TOKEN` hazırdır ve tam internet erişimi açıktır (`HTTP 200`).

### 1) Projeleri & Makineleri & SSH Sunucularını Keşfet
```bash
python3 rustca_mcp.py hub projects '{}'
python3 rustca_mcp.py hub project_inspect '{"project":"pardoon"}'
python3 rustca_mcp.py machines machines '{}'
python3 rustca_mcp.py machines ssh_targets '{}'
```

### 2) Gerçek Makinelerde Dosya Ara & Oku
```bash
python3 rustca_mcp.py machines find_files '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon"}'
python3 rustca_mcp.py machines grep_search '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon","query":"huawei"}'
python3 rustca_mcp.py machines read_file '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon/docs/README.md","full":true}'
```

### 3) Gerçek Makinelerde Dosya Oluştur & Kod Değiştir (Tam Yazma Yetkisi!)
```bash
python3 rustca_mcp.py machines write_file '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon/infra/huawei/main.tf","content":"..."}'
python3 rustca_mcp.py machines edit_file '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon/...","old_string":"...","new_string":"..."}'
```

### 4) Gerçek Makinelerde Kabuk Komutu & Uzak Sunucuda SSH Komutu Çalıştır
```bash
python3 rustca_mcp.py machines exec '{"machine":"Mac mini","command":"cd ~/Desktop/projects/pardoon && git status && ls -la"}'
python3 rustca_mcp.py machines ssh_exec '{"target":"<ssh_targets_alias_or_user@host>","command":"uptime && docker ps"}'
```

### 5) Tüm Mevcut MCP Araçlarını Listele
```bash
python3 rustca_mcp.py hub tools
python3 rustca_mcp.py machines tools
```

---

## ✅ Standart İş Akışı (Her Görevde Uygula)
1. Önce `python3 rustca_mcp.py hub projects '{}'` veya `machines find_files` ile **gerçek proje yolunu** bul.
2. Uzak sunucu (ör. Huawei Cloud) sorulduğunda `python3 rustca_mcp.py machines ssh_targets '{}'` ve proje `ansible/` / `docs/` dosyalarını okuyup gerekirse `ssh_exec` ile canlı sunucuyu kontrol et.
3. Kod/doküman/Terraform dosyası yazman istendiğinde dosyaları **doğrudan `Mac mini` (veya ilgili makine) üzerindeki gerçek proje klasörüne** `write_file` / `edit_file` ile yaz, yerel araçlarla (`terraform`, `tofu`, `git`, `go`, `bun` vb.) orada test et ve gerçek projede commit et.
4. `/workspace/coolify` içine **ASLA** dosya oluşturma veya commit atma!
