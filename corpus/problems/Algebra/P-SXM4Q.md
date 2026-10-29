---
schema: qual/card@1
id: P-SXM4Q
kind: problem
title: The centralizer $C_G(s)$ is a subgroup in which $\langle s\rangle$ is normal
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
---

::: {.problem}
Let $s\in G$. Define $C_G(s)$, prove that it is a subgroup of $G$, and show that $\langle s\rangle\normal C_G(s)$.
:::

::: {.solution}

The centralizer of $s$ in $G$ is $C_G(s)=\{g\in G: gs=sg\}$.

::: pf

::: pf-step

$C_G(s)\le G$.

::: pf-proof

The identity commutes with $s$. If $g,h\in C_G(s)$, then
$$
(gh)s=g(hs)=g(sh)=(gs)h=(sg)h=s(gh),
$$
so $gh\in C_G(s)$. If $g\in C_G(s)$, multiplying $gs=sg$ on both sides by $g^{-1}$ gives $sg^{-1}=g^{-1}s$, so $g^{-1}\in C_G(s)$.

:::

:::

::: pf-qed

Since $s$ commutes with itself, $\langle s\rangle\le C_G(s)$. For $g\in C_G(s)$ and $k\in\ZZ$, $g$ commutes with $s^k$, so $gs^kg^{-1}=s^k$. Thus conjugation by every element of $C_G(s)$ fixes $\langle s\rangle$ pointwise, and $\langle s\rangle\normal C_G(s)$.

:::

:::

:::
