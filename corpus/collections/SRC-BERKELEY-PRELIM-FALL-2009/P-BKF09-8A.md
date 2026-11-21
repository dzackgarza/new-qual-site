---
schema: qual/card@1
id: P-BKF09-8A
kind: problem
title: Number of fifth powers in $\ZZ/6464\ZZ$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the splitting of the ring, the fifth powers modulo
    $101$, the units and the two non-unit fifth powers modulo $64$, and the product. No retained solution
    set covers this exercise, so the argument is the card's own; the counts $20$, $32$, $2$ and $714$ were
    recomputed for this pass.
---

::: {.problem}
Find the number of elements $a$ in the ring $R=\ZZ/6464\ZZ$ such that $a=x^5$ for some $x\in R$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and the four counts below were recomputed for this pass. Since $6464=64\cdot101$ with the two factors coprime, the Chinese remainder theorem gives $R\cong(\ZZ/64\ZZ)\times(\ZZ/101\ZZ)$, and an element of $R$ is a fifth power exactly when both of its components are.

::: pf

::: {.pf-step #mod101}
$\ZZ/101\ZZ$ has exactly $21$ fifth powers.

::: pf-proof
$101$ is prime, so $(\ZZ/101\ZZ)^{\times}$ is cyclic of order $100$. In a cyclic group of order $100$ the map $x\mapsto x^{5}$ has image of order $100/\gcd(5,100)=100/5=20$, so there are $20$ nonzero fifth powers; together with $0=0^{5}$ this gives $21$.
:::

:::

::: {.pf-step #units64}
Every unit of $\ZZ/64\ZZ$ is a fifth power.

::: pf-proof
$\abs{(\ZZ/64\ZZ)^{\times}}=\varphi(64)=32$, and $32$ is coprime to $5$; raising to the $5$-th power is an automorphism of any finite abelian group of order coprime to $5$, so every unit has a fifth root among the units.
:::

:::

::: {.pf-step #nonunits64}
The fifth powers of the non-units of $\ZZ/64\ZZ$ are exactly $0$ and $32$.

::: pf-proof
A non-unit is a multiple of $2$, say $x=2k$; then $x^{5}=32k^{5}$, and modulo $64$ this is $0$ when $k$ is even and $32$ when $k$ is odd, since $32k^{5}\equiv32k\equiv32\pmod{64}$ for odd $k$. Both values occur: $0=0^{5}$ and $32=2^{5}$. So the non-unit fifth powers are exactly $\{0,32\}$, and $\ZZ/64\ZZ$ has $32+2=34$ fifth powers in all.
:::

:::

::: {.pf-step}
$R$ has $21\cdot34=714$ fifth powers.

::: pf-proof
By the Chinese remainder theorem $R\cong(\ZZ/64\ZZ)\times(\ZZ/101\ZZ)$, and under a product decomposition an element is a fifth power exactly when each component is: one direction is immediate, and the other takes a fifth root of each component and assembles them. The number of fifth powers is therefore the product of the numbers in the two rings, $34\cdot21=714$ by steps [](#units64){.pf-ref} with [](#nonunits64){.pf-ref} and [](#mod101){.pf-ref}.
:::

:::

:::
:::
