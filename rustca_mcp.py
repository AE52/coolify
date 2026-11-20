#!/usr/bin/env python3
"""Zero-dependency CLI client for Rustca MCP (/mcp/hub and /mcp/machines).
Uses RUSTCA_MCP_TOKEN and RUSTCA_MCP_URL from environment secrets.

Usage:
  python3 rustca_mcp.py hub tools
  python3 rustca_mcp.py hub projects
  python3 rustca_mcp.py hub project_inspect '{"project":"pardoon"}'
  python3 rustca_mcp.py hub task_checkpoint_get '{}'
  python3 rustca_mcp.py machines machines
  python3 rustca_mcp.py machines exec '{"machine":"Mac mini","command":"ls -la"}'
  python3 rustca_mcp.py machines read_file '{"machine":"Mac mini","path":"~/Desktop/projects/..."}'
"""
import json, os, sys, urllib.request, urllib.error

BASE = os.environ.get("RUSTCA_MCP_URL", "https://rustca.erenozdemir.com.tr").rstrip("/")
TOKEN = os.environ.get("RUSTCA_MCP_TOKEN", "").strip()

def _post(url, payload, sess_id=None):
    hdrs = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if sess_id:
        hdrs["Mcp-Session-Id"] = sess_id
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=hdrs)
    with urllib.request.urlopen(req, timeout=55) as resp:
        new_sid = resp.headers.get("Mcp-Session-Id") or sess_id
        raw = resp.read().decode("utf-8", "ignore")
    for line in raw.splitlines():
        if line.startswith("data: "):
            raw = line[6:]
            break
    return json.loads(raw), new_sid

def main():
    if not TOKEN:
        print("ERROR: RUSTCA_MCP_TOKEN env secret is not set.", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) < 3:
        print("Usage: python3 rustca_mcp.py <hub|machines> <tool_name|tools> [json_args]", file=sys.stderr)
        sys.exit(1)
    target = sys.argv[1]
    tool = sys.argv[2]
    args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    url = f"{BASE}/mcp/{target}"

    _, sid = _post(url, {
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "codex-cloud", "version": "1.0"}},
    })
    if tool == "tools":
        res, _ = _post(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}, sid)
        for t in res.get("result", {}).get("tools", []):
            print(f"- {t['name']}: {t.get('description', '')[:120]}")
        return
    res, _ = _post(url, {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": tool, "arguments": args}}, sid)
    for c in res.get("result", {}).get("content", []):
        if c.get("type") == "text":
            print(c["text"])

if __name__ == "__main__":
    main()
