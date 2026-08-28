---
schema: qual/card@1
id: P-RAF10A
kind: problem
title: "True/false on Banach spaces, L^p spaces, and topologies"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
For each of the following, determine if the statement is true (always) or false (not always true).
If true, give a brief proof, citing appropriate theorem(s); if false, give a counterexample or prove it is false in some other rigorous way.

(a) Any bounded sequence in a Banach space has a convergent subsequence.

(b) There exists a sequence of functions $f_n \in L^1([0,1])$ such that $f_n$ converges to $0$ in $L^1$, but there is no subsequence $f_{n_k}$ that converges pointwise to $0$ a.e.

(c) The space $C([0,1])$ is dense in $L^\infty([0,1])$.

(d) The sequence $e^{i2\pi n x}$ converges to $0$ weakly in $L^2([0,1])$.

(e) Let $a_j \in \mathbb{R}$, $j = 1, \ldots, n$, and $\frac{1}{p} + \frac{1}{q} = 1$, $1 < p < \infty$.
Then
$$
\sum_{j=1}^{n} a_j \leq n^{1/p} \left(\sum_{j=1}^{n} |a_j|^q\right)^{1/q}.
$$

(f) Let $Y = \{f : \mathbb{R} \to [-\pi, \pi]\}$.
Let $[-\pi, \pi]$ have its natural topology, and give $Y$ the weakest topology such that the mappings $p_r : Y \to [-\pi, \pi]$ defined by $p_r(f) := f(r)$ are continuous for all $r \in \mathbb{R}$.
Then $Y$ is compact.
:::

::: {.solution}
**Goal.** Determine the truth of each statement.

<1>1. (a) FALSE.
<2>1. Counterexample: the unit ball of $\ell^2$ (or any infinite-dimensional Banach space).
Proof: the sequence of standard basis vectors $e_n$ is bounded ($\|e_n\| = 1$) but has no convergent subsequence (since $\|e_n - e_m\| = \sqrt2$ for $n \neq m$).
<2>2. This fails because the unit ball of an infinite-dimensional Banach space is not compact.
Proof: Riesz's lemma / non-compactness of the unit ball in infinite dimensions.

<1>2. (b) TRUE.
<2>1. Take $f_n = n \mathbf 1_{[0, 1/n]}$ (the "typewriter" sequence).
Proof: define the sequence.
<2>2. $\|f_n\|_1 = 1 \cdot n \cdot (1/n) = 1 \not\to 0$... this does not converge to $0$ in $L^1$.
Proof: recompute — we need $f_n \to 0$ in $L^1$ but no a.e. convergent subsequence.
<2>3. Use the standard example: $f_n = \mathbf 1_{[j/2^k, (j+1)/2^k]}$ (sliding intervals of shrinking length).
Proof: the typewriter sequence converges to $0$ in $L^1$ (each $f_n$ has $L^1$ norm $2^{-k} \to 0$), but every point is hit infinitely often, so no subsequence converges pointwise a.e. to $0$.
<2>4. Hence the statement is true.
Proof: <1>2.3 gives the example.

<1>3. (c) FALSE.
<2>1. $C([0,1])$ is not dense in $L^\infty([0,1])$.
Proof: $L^\infty$ is the uniform closure of simple functions, and $C([0,1])$ is closed in $L^\infty$ (uniform limit of continuous functions is continuous), so its closure is $C([0,1]) \neq L^\infty$.
<2>2. Counterexample: $\mathbf 1_{[0, 1/2]}$ is not in the $L^\infty$-closure of $C([0,1])$.
Proof: any continuous function is at distance $\ge 1/2$ from $\mathbf 1_{[0,1/2]}$ in the $L^\infty$ norm (at the jump).

<1>4. (d) TRUE.
<2>1. $e^{2\pi i n x} \to 0$ weakly in $L^2([0,1])$.
Proof: the functions $e^{2\pi i n x}$ form an orthonormal basis of $L^2([0,1])$, so by Bessel's inequality, for any $g \in L^2$, $\langle g, e^{2\pi i n x}\rangle \to 0$ (the Fourier coefficients tend to $0$).
<2>2. Hence the sequence converges weakly to $0$.
Proof: the inner products with every test function tend to $0$.

<1>5. (e) TRUE.
<2>1. $\sum_{j=1}^n a_j \le n^{1/p}\qty(\sum_{j=1}^n |a_j|^q)^{1/q}$.
Proof: this is Hölder's inequality applied to the vectors $(a_1, \dots, a_n)$ and $(1, \dots, 1)$: $\sum a_j \le \qty(\sum |a_j|^q)^{1/q}\qty(\sum 1^p)^{1/p} = n^{1/p}\qty(\sum |a_j|^q)^{1/q}$.

<1>6. (f) TRUE.
<2>1. $Y = \theset{f : \RR \to [-\pi, \pi]}$ with the product topology (weakest making all $p_r$ continuous) is $[-\pi, \pi]^\RR$.
Proof: $Y$ is the product of copies of $[-\pi, \pi]$ indexed by $\RR$.
<2>2. $[-\pi, \pi]$ is compact, so $Y = [-\pi, \pi]^\RR$ is compact.
Proof: Tychonoff's theorem: a product of compact spaces is compact.

<1>7. Q.E.D.
Proof: (a) F, (b) T, (c) F, (d) T, (e) T, (f) T.
:::
