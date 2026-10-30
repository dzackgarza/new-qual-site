---
schema: qual/card@1
id: P-UCLAB06S-05
kind: problem
title: Uniform continuity of $x^\alpha$ on $[0,\infty)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
(A) Define uniform continuity for a function $f$ defined on a metric space $X$ with distance function $\rho(x, y)$.

(B) Prove that if $0 < \alpha < 1$, then $F(x) = x^\alpha$ is uniformly continuous on $[0, \infty)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function
$$
f:X\to\RR
$$
on a metric space $(X,\rho)$ is uniformly continuous if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $x,y\in X$,
$$
\rho(x,y)<\delta
$$
implies
$$
\abs{f(x)-f(y)}<\varepsilon.
$$


::: pf-proof

This is the definition of uniform continuity.
The same $\delta$ must work for all pairs $x,y\in X$.

:::

:::

::: {.pf-step #s1-2}

For
$$
0<\alpha<1
$$
and
$$
s,t\ge0,
$$
one has
$$
\boxed{
(s+t)^\alpha
\le
s^\alpha+t^\alpha
}.
$$


::: pf-proof

Fix $t>0$ and write
$$
s=ut,
\qquad
u\ge0.
$$
It is enough to prove
$$
(1+u)^\alpha
\le
1+u^\alpha.
$$
Define
$$
h(u)
=
1+u^\alpha-(1+u)^\alpha.
$$
Then
$$
h(0)=0.
$$
For $u>0$,
$$
h'(u)
=
\alpha u^{\alpha-1}
-
\alpha(1+u)^{\alpha-1}.
$$
Since
$$
\alpha-1<0
$$
and
$$
u<1+u,
$$
one has
$$
u^{\alpha-1}
>
(1+u)^{\alpha-1}.
$$
Thus
$$
h'(u)>0.
$$
Hence
$$
h(u)\ge0
$$
for all $u\ge0$.
Multiplying by $t^\alpha$ gives the desired inequality.
The case $t=0$ is immediate.

:::

:::

::: {.pf-step #s1-3}

For all $x,y\ge0$,
$$
\boxed{
\abs{x^\alpha-y^\alpha}
\le
\abs{x-y}^\alpha
}.
$$


::: pf-proof

Assume without loss of generality that
$$
x\ge y.
$$
Then
$$
x=y+(x-y).
$$
By step [](#s1-2){.pf-ref},
$$
x^\alpha
\le
y^\alpha+(x-y)^\alpha.
$$
Therefore
$$
0
\le
x^\alpha-y^\alpha
\le
(x-y)^\alpha.
$$
This is the stated inequality.

:::

:::

::: {.pf-step #s1-4}

Given
$$
\varepsilon>0,
$$
choose
$$
\delta=\varepsilon^{1/\alpha}.
$$
Then
$$
\abs{x-y}<\delta
$$
implies
$$
\abs{x^\alpha-y^\alpha}<\varepsilon.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\abs{x^\alpha-y^\alpha}
\le
\abs{x-y}^\alpha
<
\delta^\alpha
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
x\longmapsto x^\alpha
\text{ is uniformly continuous on }[0,\infty)
}
$$
for every
$$
0<\alpha<1.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives, for each $\varepsilon>0$, a $\delta>0$ depending only on $\varepsilon$ and $\alpha$, not on $x$ or $y$.
This is exactly the definition in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (A), and step [](#s1-5){.pf-ref} proves part (B).

:::

:::

:::
