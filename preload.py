from os import walk
from os.path import join, splitext
import re
import subprocess as sp

postDir = "_posts"

pattern_tikzs = re.compile(r"\$%%%tikzs\$((?:[\n]|.)*?)\$%%%tikzs\$")

CS = r"""\documentclass[dvisvgm]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{kotex}
\usepackage{tikz}
\usepackage{tkz-euclide}
\usepackage{pgfplots}
\usepackage{tikz-3dplot}
\pgfplotsset{compat=1.9}
\thispagestyle{empty}
\begin{document}
%s
\end{document}
"""


for path, dirs, files in walk(postDir):
    for file in files:
        temp_str = ""
        with open(join(path, file), "r", encoding="utf-8") as f:
            temp_str = f.read()

        temp_tikzs = pattern_tikzs.findall(temp_str)
        for i, ttkzs in enumerate( temp_tikzs):
            with open(join("assets\\tikzs", file + "." + str(i) + ".tex"), "w", encoding="utf-8") as f:
                f.write(CS%ttkzs)
            op = sp.call(
                "xelatex --no-pdf --output-directory={0} --interaction=nonstopmode --halt-on-error {1}".format(r"./assets/tikzs/", r"./assets/tikzs/" + file + "." + str(i) + ".tex")
            )
            print(join(".\\assets\\tikzs", file + "." + str(i) + ".tex"))
            if op == 1:
                continue

            temp_dvifname = join("assets\\tikzs", file + "." + str(i) + ".xdv")
            temp_svgfname = join("assets\\tikzs", file + "." + str(i) + ".svg")
            op2 = sp.call(
                "dvisvgm --bbox=min -o {1} --clipjoin -e --no-fonts {0}".format(temp_dvifname, temp_svgfname)
            )






