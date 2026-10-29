---
schema: qual/card@1
id: P-AMH-ALG-SG16-30
kind: problem
title: Reducibility of $X^4+X^2+1$ over $\FF_2$ and irreducibility of $X^3+2X^2+2X+3$ over $\FF_5$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(a) Prove that $f(X)=X^4+X^2+1$ is reducible in the polynomial ring $\FF_2[X]$, where $\FF_2=\{0,1\}$ is the field of two elements.
(b) Prove that $g(X)=X^3+2X^2+2X+3$ is irreducible in the polynomial ring $\FF_5[X]$, where $\FF_5=\{0,1,2,3,4\}$ is the field of five elements.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
In $\FF_2[X]$,
$$
X^4+X^2+1=(X^2+X+1)^2.
$$

::: pf-proof
Because the characteristic is $2$,
$$
(a+b+c)^2=a^2+b^2+c^2
$$
for all $a,b,c\in\FF_2[X]$.  Therefore
$$
(X^2+X+1)^2
=X^4+X^2+1.
$$
:::

:::

::: {.pf-step #s1-2}
The polynomial $f(X)=X^4+X^2+1$ is reducible in $\FF_2[X]$.

::: pf-proof
Step [](#s1-1){.pf-ref} expresses $f$ as a product of two degree-$2$ polynomials:
$$
f=(X^2+X+1)(X^2+X+1).
$$
Both factors have positive degree strictly less than $4$, so this is a
nontrivial factorization.
:::

:::

::: pf-step
Part (a) follows.

::: pf-proof
This is step [](#s1-2){.pf-ref}.
:::

:::

::: {.pf-step #s1-4}
The cubic
$$
g(X)=X^3+2X^2+2X+3
$$
has no root in $\FF_5$.

::: pf-proof
Evaluating at the five elements of $\FF_5$ gives
$$
g(0)=3,
$$
$$
g(1)=1+2+2+3=8\equiv3\pmod5,
$$
$$
g(2)=8+8+4+3=23\equiv3\pmod5,
$$
$$
g(3)=27+18+6+3=54\equiv4\pmod5,
$$
and
$$
g(4)=64+32+8+3=107\equiv2\pmod5.
$$
None of these values is zero.
:::

:::

::: {.pf-step #s1-5}
The polynomial $g$ is irreducible in $\FF_5[X]$.

::: pf-proof
A cubic polynomial over a field is reducible if and only if it has a root in
that field.  Step [](#s1-4){.pf-ref} shows that $g$ has no root in $\FF_5$, so $g$ is
irreducible.
:::

:::

::: pf-step
Part (b) follows.

::: pf-proof
This is step [](#s1-5){.pf-ref}.
:::

:::

:::

:::
