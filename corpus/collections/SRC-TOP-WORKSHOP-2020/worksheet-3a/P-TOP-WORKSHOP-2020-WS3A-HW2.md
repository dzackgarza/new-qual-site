---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3A-HW2
kind: problem
title: 'Seifert–van Kampen theorem'
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the hypotheses, the surjection, the kernel, and the
    equivalence with the amalgamated free product. The exercise asks only that the theorem be stated, so
    the steps separate its clauses rather than proving them; no proof is claimed. No retained solution set
    covers this exercise (the collection retains the worksheets, not solutions).
---

::: {.problem}
State the Seifert--van Kampen Theorem.
:::

::: {.solution}
The exercise asks for the statement of the Seifert--van Kampen theorem, so the steps below separate its clauses; nothing here is proved, and no retained solution set covers the exercise.

::: pf

::: {.pf-step #hypotheses}
Let $X=U\cup V$ with $U,V\subseteq X$ open and path connected and $U\cap V$ path connected and nonempty, and let $x_{0}\in U\cap V$.

::: pf-proof
These are the hypotheses of the theorem: the two open sets cover $X$, each is path connected, and their intersection is path connected, which makes every fundamental group below based at $x_{0}$ meaningful and makes the inclusions induce the maps named next.
:::

:::

::: {.pf-step #surjection}
The inclusions $U\hookrightarrow X$ and $V\hookrightarrow X$ induce a surjective homomorphism $\pi_{1}(U,x_{0})*\pi_{1}(V,x_{0})\twoheadrightarrow\pi_{1}(X,x_{0})$.

::: pf-proof
For a loop in $X$ based at $x_{0}$, compactness of the circle splits it into finitely many subpaths each lying in $U$ or in $V$; by path connectedness of $U\cap V$ the endpoints of those subpaths can be joined to $x_{0}$ inside the intersection, so the loop is a product of loops lying in $U$ or in $V$. Reading each of those as an element of $\pi_{1}(U,x_{0})$ or $\pi_{1}(V,x_{0})$ gives a word in the free product mapping to the class of the original loop; that is the surjectivity asserted by the theorem.
:::

:::

::: {.pf-step #kernel}
The kernel of that homomorphism is the normal closure of the elements $i_{U*}(\omega)i_{V*}(\omega)^{-1}$ for $\omega\in\pi_{1}(U\cap V,x_{0})$, where $i_{U}$ and $i_{V}$ are the inclusions of $U\cap V$ into $U$ and into $V$.

::: pf-proof
A loop $\omega$ of $U\cap V$ gives the same element of $\pi_{1}(X,x_{0})$ whether it is read through $U$ or through $V$, so each $i_{U*}(\omega)i_{V*}(\omega)^{-1}$ lies in the kernel, and so does the normal closure of all of them. The theorem states that nothing else does, which is the second clause of the statement.
:::

:::

::: {.pf-step}
Equivalently $\pi_{1}(X,x_{0})\cong\pi_{1}(U,x_{0})*_{\pi_{1}(U\cap V,x_{0})}\pi_{1}(V,x_{0})$, the pushout of the two induced maps.

::: pf-proof
By the two previous steps $\pi_{1}(X,x_{0})$ is the quotient of the free product by the normal closure of the elements $i_{U*}(\omega)i_{V*}(\omega)^{-1}$; that quotient is exactly the amalgamated free product of $\pi_{1}(U,x_{0})$ and $\pi_{1}(V,x_{0})$ over $\pi_{1}(U\cap V,x_{0})$, and the amalgamated free product is characterised by the universal property of the pushout of $i_{U*}$ and $i_{V*}$ in the category of groups. So the two formulations of the statement agree.
:::

:::

:::
:::
