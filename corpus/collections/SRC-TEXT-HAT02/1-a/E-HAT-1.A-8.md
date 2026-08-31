---
schema: qual/card@1
id: E-HAT-1.A-8
kind: exercise
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

Show that a finitely generated group has only a finite number of subgroups of a given finite index.
[First do the case of free groups, using covering spaces of graphs. The general case then follows since every group is a quotient group of a free group.]

::: {.solution}
<1>1. Let $F$ be a free group of rank $r$, realized as $\pi_1$ of a wedge of $r$ circles (a finite graph $\Gamma$).
::: {.proof}
a free group is the fundamental group of a finite graph.
:::

<1>2. A subgroup $H \le F$ of index $n$ corresponds to a connected $n$-fold covering space $\tilde\Gamma \to \Gamma$.
::: {.proof}
covering space theory (subgroups of $\pi_1$ correspond to connected covers).
:::

<1>3. An $n$-fold cover of a finite graph $\Gamma$ is itself a finite graph with $n \cdot |V(\Gamma)|$ vertices and $n \cdot |E(\Gamma)|$ edges.
::: {.proof}
each vertex/edge of $\Gamma$ has $n$ preimages.
:::

<1>4. There are only finitely many such covering graphs (up to isomorphism), since there are finitely many graphs with a fixed finite number of vertices and edges.
::: {.proof}
<1>3 (the number of vertices and edges is fixed, so only finitely many combinatorial types exist).
:::

<1>5. Hence $F$ has only finitely many subgroups of index $n$.
::: {.proof}
<1>2 and <1>4.
:::

<1>6. Now let $G$ be a finitely generated group, written as $G = F/N$ for a free group $F$ (of finite rank) and normal subgroup $N$.
::: {.proof}
every finitely generated group is a quotient of a finitely generated free group.
:::

<1>7. Subgroups of $G$ of index $n$ correspond bijectively to subgroups $H \le F$ with $N \le H$ and $[F : H] = n$.
::: {.proof}
the correspondence theorem for the quotient $F \to F/N = G$.
:::

<1>8. These $H$ are among the (finitely many) index-$n$ subgroups of $F$.
::: {.proof}
<1>5 and <1>7.
:::

<1>9. Hence $G$ has only finitely many subgroups of index $n$.
::: {.proof}
<1>7 and <1>8.
:::

<1>10. Q.E.D.
::: {.proof}
<1>5 and <1>9.
:::
:::
