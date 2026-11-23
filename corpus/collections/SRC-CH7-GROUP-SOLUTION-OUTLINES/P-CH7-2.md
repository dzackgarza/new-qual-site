---
schema: qual/card@1
id: P-CH7-2
kind: problem
title: Index of the Klein four-subgroup in $S_4$
classification:
  areas: [algebra]
  topics:
    - Cosets and Lagrange's Theorem
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Stated the subgroup H of Exercise 1 in the statement, per page 1 of Ch7Sltns.pdf.
  - event: solution-written
    by: kimi
    date: 2026-11-23
    note: >-
      Structured into a Lamport proof from the retained solution outline
      `assets/attachments/Ch7Sltns.pdf`, entry "# 2", which covers Gallian 7e
      Chapter 7 Exercise 2. The outline's Lagrange quotient is retained; the
      card supplies the order and subgroup calculations and proves directly
      that the left cosets partition $S_4$ into sets of equal size.
---

::: {.problem}
Let $H = \{(1), (12)(34), (13)(24), (14)(23)\}$ be as in Exercise 1. How many left cosets of $H$ in $S_4$ are there? (Determine this without listing them.)
:::

::: {.solution}
The collection retains its solution outline as `assets/attachments/Ch7Sltns.pdf`, and entry "# 2" of that outline covers Gallian 7e Chapter 7 Exercise 2. The outline applies Corollary 1 of Lagrange's theorem to obtain $\cardinality{S_4}/\cardinality{H}=4!/4=6$. The argument below retains that quotient and supplies the subgroup and order calculations, together with the left-coset partition that justifies it.

::: pf

::: {.pf-step #orders}
The subgroup $H$ has order $4$, and $\cardinality{S_4}=24$.

::: pf-proof

::: {.pf-step #klein}
The displayed set $H$ is a subgroup of $S_4$ with $\cardinality{H}=4$.

::: pf-proof
The four displayed permutations are distinct, so the displayed set has four elements. It contains the identity, every nonidentity element is its own inverse, and direct cycle multiplication shows that the product of any two distinct nonidentity elements is the third. Thus $H$ is closed under products and inverses; in particular, it is the Klein four-subgroup $V_4$ of $S_4$, and $\cardinality{H}=4$.
:::

:::

::: {.pf-step #symmetric-order}
$\cardinality{S_4}=4!=24$.

::: pf-proof
An element of $S_4$ is a bijection from $\theset{1,2,3,4}$ to itself. Its values at $1,2,3,4$ can be chosen successively in $4,3,2,1$ ways, and these values determine the bijection. Hence $\cardinality{S_4}=4\cdot3\cdot2\cdot1=24$.
:::

:::

:::

:::

::: {.pf-step #coset-partition}
The distinct left cosets of $H$ partition $S_4$ into sets of four elements.

::: pf-proof

::: {.pf-step #coset-size}
For every $g\in S_4$, the left coset $gH$ has exactly four elements.

::: pf-proof
Left multiplication by $g$ maps $H$ onto $gH$. It is injective, since $gh_1=gh_2$ implies $h_1=h_2$ after left multiplication by $g^{-1}$. Hence it is a bijection from $H$ to $gH$, and step [](#klein){.pf-ref} gives $\cardinality{gH}=\cardinality{H}=4$.
:::

:::

::: {.pf-step #cosets-disjoint}
Every element of $S_4$ lies in a left coset, and two left cosets that intersect are equal.

::: pf-proof
For $g\in S_4$, the identity lies in $H$, so $g=g(1)\in gH$. Now suppose $x\in g_1H\cap g_2H$, and write $x=g_1h_1=g_2h_2$ with $h_1,h_2\in H$. Then $g_1^{-1}g_2=h_1h_2^{-1}\in H$ because $H$ is a subgroup. Thus $g_2\in g_1H$; conversely, $g_2^{-1}g_1=(g_1^{-1}g_2)^{-1}\in H$, so $g_1\in g_2H$. Consequently every element of $g_1H$ lies in $g_2H$ and conversely, proving $g_1H=g_2H$.
:::

:::

:::

:::

::: pf-step
The number of left cosets of $H$ in $S_4$ is $\boxed{6}$.

::: pf-proof
By step [](#coset-partition){.pf-ref}, if $r$ is the number of distinct left cosets, counting the elements of $S_4$ by those disjoint cosets gives $24=4r$. Therefore $r=24/4=6$, which is the quotient asserted by Corollary 1 of Lagrange's theorem. This counts the cosets without listing them.
:::

:::
:::

:::
