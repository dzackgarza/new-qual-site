---
schema: qual/card@1
id: E-XFXGM
kind: problem
title: Product metrics, finite and countable
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 3, printed p. 133, with Theorem 20.5
    for the comparison; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.3, PDF pp. 23-24. The maximum metric on a
    finite product and the supremum of the truncated metrics divided by the index on a
    countable one both induce the product topology, by the two ball inclusions in each case
    and the choice of a finite initial segment where 1/N is below the radius.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $X_n$ be a metric space with metric $d_n$, for $n \in \ZZ_+$.

(a) Show that

$$
\rho(x, y) = \max\theset{d_1(x_1, y_1), \dots, d_n(x_n, y_n)}
$$

is a metric for the product space $X_1 \times \cdots \times X_n$.

(b) Let $\bar{d}_i = \min\theset{d_i, 1}$.
Show that

$$
D(x, y) = \sup\theset{\bar{d}_i(x_i, y_i)/i}
$$

is a metric for the product space $\prod X_i$.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.3** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs, with the metric axioms and the two inclusions of neighbourhood bases separated.

::: pf

::: {.pf-step #finite-metric}
(a) $\rho(\mathbf{x},\mathbf{y})=\max\theset{d_{1}(x_{1},y_{1}),\dots,d_{n}(x_{n},y_{n})}$ is a metric on $X_{1}\times\cdots\times X_{n}$.

::: pf-proof
$\rho\ge0$ and $\rho(\mathbf{x},\mathbf{y})=\rho(\mathbf{y},\mathbf{x})$ because each $d_{i}$ is a metric; $\rho(\mathbf{x},\mathbf{y})=0$ means $d_{i}(x_{i},y_{i})=0$ for every $i$, that is $\mathbf{x}=\mathbf{y}$. For the triangle inequality fix $i$: then $d_{i}(x_{i},z_{i})\le d_{i}(x_{i},y_{i})+d_{i}(y_{i},z_{i})\le\rho(\mathbf{x},\mathbf{y})+\rho(\mathbf{y},\mathbf{z})$, and $i$ was arbitrary, so the maximum $\rho(\mathbf{x},\mathbf{z})$ is at most $\rho(\mathbf{x},\mathbf{y})+\rho(\mathbf{y},\mathbf{z})$.
:::

:::

::: {.pf-step #finite-topology}
$\rho$ induces the product topology on $X_{1}\times\cdots\times X_{n}$.

::: pf-proof
Let $B_{d_{1}}(x_{1},r_{1})\times\cdots\times B_{d_{n}}(x_{n},r_{n})$ be a product basis element containing $\mathbf{x}$ and put $r=\min\theset{r_{1},\dots,r_{n}}>0$; then $\rho(\mathbf{x},\mathbf{y})<r$ forces $d_{i}(x_{i},y_{i})<r\le r_{i}$ for every $i$, so $B_{\rho}(\mathbf{x},r)\subseteq\prod B_{d_{i}}(x_{i},r_{i})$. Conversely, given $\varepsilon>0$, the set $\prod B_{d_{i}}(x_{i},\varepsilon)$ is a product neighbourhood of $\mathbf{x}$ contained in $B_{\rho}(\mathbf{x},\varepsilon)$, since $\rho(\mathbf{x},\mathbf{y})<\varepsilon$ follows from $d_{i}(x_{i},y_{i})<\varepsilon$ for all $i$. So the $\rho$-balls and the product basis elements generate each other's neighbourhoods, and the topologies agree.
:::

:::

::: {.pf-step #countable-metric}
(b) $D(\mathbf{x},\mathbf{y})=\sup_{i}\bar d_{i}(x_{i},y_{i})/i$, with $\bar d_{i}=\min\theset{d_{i},1}$, is a metric on $\prod_{i\in\ZZ_{+}}X_{i}$.

::: pf-proof
Each $\bar d_{i}$ is a metric bounded by $1$. So $D\ge0$, $D$ is symmetric, and $D(\mathbf{x},\mathbf{y})=0$ exactly when $x_{i}=y_{i}$ for all $i$. For the triangle inequality, each $i$ gives $\bar d_{i}(x_{i},z_{i})/i\le\bar d_{i}(x_{i},y_{i})/i+\bar d_{i}(y_{i},z_{i})/i\le D(\mathbf{x},\mathbf{y})+D(\mathbf{y},\mathbf{z})$; taking the supremum, $D(\mathbf{x},\mathbf{z})\le D(\mathbf{x},\mathbf{y})+D(\mathbf{y},\mathbf{z})$.
:::

:::

::: {.pf-step #countable-topology}
$D$ induces the product topology on $\prod_{i}X_{i}$.

::: pf-proof
First, $B_{D}(\mathbf{x},\varepsilon)$ contains a product neighbourhood: choose $N$ with $1/N<\varepsilon$ and take $U=\prod U_{i}$ with $U_{i}=B_{d_{i}}(x_{i},\varepsilon)$ for $i<N$ and $U_{i}=X_{i}$ for $i\ge N$. For $\mathbf{y}\in U$, each of the finitely many coordinates $i<N$ satisfies $\bar d_{i}(x_{i},y_{i})/i<\varepsilon$ and every coordinate with $i\ge N$ satisfies $\bar d_{i}(x_{i},y_{i})/i\le1/i\le1/N<\varepsilon$, so $D(\mathbf{x},\mathbf{y})<\varepsilon$. Conversely, let $\prod U_{i}$ be a product basis element containing $\mathbf{x}$, with $U_{i}=X_{i}$ except for $i_{1}<\cdots<i_{N}$; for each $k$ choose $0<r_{k}<1$ with $B_{d_{i_{k}}}(x_{i_{k}},r_{k})\subseteq U_{i_{k}}$ and put $\varepsilon=\min_{k}r_{k}/i_{N}$. If $D(\mathbf{x},\mathbf{y})<\varepsilon$ then for each $k$, $\bar d_{i_{k}}(x_{i_{k}},y_{i_{k}})<i_{k}\varepsilon\le r_{k}<1$, so $\bar d_{i_{k}}=d_{i_{k}}$ there and $y_{i_{k}}\in U_{i_{k}}$; in the other coordinates $\mathbf{y}$ is automatically in $U_{i}=X_{i}$. Hence $B_{D}(\mathbf{x},\varepsilon)\subseteq\prod U_{i}$.
:::

:::

::: {.pf-qed}
In (a) the maximum metric is a metric inducing the product topology by steps [](#finite-metric){.pf-ref} and [](#finite-topology){.pf-ref}; in (b) the supremum metric is a metric inducing the product topology by steps [](#countable-metric){.pf-ref} and [](#countable-topology){.pf-ref}.
:::

:::

:::
