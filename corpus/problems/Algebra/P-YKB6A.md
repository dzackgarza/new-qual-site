---
schema: qual/card@1
id: P-YKB6A
kind: problem
title: Abelianness of Galois groups is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Abelian Groups
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Suppose $F\subset E\subset K$, with $K/F$ Galois, and both $E/F$ and $K/E$ have abelian Galois groups. Must $\Gal(K/F)$ be abelian? Give counterexamples for number fields and function fields.
:::

::: {.solution}
The answer is $\boxed{\text{no}}$; each step below gives a tower with $E/F$ and $K/E$ Galois with abelian groups and $\Gal(K/F)\cong S_3$.

::: pf

::: pf-step
(Number fields) Let $K$ be the splitting field of $x^3-2$ over $F=\QQ$, and let $E=\QQ(\sqrt{-3})$.
Then $\Gal(E/\QQ)\cong C_2$ and $\Gal(K/E)\cong C_3$, while $\Gal(K/\QQ)\cong S_3$.

::: pf-proof
$\Gal(K/\QQ)\cong S_3$, and $E$ is the fixed field of the normal subgroup $A_3$, because it is the unique quadratic subfield of $K$.
So $\Gal(K/E)\cong A_3\cong C_3$ and $\Gal(E/\QQ)\cong S_3/A_3\cong C_2$.
:::

:::

::: pf-step
(Function fields) Let $\omega\in\CC$ be a primitive cube root of unity, $K=\CC(x)$, and let $r,s$ be the $\CC$-automorphisms of $K$ with $r(x)=\omega x$ and $s(x)=x^{-1}$.
With $E=\CC(x^3)$ and $F=\CC(x^3+x^{-3})$, we have $\Gal(K/E)\cong C_3$ and $\Gal(E/F)\cong C_2$, while $\Gal(K/F)\cong S_3$.

::: pf-proof
$r$ has order $3$, $s$ has order $2$, and $srs^{-1}=r^{-1}$, so $\langle r,s\rangle\cong S_3$.
By Artin's theorem, $K$ is Galois over the fixed field of $\langle r\rangle$ with group $\langle r\rangle$, and over the fixed field of $\langle r,s\rangle$ with group $\langle r,s\rangle$.
The field $\CC(x^3)$ is fixed by $r$ and $[K:\CC(x^3)]=3$, so it is the fixed field of $\langle r\rangle$.
The field $\CC(x^3+x^{-3})$ is fixed by $r$ and $s$, and $x$ is a root of $(t^3)^2-(x^3+x^{-3})t^3+1$ of degree $6$, so $[K:\CC(x^3+x^{-3})]\le6$ and it is the fixed field of $\langle r,s\rangle$.
Since $\langle r\rangle$ is normal, $\Gal(E/F)\cong S_3/C_3\cong C_2$.
:::

:::

:::

:::
