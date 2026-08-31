---
schema: qual/card@1
id: P-LOHM5
kind: problem
title: Groups of order $p^3$ have a normal subgroup of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Let $p$ be a prime and $\abs{G} = p^3$.
  Prove that $G$ has a normal subgroup $N$ of order $p^2$.

  - Suppose $N = \gens{h}$ is cyclic and classify all possibilities for $G$ if:

    - $\abs h = p^3$

    - $\abs h = p$.

    > Hint: Sylow and semidirect products.
:::

::: {.solution}
**Goal.** Show a group of order $p^3$ has a normal subgroup of order $p^2$, and classify the cyclic cases.

<1>1. $G$ has a normal subgroup of order $p^2$.
<2>1. $G$ is a $p$-group, so it has a nontrivial center $Z(G)$.
::: {.proof}
a nontrivial $p$-group has a nontrivial center.
:::
<2>2. $|Z(G)|$ is $p$, $p^2$, or $p^3$.
::: {.proof}
$Z(G)$ is a subgroup of $G$, so its order divides $p^3$.
:::
<2>3. If $|Z(G)| \ge p^2$, then $Z(G)$ (or a subgroup of it of order $p^2$) is a normal subgroup of order $p^2$.
::: {.proof}
the center is normal, and a subgroup of the center is normal.
:::
<2>4. If $|Z(G)| = p$, then $G/Z(G)$ has order $p^2$, hence is abelian.
::: {.proof}
a group of order $p^2$ is abelian.
:::
<2>5. $G/Z(G)$ abelian implies $G$ is abelian (since $[G,G] \subseteq Z(G)$ and $G/Z(G)$ abelian forces $[G,G] \subseteq Z(G)$, but this does not force $G$ abelian in general; however, a group of order $p^3$ with $|Z(G)| = p$ has $G/Z(G) \cong \ZZ/p \times \ZZ/p$).
::: {.proof}
standard.
:::
<2>6. In any case, $G$ has a subgroup of order $p^2$ (a subgroup of index $p$), and a subgroup of index $p$ in a $p$-group is normal.
::: {.proof}
a subgroup of index $p$ in a $p$-group is normal (its normalizer has index dividing $p$, and index $1$ or $p$; a subgroup of index $p$ is normal since $[G:N_G(H)] \mid p$ and $[G:N_G(H)] \equiv 1 \pmod p$ forces $[G:N_G(H)] = 1$).
:::

<1>2. Classification when $N = \langle h \rangle$ is cyclic.
<2>1. If $|h| = p^3$, then $G = \langle h \rangle \cong \ZZ/p^3$ is cyclic.
::: {.proof}
$h$ has order $p^3 = |G|$, so it generates $G$.
:::
<2>2. If $|h| = p$, then $N = \langle h \rangle \cong \ZZ/p$, and $G/N$ has order $p^2$.
::: {.proof}
$|G/N| = p^3/p = p^2$.
:::
<2>3. $G/N$ is abelian (order $p^2$), so $G/N \cong \ZZ/p^2$ or $\ZZ/p \times \ZZ/p$.
::: {.proof}
classification of groups of order $p^2$.
:::
<2>4. $G$ is a semidirect product $N \rtimes (G/N)$ (or an extension of $N$ by $G/N$).
::: {.proof}
$N$ is normal, and $G$ is an extension of $N$ by $G/N$; since $N$ is cyclic of order $p$, the extension is a semidirect product (or a central extension).
:::
<2>5. The possibilities for $G$ (with $N = \langle h \rangle$ cyclic of order $p$) are: $\ZZ/p \times \ZZ/p^2$, $\ZZ/p \times \ZZ/p \times \ZZ/p$, and the nonabelian groups of order $p^3$ (the Heisenberg group and the semidirect product $\ZZ/p^2 \rtimes \ZZ/p$).
::: {.proof}
the classification of groups of order $p^3$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves the normal subgroup; <1>2 classifies the cyclic cases.
:::
:::
