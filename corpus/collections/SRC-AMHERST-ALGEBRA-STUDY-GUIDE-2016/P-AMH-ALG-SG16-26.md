---
schema: qual/card@1
id: P-AMH-ALG-SG16-26
kind: problem
title: Polynomials vanishing at 2 and 5 form an ideal of $\mathbb R[x]$
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
(January 2014) For the polynomial ring $R=\mathbb{R}[x]$, define
\[
I=\{f\in R\mid f(2)=f(5)=0\}.
\]
Prove that $I$ is an ideal of $R$.
:::

::: {.solution}
<1>1. The set $I$ is nonempty.

::: {.proof}
The zero polynomial satisfies
$$
0(2)=0(5)=0,
$$
so $0\in I$.
:::

<1>2. The set $I$ is closed under subtraction.

::: {.proof}
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

<1>3. The set $I$ absorbs multiplication by arbitrary elements of $R$.

::: {.proof}
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

<1>4. Therefore $I$ is an ideal of $R$.

::: {.proof}
Steps <1>1 and <1>2 show that $I$ is an additive subgroup by the subtraction
criterion, and step <1>3 gives the absorption property.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
