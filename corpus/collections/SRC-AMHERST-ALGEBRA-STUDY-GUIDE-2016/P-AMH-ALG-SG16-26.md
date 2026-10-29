---
schema: qual/card@1
id: P-AMH-ALG-SG16-26
kind: problem
title: Polynomials vanishing at 2 and 5 form an ideal of $\RR[x]$
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
(January 2014) For the polynomial ring $R=\RR[x]$, define
$$
I=\{f\in R\mid f(2)=f(5)=0\}.
$$
Prove that $I$ is an ideal of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The set $I$ is nonempty.

::: pf-proof
The zero polynomial satisfies
$$
0(2)=0(5)=0,
$$
so $0\in I$.
:::

:::

::: {.pf-step #s1-2}
The set $I$ is closed under subtraction.

::: pf-proof
Let $f,g\in I$.  Then
$$
f(2)=f(5)=g(2)=g(5)=0.
$$
Hence
$$
(f-g)(2)=f(2)-g(2)=0
$$
and
$$
(f-g)(5)=f(5)-g(5)=0.
$$
Therefore $f-g\in I$.
:::

:::

::: {.pf-step #s1-3}
The set $I$ absorbs multiplication by arbitrary elements of $R$.

::: pf-proof
Let $f\in I$ and $h\in R$.  Since $f(2)=f(5)=0$,
$$
(hf)(2)=h(2)f(2)=0
$$
and
$$
(hf)(5)=h(5)f(5)=0.
$$
Thus $hf\in I$.  Since $R=\RR[x]$ is commutative, $fh=hf\in I$ as well.
:::

:::

::: pf-step
Therefore $I$ is an ideal of $R$.

::: pf-proof
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that $I$ is an additive subgroup by the subtraction
criterion, and step [](#s1-3){.pf-ref} gives the absorption property.
:::

:::

:::

:::
