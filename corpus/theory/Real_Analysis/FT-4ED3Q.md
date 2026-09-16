---
schema: qual/card@1
id: FT-4ED3Q
kind: theorem
title: Continuity of translation in $L^1$
prompts:
- What is continuity in $L^1$, and how is it proved?
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
---

::: {.theorem}
For every $f \in L^{1}(\RR^n)$,
$$
\lim_{h \to 0} \int_{\RR^n}\abs{f(x+h)-f(x)}\,dx=0 .
$$
:::

::: {.proof}
Let $\varepsilon>0$.
Since compactly supported continuous functions are dense in $L^1(\RR^n)$, choose $g\in C_c(\RR^n)$ with $\norm{f-g}_{L^1}<\varepsilon/3$.
By translation invariance of Lebesgue measure, $\int\abs{f(x+h)-g(x+h)}\,dx=\norm{f-g}_{L^1}<\varepsilon/3$ for every $h$.
The function $g$ is uniformly continuous and, for $\abs{h}\le1$, $x\mapsto g(x+h)-g(x)$ vanishes outside the compact set $K=\supp g+\overline{B(0,1)}$, so $\int\abs{g(x+h)-g(x)}\,dx\le \vol(K)\sup_x\abs{g(x+h)-g(x)}<\varepsilon/3$ for $\abs{h}$ small enough.
The triangle inequality then gives $\int\abs{f(x+h)-f(x)}\,dx<\varepsilon$ for $\abs{h}$ small enough.
A detailed version is [[FR-EM6AL]].
:::
