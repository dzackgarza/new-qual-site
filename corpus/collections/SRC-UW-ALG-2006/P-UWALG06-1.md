---
schema: qual/card@1
id: P-UWALG06-1
kind: problem
title: A finitely generated abelian group killed by tensoring with every field is zero
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Tensor Products
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $\ZZ$ be the ring of integers and let $\{0\}$ be the trivial $\ZZ$-module.
Let $G$ be a finitely generated $\ZZ$-module, i.e., a finitely generated Abelian group.
Show that if $G\otimes_{\ZZ}F=\{0\}$ for all fields $F$, then $G=\{0\}$.
:::

::: {.solution}
By the structure theorem for finitely generated abelian groups, $G\cong\ZZ^r\oplus T$ with $T$ finite.

::: pf

::: {.pf-step #no-free-part}
$r=0$.

::: pf-proof
If $r\ge1$ then $G\otimes_\ZZ\QQ\cong\QQ^r\oplus(T\otimes_\ZZ\QQ)$, and $T\otimes_\ZZ\QQ=0$ because every element of the finite group $T$ is annihilated by some positive integer, while multiplication by that integer is invertible on $\QQ$.
Hence $G\otimes_\ZZ\QQ\cong\QQ^r\ne0$, contradicting the hypothesis for the field $F=\QQ$.
:::

:::

::: {.pf-step #no-torsion}
$T=0$.

::: pf-proof
Suppose $T\ne0$ and write $T\cong\bigoplus_i\ZZ/p_i^{e_i}\ZZ$ with the $p_i$ prime.
Choose one prime $p$ occurring, and take $F=\FF_p$.
Then $G\otimes_\ZZ\FF_p\cong\bigoplus_i\bigl(\ZZ/p_i^{e_i}\ZZ\otimes_\ZZ\FF_p\bigr)$, and the summand for that $p$ is isomorphic to $\FF_p/p^e\FF_p\cong\FF_p\ne0$, because $p=0$ in $\FF_p$ and therefore $p^e\FF_p=0$.
So $G\otimes_\ZZ\FF_p\ne0$, contradicting the hypothesis.
:::

:::

::: {.pf-step #trivial}
$G=0$.

::: pf-proof
Steps [](#no-free-part){.pf-ref} and [](#no-torsion){.pf-ref} leave $G\cong\ZZ^0\oplus0$, the trivial group.
:::

:::

:::

:::
