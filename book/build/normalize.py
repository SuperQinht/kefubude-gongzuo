"""规范化章节：引号统一为“”‘’，脚注标签加章节前缀避免跨章冲突。"""
import re, sys, pathlib
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out.mkdir(exist_ok=True)
for f in sorted(src.glob("[0-9][0-9]_[0-9][0-9].md")):
    pre = f.stem.replace("_", "")
    res = []
    for ln in f.read_text(encoding="utf-8").splitlines():
        ln = ln.replace("「", "“").replace("」", "”").replace("『", "‘").replace("』", "’")
        n = [0]
        def q(m):
            n[0] += 1; return "“" if n[0] % 2 else "”"
        ln = re.sub(r'"', q, ln)
        ln = re.sub(r"\[\^([^\]]+)\]", lambda m: f"[^c{pre}-{m.group(1)}]", ln)
        res.append(ln)
    (out / f.name).write_text("\n".join(res) + "\n", encoding="utf-8")
