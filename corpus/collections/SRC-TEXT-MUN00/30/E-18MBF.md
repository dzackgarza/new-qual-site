---
schema: qual/card@1
id: E-18MBF
kind: problem
title: Products with a compact factor are Lindelof
classification:
  areas:
  - topology
  topics:
  - Countability
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $X$ is Lindelöf and $Y$ is compact, then $X \times Y$ is Lindelöf.
:::

::: {.solution}
**Goal:** Prove that the product space $X \times Y$ of a Lindelöf space $X$ and a compact space $Y$ is Lindelöf.

::: pf

::: {.pf-step #slices-finite-subcovers}
Slices $\{x\} \times Y$ and finite subcovers:
Let $\mathcal{A}$ be any open cover of $X \times Y$.
For each $x \in X$, there exists a finite subcollection $\mathcal{A}_x \subset \mathcal{A}$ and an open neighborhood $U_x \subseteq X$ of $x$ such that:
$$U_x \times Y \subseteq \bigcup_{A \in \mathcal{A}_x} A.$$

::: pf-proof

::: pf-step
The slice $\{x\} \times Y$ is homeomorphic to $Y$, hence compact.
:::

::: pf-step
Since $\mathcal{A}$ is an open cover of $X \times Y$, it covers $\{x\} \times Y$. By compactness of $\{x\} \times Y$, there exists a finite subcollection $\mathcal{A}_x = \{A_1, \dots, A_k\} \subset \mathcal{A}$ such that $\{x\} \times Y \subseteq \bigcup_{i=1}^k A_i =: W_x$.
:::

::: pf-step
The set $W_x$ is open in $X \times Y$ and contains the slice $\{x\} \times Y$.
:::

::: pf-step
Since $Y$ is compact, the Tube Lemma applies: there exists an open neighborhood $U_x$ of $x$ in $X$ such that $U_x \times Y \subseteq W_x$.
:::

:::

:::

::: {.pf-step #countable-subcover-of-x}
Countable subcover of $X$:
There exists a countable sequence of points $(x_n)_{n=1}^\infty$ in $X$ such that $X = \bigcup_{n=1}^\infty U_{x_n}$.

::: pf-proof
The collection $\{U_x : x \in X\}$ is an open cover of $X$. Since $X$ is Lindelöf, there exists a countable subcover $\{U_{x_n} : n \in \mathbb{Z}_+\}$.
:::

:::

::: pf-step
Construction of the countable subcover of $X \times Y$:
The subcollection $\mathcal{A}^* = \bigcup_{n=1}^\infty \mathcal{A}_{x_n} \subset \mathcal{A}$ is a countable open cover of $X \times Y$.

::: pf-proof

::: pf-step
Countability: Each $\mathcal{A}_{x_n}$ is finite by step [](#slices-finite-subcovers){.pf-ref}. A countable union of finite sets is countable, so $\mathcal{A}^*$ is countable.
:::

::: pf-step
Covering property: For any $(x, y) \in X \times Y$, step [](#countable-subcover-of-x){.pf-ref} guarantees $x \in U_{x_m}$ for some $m \in \mathbb{Z}_+$.
:::

::: pf-step
Then $(x, y) \in U_{x_m} \times Y \subseteq \bigcup_{A \in \mathcal{A}_{x_m}} A \subseteq \bigcup_{A \in \mathcal{A}^*} A$.
:::

::: pf-step
Thus $\mathcal{A}^*$ covers $X \times Y$.
:::

:::

:::

::: pf-step
Conclusion:
Every open cover $\mathcal{A}$ of $X \times Y$ admits a countable subcover $\mathcal{A}^*$, so $X \times Y$ is Lindelöf. Q.E.D.
:::

:::

:::
