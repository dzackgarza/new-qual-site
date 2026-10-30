---
schema: qual/card@1
id: P-BKS06-9A
kind: problem
title: A non-cyclic finite $p$-group has at least $p+3$ subgroups
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
---

::: {.problem}
Let $p$ be a prime.
Let $G$ be a finite non-cyclic group of order $p^{m}$ for some $m$. Prove that $G$ has at least $p + 3$ subgroups.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A nontrivial finite $p$-group has a nontrivial center.

::: pf-proof

By the class equation, $\abs{G}=\abs{Z(G)}+\sum\abs{G:C_G(x)}$, where the sum runs over representatives of the conjugacy classes of size greater than $1$. Each index in the sum is a positive power of $p$, and $p\mid\abs{G}$, so $p\mid\abs{Z(G)}$.

:::

:::

::: {.pf-step #s2}

If $G/Z(G)$ is cyclic, then $G$ is abelian.

::: pf-proof

Let $aZ(G)$ generate $G/Z(G)$. Then every element of $G$ is $a^nz$ with $n\in\ZZ$ and $z\in Z(G)$, and two such elements commute.

:::

:::

::: {.pf-step #s3}

A non-cyclic abelian $p$-group contains a subgroup isomorphic to $(\ZZ/p\ZZ)^2$, and $(\ZZ/p\ZZ)^2$ has exactly $p+3$ subgroups.

::: pf-proof

By the structure theorem, the group is $\prod_{i=1}^r\ZZ/p^{e_i}\ZZ$ with all $e_i\ge1$, and $r\ge2$ because it is not cyclic. The elements of order dividing $p$ form a subgroup isomorphic to $(\ZZ/p\ZZ)^r$, which contains $(\ZZ/p\ZZ)^2$. The subgroups of $(\ZZ/p\ZZ)^2$ are the trivial subgroup, the whole group, and the $(p^2-1)/(p-1)=p+1$ lines of the $\FF_p$-vector space $\FF_p^2$.

:::

:::

::: {.pf-step #s4}

Every non-cyclic group of order $p^m$ has at least $p+3$ subgroups.

::: pf-proof

Use strong induction on $m$. A group of order $1$ or $p$ is cyclic, so $m\ge2$. Let $Z=Z(G)$, which is nontrivial by step [](#s1){.pf-ref}. If $G/Z$ is cyclic, then $G$ is abelian by step [](#s2){.pf-ref}, and step [](#s3){.pf-ref} gives at least $p+3$ subgroups. If $G/Z$ is not cyclic, then $\abs{G/Z}=p^{m'}$ with $m'<m$, so by the induction hypothesis $G/Z$ has at least $p+3$ subgroups. Their inverse images under $G\to G/Z$ are distinct subgroups of $G$.

:::

:::

::: pf-qed

This is step [](#s4){.pf-ref}.

:::

:::

:::
