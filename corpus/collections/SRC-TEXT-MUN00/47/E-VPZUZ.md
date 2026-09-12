---
schema: qual/card@1
id: E-VPZUZ
kind: problem
title: Equicontinuous pointwise limits converge compactly
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Function Spaces
relations: []
review: draft
---

::: {.exercise}

Let $(Y, d)$ be a metric space; let $f_n: X \to Y$ be a sequence of continuous functions; let $f: X \to Y$ be a function (not necessarily continuous).
Suppose $f_n$ converges to $f$ in the topology of pointwise convergence.
Show that if $\ts{f_n}$ is equicontinuous, then $f$ is continuous and $f_n$ converges to $f$ in the topology of compact convergence.
:::

::: {.solution}
Fix $x\in X$ and $\varepsilon>0$. Equicontinuity gives a neighborhood $U$ of $x$ such that
\[
d(f_n(y),f_n(x))<\varepsilon/3
\]
for all $y\in U$ and all $n$. Passing to the pointwise limit in $n$ gives $d(f(y),f(x))\le\varepsilon/3$ for $y\in U$, so $f$ is continuous.

Now let $K\subset X$ be compact and fix $\varepsilon>0$. For every $x\in K$, equicontinuity supplies a neighborhood $U_x$ such that
\[
d(f_n(y),f_n(x))<\varepsilon/3
\]
for all $n$ and $y\in U_x$; the same inequality holds for $f$ after passing to the limit. Choose $x_1,\dots,x_r$ with $K\subset\bigcup U_{x_i}$. Pointwise convergence gives $N$ such that for $n\ge N$ and every $i$,
\[
d(f_n(x_i),f(x_i))<\varepsilon/3.
\]
If $y\in K$, choose $i$ with $y\in U_{x_i}$. Then
\[
d(f_n(y),f(y))<\varepsilon.
\]
Hence convergence is uniform on every compact $K$, i.e. convergence in the compact-convergence topology.
:::
