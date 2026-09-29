---
schema: qual/card@1
id: E-HAT-1.A-8
kind: problem
title: Finitely generated group has finitely many subgroups of given finite index
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that a finitely generated group has only a finite number of subgroups of a given finite index.
[First do the case of free groups, using covering spaces of graphs. The general case then follows since every group is a quotient group of a free group.]
:::

::: {.solution}

::: pf

::: pf-step

Let $F$ be a free group of rank $r$, realized as $\pi_1$ of a wedge of $r$ circles (a finite graph $\Gamma$).

::: pf-proof

a free group is the fundamental group of a finite graph.

:::

:::

::: {.pf-step #s2}

A subgroup $H \le F$ of index $n$ corresponds to a connected $n$-fold covering space $\tilde\Gamma \to \Gamma$.

::: pf-proof

covering space theory (subgroups of $\pi_1$ correspond to connected covers).

:::

:::

::: {.pf-step #s3}

An $n$-fold cover of a finite graph $\Gamma$ is itself a finite graph with $n \cdot |V(\Gamma)|$ vertices and $n \cdot |E(\Gamma)|$ edges.

::: pf-proof

each vertex/edge of $\Gamma$ has $n$ preimages.

:::

:::

::: {.pf-step #s4}

There are only finitely many such covering graphs (up to isomorphism), since there are finitely many graphs with a fixed finite number of vertices and edges.

::: pf-proof

Step [](#s3){.pf-ref} (the number of vertices and edges is fixed, so only finitely many combinatorial types exist).

:::

:::

::: {.pf-step #s5}

Hence $F$ has only finitely many subgroups of index $n$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: pf-step

Now let $G$ be a finitely generated group, written as $G = F/N$ for a free group $F$ (of finite rank) and normal subgroup $N$.

::: pf-proof

every finitely generated group is a quotient of a finitely generated free group.

:::

:::

::: {.pf-step #s7}

Subgroups of $G$ of index $n$ correspond bijectively to subgroups $H \le F$ with $N \le H$ and $[F : H] = n$.

::: pf-proof

the correspondence theorem for the quotient $F \to F/N = G$.

:::

:::

::: {.pf-step #s8}

These $H$ are among the (finitely many) index-$n$ subgroups of $F$.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

::: {.pf-step #s9}

Hence $G$ has only finitely many subgroups of index $n$.

::: pf-proof

Steps [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s5){.pf-ref} and [](#s9){.pf-ref}.

:::

:::

:::
