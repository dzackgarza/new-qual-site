---
schema: qual/card@1
id: P-BKF05-4B
kind: problem
title: Holomorphic interpolation at reciprocal integers
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained identity-theorem argument using
    h(z)=(1+az)f(z)-z. An interior zero of 1+az is impossible, while the
    rational formula is holomorphic throughout the disk exactly when
    |a|<=1.
---

::: {.problem}
Determine all \(a\in\mathbb C\) for which there exists a holomorphic function \(f\) on the open unit disk such that
\[
f(1/n)=\frac1{n+a}
\]
for every integer \(n\ge2\).
:::

::: {.solution}
Let
$$
D=\{z\in\CC:\abs z<1\}.
$$

<1>1. If such a holomorphic function $f$ exists, then
$$
(1+az)f(z)=z
$$
for every $z\in D$.

::: {.proof}
Define
$$
h(z)=(1+az)f(z)-z.
$$
The function $h$ is holomorphic on $D$. For every integer $n\ge2$,
the prescribed value gives
$$
h(1/n)
=
\left(1+\frac an\right)\frac1{n+a}
-
\frac1n
=
0.
$$
The points $1/n$ are distinct and converge to $0\in D$. Hence the
identity theorem implies $h\equiv0$ on $D$, proving the identity.
:::

<1>2. Existence of such an $f$ forces
$$
\abs a\le1.
$$

::: {.proof}
Suppose $\abs a>1$. Then $a\ne0$ and
$$
z_0=-\frac1a
$$
satisfies $\abs{z_0}<1$, so $z_0\in D$. Evaluating the identity from
step <1>1 at $z_0$ gives
$$
0
=
(1+az_0)f(z_0)
=
z_0,
$$
which is impossible because $z_0\ne0$. Therefore $\abs a\le1$.
:::

<1>3. If $\abs a\le1$, then
$$
f(z)=\frac{z}{1+az}
$$
is holomorphic on $D$ and satisfies all the required interpolation
conditions.

::: {.proof}
If $a=0$, the denominator is identically one. If $a\ne0$, its only
zero is $-1/a$, whose modulus is
$$
\frac1{\abs a}\ge1.
$$
Thus $1+az$ has no zero in the open unit disk, so the displayed $f$ is
holomorphic there. For every $n\ge2$,
$$
f(1/n)
=
\frac{1/n}{1+a/n}
=
\frac1{n+a}.
$$
:::

<1>4. The required set of parameters is
$$
\boxed{\{a\in\CC:\abs a\le1\}}.
$$

::: {.proof}
Step <1>2 proves necessity, and step <1>3 proves sufficiency.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the complete classification.
:::
:::
