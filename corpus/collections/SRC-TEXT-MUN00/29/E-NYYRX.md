---
schema: qual/card@1
id: E-NYYRX
kind: problem
title: Accumulation points of nets
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
    Transcribed from Martin Sleziak's answer 3656282 to his question 3656281, "Cluster point of a
    net is a limit of a subnet" (2020-05-03),
    https://math.stackexchange.com/questions/3656281, text at
    tmp/sources/mse-3656281-munkres-29-net-9b.md: the set of pairs (U, d) with x_d in U, ordered
    by reverse inclusion in U and the order of D, is directed, and its projection is monotone and
    cofinal. Sleziak proves only this implication, being asked for it, and writes the index set
    with U first where Munkres writes the index first; the card restates it in Munkres' order,
    proves the converse (a convergent subnet puts the net frequently in each neighborhood of its
    limit), and records that accumulation point as Munkres defines it means exactly Sleziak's
    "frequently in U". dbFin's solution to this exercise reaches the same directed set, and its
    argument for that converse, with the set L of values of the subnet at the indices above a fixed
    one, which it shows to be cofinal in J, is valid: the set of indices at which the net lies in a
    neighborhood of the limit contains L and is therefore cofinal. An earlier version of this note
    recorded that argument as not a proof, which was wrong. This supersedes the 2026-11-10 note
    above.
---

::: {.exercise}

Let $(x_\alpha)_{\alpha \in J}$ be a net in $X$.
We say that $x$ is an accumulation point of the net $(x_\alpha)$ if for each neighborhood $U$ of $x$, the set of those $\alpha$ for which $x_\alpha \in U$ is cofinal in $J$.

Lemma.
The net $(x_\alpha)$ has the point $x$ as an accumulation point if and only if some subnet of $(x_\alpha)$ converges to $x$.

[Hint: To prove the implication $\Rightarrow$, let $K$ be the set of all pairs $(\alpha, U)$ where $\alpha \in J$ and $U$ is a neighborhood of $x$ containing $x_\alpha$. Define $(\alpha, U) \preceq (\beta, V)$ if $\alpha \preceq \beta$ and $V \subseteq U$. Show that $K$ is a directed set and use it to define the subnet.]
:::

::: {.solution}

For a net $(x_\alpha)_{\alpha \in J}$ and a point $x$, the two formulations of accumulation point used below agree: the set of $\alpha$ with $x_\alpha \in U$ is cofinal in $J$ for every neighborhood $U$ of $x$ if and only if for every neighborhood $U$ of $x$ and every $\alpha_0 \in J$ there is $\delta \succeq \alpha_0$ with $x_\delta \in U$.

::: pf

::: pf-step
If $x$ is an accumulation point of $(x_\alpha)$, then some subnet of $(x_\alpha)$ converges to $x$.

::: pf-proof
Let $K$ be the set of pairs $(\alpha, U)$ with $\alpha \in J$, $U$ a neighborhood of $x$ and $x_\alpha \in U$, ordered by $(\alpha, U) \preceq (\beta, V)$ when $\alpha \preceq \beta$ and $V \subset U$.

$K$ is a directed set. The order is a partial order, being a product of two partial orders. Given $(\alpha_1, U_1)$ and $(\alpha_2, U_2)$ in $K$, choose $\delta \in J$ with $\alpha_1 \preceq \delta$ and $\alpha_2 \preceq \delta$; the set $U_1 \cap U_2$ is a neighborhood of $x$, and since $x$ is an accumulation point some $\alpha \succeq \delta$ has $x_\alpha \in U_1 \cap U_2$. Then $(\alpha, U_1 \cap U_2) \in K$ and dominates both.

The projection $g : K \to J$, $g(\alpha, U) = \alpha$, is order preserving, and its image is cofinal in $J$: for $\alpha_0 \in J$ and any neighborhood $U$ of $x$, some $\alpha \succeq \alpha_0$ has $x_\alpha \in U$, so $(\alpha, U) \in K$ and $g(\alpha, U) = \alpha \succeq \alpha_0$. Hence $(x_{g(k)})_{k \in K}$ is a subnet of $(x_\alpha)$.

That subnet converges to $x$: given a neighborhood $W$ of $x$, the set of $\alpha$ with $x_\alpha \in W$ is cofinal, so there is $\alpha_W$ with $x_{\alpha_W} \in W$ and $(\alpha_W, W) \in K$; for $(\beta, V) \succeq (\alpha_W, W)$ we have $V \subset W$ and $x_\beta \in V \subset W$.
:::

:::

::: pf-step
If some subnet of $(x_\alpha)$ converges to $x$, then $x$ is an accumulation point of $(x_\alpha)$.

::: pf-proof
Let the subnet be $(x_{g(\kappa)})_{\kappa \in K}$ for an order preserving $g : K \to J$ with cofinal image, and let $U$ be a neighborhood of $x$ and $\alpha_0 \in J$. Convergence gives $\kappa_0 \in K$ with $x_{g(\kappa)} \in U$ whenever $\kappa_0 \preceq \kappa$, and cofinality of $g(K)$ gives $\kappa_1 \in K$ with $\alpha_0 \preceq g(\kappa_1)$. Choose $\kappa \in K$ with $\kappa_0 \preceq \kappa$ and $\kappa_1 \preceq \kappa$; then $x_{g(\kappa)} \in U$ and $\alpha_0 \preceq g(\kappa_1) \preceq g(\kappa)$. So indices with $x_\alpha \in U$ occur above $\alpha_0$, and $x$ is an accumulation point.
:::

:::

::: pf-step
The net $(x_\alpha)$ has $x$ as an accumulation point if and only if some subnet of it converges to $x$. $\square$

::: pf-proof
The two implications are steps 1 and 2.
:::

:::

:::

:::
