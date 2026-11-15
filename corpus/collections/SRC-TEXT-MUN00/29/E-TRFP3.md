---
schema: qual/card@1
id: E-TRFP3
kind: problem
title: Directed sets without antisymmetry
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 12 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-12-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-12.md, which
    answers the exercise by passing to the classes of mutually comparable indices, a partially
    ordered directed set, and checking the earlier exercises one by one. The card keeps that shape;
    its version of the passage to classes proves well-definedness, monotonicity and cofinality of
    the choice map, where dbFin calls them straightforward, and its check of Exercise 2 follows the
    order-theoretic statement rather than dbFin's remark about equivalent indices alone. Martin
    Sleziak's question 84994 on Math StackExchange (2011-11-23),
    https://math.stackexchange.com/questions/84994, and GEdgar's answer there record that the
    preorder form is the one used by Kelley and by Moore and Smith, and that the constructions do
    not need antisymmetry; nothing from that page is transcribed. This supersedes the 2026-11-10
    note above.
---

::: {.exercise}

Check that the preceding exercises remain correct if condition (2) is omitted from the definition of directed set.
Many mathematicians use the term "directed set" in this more general sense.
:::

::: {.solution}

Call a directed set in the wider sense a set $J$ with a relation $\preceq$ that is reflexive and transitive, such that each pair of elements has an upper bound in $J$; condition (2), antisymmetry, is not required.

::: pf

::: pf-step
If $J$ is directed in the wider sense, then $\alpha \sim \beta$ defined by $\alpha \preceq \beta$ and $\beta \preceq \alpha$ is an equivalence relation, and the classes form a directed set $\bar{J}$ under $[\alpha] \preceq [\beta]$ if and only if $\alpha \preceq \beta$.

::: pf-proof
Reflexivity and symmetry are immediate, and transitivity follows from transitivity of $\preceq$. If $\alpha \sim \alpha'$ and $\beta \sim \beta'$, then $\alpha' \preceq \alpha \preceq \beta \preceq \beta'$ shows $\alpha \preceq \beta$ implies $\alpha' \preceq \beta'$, and the converse holds by symmetry, so the relation on classes is well defined. It is reflexive and transitive because $\preceq$ is, and $[\alpha] \preceq [\beta]$ with $[\beta] \preceq [\alpha]$ says $\alpha \sim \beta$, that is $[\alpha] = [\beta]$, so it is a partial order. An upper bound of $\alpha, \beta$ in $J$ is one for $[\alpha], [\beta]$ in $\bar J$, so $\bar J$ is directed.
:::

:::

::: pf-step
Every net indexed by a set directed in the wider sense has a subnet indexed by a partially ordered directed set, with the same limits; and a point is an accumulation point of the net if and only if it is one of that subnet.

::: pf-proof
Choose $f([\alpha]) \in [\alpha]$ for each class. If $[\alpha] \preceq [\beta]$, then $f([\alpha]) \sim \alpha \preceq \beta \sim f([\beta])$, so $f$ is order preserving, and $f(\bar J)$ is cofinal in $J$ because $\alpha \preceq f([\alpha])$. Hence $(x_{f([\alpha])})_{[\alpha] \in \bar J}$ is a subnet of $(x_\alpha)_{\alpha \in J}$, and by the preceding exercise it converges to every limit of $(x_\alpha)$. Moreover a subnet of this subnet is again a subnet of $(x_\alpha)_{\alpha \in J}$, a composite of two order preserving maps with cofinal image being order preserving with cofinal image, and by the preceding exercise a point to which some subnet converges is an accumulation point of $(x_\alpha)$. So the existence of a convergent subnet, and by that exercise the existence of an accumulation point, transfers between $(x_\alpha)$ and its subnet on $\bar J$.
:::

:::

::: pf-step
Exercises 1 to 11 remain correct in the wider sense.

::: pf-proof
Exercise 1 asks for directed sets under a relation that is already a partial order in all four parts, so its answers are unchanged; Exercise 2 uses only that a restriction of a reflexive, transitive relation is one and that an upper bound followed by a class representative stays above, both of which hold without antisymmetry; Exercise 3 has $J = \ZZ_+$, whose order is a partial order. Exercises 4, 5, 6 and 7 argue only from reflexivity, transitivity and the existence of an upper bound of two indices, and the index sets they build, neighborhoods under reverse inclusion and products of two such sets, are partially ordered. Exercise 8 is a statement about all subnets of a net and its proof uses only order preservation and cofinality, and Exercise 9, 10 and 11 rest on Exercises 1 to 8 together with Theorem 26.6 and continuity of the group operations. For a net indexed by a wider directed set, step 2 supplies a subnet indexed by an ordinary directed set, with the same limits and the same accumulation points, and a subnet of that subnet is a subnet of the original net; so each of these statements about the net reduces to the statement for nets on partially ordered sets, which is what the exercises prove.
:::

:::

::: pf-step
The preceding exercises remain correct when condition (2) is omitted from the definition of directed set. $\square$

::: pf-proof
Steps 1 and 2 reduce the wider setting to the partially ordered one without changing limits or accumulation points, and step 3 checks each of the exercises in it.
:::

:::

:::

:::
