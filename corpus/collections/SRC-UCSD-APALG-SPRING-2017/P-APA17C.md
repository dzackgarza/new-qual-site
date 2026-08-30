---
schema: qual/card@1
id: P-APA17C
kind: problem
title: Pointwise larger Euclidean action implies strictly larger singular values
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Singular Values
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $A, B \in \mathbb{R}^{n \times n}$ be two real matrices.
Denote by $\sigma_i(A)$ (resp., $\sigma_i(B)$) the $i$-th largest singular value of $A$ (resp., $B$). If $\|Ax\|_2 > \|Bx\|_2$ for all $x \neq 0$, show that $\sigma_i(A) > \sigma_i(B)$ for all $i = 1, \dots, n$.
:::

::: {.solution}
<1>1. By the Courant–Fischer (min-max) characterization, the $i$-th singular value of an $n \times n$ matrix $M$ is given by:
\[
\sigma_i(M) = \max_{\substack{V \subseteq \mathbb{R}^n \\ \dim V = n - i + 1}} \min_{\substack{x \in V \\ \|x\|_2 = 1}} \|Mx\|_2.
\]
Proof: min-max theorem for singular values (eigenvalues of $M^T M$).

<1>2. Choose a subspace $V_i \subseteq \mathbb{R}^n$ of dimension $n - i + 1$ that achieves the maximum for $B$:
\[
\sigma_i(B) = \min_{\substack{x \in V_i \\ \|x\|_2 = 1}} \|Bx\|_2.
\]
Proof: the set of $(n-i+1)$-dimensional subspaces is a Grassmannian, and the maximum is attained (for instance, by the span of the right singular vectors $v_i, v_{i+1}, \dots, v_n$ of $B$).

<1>3. The unit sphere $S(V_i) = \{x \in V_i : \|x\|_2 = 1\}$ is compact.
Proof: the unit sphere in a finite-dimensional Euclidean subspace is closed and bounded.

<1>4. For all $x \in S(V_i)$, $\|Ax\|_2 > \|Bx\|_2$.
Proof: hypothesis applied to nonzero vectors $x \in S(V_i)$.

<1>5. The function $f(x) = \|Ax\|_2 - \|Bx\|_2$ is continuous and strictly positive on the compact set $S(V_i)$, so it attains a strictly positive minimum:
\[
\min_{x \in S(V_i)} \bigl(\|Ax\|_2 - \|Bx\|_2\bigr) = \varepsilon > 0.
\]
Proof: Extreme Value Theorem for continuous functions on compact sets.

<1>6. Therefore, for every $x \in S(V_i)$, $\|Ax\|_2 \ge \|Bx\|_2 + \varepsilon$.
Proof: <1>5.

<1>7. Taking the minimum over $x \in S(V_i)$ gives:
\[
\min_{x \in S(V_i)} \|Ax\|_2 \ge \min_{x \in S(V_i)} \|Bx\|_2 + \varepsilon = \sigma_i(B) + \varepsilon > \sigma_i(B).
\]
Proof: <1>2 and <1>6.

<1>8. By the min-max characterization <1>1 for $A$, since $\dim V_i = n - i + 1$:
\[
\sigma_i(A) \ge \min_{x \in S(V_i)} \|Ax\|_2 > \sigma_i(B).
\]
Proof: <1>1 and <1>7.

<1>9. Thus $\sigma_i(A) > \sigma_i(B)$ for all $i = 1, \dots, n$.
Proof: <1>8 holds for each index $i \in \{1, \dots, n\}$.

<1>10. Q.E.D. Proof: <1>9.
:::
