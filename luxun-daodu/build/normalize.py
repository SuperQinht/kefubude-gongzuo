import re, sys, pathlib
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out.mkdir(exist_ok=True)
for f in sorted(src.glob("0*.md")):
    lines, res, fence = f.read_text(encoding="utf-8").splitlines(), [], False
    for ln in lines:
        if ln.startswith("```"): fence = not fence; res.append(ln); continue
        if fence or ln.startswith(":::"): res.append(ln); continue
        ln = ln.replace("「", "“").replace("」", "”").replace("『", "‘").replace("』", "’")
        n = [0]
        def q(m):
            n[0] += 1; return "“" if n[0] % 2 else "”"
        ln = re.sub(r'"', q, ln)
        res.append(ln)
    (out / f.name).write_text("\n".join(res) + "\n", encoding="utf-8")
