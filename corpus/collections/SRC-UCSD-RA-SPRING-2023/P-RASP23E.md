---
schema: qual/card@1
id: P-RASP23E
kind: problem
title: "Banach limit as weak* cluster point not from l^1"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\ell^\infty$ denote the vector space of sequences of complex numbers $x = (x_1, x_2, \ldots)$ with $\|x\|_\infty := \sup_n |x_n| < \infty$.
Define $\phi_n(x) := \frac{1}{n} \sum_{k=1}^{n} x_k$.

Prove that

(i) $\phi_n \in (\ell^\infty)^*$ and $\{\phi_n\}$ has a weak* cluster point $\phi$;

(ii) $\phi$ is an element of $(\ell^\infty)^*$ which does not arise from an element of $\ell^1$.
:::


::: solution
<1>1. Show that the Cesàro functionals lie in the dual unit ball.
::: proof
For $x\in\ell^\infty$,
\[
|\phi_n(x)|
=\left|\frac1n\sum_{k=1}^nx_k\right|
\le\frac1n\sum_{k=1}^n|x_k|
\le\|x\|_\infty.
\]
Thus $\phi_n\in(\ell^\infty)^*$ and $\|\phi_n\|\le1$. On the constant sequence
\[
\mathbf1=(1,1,\dots),
\]
we have $\phi_n(\mathbf1)=1$, so in fact
\[
\|\phi_n\|=1.
\]
:::

<1>2. Obtain a weak* cluster point.
::: proof
The sequence $(\phi_n)$ lies in the closed unit ball of $(\ell^\infty)^*$. By the Banach--Alaoglu theorem, this ball is compact in the weak* topology
\[
\sigma((\ell^\infty)^*,\ell^\infty).
\]
Hence the sequence has a weak* cluster point $\phi$; equivalently, there is a subnet $(\phi_{n_\alpha})$ converging weak* to $\phi$. Since the unit ball is weak* closed,
\[
\phi\in(\ell^\infty)^*,
\qquad
\|\phi\|\le1.
\]
Moreover,
\[
\phi(\mathbf1)
=\lim_\alpha\phi_{n_\alpha}(\mathbf1)
=1,
\]
so $\|\phi\|=1$.
:::

<1>3. Show that $\phi$ vanishes on $c_0$.
::: proof
If $x=(x_k)\in c_0$, then $x_k\to0$. Cesàro convergence gives
\[
\phi_n(x)=\frac1n\sum_{k=1}^nx_k\longrightarrow0.
\]
Therefore every weak* cluster point satisfies
\[
\phi(x)=0
\qquad(x\in c_0).
\]
In particular, for the standard basis vector $e_j$,
\[
\phi(e_j)=0
\qquad(j\ge1).
\]
:::

<1>4. Rule out representation by an element of $\ell^1$.
::: proof
Suppose that there were $a=(a_j)\in\ell^1$ such that
\[
\phi(x)=\sum_{j=1}^\infty a_jx_j
\qquad(x\in\ell^\infty).
\]
Evaluating at $e_j$ gives
\[
a_j=\phi(e_j)=0
\]
for every $j$. Hence $a=0$, so the represented functional would be identically zero. But Step 2 gives
\[
\phi(\mathbf1)=1.
\]
This contradiction shows that
\[
\boxed{\phi\text{ is not induced by any element of }\ell^1.}
\]
:::
:::
