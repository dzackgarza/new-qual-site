---
schema: qual/card@1
id: P-WMJZB
kind: problem
title: "Let $\\mathcal{H}$ be a Hilbert space equipped with an inner product $(\\cdot,\\cdot)$ and\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - weak-convergence
  - hilbert-spaces
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $\mathcal{H}$ be a Hilbert space equipped with an inner product $(\cdot,\cdot)$ and a norm $\|\cdot\| = (\cdot,\cdot)^{1/2}$.
Recall the following: A sequence $\{f_k\} \subset \mathcal{H}$ is said to converge to $f \in \mathcal{H}$ if $\|f_k - f\| \to 0$.
A sequence $\{f_k\} \subset \mathcal{H}$ is said to converge weakly to $f \in \mathcal{H}$ if $(f_k, g) \to (f,g)$ for any $g \in \mathcal{H}$.
Prove the following statements:

a. $\{f_k\}$ converges to $f$ if and only if $\|f_k\| \to \|f\|$ and $\{f_k\}$ converges weakly to $f$.
b. If $\mathcal{H}$ is a finite dimensional Hilbert space, then the weak convergence implies convergence.
Give a counter example to show that weak convergence does not necessarily imply convergence in an infinite dimensional Hilbert space.
c. If a sequence $\{f_k\}$ converges weakly to $f$, then there exists a subsequence $\{f_{k_n}\}$ such that $$\frac{f_{k_1}+\cdots+f_{k_n}}{n}$$ converges to $f$.
(You may use the fact that a weakly convergent sequence is a bounded sequence.)
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove (a) strong convergence iff norm + weak convergence; (b) finite-dimensional: weak implies strong, with infinite-dimensional counterexample; (c) Cesàro means of a weakly convergent sequence converge to $f$ after passing to a subsequence.

<1>1. (a) $f_k \to f$ strongly iff $\|f_k\| \to \|f\|$ and $f_k \rightharpoonup f$ weakly.
<2>1. If $f_k \to f$ strongly, then $\|f_k\| \to \|f\|$ and $f_k \rightharpoonup f$.
Proof: continuity of the norm; and $|(f_k - f, g)| \le \|f_k - f\|\|g\| \to 0$ for every $g$.
<2>2. If $\|f_k\| \to \|f\|$ and $f_k \rightharpoonup f$: $\|f_k - f\|^2 = \|f_k\|^2 - 2\operatorname{Re}(f_k, f) + \|f\|^2 \to \|f\|^2 - 2\|f\|^2 + \|f\|^2 = 0$.
Proof: expand the norm; $(f_k, f) \to (f, f) = \|f\|^2$ by weak convergence with test vector $f$.
<2>3. Q.E.D. Proof: <2>1 and <2>2 are the two directions.

<1>2. (b) Finite-dimensional: weak convergence implies strong convergence.
<2>1. Let $\{e_1, \ldots, e_n\}$ be an orthonormal basis; $f_k = \sum_j (f_k, e_j)e_j$ and $f = \sum_j (f, e_j)e_j$.
<2>2. $\|f_k - f\|^2 = \sum_j |(f_k - f, e_j)|^2 \to 0$.
Proof: weak convergence gives $(f_k, e_j) \to (f, e_j)$ for each basis vector; the sum is finite.
<2>3. Q.E.D. Proof: <2>2 shows $f_k \to f$ strongly.

<1>3. (b) Counterexample in infinite dimensions: $f_k = e_k$, an orthonormal sequence in $\mathcal H = \ell^2$ (or $L^2$). <2>1. $e_k \rightharpoonup 0$ weakly: $(e_k, g) = g_k \to 0$ for every $g$ by Bessel's inequality ($\sum_k|g_k|^2 < \infty$). <2>2. $e_k$ does not converge strongly: $\|e_k\| = 1 \not\to 0$.
<2>3. Q.E.D. Proof: <2>1 and <2>2: weak convergence without strong convergence.

<1>4. (c) There is a subsequence $k_n$ with $\sigma_n := \frac{f_{k_1} + \cdots + f_{k_n}}{n} \to f$ strongly (Banach–Saks).
<2>1. $\{f_k\}$ is bounded: $\|f_k\| \le B$ for all $k$ (given fact).
<2>2. Choose $k_n$ recursively so that $|(f_{k_n} - f,\, \sigma_{n-1} - f)| < \frac{1}{n}$ for $n \ge 2$, where $\sigma_{n-1} := \frac{f_{k_1} + \cdots + f_{k_{n-1}}}{n-1}$.
Proof: $\sigma_{n-1} - f$ is a fixed vector once $k_1, \ldots, k_{n-1}$ are chosen; weak convergence $(f_k - f, g) \to 0$ for $g = \sigma_{n-1} - f$ lets us pick $k_n > k_{n-1}$ making the inner product $< 1/n$.
<2>3. $\|\sigma_n - f\|^2 = \frac{1}{n^2}\left(\sum_{j=1}^n\|f_{k_j} - f\|^2 + 2\sum_{1 \le j < l \le n}(f_{k_j} - f,\, f_{k_l} - f)\right)$.
Proof: expand $\|\frac1n\sum_j(f_{k_j} - f)\|^2$.
<2>4. The diagonal terms are small: $\frac{1}{n^2}\sum_j\|f_{k_j} - f\|^2 \le \frac{(B + \|f\|)^2}{n} \to 0$.
Proof: each $\|f_{k_j} - f\| \le B + \|f\|$, and there are $n$ of them.
<2>5. The cross terms are small: $\frac{2}{n^2}\sum_{j<l}(f_{k_j} - f, f_{k_l} - f) = \frac{2}{n^2}\sum_{l=2}^n (f_{k_l} - f,\, \sum_{j<l}(f_{k_j} - f)) = \frac{2}{n^2}\sum_{l=2}^n (l-1)(f_{k_l} - f,\, \sigma_{l-1} - f) \le \frac{2}{n^2}\sum_{l=2}^n \frac{l-1}{l} \le \frac{2}{n} \to 0$.
Proof: $\sum_{j<l}(f_{k_j} - f) = (l-1)(\sigma_{l-1} - f)$, and $|(f_{k_l} - f, \sigma_{l-1} - f)| < 1/l$ by <2>2. <2>6. $\sigma_n \to f$ strongly.
Proof: <2>3–<2>5: $\|\sigma_n - f\|^2 \to 0$.
<2>7. Q.E.D. Proof: <2>2–<2>6 prove (c) — the classical Banach–Saks theorem.
:::
