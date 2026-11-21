---
schema: qual/card@1
id: P-OKDFC
kind: problem
title: A countable base implies a countable dense subset, and the converse in metric
  spaces
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts of the statement verbatim against problem 4 of the official UGA Spring 2015 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Repaired the countability argument and added the empty-space case; verified the rational-ball basis proof.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight of the card's eleven steps --- the three of part (a) and the five of part (b) ---
    asserted their claim with no proof body; each now carries a `pf-proof`. No claim was
    changed and both statements stand as the examination prints them. Checked: that the choice
    made in part (a) is a choice over a countable index set, that a basis element inside a
    nonempty open set may be taken nonempty, the density criterion used, the countability of
    $J\times\QQ_{>0}$, the basis criterion of Munkres Lemma 13.2 applied in part (b), and the
    strict inequality chain $d(y,x)<2r<\epsilon$. Not checked: the printed examination paper;
    the statement is vouched for by the `source-checked` event of 2026-09-05.
---

::: {.problem}
a. Prove that a topological space that has a countable base for its topology also contains a countable dense subset.

b. Prove that the converse to (a) holds if the space is a metric space.
:::

::: {.solution}

::: pf

::: pf-step

If $X=\emptyset$, both assertions are immediate.
Henceforth assume $X\ne\emptyset$.

::: pf-proof

The empty set is a countable dense subset of the empty space, and the empty family is a countable basis for its topology.

:::

:::

::: pf-step

Part (a): second countable implies separable.

::: pf-proof

Steps 1.1--1.3 choose one point from each nonempty basis element and check that the resulting countable set meets every nonempty open set.

::: pf-step

Let $\mathcal{B} = \{B_n:n\in J\}$ be a countable basis for the topology of $X$, where $J\subseteq\NN$.
For each non-empty basis element $B_n \in \mathcal{B}$, choose an element $x_n \in B_n$.
Define the set:
$$
D = \{x_n \mid n\in J,\ B_n \neq \emptyset\}.
$$
The set $D$ is the image of a subset of $J\subseteq\NN$ under the map $n\mapsto x_n$, so $D$ is at most countable.

::: pf-proof

Choosing one point from each nonempty $B_n$ is a choice over the countable index set $\{n\in J:B_n\ne\emptyset\}$. $D$ is the image of that subset of $J$ under $n\mapsto x_n$; a subset of $\NN$ is at most countable, and the image of an at most countable set is at most countable, so $D$ is at most countable.

:::

:::

::: pf-step

To prove $D$ is dense in $X$, let $U \subseteq X$ be any non-empty open set.
Since $\mathcal{B}$ is a basis, there exists a non-empty basis element $B_k \in \mathcal{B}$ such that $B_k \subseteq U$.

::: pf-proof

Take a point $x\in U$, possible because $U$ is nonempty. A basis for the topology is a family such that every open set is a union of its members (Munkres, §13), so some $B_k\in\mathcal{B}$ contains $x$ and is contained in $U$. Being a set containing $x$, $B_k$ is nonempty.

:::

:::

::: pf-step

By construction, $x_k \in B_k \subseteq U$, so $x_k \in D \cap U \neq \emptyset$.
Thus $D$ intersects every non-empty open set of $X$, so $\overline{D} = X$.
Hence $X$ has a countable dense subset (is separable).

::: pf-proof

$B_k$ is nonempty, so $x_k$ was chosen in $B_k$ by step 1.1, and $B_k\subseteq U$ by step 1.2; hence $x_k\in D\cap U$. A set meeting every nonempty open set is dense: if $x\notin\overline D$, the open set $X\setminus\overline D$ contains $x$ and misses $D$ (Munkres, §17). So $\overline D=X$ and $D$ is a countable dense subset.

:::

:::

:::

:::

::: pf-step

Part (b): separable metric space implies second countable.

::: pf-proof

Steps 2.1--2.4 show that the rational balls about the dense set form a basis: every point of an open set lies in one of them contained in that set. Step 2.5 applies the basis criterion.

::: pf-step

Let $(X, d)$ be a metric space containing a countable dense subset $D = \{d_n:n\in J\}$, where $J\subseteq\NN$.
Consider the collection of open balls with centers in $D$ and rational radii:
$$
\mathcal{B} = \{ B(d_n, r) \mid n\in J, \, r \in \QQ_{>0} \}.
$$
As the image of the countable set $J \times \QQ_{>0}$, $\mathcal{B}$ is a countable collection of open subsets of $X$.

::: pf-proof

$J\subseteq\NN$ is at most countable and $\QQ_{>0}$ is countable, so $J\times\QQ_{>0}$ is at most countable (Munkres, Corollary 7.6). $\mathcal{B}$ is the image of that set under $(n,r)\mapsto B(d_n,r)$, hence at most countable, and each $B(d_n,r)$ is open in the metric topology (Munkres, §20).

:::

:::

::: pf-step

Let $U \subseteq X$ be an open set and $x \in U$.
By definition of the metric topology, there exists $\epsilon > 0$ such that $B(x, \epsilon) \subseteq U$.
Choose a rational number $r \in \QQ$ such that $0 < r < \epsilon / 2$.

::: pf-proof

The open balls form a basis for the metric topology, so $U$, being open and containing $x$, contains a ball $B(x,\epsilon)$ about $x$ with $\epsilon>0$. Since $\epsilon/2>0$ and $\QQ$ is dense in $\RR$, there is a rational $r$ with $0<r<\epsilon/2$.

:::

:::

::: pf-step

Since $D$ is dense in $X$, the open ball $B(x, r)$ contains some point $d_n \in D$, so $d(x, d_n) < r$.
Then $x \in B(d_n, r)$.

::: pf-proof

$B(x,r)$ is a nonempty open set and $\overline D=X$, so $B(x,r)\cap D\ne\emptyset$: a point of $X$ outside $\overline D$ would have an open neighbourhood missing $D$. Take $d_n$ in that intersection; $d(x,d_n)<r$ is exactly $x\in B(d_n,r)$, since the metric is symmetric.

:::

:::

::: pf-step

For any $y \in B(d_n, r)$, by the triangle inequality:
$$
d(y, x) \le d(y, d_n) + d(d_n, x) < r + r = 2r < \epsilon.
$$
Thus $y \in B(x, \epsilon) \subseteq U$, which proves $B(d_n, r) \subseteq U$.
Therefore $x \in B(d_n, r) \subseteq U$ with $B(d_n, r) \in \mathcal{B}$.

::: pf-proof

The triangle inequality is a metric axiom. $d(y,d_n)<r$ because $y\in B(d_n,r)$, and $d(d_n,x)<r$ by step 2.3; so $d(y,x)<2r$, and $2r<\epsilon$ by the choice of $r$ in step 2.2. Hence every $y\in B(d_n,r)$ lies in $B(x,\epsilon)$, which is contained in $U$.

:::

:::

::: pf-step

Thus $\mathcal{B}$ is a countable basis for the topology of $X$, so $X$ is second countable.

::: pf-proof

Steps 2.2--2.4 verify the basis criterion of Munkres, Lemma 13.2: for every open $U$ and every $x\in U$ there is a member $B$ of $\mathcal{B}$ with $x\in B\subseteq U$. So $\mathcal{B}$ is a basis, and it is countable by step 2.1; hence $X$ is second countable.

:::

:::

:::

:::

:::
:::