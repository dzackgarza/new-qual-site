---
schema: qual/card@1
id: P-B2ZXW
kind: problem
title: $\lim_n\|f+g(\,\cdot\,-n)\|_1=\|f\|_1+\|g\|_1$ for $f,g\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Small Tails
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 4 of the official UGA January 2021 Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Replaced the legacy tail proof, which contained false equalities, reversed inequality labels, and sign inconsistencies, by a compact-support approximation argument.
---

::: {.problem}
Let $f, g$ be Lebesgue integrable on $\RR$ and let $g_n(x) \da g(x- n)$.
Prove that
\[
\lim_{n\to \infty } \norm{f + g_n}_1 = \norm{f}_1 + \norm{g}_1
.\]
:::

::: {.concept}
\envlist

- For $f\in L^1(X)$, $\norm{f}_1 \da \int_X \abs{f(x)} \dx < \infty$.

- Small tails in $L^1$: if $f\in L^1(\RR^n)$, then for every $\eps>0$ there exists a radius $R$ such that
\[
\norm{f}_{L^1(B_R^c)} < \eps
.\]

- For $n>2R$, the truncations $f\mathbf{1}_{[-R,R]}$ and $g_n\mathbf{1}_{[n-R,n+R]}$ have disjoint supports:

![Shifting density](../../assets/figures/densities.png)

- For $R>0$, $\norm{f}_1-\norm{f\mathbf{1}_{[-R,R]}}_1=\norm{f}_{L^1([-R,R]^c)}$.

- If $a,b\in\RR$ and $a-\eps \leq b \leq a+\eps$ for every $\eps>0$, then $b=a$.

:::

::: {.solution}

::: pf

::: pf-step
Approximate by compactly supported truncations.

::: pf-proof
Fix $\varepsilon>0$. Choose $R>0$ such that, for
\[
f_R=f\mathbf1_{[-R,R]},\qquad g_R=g\mathbf1_{[-R,R]},
\]
we have
\[
\|f-f_R\|_1<\varepsilon,
\qquad
\|g-g_R\|_1<\varepsilon.
\]
If $n>2R$, then $f_R$ and $(g_R)_n(x):=g_R(x-n)$ have disjoint supports, so
\[
\|f_R+(g_R)_n\|_1=\|f_R\|_1+\|g_R\|_1.
\]
:::

:::

::: pf-step
Compare with the original functions.

::: pf-proof
Translation invariance gives
\[
\|g_n-(g_R)_n\|_1=\|g-g_R\|_1<\varepsilon.
\]
Hence
\[
\left|\|f+g_n\|_1-\|f_R+(g_R)_n\|_1\right|<2\varepsilon.
\]
Also
\[
0\le\|f\|_1-\|f_R\|_1<\varepsilon,
\qquad
0\le\|g\|_1-\|g_R\|_1<\varepsilon.
\]
Thus, for $n>2R$,
\[
\left|\|f+g_n\|_1-(\|f\|_1+\|g\|_1)\right|<4\varepsilon.
\]
Letting $\varepsilon\downarrow0$ proves
\[
\boxed{\lim_{n\to\infty}\|f+g(\cdot-n)\|_1=\|f\|_1+\|g\|_1.}
\]
:::

:::

:::
