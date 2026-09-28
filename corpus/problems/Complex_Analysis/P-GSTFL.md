---
schema: qual/card@1
id: P-GSTFL
kind: problem
title: Uniformly continuous functions preserve uniform convergence of sequences
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Uniform Continuity
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{g_n}$ is a uniformly convergent sequence of functions from $\RR$ to $\RR$ and $f:\RR\to \RR$ is uniformly continuous.
Prove that the sequence $\theset{f\circ g_n}$ is uniformly convergent.
:::

::: {.solution}
Let $g_n\to g$ uniformly on $\mathbb R$. Fix $\varepsilon>0$. Since $f$ is
uniformly continuous, there exists $\delta>0$ such that
\[
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
\]
Uniform convergence of $g_n$ gives $N$ such that, for $n\ge N$,
\[
\sup_{x\in\mathbb R}|g_n(x)-g(x)|<\delta.
\]
Therefore for every $x\in\mathbb R$ and $n\ge N$,
\[
|f(g_n(x))-f(g(x))|<\varepsilon.
\]
Hence
\[
\sup_{x\in\mathbb R}|f(g_n(x))-f(g(x))|\le\varepsilon,
\]
so $f\circ g_n\to f\circ g$ uniformly.
:::
