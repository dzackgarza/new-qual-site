---
schema: qual/card@1
id: P-DQE3F
kind: problem
title: '$L^1$ convergence of an $L^2$ sequence: the limit, a.e. failure, and an a.e.
  subsequence'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Convergence of Functions
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let \( \ts{ f_k }_{k=1}^{\infty } \subseteq L^2([0, 1]) \) be a sequence which *converges in $L^1$* to a function $f$.

a. Prove that $f\in L^1([0, 1])$.

b. Give an example illustrating that $f_k$ may not converge to $f$ almost everywhere.

c. Prove that $\ts{f_k}$ must contain a subsequence that converges to $f$ almost everywhere.
:::
::: {.solution}
**Setup.** $\ts{f_k} \subseteq L^2([0,1])$ converges in $L^1$ to $f$.
Since $m([0,1]) = 1 < \infty$, convergence in $L^2$ would imply convergence in $L^1$ by Hölder, but here only $L^1$ convergence is assumed.

<1>1. (a) $f \in L^1([0,1])$.
Proof: $L^1$ is complete (a Banach space), so the $L^1$-Cauchy sequence $(f_k)$ has its $L^1$-limit $f$ in $L^1$.
Alternatively, $\|f\|_1 \le \|f - f_k\|_1 + \|f_k\|_1 < \infty$ for large $k$.

<1>2. (b) $f_k$ need not converge to $f$ a.e. Proof: take the typewriter sequence $f_k = \chi_{E_k}$ where $E_1 = [0, 1/2]$, $E_2 = [1/2, 1]$, $E_3 = [0, 1/4]$, $E_4 = [1/4, 1/2]$, $\ldots$ (blocks of dyadic intervals).
Then $\|f_k - 0\|_1 = m(E_k) \to 0$, so $f_k \to 0$ in $L^1$, but every $x$ lies in infinitely many $E_k$'s and misses infinitely many, so $f_k(x)$ does not converge anywhere.
<2>1. $f_k \in L^2([0,1])$ for all $k$.
Proof: $|f_k| \le 1$, so $\|f_k\|_2 \le 1$.
<2>2. $f_k \to 0$ in $L^1$.
Proof: $\|f_k\|_1 = m(E_k) \to 0$.
<2>3. $f_k(x)$ fails to converge for every $x$.
Proof: for each $x$, the dyadic-interval construction visits and leaves $x$ infinitely often, so $\liminf f_k(x) = 0 < 1 = \limsup f_k(x)$.

<1>3. (c) Some subsequence $f_{k_j} \to f$ a.e. <2>1. Choose $k_j$ with $\|f_{k_j} - f\|_1 < 2^{-j}$ (possible since $\|f_k - f\|_1 \to 0$). Proof: definition of convergence in $L^1$.
<2>2. Then $\sum_j \|f_{k_j} - f\|_1 < \infty$; in particular $\sum_j m\{|f_{k_j} - f| > \eps\} \le \sum_j \frac{1}{\eps}\|f_{k_j} - f\|_1 < \infty$ for each $\eps > 0$ (Markov's inequality).
Proof: Markov/Chebyshev and <2>1. <2>3. Borel–Cantelli: for each $\eps > 0$, $m\{x : |f_{k_j}(x) - f(x)| > \eps \text{ infinitely often}\} = 0$.
Proof: $\sum_j m\{|f_{k_j} - f| > \eps\} < \infty$ by <2>2, and Borel–Cantelli.
<2>4. $f_{k_j}(x) \to f(x)$ for a.e. $x$.
Proof: <2>3 for $\eps = 1/m$, $m = 1, 2, \ldots$, union over $m$ gives a null set off which convergence holds for every $\eps$.

<1>4. Q.E.D. Proof: <1>1, <1>2, <1>3 settle (a), (b), (c). (In fact any $L^p$-convergent sequence, $p \ge 1$, has an a.e.-convergent subsequence on a finite measure space; the argument only needs the Markov inequality, which holds for all $p$.)
:::
