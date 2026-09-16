---
schema: qual/card@1
id: P-WBB2M
kind: problem
title: Intermediate fields of a $D_8$-extension with $E/F$ and $K/E$ Galois but $K/F$
  not Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $F \subset L$ be fields such that $L/F$ is a Galois field extension with Galois group equal to $D_8 = \left< \sigma,\tau \mid \sigma^4 = \tau^2 = 1,~ \sigma\tau = \tau \sigma^3 \right>$.
Show that there are fields $F \subset E \subset K \subset L$ such that $E/F$ and $K/E$ are Galois field extensions, but $K/F$ is not Galois.
:::
::: {.problem}
Let $L/F$ be Galois with
\[
\operatorname{Gal}(L/F)=D_8=\langle\sigma,\tau\mid \sigma^4=\tau^2=1,\ \tau\sigma\tau=\sigma^{-1}\rangle.
\]
Show that there are fields
\[
F\subset E\subset K\subset L
\]
such that $E/F$ and $K/E$ are Galois, but $K/F$ is not Galois.
:::

::: {.solution}
Let
\[
H=\langle\sigma^2,\tau\rangle\cong C_2\times C_2,
\qquad
J=\langle\tau\rangle.
\]
The subgroup $H$ has index $2$ in $D_8$, so $H\trianglelefteq D_8$. Since $H$ is abelian, $J\trianglelefteq H$.

However, $J$ is not normal in $D_8$: for example,
\[
\sigma\tau\sigma^{-1}=\sigma^2\tau\notin\langle\tau\rangle.
\]

Define the fixed fields
\[
E=L^H,
\qquad
K=L^J.
\]
Then $F\subset E\subset K\subset L$. By the fundamental theorem of Galois theory,
\[
E/F\text{ is Galois}
\iff H\trianglelefteq D_8,
\]
so $E/F$ is Galois. Likewise
\[
K/E\text{ is Galois}
\iff J\trianglelefteq H,
\]
so $K/E$ is Galois. But
\[
K/F\text{ is Galois}
\iff J\trianglelefteq D_8,
\]
which is false.
:::
