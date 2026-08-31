---
schema: qual/card@1
id: E-HAT-4.G-4
kind: exercise
title: "Nerve lemma for subcomplex covers of CW complexes"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.

::: {.solution}
<1>1. Proposition 4G.2 (the nerve lemma) states: if $X$ is covered by a family of open sets $\{U_\alpha\}$ such that every nonempty finite intersection $U_{\alpha_1} \cap \cdots \cap U_{\alpha_k}$ is contractible, then $X$ is homotopy equivalent to the nerve $N$ of the cover.
::: {.proof}
statement of the proposition.
:::

<1>2. The same conclusion holds when $X$ is a CW complex covered by subcomplexes $\{X_\alpha\}$ with every nonempty finite intersection contractible.
<2>1. Each subcomplex $X_\alpha$ has an open neighborhood $U_\alpha$ that deformation retracts onto $X_\alpha$.
::: {.proof}
a subcomplex of a CW complex has a regular neighborhood that deformation retracts onto it.
:::
<2>2. The open sets $U_\alpha$ form an open cover of $X$, and every nonempty finite intersection $U_{\alpha_1} \cap \cdots \cap U_{\alpha_k}$ deformation retracts onto $X_{\alpha_1} \cap \cdots \cap X_{\alpha_k}$, which is contractible.
::: {.proof}
the regular neighborhoods can be chosen so that intersections of neighborhoods retract onto intersections of subcomplexes.
:::
<2>3. Hence every nonempty finite intersection of the $U_\alpha$ is contractible.
::: {.proof}
<2>2.
:::
<2>4. By the nerve lemma (<1>1), $X$ is homotopy equivalent to the nerve of the cover $\{U_\alpha\}$.
::: {.proof}
<2>3.
:::
<2>5. The nerve of $\{U_\alpha\}$ equals the nerve of $\{X_\alpha\}$ (the same intersection pattern).
::: {.proof}
$U_{\alpha_1} \cap \cdots \cap U_{\alpha_k} \neq \varnothing$ iff $X_{\alpha_1} \cap \cdots \cap X_{\alpha_k} \neq \varnothing$.
:::

<1>3. Hence $X$ is homotopy equivalent to the nerve of the subcomplex cover $\{X_\alpha\}$.
::: {.proof}
<1>2.
:::

<1>4. The corollary (that a CW complex covered by contractible subcomplexes with contractible intersections is homotopy equivalent to the nerve) follows immediately.
::: {.proof}
<1>3 is exactly the corollary's statement.
:::

<1>5. Q.E.D.
::: {.proof}
<1>3 and <1>4.
:::
:::
