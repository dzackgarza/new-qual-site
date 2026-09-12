---
schema: qual/card@1
id: P-DD42S
kind: problem
title: An intermediate field of a Galois extension is normal iff its Galois group
  is a normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $E/F$ be a Galois field extension, and let $K/F$ be an intermediate field of $E/F$.
Show that $K$ is normal over $F$ iff $\mathrm{Gal}(E/K) \trianglelefteq \mathrm{Gal}(E/F)$.
:::


::: {.solution}
Let
\[
G=\operatorname{Gal}(E/F),
\qquad
H=\operatorname{Gal}(E/K).
\]

<1>1. For every $g\in G$,
\[
gHg^{-1}=\operatorname{Gal}(E/gK).
\]
::: {.proof}
An automorphism $\sigma\in G$ lies in $gHg^{-1}$ iff
\[
g^{-1}\sigma g\in H,
\]
which means that $g^{-1}\sigma g$ fixes every element of $K$. Equivalently, $\sigma$ fixes every element of $gK$. Thus the two subgroups are equal.
:::

<1>2. If $K/F$ is normal, then $H\trianglelefteq G$.
::: {.proof}
Because $E/F$ is Galois, every $g\in G$ is an $F$-automorphism of $E$. Normality of $K/F$ implies
\[
gK=K.
\]
Therefore <1>1 gives
\[
gHg^{-1}=\operatorname{Gal}(E/gK)=\operatorname{Gal}(E/K)=H
\]
for every $g\in G$.
:::

<1>3. If $H\trianglelefteq G$, then $K/F$ is normal.
::: {.proof}
By the fundamental theorem of Galois theory,
\[
K=E^H.
\]
For $g\in G$, <1>1 and normality of $H$ give
\[
\operatorname{Gal}(E/gK)=gHg^{-1}=H=\operatorname{Gal}(E/K).
\]
The Galois correspondence is injective, so
\[
gK=K
\]
for every $g\in G$.

Since $E/F$ is normal, every $F$-embedding of $K$ into an algebraic closure extends to an $F$-automorphism of $E$. The preceding equality shows that every such embedding sends $K$ onto itself. Hence $K/F$ is normal.
:::

Thus
\[
K/F\text{ is normal}
\iff
\operatorname{Gal}(E/K)\trianglelefteq\operatorname{Gal}(E/F).
\]
:::
