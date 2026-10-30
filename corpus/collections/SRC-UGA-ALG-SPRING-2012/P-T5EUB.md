---
schema: qual/card@1
id: P-T5EUB
kind: problem
title: A normal $p$-subgroup lies in every Sylow $p$-subgroup, and $G$ has a nontrivial
  abelian normal subgroup of order divisible by $p$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and $p$ a prime number such that there is a normal subgroup $H\normal G$ with $\abs{H} = p^i > 1$.

a.
Show that $H$ is a subgroup of any Sylow $p\dash$subgroup of $G$.

b.
Show that $G$ contains a nontrivial abelian normal subgroup of order divisible by $p$.
:::

::: {.concept}
\envlist

- $p$ groups have nontrivial centers.
- Definition of maximality and $p\dash$groups
- Sylows are conjugate
- $Z(G) \ch G$ always.
- Transitivity of characteristic: $A \ch B$ and $B\normal C$ implies $A \normal C$.
:::

::: {.strategy}
Just use maximality for (a).
For (b), centers are always abelian, so $Z(H)$ is good to consider, just need to ensure it's normal in $G$.
Use transitivity of characteristic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every Sylow $p$-subgroup $S$ of $G$ contains $H$.


::: pf-proof

Since $H$ is a $p$-subgroup, Sylow's containment theorem places it in some Sylow $p$-subgroup $S_0$. For any other Sylow $p$-subgroup $S$, conjugacy gives $S=gS_0g^{-1}$ for some $g\in G$. Normality of $H$ implies $H=gHg^{-1}\subseteq gS_0g^{-1}=S$.

:::

:::

::: {.pf-step #s1-2}

The center $Z(H)$ is a nontrivial abelian normal subgroup of $G$, of order divisible by $p$.


::: pf-proof

Since $H$ is a nontrivial finite $p$-group, its class equation implies $\cardinality{Z(H)}$ is a positive multiple of $p$. By definition $Z(H)$ is abelian. It is characteristic in $H$, since every automorphism of $H$ preserves the condition of commuting with all members of $H$. Conjugation by an element of $G$ restricts to an automorphism of $H$ because $H\trianglelefteq G$, so it preserves $Z(H)$. Thus $Z(H)\trianglelefteq G$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-2){.pf-ref} proves part (b).

:::

:::

:::
