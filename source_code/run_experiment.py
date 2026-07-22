import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_toolkit"))
import build_med_paper as B, medical_papers_content as MP
c = MP.CONTENT[12]
B._run(os.path.join(os.path.dirname(__file__),"..","figures"),
       os.path.join(os.path.dirname(__file__),"..","outputs"), list(c["iters"]), c["demo_key"])
print("experiment done paper 12")
