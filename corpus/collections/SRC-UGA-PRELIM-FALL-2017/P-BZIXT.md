---
schema: qual/card@1
id: P-BZIXT
kind: problem
title: A left inverse forces $f$ injective and $g$ surjective, but neither need be
  bijective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
---

::: problem
Let $X$ and $Y$ be sets, and let $f:X\to Y$ and $g:Y\to X$ satisfy
\[
g(f(x))=x
\]
for every $x\in X$.

1. Show that $f$ is injective.

2. Show that $g$ is surjective.

3. Give an example in which neither $f$ nor $g$ is bijective.
:::

::: solution
If $f(x_1)=f(x_2)$, then applying $g$ gives
\[
x_1=g(f(x_1))=g(f(x_2))=x_2.
\]
Thus $f$ is injective.

For each $x\in X$, the element $f(x)\in Y$ satisfies $g(f(x))=x$. Thus $g$ is surjective.

Let $X=\{1\}$, $Y=\{1,2\}$, $f(1)=1$, and $g(1)=g(2)=1$. Then $g\circ f=\operatorname{id}_X$, while $f$ is not surjective and $g$ is not injective.
:::
