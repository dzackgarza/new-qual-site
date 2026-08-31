---
schema: qual/card@1
id: P-UIHJF
kind: problem
title: A finitely generated group has finitely many subgroups of index $n$, and the
  possible numbers of index-$p$ subgroups of a finitely generated abelian group
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Abelian Groups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Suppose that $G$ is a finitely generated group.
  Let $n$ be a positive integer.
  Prove that $G$ has only finitely many subgroups of index $n$

- Let $p$ be a prime number.
  If $G$ is any finitely-generated abelian group, let $t_p(G)$ denote the number of subgroups of $G$ of index $p$.
  Determine the possible values of $t_p(G)$ as $G$ varies over all finitely-generated abelian groups.
:::

::: {.solution}
**Goal.** (1) A finitely generated group has finitely many subgroups of index $n$. (2) Determine the possible values of $t_p(G)$ for finitely generated abelian $G$.

<1>1. (1) $G$ has finitely many subgroups of index $n$.
<2>1. A subgroup $H \le G$ of index $n$ corresponds to a transitive action of $G$ on a set of $n$ elements (the cosets $G/H$).
::: {.proof}
$G$ acts on $G/H$ by left multiplication, transitively, with stabilizer $H$.
:::
<2>2. A transitive action of $G$ on an $n$-element set is determined by a homomorphism $G \to S_n$ (up to conjugacy).
::: {.proof}
the action is a homomorphism $G \to S_n$, and the stabilizer of a point determines the action up to conjugacy.
:::
<2>3. There are finitely many homomorphisms $G \to S_n$.
::: {.proof}
$G$ is finitely generated, say by $g_1, \dots, g_m$; a homomorphism $G \to S_n$ is determined by the images of the generators, and there are $|S_n|^m = (n!)^m$ choices.
:::
<2>4. Hence there are finitely many subgroups of index $n$.
::: {.proof}
each subgroup of index $n$ gives a homomorphism $G \to S_n$ (the action on cosets), and finitely many homomorphisms give finitely many subgroups.
:::

<1>2. (2) The possible values of $t_p(G)$.
<2>1. Subgroups of index $p$ in an abelian group correspond to surjections $G \to \ZZ/p$.
::: {.proof}
a subgroup $H$ of index $p$ gives $G/H \cong \ZZ/p$ (the only group of order $p$), and conversely the kernel of a surjection $G \to \ZZ/p$ has index $p$.
:::
<2>2. The number of surjections $G \to \ZZ/p$ is $p^r - 1$ where $r = \dim_{\ZZ/p}(G/pG)$.
::: {.proof}
$\operatorname{Hom}(G, \ZZ/p) \cong \operatorname{Hom}(G/pG, \ZZ/p) \cong (\ZZ/p)^r$, and the nonzero homomorphisms (surjections) number $p^r - 1$.
:::
<2>3. $r = \operatorname{rank}(G) + (\text{number of } p\text{-torsion cyclic factors})$.
::: {.proof}
$G \cong \ZZ^s \oplus (\text{torsion})$, and $G/pG \cong (\ZZ/p)^s \oplus (\text{torsion}/p\text{-torsion})$, so $r = s + t$ where $t$ is the number of cyclic $p$-power torsion summands.
:::
<2>4. Hence $t_p(G) = p^r - 1$ for some $r \ge 0$, and every value of the form $p^r - 1$ ($r \ge 0$) occurs.
::: {.proof}
$t_p(G) = p^r - 1$ by <1>2.2, and $r$ can be any nonnegative integer (take $G = \ZZ^r$).
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves (1); <1>2 shows $t_p(G) \in \theset{p^r - 1 : r \ge 0}$.
:::
:::
