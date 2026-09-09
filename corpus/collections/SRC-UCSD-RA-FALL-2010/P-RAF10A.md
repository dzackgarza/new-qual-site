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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2010 real-analysis qualifying exam.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
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

::: solution
<1>1. Part (a) is false.
::: proof
In the Banach space $\ell^2$, let $e_n$ be the standard basis vectors. Then
\[
\|e_n\|_2=1
\]
for every $n$, so $(e_n)$ is bounded. But for $m\ne n$,
\[
\|e_n-e_m\|_2=\sqrt2.
\]
Hence no subsequence is Cauchy, and therefore no subsequence converges in norm.
:::

<1>2. Part (b) is false.
::: proof
Suppose $f_n\to0$ in $L^1([0,1])$. Choose a subsequence $(f_{n_k})$ such that
\[
\|f_{n_k}\|_1<2^{-2k}.
\]
Set
\[
E_k:=\{|f_{n_k}|>2^{-k}\}.
\]
By Chebyshev's inequality,
\[
m(E_k)\le 2^k\|f_{n_k}\|_1<2^{-k}.
\]
Thus
\[
\sum_{k=1}^\infty m(E_k)<\infty.
\]
By the Borel--Cantelli lemma, almost every $x$ belongs to only finitely many $E_k$. Hence for almost every $x$,
\[
|f_{n_k}(x)|\le2^{-k}
\]
for all sufficiently large $k$, so $f_{n_k}(x)\to0$. Therefore every $L^1$-null sequence has a subsequence converging pointwise to $0$ almost everywhere, contradicting the asserted existence.
:::

<1>3. Part (c) is false.
::: proof
Let
\[
h=\mathbf1_{[0,1/2]}.
\]
We claim that
\[
\|h-g\|_\infty\ge\frac12
\]
for every $g\in C([0,1])$, where the norm is the essential supremum.

Indeed, if the essential-supremum distance were $<1/2$, then for some $\delta>0$ we would have
\[
|g(x)-1|\le\frac12-\delta
\]
for almost every $x<1/2$, and
\[
|g(x)|\le\frac12-\delta
\]
for almost every $x>1/2$. Continuity upgrades these inequalities to all points on the respective open half-intervals, forcing
\[
g(1/2)\ge\frac12+\delta
\quad\text{and}\quad
g(1/2)\le\frac12-\delta,
\]
a contradiction. Thus $C([0,1])$ is not dense in $L^\infty([0,1])$.
:::

<1>4. Part (d) is true.
::: proof
The functions
\[
e_n(x)=e^{2\pi i n x}
\]
form an orthonormal sequence in $L^2([0,1])$. For any $g\in L^2([0,1])$, Bessel's inequality gives
\[
\sum_{n=1}^\infty |\langle g,e_n\rangle|^2\le\|g\|_2^2.
\]
Hence
\[
\langle g,e_n\rangle\to0.
\]
Therefore $e_n\rightharpoonup0$ weakly in $L^2([0,1])$.
:::

<1>5. Part (e) is true.
::: proof
By Hölder's inequality applied to $(a_j)_{j=1}^n$ and $(1)_{j=1}^n$ with exponents $q$ and $p$,
\[
\sum_{j=1}^n a_j
\le\sum_{j=1}^n|a_j|
\le
\left(\sum_{j=1}^n|a_j|^q\right)^{1/q}
\left(\sum_{j=1}^n1^p\right)^{1/p}.
\]
Since the second factor is $n^{1/p}$,
\[
\boxed{
\sum_{j=1}^n a_j
\le n^{1/p}\left(\sum_{j=1}^n|a_j|^q\right)^{1/q}.}
\]
:::

<1>6. Part (f) is true.
::: proof
The specified topology is exactly the product topology on
\[
Y=[-\pi,\pi]^{\mathbb R},
\]
because it is the weakest topology making every coordinate projection
\[
p_r(f)=f(r)
\]
continuous. Each factor $[-\pi,\pi]$ is compact. By Tychonoff's theorem, their arbitrary product is compact. Hence $Y$ is compact.
:::
:::
