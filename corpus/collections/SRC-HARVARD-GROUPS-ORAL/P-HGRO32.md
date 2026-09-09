---
schema: qual/card@1
id: P-HGRO32
kind: problem
title: Define a free group
classification:
  areas: [algebra]
  topics: [Free Groups]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define a free group and state its universal property.
:::

::: solution
Let $X$ be a set. A **free group on $X$** is a group $F(X)$ together with a map
\[
i:X\to F(X)
\]
such that the following universal property holds:

<1>1. For every group $G$ and every function $f:X\to G$, there exists a unique
group homomorphism
\[
\widetilde f:F(X)\to G
\]
such that
\[
\widetilde f\circ i=f.
\]
::: proof
This is the defining universal property of the free group on $X$.
:::

<1>2. Concretely, $F(X)$ may be realized as reduced words in the alphabet
$X\sqcup X^{-1}$.
::: proof
Multiplication is concatenation followed by cancellation of adjacent pairs
$xx^{-1}$ and $x^{-1}x$. Given $f:X\to G$, define $\widetilde f$ on a reduced
word by replacing each $x$ by $f(x)$ and each $x^{-1}$ by $f(x)^{-1}$ and
multiplying in $G$. Cancellation does not change the resulting product, so this
defines a homomorphism. Its values on the generators are forced to equal $f$,
which proves uniqueness.
:::
:::
