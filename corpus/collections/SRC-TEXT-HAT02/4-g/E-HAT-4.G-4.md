---
schema: qual/card@1
id: E-HAT-4.G-4
kind: problem
title: Nerve lemma for subcomplex covers of CW complexes
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Proposition 4G.2 (the nerve lemma) states: if $X$ is covered by a family of open sets $\{U_\alpha\}$ such that every nonempty finite intersection $U_{\alpha_1} \cap \cdots \cap U_{\alpha_k}$ is contractible, then $X$ is homotopy equivalent to the nerve $N$ of the cover.

::: pf-proof

statement of the proposition.

:::

:::

::: {.pf-step #s2}

The same conclusion holds when $X$ is a CW complex covered by subcomplexes $\{X_\alpha\}$ with every nonempty finite intersection contractible.

::: pf-proof

::: pf-step

Each subcomplex $X_\alpha$ has an open neighborhood $U_\alpha$ that deformation retracts onto $X_\alpha$.

::: pf-proof

a subcomplex of a CW complex has a regular neighborhood that deformation retracts onto it.

:::

:::

::: {.pf-step #s2-2}

The open sets $U_\alpha$ form an open cover of $X$, and every nonempty finite intersection $U_{\alpha_1} \cap \cdots \cap U_{\alpha_k}$ deformation retracts onto $X_{\alpha_1} \cap \cdots \cap X_{\alpha_k}$, which is contractible.

::: pf-proof

the regular neighborhoods can be chosen so that intersections of neighborhoods retract onto intersections of subcomplexes.

:::

:::

::: {.pf-step #s2-3}

Hence every nonempty finite intersection of the $U_\alpha$ is contractible.

::: pf-proof

Step [](#s2-2){.pf-ref}.

:::

:::

::: pf-step

By the nerve lemma (step [](#s1){.pf-ref}), $X$ is homotopy equivalent to the nerve of the cover $\{U_\alpha\}$.

::: pf-proof

Step [](#s2-3){.pf-ref}.

:::

:::

::: pf-step

The nerve of $\{U_\alpha\}$ equals the nerve of $\{X_\alpha\}$ (the same intersection pattern).

::: pf-proof

$U_{\alpha_1} \cap \cdots \cap U_{\alpha_k} \neq \varnothing$ iff $X_{\alpha_1} \cap \cdots \cap X_{\alpha_k} \neq \varnothing$.

:::

:::

:::

:::

::: {.pf-step #s3}

Hence $X$ is homotopy equivalent to the nerve of the subcomplex cover $\{X_\alpha\}$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The corollary (that a CW complex covered by contractible subcomplexes with contractible intersections is homotopy equivalent to the nerve) follows immediately.

::: pf-proof

Step [](#s3){.pf-ref} is exactly the corollary's statement.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::
