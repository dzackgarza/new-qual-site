---
schema: qual/card@1
id: P-BKS04-2A
kind: problem
title: A countable abelian group with $2^{\aleph_0}$ endomorphisms
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the countable group, the injection of the power set into
    $\operatorname{End}G$, and the cardinality bound. The argument is the retained packet's (problem 2A of
    `assets/attachments/s04solution.pdf`, text at `assets/attachments/s04solution_extracted.md`), read again
    for this pass and unchanged.
---

::: {.problem}
Find a countable abelian group whose endomorphism ring has the same cardinality as the set of real numbers.
Justify your answer.
:::

::: {.solution}
The retained solution set is the **Berkeley Spring 2004 preliminary solution packet** (`assets/attachments/s04solution.pdf`, extracted text at `assets/attachments/s04solution_extracted.md`), problem 2A; the argument below is its, split into steps. The group is $G=\FF_{2}^{(\aleph_{0})}$, the direct sum of countably many copies of $\FF_{2}$.

::: pf

::: {.pf-step #countable}
$G$ is a countable abelian group.

::: pf-proof
$G$ is the $\FF_{2}$-vector space with basis $v_{1},v_{2},\dots$, so its elements are the finite subsets of the basis, and $G=\bigcup_{n}G_{n}$ where $G_{n}=\operatorname{span}\{v_{1},\dots,v_{n}\}$ has $2^{n}$ elements. A countable union of finite sets is countable, so $G$ is countably infinite; it is abelian as a vector space over $\FF_{2}$, and $2=0$ there.
:::

:::

::: {.pf-step #lower}
$\abs{\operatorname{End}G}\ge2^{\aleph_{0}}$.

::: pf-proof
For each subset $S\subseteq\{1,2,3,\dots\}$ let $\phi_{S}$ be the linear map with $\phi_{S}(v_{i})=v_{i}$ for $i\in S$ and $\phi_{S}(v_{i})=0$ otherwise; it is defined on a basis, so it extends uniquely to an endomorphism of $G$. If $S\ne T$ pick $i$ in one and not the other; then $\phi_{S}(v_{i})\ne\phi_{T}(v_{i})$, so the maps differ. Hence $S\mapsto\phi_{S}$ is injective from the power set of $\ZZ_{+}$ into $\operatorname{End}G$, whose cardinality is therefore at least $2^{\aleph_{0}}$.
:::

:::

::: {.pf-step}
$\abs{\operatorname{End}G}=2^{\aleph_{0}}=\abs{\RR}$.

::: pf-proof
An endomorphism of $G$ is a function from the countable set $G$ to itself, so $\abs{\operatorname{End}G}\le\abs{G}^{\abs{G}}=\aleph_{0}^{\aleph_{0}}$, and $\aleph_{0}^{\aleph_{0}}\le(2^{\aleph_{0}})^{\aleph_{0}}=2^{\aleph_{0}\cdot\aleph_{0}}=2^{\aleph_{0}}$. With step [](#lower){.pf-ref} this gives equality, and $\abs{\RR}=2^{\aleph_{0}}$, so $G$ is a countable abelian group whose endomorphism ring has as many elements as the reals.
:::

:::

:::
:::
