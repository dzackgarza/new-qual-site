---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3B-HW3
kind: problem
title: 'Galois correspondence for covering spaces'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own statement, which is a correct statement of the
    Galois correspondence for covering spaces. Each clause now says what makes it true rather than
    standing alone: injectivity of the induced map on pi_1 for a covering and the realisation of a
    subgroup by the quotient of the universal cover; the basepoint change conjugating H and its
    converse; the identification of the deck group with N(H)/H and the coincidence of regularity
    with normality of H; and that a subgroup of the deck group acts freely and properly, so the
    quotient is again a covering of X with that image subgroup. Not checked: the printed worksheet.
---

::: {.problem}
State the Galois Correspondence Theorem for a path-connected, locally path-connected, and semilocally simply connected space $X$.
:::

::: {.solution}
This is a worksheet question of the 2020 topology workshop (`SRC-TOP-WORKSHOP-2020`, worksheet 3B), which asks for the Galois correspondence to be *stated*. No solution set is retained for it and the worksheet itself was not re-read in this pass; the card states the theorem with each clause attributed to the part of the classification that gives it.

::: pf

::: {.pf-step #correspondence}
Let $X$ be path connected, locally path connected and semilocally simply connected, with basepoint $x_{0}$. Then isomorphism classes of based connected coverings $(p\colon E\to X,e_{0})$ with $p(e_{0})=x_{0}$ correspond bijectively to subgroups $H\leq\pi_{1}(X,x_{0})$, the subgroup attached to $(E,e_{0})$ being $H=p_{*}\pi_{1}(E,e_{0})$.

::: pf-proof
This is the classification of covering spaces: path connectedness and local path connectedness of $X$ let paths and homotopies in $X$ be lifted, and semilocal simple connectedness produces the simply connected cover from which all others are quotients. The map from based coverings to subgroups is well defined because $p_{*}$ is injective for a covering, and it is a bijection: a subgroup $H$ is realised by the cover $\widetilde{X}/H$ and two based covers with the same image subgroup are isomorphic over $X$, the isomorphism being unique once the basepoint is fixed.
:::
:::

::: {.pf-step #unbased}
Forgetting the basepoints, connected coverings of $X$ correspond to conjugacy classes of subgroups of $\pi_{1}(X,x_{0})$.

::: pf-proof
Changing the basepoint $e_{0}$ in a fibre of a fixed connected cover replaces $H$ by a conjugate: another choice $e_{0}'$ lies in the same fibre, and the class of a loop in $X$ at $x_{0}$ that lifts to a path from $e_{0}$ to $e_{0}'$ conjugates $H$ to $p_{*}\pi_{1}(E,e_{0}')$. Two based covers whose subgroups are conjugate are isomorphic as covers of $X$ after transporting the basepoint, and conversely an isomorphism of unbased covers carries $p_{*}\pi_{1}(E,e_{0})$ to a conjugate subgroup. So the unbased classification is by conjugacy classes.
:::
:::

::: {.pf-step #deck}
For a connected covering with $H=p_{*}\pi_{1}(E,e_{0})$, the deck group is $N(H)/H$ where $N(H)$ is the normalizer of $H$ in $\pi_{1}(X,x_{0})$; the covering is regular exactly when $H$ is normal, and then the deck group is $\pi_{1}(X,x_{0})/H$.

::: pf-proof
Deck transformations correspond to those loops at $x_{0}$ whose lift starts and ends at the same point of the fibre in a way compatible with $H$, and the computation gives the automorphism group of the cover $\widetilde{X}/H\to X$ as $N(H)/H$. When $H$ is normal, $N(H)=\pi_{1}(X,x_{0})$. The covering is regular by definition when the deck group acts transitively on each fibre, which for this cover happens exactly in that case; so regularity, normality of $H$, and transitivity of the deck action are one condition.
:::
:::

::: {.pf-step #universal}
The universal cover corresponds to the trivial subgroup, and every connected cover is $\widetilde{X}/H\to X$ for some $H\leq\operatorname{Deck}(\widetilde{X}/X)\cong\pi_{1}(X,x_{0})$.

::: pf-proof
A covering is simply connected exactly when $p_{*}\pi_{1}(E,e_{0})$ is trivial, so by step [](#correspondence){.pf-ref} the universal cover is the one attached to the trivial subgroup. Since the universal cover is simply connected, its deck group is $\pi_{1}(X,x_{0})$ by step [](#deck){.pf-ref} with $H=1$; and every subgroup $H$ acts on $\widetilde{X}$ by deck transformations, freely and properly, so the quotient $\widetilde{X}/H\to X$ is a covering whose image subgroup is $H$ and which is therefore the cover attached to $H$.
:::
:::
:::

:::
