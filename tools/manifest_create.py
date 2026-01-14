import json
from pathlib import Path

TAG = "v1.0.2"  # change this
repo = "abubakr3800/CCT_VS_CRI"

manifest = {
    "version": TAG.lstrip("v"),
    "bundle_url": f"https://github.com/{repo}/releases/download/{TAG}/dist.zip",
}

out = Path("dist") / "manifest.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print("Wrote:", out)
