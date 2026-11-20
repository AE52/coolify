# ⚠️ ZORUNLU KURAL: BU KLASÖR GERÇEK PROJE DEĞİLDİR — HER ŞEY `rustca_mcp.py` İLE YAPILIR!

## 🛑 ASLA YAPMA (CRITICAL)
1. **`/workspace/coolify` (`rustca-mcp` dalı) BOŞ BİR KÖPRÜ DİZİNİDİR.**
   - Bu dizine **ASLA** `infra/`, `docs/`, kod dosyası oluşturma veya `git commit` atma!
   - Kullanıcı `pardoon`, `rustca`, `akis-erp`, `egundem`, `ihg`, `istanbooltoday`, `gaphaber`, Huawei Cloud, sunucu veya herhangi bir proje hakkında iş istediğinde, o projenin gerçek dosyaları bu konteynerde değil, **kullanıcının canlı makinelerinde (`Mac mini`, `Mac Pro`, `Windows`, SSH sunucuları)** bulunur.
2. **"Bu repoda yok / ortamda kurulu değil / değiştiremiyorum" DEME!**
   - Senin elinde `python3 rustca_mcp.py` üzerinden **canlı makinelerde tam yetkili dosya okuma, kod düzenleme, dosya yazma, kabuk komutu çalıştırma (`exec`) ve uzak sunuculara SSH (`ssh_exec`)** erişimi vardır!
   - `RUSTCA_MCP_URL` ve `RUSTCA_MCP_TOKEN` ortamda hazırdır ve internet erişimi açıktır (`HTTP 200`).

---

## 🚀 HER GÖREVDE İLK YAPACAĞIN ADIMLAR (ZORUNLU)

1. **Projeleri ve çevrimiçi makineleri gör:**
   ```bash
   python3 rustca_mcp.py hub projects '{}'
   python3 rustca_mcp.py machines machines '{}'
   ```
2. **İlgili projenin gerçek klasörünü ve dosyalarını `Mac mini` (veya ilgili makine) üzerinde bul ve oku:**
   ```bash
   python3 rustca_mcp.py machines find_files '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon"}'
   python3 rustca_mcp.py machines read_file '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon/README.md"}'
   python3 rustca_mcp.py machines grep_search '{"machine":"Mac mini","path":"~/Desktop/projects/pardoon","query":"huawei"}'
   ```
3. **Gerçek kod değiştirme / dosya yazma (doğrudan kullanıcının makinesinde!):**
   ```bash
   python3 rustca_mcp.py machines edit_file '{"machine":"Mac mini","path":"~/Desktop/projects/...","old_string":"...","new_string":"..."}'
   python3 rustca_mcp.py machines write_file '{"machine":"Mac mini","path":"~/Desktop/projects/...","content":"..."}'
   ```
4. **Gerçek komut çalıştırma (`terraform`, `tofu`, `ansible`, `git`, `docker`, `bun`, `go`, `php artisan` vb. kullanıcının makinesinde veya SSH sunucusunda!):**
   ```bash
   python3 rustca_mcp.py machines exec '{"machine":"Mac mini","command":"cd ~/Desktop/projects/pardoon && git status && ls -la"}'
   python3 rustca_mcp.py machines ssh_targets '{}'
   python3 rustca_mcp.py machines ssh_exec '{"machine":"Mac mini","target":"<ssh-host>","command":"..."}'
   ```
5. **Tüm mevcut MCP araçlarını görmek istersen:**
   ```bash
   python3 rustca_mcp.py hub tools
   python3 rustca_mcp.py machines tools
   ```

## ✅ KISA ÖZET
- Sen yalnızca bu konteynerin içine hapsolmuş bir kodlayıcı değilsin — **`python3 rustca_mcp.py` senin gerçek makinelere, kod depolarına, SSH sunucularına, veritabanlarına ve canlı ortamlara açılan elin ve gözündür.**
- Kullanıcı *"yap bunları"* veya *"kontrol et"* dediğinde, sahte örnek dosyaları `/workspace/coolify` içine yazmak yerine **doğrudan `rustca_mcp.py` ile gerçek makinedeki gerçek dosyaları oku, düzenle, komutları çalıştır ve sonucu doğrula!**
