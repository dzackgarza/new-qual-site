---
schema: qual/card@1
id: P-JHUFA05ANB
kind: problem
title: 'Translation continuity of $L^1$ functions on the line'
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the preserved JHU analysis qualifying exam collection containing this May 2006 card.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1(\mathbb R)$. Prove that
\[
\lim_{h\to0}\int_{\mathbb R}|f(x+h)-f(x)|\,dx=0.
\]
:::

::: {.solution}
Fix $\varepsilon>0$. Choose $g\in C_c(\mathbb R)$ such that
\[
\|f-g\|_1<\frac{\varepsilon}{3},
\]
using density of $C_c(\mathbb R)$ in $L^1(\mathbb R)$.

Because $g$ is continuous with compact support, it is uniformly continuous. If $K$ is a compact interval containing the support of $g$ and all its sufficiently small translates, then for small $h$ one has
\[
\|g(\cdot+h)-g\|_1
\le m(K)\,\sup_{x\in K}|g(x+h)-g(x)|
\longrightarrow0.
\]
Hence there exists $\delta>0$ such that $|h|<\delta$ implies
\[
\|g(\cdot+h)-g\|_1<\frac{\varepsilon}{3}.
\]

Translations preserve Lebesgue measure, so
\[
\|f(\cdot+h)-g(\cdot+h)\|_1=\|f-g\|_1.
\]
Therefore, for $|h|<\delta$,
\[
\begin{aligned}
\|f(\cdot+h)-f\|_1
&\le \|f(\cdot+h)-g(\cdot+h)\|_1
 +\|g(\cdot+h)-g\|_1
 +\|g-f\|_1\\
&<\varepsilon.
\end{aligned}
\]
Thus
\[
\|f(\cdot+h)-f\|_1\longrightarrow0
\qquad(h\to0).
\]
:::
