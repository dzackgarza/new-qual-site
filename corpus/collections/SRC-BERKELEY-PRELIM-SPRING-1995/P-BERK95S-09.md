---
schema: qual/card@1
id: P-BERK95S-09
kind: problem
title: A monic real polynomial avoiding the open unit disk must vanish at $1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $P(x)$ be a monic polynomial with real coefficients. Suppose
\[
P(0)=-1
\]
and $P$ has no complex zeros in the open unit disk. Prove that
\[
P(1)=0.
\]
:::

::: {.solution}
Let $d=\deg P$, and let
$$
z_1,\ldots,z_d
$$
be the complex roots of $P$, counted with multiplicity.

<1>1. Every root of $P$ has modulus $1$.

::: {.proof}
Since $P$ is monic,
$$
P(0)=(-1)^d\prod_{j=1}^d z_j=-1.
$$
Taking absolute values gives
$$
\prod_{j=1}^d\abs{z_j}=1.
$$
By hypothesis no root lies in the open unit disk, so
$\abs{z_j}\ge1$ for every $j$. A finite product of numbers at least
$1$ can equal $1$ only if every factor equals $1$. Thus
$$
\abs{z_j}=1
\qquad(1\le j\le d).
$$
:::

<1>2. At least one root of $P$ equals $1$.

::: {.proof}
Because $P$ has real coefficients, every nonreal root occurs with its
complex conjugate, with the same multiplicity. By step <1>1, each
nonreal conjugate pair has product
$$
z\overline z=\abs z^2=1.
$$
Every real root on the unit circle is either $1$ or $-1$.

Suppose, for contradiction, that $1$ is not a root. Then every real
root is $-1$. Let $r$ be the number of real roots counted with
multiplicity. The remaining $d-r$ roots occur in conjugate pairs, so
$$
d\equiv r\pmod2.
$$
The product of all roots is then $(-1)^r$. On the other hand, the
constant-term identity gives
$$
\prod_{j=1}^d z_j=(-1)^{d+1}.
$$
Since $d$ and $r$ have the same parity, these two values are
opposites, a contradiction.
:::

<1>3. $P(1)=0$.

::: {.proof}
By step <1>2, $1$ is a root of $P$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the assertion.
:::
:::
