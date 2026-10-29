---
schema: qual/card@1
id: P-MMVBC
kind: problem
title: The Galois group of $x^4-2$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
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
Find the Galois group of $x^4-2$ over $\QQ$.
:::

::: {.solution}
Let $\alpha=2^{1/4}\in\RR$. The roots of $x^4-2$ are $\pm\alpha$ and $\pm i\alpha$, so the splitting field is $L=\QQ(\alpha,i)$.

::: pf

::: {.pf-step #degree}
$[L:\QQ]=8$.

::: pf-proof
The polynomial $x^4-2$ is Eisenstein at $2$, so $[\QQ(\alpha):\QQ]=4$.
Since $\QQ(\alpha)\subset\RR$ and $i\notin\RR$, $[L:\QQ(\alpha)]=2$, and the tower law gives $[L:\QQ]=8$.
:::

:::

::: {.pf-step #gens}
There are automorphisms $r,s\in\Gal(L/\QQ)$ with $r(\alpha)=i\alpha$, $r(i)=i$, $s(\alpha)=\alpha$, $s(i)=-i$.

::: pf-proof
By step [](#degree){.pf-ref}, $[L:\QQ(i)]=4$, so $x^4-2$ is the minimal polynomial of $\alpha$ over $\QQ(i)$, and there is an automorphism of $L/\QQ(i)$ sending $\alpha$ to the root $i\alpha$; this is $r$.
Complex conjugation restricts to an automorphism $s$ of $L$ that fixes $\alpha\in\RR$ and sends $i$ to $-i$.
:::

:::

::: pf-step
$\Gal(L/\QQ)\cong\boxed{\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle}$, the dihedral group of order $8$.

::: pf-proof
From the formulas of step [](#gens){.pf-ref}, $r^k(\alpha)=i^k\alpha$, so $r$ has order $4$, and $s$ has order $2$.
Also $srs(\alpha)=s(i\alpha)=-i\alpha=r^{-1}(\alpha)$ and $srs(i)=i=r^{-1}(i)$, so $srs=r^{-1}$.
Hence $\langle r,s\rangle$ is a quotient of the dihedral group of order $8$; it contains the four powers of $r$ and $s\notin\langle r\rangle$, because $s$ moves $i$, so it has order $8$.
By step [](#degree){.pf-ref}, $\abs{\Gal(L/\QQ)}=8$, so $\langle r,s\rangle$ is the whole Galois group.
:::

:::

:::

:::
