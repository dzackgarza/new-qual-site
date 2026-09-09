---
schema: qual/card@1
id: P-ALGS13E
kind: problem
title: Torsion elements of $\mathrm{GL}_n(\mathbb{Q})$ are diagonalizable and of bounded order
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $g$ be a torsion element of $\mathrm{GL}_n(\mathbb{Q})$, i.e. $g^m = 1$ for some positive integer $m$.
Let us assume $m$ is the order of $g$, i.e. $g^{m'} \neq 1$ for $0 < m' < m$.

(a) Prove that $g$ is diagonalizable over $\mathbb{C}$.
(Hint: think about the minimal polynomial of $g$ and its Jordan form.)

(b) Prove that there is a positive number $M$ depending on $n$ such that the order of any torsion element $g \in \mathrm{GL}_n(\mathbb{Q})$ is at most $M$.
(Hint: think about the eigenvalues of $g$ and field theory.)
:::

::: {.solution}
**Part (a).**

<1>1. The minimal polynomial $m_g$ of $g$ divides $x^m - 1$.
::: {.proof}
$g^m = 1$, so $g$ satisfies $x^m - 1$, and the minimal polynomial divides any polynomial satisfied by $g$.
:::

<1>2. $x^m - 1$ has distinct roots (over $\CC$).
::: {.proof}
$x^m - 1$ and its derivative $mx^{m-1}$ have no common root (the roots of $x^m - 1$ are nonzero, and $mx^{m-1}$ vanishes only at $0$).
:::

<1>3. Hence $m_g$ has distinct roots.
::: {.proof}
$m_g \mid x^m - 1$ (<1>1), and a divisor of a polynomial with distinct roots has distinct roots.
:::

<1>4. A matrix is diagonalizable over $\CC$ iff its minimal polynomial has distinct roots.
::: {.proof}
standard criterion (the Jordan form has a nontrivial block iff the minimal polynomial has a repeated root).
:::

<1>5. Hence $g$ is diagonalizable over $\CC$.
::: {.proof}
<1>3 and <1>4.
:::

**Part (b).**

<1>1. The eigenvalues of $g$ are roots of unity of order dividing $m$.
::: {.proof}
$g^m = 1$, so each eigenvalue $\lambda$ satisfies $\lambda^m = 1$.
:::

<1>2. Each eigenvalue $\lambda$ is algebraic over $\QQ$ of degree at most $n$.
::: {.proof}
$\lambda$ is a root of the characteristic polynomial of $g$, which has degree $n$ over $\QQ$.
:::

<1>3. If $d$ is the order of an eigenvalue $\lambda$, then $\varphi(d) \le n$.
::: {.proof}
$\lambda$ is a primitive $d$-th root of unity, so its minimal polynomial over $\QQ$ is the cyclotomic polynomial $\Phi_d$, of degree $\varphi(d)$.
By <1>2, this degree is at most $n$.
:::

<1>4. There are only finitely many possible orders of eigenvalues of torsion elements of $\mathrm{GL}_n(\QQ)$.
::: {.proof}
The Euler totient function satisfies $\varphi(d) \to \infty$ as $d \to \infty$.
Thus
\[
D_n=\{d\ge 1:\varphi(d)\le n\}
\]
is finite.
By <1>3, the order of every eigenvalue belongs to $D_n$.
:::

<1>5. The order $m$ of $g$ is the least common multiple of the orders of its eigenvalues.
::: {.proof}
By Part (a), $g$ is diagonalizable over $\CC$.
If its eigenvalues are $\lambda_1,\ldots,\lambda_n$, then $g^r=1$ exactly when $\lambda_i^r=1$ for every $i$.
Hence
\[
m=\operatorname{lcm}(\operatorname{ord}(\lambda_1),\ldots,\operatorname{ord}(\lambda_n)).
\]
:::

<1>6. Hence $m$ is bounded by a constant depending only on $n$.
::: {.proof}
Let
\[
M_n=\operatorname{lcm}\{d:d\in D_n\}.
\]
The integer $M_n$ is finite by <1>4. By <1>5, the order of every torsion element of $\mathrm{GL}_n(\QQ)$ divides $M_n$, so it is at most $M_n$.
:::

<1>7. Q.E.D.
::: {.proof}
Part (a) is <1>5 above, and Part (b) follows from <1>6.
:::
:::
