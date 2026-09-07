---
schema: qual/card@1
id: P-ALGF25D
kind: problem
title: Projective modules are flat
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Projective Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared the statement with Problem 4 on page 5 of the official FA25 algebra exam PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified flatness directly from the direct-summand characterization of projectives and injectivity after tensoring with a free module.
---

::: problem
Prove that if $M$ is a projective $A$-module, then it is flat.
:::

::: {.solution}
<1>1. A projective module is a direct summand of a free module.
::: {.proof}
Choose a surjection $\pi:F\twoheadrightarrow M$ from a free $A$-module $F$.
Since $M$ is projective, the identity map on $M$ lifts through $\pi$: there is an $A$-linear map
\[
s:M\longrightarrow F
\qquad\text{such that}\qquad
\pi s=\operatorname{id}_M.
\]
Thus $s$ identifies $M$ with a direct summand of $F$.
Writing $Q=\ker\pi$, every $f\in F$ has the unique decomposition
\[
f=s(\pi(f))+(f-s(\pi(f)))
\]
with the second summand in $Q$.
Hence
\[
F\cong M\oplus Q.
\]
:::

<1>2. Tensoring with a free module preserves injections.
::: {.proof}
Write
\[
F\cong\bigoplus_{i\in I}A
\]
for some index set $I$.
For every $A$-module $X$,
\[
X\otimes_A F
\cong X\otimes_A\left(\bigoplus_{i\in I}A\right)
\cong\bigoplus_{i\in I}X.
\]
If $u:X'\hookrightarrow X$ is injective, then under these identifications
\[
u\otimes_A\operatorname{id}_F
\]
is the direct sum of copies of $u$.
It is therefore injective.
Thus every free $A$-module is flat.
:::

<1>3. A direct summand of a flat module is flat; hence $M$ is flat.
::: {.proof}
Let $u:X'\hookrightarrow X$ be any injective $A$-linear map.
Using $F\cong M\oplus Q$ from <1>1 and distributivity of tensor product over direct sums, the injective map from <1>2 becomes
\[
u\otimes_A\operatorname{id}_F
\cong
(u\otimes_A\operatorname{id}_M)
\oplus
(u\otimes_A\operatorname{id}_Q).
\]
If $z\in X'\otimes_A M$ satisfies
\[
(u\otimes_A\operatorname{id}_M)(z)=0,
\]
then $(z,0)$ lies in the kernel of the displayed direct-sum map.
That map is injective, so $(z,0)=0$ and hence $z=0$.
Therefore
\[
u\otimes_A\operatorname{id}_M:X'\otimes_A M\longrightarrow X\otimes_A M
\]
is injective for every injection $u$.

The tensor functor $-\otimes_A M$ is always right exact, and the preceding argument shows that it also preserves monomorphisms.
Consequently it is exact, so $M$ is flat.
:::
:::
