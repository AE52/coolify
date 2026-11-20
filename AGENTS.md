# ⚠️ ZORUNLU KURAL: BU KLASÖR GERÇEK PROJE DEĞİLDİR — HER ŞEY `rustca_mcp.py` İLE YAPILIR!

## 🛑 ASLA YAPMA (CRITICAL)
1. **`/workspace/coolify` (`rustca-mcp` dalı) BOŞ BİR KÖPRÜ DİZİNİDİR.**
   - Bu dizine **ASLA** `infra/`, `docs/` veya sahte proje kodu yazıp `git commit` atma!
   - Tüm gerçek projeler kullanıcının canlı makinelerinde (`Mac mini`, `Mac Pro`, `Windows`, SSH sunucuları) bulunur.
2. **"Bu repoda yok / kurulu değil / değiştiremiyorum" DEME!**
   - `python3 rustca_mcp.py` üzerinden canlı makinelerde tam yetkili dosya okuma, kod düzenleme, dosya yazma, kabuk komutu (`exec`), SSH (`ssh_exec`) ve tarayıcı profilleri (`browser_profiles`) erişimine sahipsin (`HTTP 200`, `RUSTCA_MCP_TOKEN` hazır).

---

## 📂 MAC MINI PROJE HARİTASI (ÖNCE BURALARA BAK!)
- **Ana Proje Kökü:** `~/Desktop/projects/`
  - `~/Desktop/projects/rustca` — Rustca Hub (Go) + Panel (Next.js)
  - `~/Desktop/projects/pardoon` — Pardoon ana doküman/ansible/state (`docs/`, `ansible/`, `state/ninesix-ops`, `state/devops`)
  - `~/Desktop/projects/egundem` — Egündem video/mikroservisler
  - `~/Desktop/projects/ihg` — I Love Home Glass / ikas entegrasyonları
  - `~/Desktop/projects/erenozdemir-web`
- **Müşteri & Ops Depoları:** `~/Desktop/projects/musteriler/`
  - `~/Desktop/projects/musteriler/ninesix-ops` — **NineSixPlus Ops / Altyapı**
  - `~/Desktop/projects/musteriler/ninesix-backend`
  - `~/Desktop/projects/musteriler/ninesix-admin`
  - `~/Desktop/projects/musteriler/pardoon-web-nine-six`
  - Ayrıca `ls ~/Desktop/projects/musteriler` ile tüm müşteri repolarını (`gaphaber`, `istanbooltoday` vb.) listele!
- **Diğer Masaüstü Projeleri:** `~/Desktop/akis-erp`, `~/Desktop/pardoon`

---

## 🚀 HER GÖREVDE İLK YAPACAĞIN ADIMLAR
1. **Projeleri, makineleri, SSH hedeflerini ve tarayıcı profillerini keşfet:**
   ```bash
   python3 rustca_mcp.py hub projects '{}'
   python3 rustca_mcp.py machines machines '{}'
   python3 rustca_mcp.py machines ssh_targets '{}'
   python3 rustca_mcp.py hub browser_profiles '{}'
   ```
2. **Gerçek dosyaları bul, oku ve ara:**
   ```bash
   python3 rustca_mcp.py machines find_files '{"machine":"Mac mini","path":"~/Desktop/projects/musteriler/ninesix-ops"}'
   python3 rustca_mcp.py machines read_file '{"machine":"Mac mini","path":"..."}'
   python3 rustca_mcp.py machines grep_search '{"machine":"Mac mini","path":"~/Desktop/projects","query":"huawei"}'
   ```
3. **Doğrudan gerçek makinede kod düzenle / komut veya SSH çalıştır:**
   ```bash
   python3 rustca_mcp.py machines edit_file '{"machine":"Mac mini","path":"...","old_string":"...","new_string":"..."}'
   python3 rustca_mcp.py machines write_file '{"machine":"Mac mini","path":"...","content":"..."}'
   python3 rustca_mcp.py machines exec '{"machine":"Mac mini","command":"..."}'
   python3 rustca_mcp.py machines ssh_exec '{"machine":"Mac mini","target":"<host>","command":"..."}'
   ```
