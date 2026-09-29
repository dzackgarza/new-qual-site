---
schema: qual/card@1
id: E-GZX7B
kind: problem
title: Components of locally compact paracompact Hausdorff spaces are second countable
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Theorem.
If $X$ is a Hausdorff space that is locally compact and paracompact, then each component of $X$ has a countable basis.

Proof.
If $X_0$ is a component of $X$, then $X_0$ is locally compact and paracompact.
Let $\mathcal{C}$ be a locally finite covering of $X_0$ by sets open in $X_0$ that have compact closures.
Let $U_1$ be a nonempty element of $\mathcal{C}$, and in general let $U_n$ be the union of all elements of $\mathcal{C}$ that intersect $\overline{U}_{n-1}$.
Show that $\overline{U}_n$ is compact, and the sets $U_n$ cover $X_0$.
:::

::: {.solution}
Closures are taken in $X_0$.

::: pf

::: {.pf-step #closures-compact}
$\overline{U}_n$ is compact for every $n \ge 1$.

::: pf-proof

::: {.pf-step #u1-closure-compact}
$\overline{U}_1$ is compact.

::: pf-proof
$U_1 \in \mathcal{C}$, and every member of $\mathcal{C}$ has compact closure.
:::

:::

::: {.pf-step #finite-members-meet-closure}
If $\overline{U}_{n-1}$ is compact, then only finitely many members $V_1, \ldots, V_m$ of $\mathcal{C}$ meet $\overline{U}_{n-1}$.

::: pf-proof
By local finiteness, each $x \in \overline{U}_{n-1}$ has an open neighborhood $W_x$ that meets only finitely many members of $\mathcal{C}$. Finitely many of these, $W_{x_1}, \ldots, W_{x_k}$, cover the compact set $\overline{U}_{n-1}$. A member of $\mathcal{C}$ that meets $\overline{U}_{n-1}$ meets some $W_{x_i}$, and there are only finitely many such members.
:::

:::

::: pf-qed
Induct on $n$, with base case step [](#u1-closure-compact){.pf-ref}. If $\overline{U}_{n-1}$ is compact, step [](#finite-members-meet-closure){.pf-ref} gives $U_n = V_1 \cup \cdots \cup V_m$, so
$$\overline{U}_n = \overline{V}_1 \cup \cdots \cup \overline{V}_m$$
is a finite union of compact sets, hence compact.
:::

:::

:::

::: {.pf-step #a-nonempty-open}
$A = \bigcup_{n=1}^\infty U_n$ is nonempty and open in $X_0$.

::: pf-proof
$A$ contains the nonempty set $U_1$, and each $U_n$ is a union of sets open in $X_0$.
:::

:::

::: {.pf-step #a-closed}
$A$ is closed in $X_0$.

::: pf-proof
Let $x \in \overline{A}$. Since $\mathcal{C}$ covers $X_0$, some $V_0 \in \mathcal{C}$ contains $x$. The open set $V_0$ meets $A$, so it meets $U_{n-1}$ for some $n \ge 2$, hence meets $\overline{U}_{n-1}$. By the definition of $U_n$, $V_0 \subseteq U_n \subseteq A$, so $x \in A$.
:::

:::

::: pf-qed
Step [](#closures-compact){.pf-ref} shows that each $\overline{U}_n$ is compact. By steps [](#a-nonempty-open){.pf-ref} and [](#a-closed){.pf-ref}, $A$ is a nonempty open and closed subset of the connected space $X_0$, so $A = X_0$: the sets $U_n$ cover $X_0$.
:::

:::

:::
