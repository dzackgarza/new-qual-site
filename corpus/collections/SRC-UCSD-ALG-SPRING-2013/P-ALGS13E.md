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

<1>3. If $\lambda$ is a primitive $m$-th root of unity, then $[\QQ(\lambda) : \QQ] = \varphi(m)$.
::: {.proof}
the cyclotomic field $\QQ(\zeta_m)$ has degree $\varphi(m)$ over $\QQ$.
:::

<1>4. Hence $\varphi(m) \le n$.
::: {.proof}
$\lambda$ (a primitive $m$-th root of unity, since $m$ is the order of $g$) has degree $\varphi(m) \le n$ by <1>2 and <1>3.
:::

<1>5. $\varphi(m) \to \infty$ as $m \to \infty$, so there are only finitely many $m$ with $\varphi(m) \le n$.
::: {.proof}
standard fact about the Euler totient function.
:::

<1>6. Hence $m$ is bounded by a constant $M$ depending only on $n$.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>5 (a) and <1>6 (b).
:::
:::
