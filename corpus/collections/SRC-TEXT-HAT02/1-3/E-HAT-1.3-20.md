---
schema: qual/card@1
id: E-HAT-1.3-20
kind: problem
title: Nonnormal covering spaces of the Klein bottle
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Construct nonnormal covering spaces of the Klein bottle by a Klein bottle and by a torus.
:::

::: {.solution}
Use the presentation
$$
\pi_1(K)=\langle a,b\mid aba^{-1}=b^{-1}\rangle
$$
for the Klein bottle. Every element has a unique form $a^m b^n$. The orientation character sends $a$ to $-1$ and $b$ to $1$.

::: pf

::: pf-step
The subgroup $H_K=\langle a,b^3\rangle$ defines a nonnormal three-sheeted cover by a Klein bottle.

::: pf-proof
The normal form gives $H_K=\{a^m b^{3n}:m,n\in\ZZ\}$, so its index is $3$. It is not normal: the defining relation gives
$$
bab^{-1}=ab^{-2}\notin H_K.
$$
The corresponding cover is a closed connected surface with Euler characteristic $3\chi(K)=0$. It is nonorientable because its subgroup contains $a$, whose orientation character is $-1$. By the classification of closed surfaces, it is a Klein bottle.
:::

:::

::: pf-step
The subgroup $H_T=\langle a^2b,b^3\rangle$ defines a nonnormal six-sheeted cover by a torus.

::: pf-proof
The element $a^2$ commutes with $b$, so
$$
H_T=\{a^{2m}b^{m+3n}:m,n\in\ZZ\}.
$$
Its index is $6$: the exponent of $a$ must be even, and for each even exponent the exponent of $b$ has one prescribed residue modulo $3$. Conjugation by $a$ gives
$$
a(a^2b)a^{-1}=a^2b^{-1}\notin H_T,
$$
since $-1$ is not congruent to $1$ modulo $3$. Thus the subgroup is not normal. Every element of $H_T$ has even $a$-exponent, so the corresponding closed connected cover is orientable. Its Euler characteristic is $6\chi(K)=0$; hence it is a torus.
:::

:::

:::

:::
