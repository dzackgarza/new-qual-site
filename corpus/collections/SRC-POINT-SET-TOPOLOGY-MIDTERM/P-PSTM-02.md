---
schema: qual/card@1
id: P-PSTM-02
kind: problem
title: Hausdorff spaces and the closed diagonal criterion
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $X$ be a space.
Show that $X$ is Hausdorff if, and only if, the diagonal $\Delta \coloneqq \{ (x, x) \mid x \in X \}$ is a closed subspace of $X \times X$.
:::

::: {.solution}
Write $\Delta^c \coloneqq (X \times X) \setminus \Delta$.
For subsets $U, V \subseteq X$, the product $U \times V$ meets $\Delta$ exactly when $U \cap V \neq \emptyset$.

::: pf

::: pf-step
If $X$ is Hausdorff, then $\Delta$ is closed.

::: pf-proof
Let $(x, y) \in \Delta^c$, so $x \neq y$.
There are disjoint open sets $U \ni x$ and $V \ni y$.
Then $U \times V$ is open in $X \times X$, contains $(x, y)$, and does not meet $\Delta$, because $U \cap V = \emptyset$.
So $\Delta^c$ is open.
:::

:::

::: pf-step
If $\Delta$ is closed, then $X$ is Hausdorff.

::: pf-proof
Let $x \neq y$ in $X$, so $(x, y)$ lies in the open set $\Delta^c$.
Products of open sets form a basis of $X \times X$, so there are open $U \ni x$ and $V \ni y$ with $U \times V \subseteq \Delta^c$.
Then $U \times V$ does not meet $\Delta$, so $U \cap V = \emptyset$.
:::

:::

:::
:::
