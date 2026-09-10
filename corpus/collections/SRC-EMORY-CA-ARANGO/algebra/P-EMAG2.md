---
schema: qual/card@1
id: P-EMAG2
kind: problem
title: Normalizers of non-Sylow $p$-subgroups
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared Groups 2 on PDF page 1; the source requires a non-Sylow p-subgroup, not just a proper p-subgroup as the former title suggested."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the fixed-coset equivalence using finiteness, the orbit congruence in the full coset space G/H, and positivity of the resulting index."
---

::: problem
Let $G$ be a finite group of order $p^n m$ where $p$ is a prime and $m$ is not divisible by $p$.
Prove that if $H$ is a subgroup of $G$ of order $p^k$ for some $k < n$, then the normalizer of $H$ in $G$ properly contains $H$.
:::

::: solution
<1>1. The left action of $H$ on the coset set $G/H$
has $[N_G(H):H]$ fixed points.

::: proof
The action is $h\cdot(gH)=hgH$. It is independent
of the representative of the coset and respects
the identity and multiplication laws of $H$.
A coset $gH$ is fixed by all elements of $H$
exactly when $g^{-1}hg\in H$ for every $h\in H$,
that is, $g^{-1}Hg\subseteq H$. These finite
subgroups have the same order, so this inclusion
is equality. Thus precisely the cosets represented
by elements of $N_G(H)$ are fixed. Their number
is the asserted index.
:::

<1>2. The index $[N_G(H):H]$ is a positive multiple of $p$.

::: proof
By orbit-stabilizer, each $H$-orbit has order dividing
$|H|=p^k$ [@DF04]. A non-singleton orbit therefore
has size divisible by $p$. Counting all cosets gives
$$
[N_G(H):H]\equiv |G/H|=p^{n-k}m\equiv0\pmod p,
$$
where the last congruence uses $k<n$.
The coset $H$ is fixed, so the number of fixed
points is not zero. It is at least $p$, and
$[N_G(H):H]>1$. Therefore $H\subsetneq N_G(H)$.
The argument includes the trivial subgroup, when
all cosets are fixed.
:::
:::
