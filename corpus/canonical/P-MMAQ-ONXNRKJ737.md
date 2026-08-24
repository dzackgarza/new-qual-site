---
schema: qual/card@1
id: P-MMAQ-ONXNRKJ737
kind: problem
title: The sum of group elements is central and nilpotent in $\mathbb{F}[G]$ when
  $\mathrm{char}\,\mathbb{F}=p$ and $|G|=p^n$, so $\mathbb{F}[G]$ is not semisimple
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Ideals
relations: []
review: draft
---

::: problem
Let $\mathbb F$ be a field of characteristic $p$, and $G$ a group of order $p^n$.
Let $R=\mathbb F[G]$ be the group ring (group algebra) of $G$ over $\mathbb F$, and let $u:=\sum_{x\in G}x$ (so $u$ is an element of $R$).

- Prove that $u$ lies in the center of $R$.

- Verify that $Ru$ is a 2-sided ideal of $R$.

- Show there exists a positive integer $k$ such that $u^k=0$.
  Conclude that for such a $k$, $(Ru)^k=0$.

- Show that $R$ is **not** a semi-simple ring.

  > **Warning:** Please use the definition of a semi-simple ring: do **not** use the result that a finite length ring fails to be semisimple if and only if it has a non-zero nilpotent ideal.
:::
