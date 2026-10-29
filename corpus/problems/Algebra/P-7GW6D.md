---
schema: qual/card@1
id: P-7GW6D
kind: problem
title: A Galois group that is neither $S_n$ nor $A_n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What's a Galois group that's not $S_n$ or $A_n$?
:::

::: {.solution}
Let $\alpha\coloneqq\sqrt[4]{2}$ and $K\coloneqq\QQ(\alpha,i)$.

::: pf

::: {.pf-step #degree}

$K$ is the splitting field of $x^4-2$ over $\QQ$, and $[K:\QQ]=8$.

::: pf-proof

The roots of $x^4-2$ are $\pm\alpha$ and $\pm i\alpha$, so the splitting field is $\QQ(\alpha,i)=K$. By Eisenstein's criterion at $2$, $x^4-2$ is irreducible, so $[\QQ(\alpha):\QQ]=4$. Since $\QQ(\alpha)\subset\RR$ and $i\notin\RR$, we get $[K:\QQ(\alpha)]=2$.

:::

:::

::: pf-step

$\Gal(K/\QQ)\cong D_4$, the dihedral group of order $8$.

::: pf-proof

By step [](#degree){.pf-ref}, the group has order $8$, and each automorphism is determined by the images of $\alpha$ and $i$. The automorphisms
$$
r(\alpha)=i\alpha,\quad r(i)=i,
\qquad
s(\alpha)=\alpha,\quad s(i)=-i
$$
satisfy
$$
r^4=s^2=1,\qquad srs=r^{-1},
$$
and $r$ has order $4$ while $s\notin\langle r\rangle$. Hence $r$ and $s$ generate the whole group, with the dihedral presentation.

:::

:::

::: pf-step

$\Gal(K/\QQ)$ is isomorphic to neither $S_n$ nor $A_n$ for any $n$.

::: pf-proof

The orders of the symmetric groups are $1,2,6,24,120,\ldots$ and those of the alternating groups are $1,1,3,12,60,\ldots$; none equals $8$.

:::

:::

:::

:::

::: {.remark}
Another example is $\Gal(\QQ(\zeta_7)/\QQ)\cong(\ZZ/7\ZZ)^\times\cong C_6$: it has the order of $S_3$ but is abelian.
:::
