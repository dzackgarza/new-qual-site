---
schema: qual/card@1
id: P-MW6OS
kind: problem
title: Let $\mathcal{H}$ be an infinite dimensional Hilbert space. Determine…
classification:
  areas:
  - real-analysis
  topics:
  - weak-convergence
  - hilbert-spaces
  - compactness
relations: []
review: draft
---

::: {.problem title="?"}
Let $\mathcal{H}$ be an infinite dimensional Hilbert space.
Determine if the following statements are true or false.
If true, provide a proof.
If false, provide a counter example.

a. A sequence $\{f_n\}$ in $\mathcal{H}$ with $\|f_n\| = 1$ for all $n$ has a subsequence that converges in $\mathcal{H}$.
b. A sequence $\{f_n\}$ in $\mathcal{H}$ with $\|f_n\| = 1$ for all $n$ has a subsequence that converges weakly in $\mathcal{H}$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (a) is FALSE.
    Proof: let $\{e_n\}$ be an orthonormal basis of $\mathcal{H}$, so $\|e_n\| = 1$ for all $n$. For $n \ne m$, $\|e_n - e_m\|^2 = \|e_n\|^2 + \|e_m\|^2 = 2$ (Pythagoras), so no subsequence of $\{e_n\}$ is Cauchy; $\{e_n\}$ has no convergent subsequence. (The unit sphere of an infinite-dimensional Hilbert space is not compact.)
<1>2. (b) is TRUE.
    Proof: let $\{f_n\}$ be any sequence with $\|f_n\| = 1$; we show it has a weakly convergent subsequence. Fix an orthonormal basis $\{e_k\}$ of $\mathcal{H}$.
<2>1. For each fixed $k$, the scalar sequence $\{\langle f_n, e_k\rangle\}_n$ is bounded by $\|f_n\|\|e_k\| = 1$, so by Bolzano–Weierstrass it has a convergent subsequence. A diagonal argument yields one subsequence $\{f_{n_j}\}$ along which $\langle f_{n_j}, e_k\rangle$ converges for every $k$; write $\alpha_k = \lim_j \langle f_{n_j}, e_k\rangle$.
<2>2. The sequence $\{\alpha_k\}$ is in $\ell^2$, so $\phi := \sum_k \alpha_k e_k \in \mathcal{H}$.
    Proof: for every $K$, $\sum_{k=1}^K|\alpha_k|^2 = \lim_j\sum_{k=1}^K|\langle f_{n_j}, e_k\rangle|^2 \le \limsup_j\|f_{n_j}\|^2 = 1$ (Bessel), so $\sum_k|\alpha_k|^2 \le 1$.
<2>3. $f_{n_j} \rightharpoonup \phi$.
    Proof: given $y \in \mathcal{H}$ and $\epsilon > 0$, choose $K$ with $\|y - \sum_{k=1}^K\langle y, e_k\rangle e_k\| < \epsilon/4$. For large $j$,
    \[\left|\langle f_{n_j}, y\rangle - \langle \phi, y\rangle\right| \le \sum_{k=1}^K|\langle f_{n_j} - \phi, e_k\rangle||\langle y, e_k\rangle| + \frac{\epsilon}{2} < \epsilon,\]
    since the first sum tends to $0$ (each $\langle f_{n_j} - \phi, e_k\rangle \to 0$) and the remainder term is bounded by $2\|f_{n_j}\|\cdot\epsilon/4 = \epsilon/2$ by Cauchy–Schwarz. Hence $\langle f_{n_j}, y\rangle \to \langle\phi, y\rangle$ for all $y$.
<1>3. Q.E.D.
:::
