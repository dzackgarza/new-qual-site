---
schema: qual/card@1
id: P-XIB32
kind: problem
title: Field homomorphisms from $\mathbb{Q}(\alpha)$ into $\mathbb{C}$, $\mathbb{R}$,
  and $\overline{\mathbb{Q}}$ for a root $\alpha$ of $x^{17}-2$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
---

::: {.problem}
Suppose that $\alpha$ is a root in $\mathbb C$ of $P(x) = x^{17} - 2$.
How many field homomorphisms are there from $\mathbb Q (\alpha)$ to:

1. $\mathbb C$,

2. $\mathbb R$,

3. $\overline{\mathbb Q}$, the algebraic closure of $\mathbb Q$?
:::
::: problem
Let $\alpha\in\CC$ satisfy $\alpha^{17}=2$. How many field homomorphisms are there from $\QQ(\alpha)$ to

1. $\CC$,
2. $\RR$,
3. $\overline{\QQ}$?
:::

::: solution
The polynomial
\[
f(x)=x^{17}-2
\]
is irreducible over $\QQ$ by Eisenstein's criterion at $2$. Hence it is the minimal polynomial of $\alpha$ and
\[
[\QQ(\alpha):\QQ]=17.
\]
Since the characteristic is $0$, $f$ is separable and has $17$ distinct roots in $\CC$.

Every field homomorphism from $\QQ(\alpha)$ fixing $\QQ$ is determined by the image of $\alpha$, and that image may be any root of $f$ lying in the target field.

<1>1. Into $\CC$:
All $17$ roots lie in $\CC$, so there are
\[
17
\]
homomorphisms.

<1>2. Into $\RR$:
The function $x\mapsto x^{17}$ is strictly increasing on $\RR$, so $x^{17}=2$ has exactly one real root. Hence there is exactly
\[
1
\]
homomorphism into $\RR$.

<1>3. Into $\overline{\QQ}$:
All roots of $f$ are algebraic over $\QQ$, hence lie in $\overline{\QQ}$. Therefore there are again
\[
17
\]
homomorphisms.
:::
