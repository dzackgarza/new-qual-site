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

::: {.problem}
Let $g$ be a torsion element of $\mathrm{GL}_n(\mathbb{Q})$, i.e. $g^m = 1$ for some positive integer $m$.
Let us assume $m$ is the order of $g$, i.e. $g^{m'} \neq 1$ for $0 < m' < m$.

(a) Prove that $g$ is diagonalizable over $\mathbb{C}$.
(Hint: think about the minimal polynomial of $g$ and its Jordan form.)

(b) Prove that there is a positive number $M$ depending on $n$ such that the order of any torsion element $g \in \mathrm{GL}_n(\mathbb{Q})$ is at most $M$.
(Hint: think about the eigenvalues of $g$ and field theory.)
:::

::: {.solution}
**Part (a).**

::: pf

::: {.pf-step #p1-s1}
The minimal polynomial $m_g$ of $g$ divides $x^m - 1$.

::: pf-proof
$g^m = 1$, so $g$ satisfies $x^m - 1$, and the minimal polynomial divides any polynomial satisfied by $g$.
:::

:::

::: pf-step
$x^m - 1$ has distinct roots (over $\CC$).

::: pf-proof
$x^m - 1$ and its derivative $mx^{m-1}$ have no common root (the roots of $x^m - 1$ are nonzero, and $mx^{m-1}$ vanishes only at $0$).
:::

:::

::: {.pf-step #p1-s3}
Hence $m_g$ has distinct roots.

::: pf-proof
$m_g \mid x^m - 1$ (step [](#p1-s1){.pf-ref}), and a divisor of a polynomial with distinct roots has distinct roots.
:::

:::

::: {.pf-step #p1-s4}
A matrix is diagonalizable over $\CC$ iff its minimal polynomial has distinct roots.

::: pf-proof
standard criterion (the Jordan form has a nontrivial block iff the minimal polynomial has a repeated root).
:::

:::

::: {.pf-step #p1-s5}
Hence $g$ is diagonalizable over $\CC$.

::: pf-proof
step [](#p1-s3){.pf-ref} and step [](#p1-s4){.pf-ref}.
:::

:::

:::

**Part (b).**

::: pf

::: pf-step
The eigenvalues of $g$ are roots of unity of order dividing $m$.

::: pf-proof
$g^m = 1$, so each eigenvalue $\lambda$ satisfies $\lambda^m = 1$.
:::

:::

::: {.pf-step #p2-s2}
Each eigenvalue $\lambda$ is algebraic over $\QQ$ of degree at most $n$.

::: pf-proof
$\lambda$ is a root of the characteristic polynomial of $g$, which has degree $n$ over $\QQ$.
:::

:::

::: {.pf-step #p2-s3}
If $d$ is the order of an eigenvalue $\lambda$, then $\varphi(d) \le n$.

::: pf-proof
$\lambda$ is a primitive $d$-th root of unity, so its minimal polynomial over $\QQ$ is the cyclotomic polynomial $\Phi_d$, of degree $\varphi(d)$.
By step [](#p2-s2){.pf-ref}, this degree is at most $n$.
:::

:::

::: {.pf-step #p2-s4}
There are only finitely many possible orders of eigenvalues of torsion elements of $\mathrm{GL}_n(\QQ)$.

::: pf-proof
The Euler totient function satisfies $\varphi(d) \to \infty$ as $d \to \infty$.
Thus
\[
D_n=\{d\ge 1:\varphi(d)\le n\}
\]
is finite.
By step [](#p2-s3){.pf-ref}, the order of every eigenvalue belongs to $D_n$.
:::

:::

::: {.pf-step #p2-s5}
The order $m$ of $g$ is the least common multiple of the orders of its eigenvalues.

::: pf-proof
By Part (a), $g$ is diagonalizable over $\CC$.
If its eigenvalues are $\lambda_1,\ldots,\lambda_n$, then $g^r=1$ exactly when $\lambda_i^r=1$ for every $i$.
Hence
\[
m=\operatorname{lcm}(\operatorname{ord}(\lambda_1),\ldots,\operatorname{ord}(\lambda_n)).
\]
:::

:::

::: {.pf-step #p2-s6}
Hence $m$ is bounded by a constant depending only on $n$.

::: pf-proof
Let
\[
M_n=\operatorname{lcm}\{d:d\in D_n\}.
\]
The integer $M_n$ is finite by step [](#p2-s4){.pf-ref}. By step [](#p2-s5){.pf-ref}, the order of every torsion element of $\mathrm{GL}_n(\QQ)$ divides $M_n$, so it is at most $M_n$.
:::

:::

::: pf-qed
Part (a) is step [](#p1-s5){.pf-ref} above, and Part (b) follows from step [](#p2-s6){.pf-ref}.
:::

:::
:::
