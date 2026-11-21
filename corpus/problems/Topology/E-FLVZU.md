---
schema: qual/card@1
id: E-FLVZU
kind: problem
title: Compact topological space
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}
- What does it mean for a topological space to be **compact**?
:::

::: {.solution}

No retained solution set covers this question, and the collection carries no provenance: the definition and the equivalences below are the card's own statement of the standard one, with the book's results cited where they are used.

::: pf

::: {.pf-step #definition}
$X$ is compact when every cover of $X$ by open sets has a finite subcover: if $X=\bigcup_{i\in I}U_{i}$ with each $U_{i}$ open, then $X=U_{i_{1}}\cup\cdots\cup U_{i_{r}}$ for some finitely many indices.

::: pf-proof
This is the definition of compactness (§26). It is a property of the space with its topology: the condition quantifies only over the open sets, so it is preserved by any homeomorphism.
:::

:::

::: {.pf-step #closed-form}
$X$ is compact if and only if every family of closed subsets of $X$ with the finite intersection property has nonempty intersection.

::: pf-proof
Let $\mathcal{C}$ be a family of closed sets. Put $U_{C}=X\setminus C$ for $C\in\mathcal{C}$, which is open. A finite subfamily $C_{1},\ldots,C_{r}$ has $\bigcap_{k}C_{k}\ne\varnothing$ exactly when the corresponding $U_{C_{1}},\ldots,U_{C_{r}}$ fail to cover $X$, since $X\setminus\bigcap_{k}C_{k}=\bigcup_{k}U_{C_{k}}$. So "every open cover has a finite subcover" is exactly "every family of closed sets whose finite subfamilies have nonempty intersection has nonempty total intersection", the finite intersection property.
:::

:::

::: {.pf-step #subspace}
A subspace $Y\subseteq X$ is compact if and only if every cover of $Y$ by sets open in $X$ has a finite subcollection covering $Y$.

::: pf-proof
A set is open in the subspace $Y$ exactly when it is $Y\cap U$ with $U$ open in $X$, and a family $\theset{Y\cap U_{i}}$ covers $Y$ exactly when the $U_{i}$ do. So the defining condition of compactness for the space $Y$ translates into the stated one.
:::

:::

::: {.pf-qed}
The definition is step [](#definition){.pf-ref}, with its closed-set form in step [](#closed-form){.pf-ref} and its subspace form in step [](#subspace){.pf-ref}.
:::

:::

:::
