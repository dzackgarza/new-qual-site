---
schema: qual/card@1
id: P-UCLAB15S-01
kind: problem
title: Uniform boundedness from a quadratic pointwise inequality
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:[0,\infty)\to[0,\infty)$ be continuous with $f(0)=0$.
Show that if
\[
f(t)\le 1+\frac1{10}f(t)^2\qquad\text{for all }t\in[0,\infty),
\]
then $f$ is uniformly bounded throughout $[0,\infty)$.
:::

::: pf

::: pf-step

The pointwise inequality is equivalent to
\[
f(t)^2-10f(t)+10\ge0
\]
for every
\[
t\ge0.
\]


::: pf-proof

Multiply
\[
f(t)\le1+\frac1{10}f(t)^2
\]
by $10$ and move all terms to one side:
\[
0
\le
f(t)^2-10f(t)+10.
\]

:::

:::

::: pf-step

The quadratic polynomial
\[
q(y)=y^2-10y+10
\]
has roots
\[
\alpha=5-\sqrt{15},
\qquad
\beta=5+\sqrt{15}.
\]


::: pf-proof

The quadratic formula gives
\[
y
=
\frac{10\pm\sqrt{100-40}}2
=
\frac{10\pm\sqrt{60}}2
=
5\pm\sqrt{15}.
\]

:::

:::

::: pf-step

One has
\[
q(y)<0
\]
exactly when
\[
\alpha<y<\beta.
\]


::: pf-proof

The polynomial $q$ is monic and has the two distinct real roots $\alpha<\beta$ from step <1>2.
Therefore it is negative strictly between its roots and nonnegative outside that interval.

:::

:::

::: pf-step

Hence for every
\[
t\ge0,
\]
one has either
\[
f(t)\le\alpha
\]
or
\[
f(t)\ge\beta.
\]


::: pf-proof

By step <1>1,
\[
q(f(t))\ge0.
\]
Apply the sign description from step <1>3.

:::

:::

::: pf-step

The second alternative in step <1>4 never occurs.


::: pf-proof

Suppose for contradiction that
\[
f(t_0)\ge\beta
\]
for some
\[
t_0\ge0.
\]
Since
\[
f(0)=0<\alpha
\]
and $f$ is continuous on $[0,t_0]$, the intermediate value theorem implies that $f$ assumes every value between $0$ and $f(t_0)$.

In particular, it assumes some value
\[
y\in(\alpha,\beta),
\]
for example
\[
y=5.
\]
Thus there exists
\[
s\in[0,t_0]
\]
with
\[
f(s)=5.
\]
But
\[
\alpha<5<\beta,
\]
contradicting step <1>4.
Therefore no such $t_0$ exists.

:::

:::

::: pf-step

Therefore
\[
\boxed{
0\le f(t)\le5-\sqrt{15}
}
\]
for every
\[
t\ge0.
\]


::: pf-proof

The codomain of $f$ is
\[
[0,\infty),
\]
so
\[
f(t)\ge0.
\]
By step <1>5, the alternative
\[
f(t)\ge\beta
\]
is impossible.
Hence step <1>4 forces
\[
f(t)\le\alpha=5-\sqrt{15}
\]
for every $t$.

:::

:::

::: pf-step

Thus $f$ is uniformly bounded on $[0,\infty)$.


::: pf-proof

Step <1>6 provides the global bound
\[
\boxed{
\sup_{t\ge0}f(t)\le5-\sqrt{15}<\infty.
}
\]

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
