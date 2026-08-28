---
schema: qual/card@1
id: E-8Q9TN
kind: exercise
title: Star-fine refinements of open coverings
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a space; let $\mathcal{A}$ be an open covering of $X$.
Under what conditions does there exist an open covering $\mathcal{B}$ of $X$ refining $\mathcal{A}$ such that for each pair $B, B'$ of elements of $\mathcal{B}$ that have nonempty intersection, the union $B \cup B'$ lies in an element of $\mathcal{A}$?

(a) Show that such a covering $\mathcal{B}$ exists if $X$ is metrizable.
[Hint: Choose $\epsilon(x)$ so that $B(x, 3\epsilon(x))$ lies in an element of $\mathcal{A}$. Let $\mathcal{B}$ consist of the open sets $B(x, \epsilon(x))$.]

(b) Show that such a covering exists if $X$ is compact Hausdorff.
[Hint: Let $A_1, \ldots, A_n$ be a finite subcollection of $\mathcal{A}$ that covers $X$.
Choose an open covering $C_1, \ldots, C_n$ of $X$ such that $\overline{C}_i \subset A_i$ for each $i$.
For each nonempty subset $J$ of $\ts{1, \ldots, n}$, consider the set

$$
B_J = \bigcap_{j \in J} A_j - \bigcup_{j \notin J} \overline{C}_j.]
$$
:::

::: solution
**Goal:** Prove the existence of a star-fine open refinement $\mathcal{B}$ of an open covering $\mathcal{A}$ (satisfying $B \cap B' \neq \varnothing \implies B \cup B' \subseteq A$ for some $A \in \mathcal{A}$) when $X$ is metrizable or compact Hausdorff.

<1>1. Part (a): Case where $X$ is metrizable.
    *Proof:*
    <2>1. Let $d$ be a compatible metric on $X$.
    <2>2. For each $x \in X$, choose $A_x \in \mathcal{A}$ containing $x$. Since $A_x$ is open, there is $r_x > 0$ such that the metric ball $B(x, r_x) \subseteq A_x$.
    <2>3. Set $\varepsilon(x) = r_x / 3 > 0$, so $B(x, 3\varepsilon(x)) \subseteq A_x \in \mathcal{A}$.
    <2>4. Define $\mathcal{B} = \{B(x, \varepsilon(x)) \mid x \in X\}$. Since $x \in B(x, \varepsilon(x))$, $\mathcal{B}$ is an open covering of $X$.
    <2>5. Suppose $B_1 = B(x_1, \varepsilon(x_1))$ and $B_2 = B(x_2, \varepsilon(x_2))$ have non-empty intersection, with $z \in B_1 \cap B_2$.
    <2>6. Without loss of generality, assume $\varepsilon(x_1) \ge \varepsilon(x_2)$.
    <2>7. For any $y \in B_2$, $d(y, x_1) \le d(y, x_2) + d(x_2, z) + d(z, x_1) < \varepsilon(x_2) + \varepsilon(x_2) + \varepsilon(x_1) \le 3\varepsilon(x_1)$.
    <2>8. For any $y \in B_1$, $d(y, x_1) < \varepsilon(x_1) < 3\varepsilon(x_1)$.
    <2>9. Thus $B_1 \cup B_2 \subseteq B(x_1, 3\varepsilon(x_1)) \subseteq A_{x_1} \in \mathcal{A}$.

<1>2. Part (b): Case where $X$ is compact Hausdorff.
    *Proof:*
    <2>1. By compactness of $X$, extract a finite subcover $\{A_1, \dots, A_n\} \subseteq \mathcal{A}$.
    <2>2. Because compact Hausdorff spaces are normal, the Shrinking Lemma gives an open cover $\{C_1, \dots, C_n\}$ of $X$ with $\overline{C}_i \subseteq A_i$ for each $i = 1, \dots, n$.
    <2>3. For each non-empty subset $J \subseteq \{1, \dots, n\}$, define:
        $$B_J = \left( \bigcap_{j \in J} A_j \right) \setminus \left( \bigcup_{k \notin J} \overline{C}_k \right) = \left( \bigcap_{j \in J} A_j \right) \cap \left( \bigcap_{k \notin J} (X \setminus \overline{C}_k) \right).$$
    <2>4. Each $B_J$ is open, being a finite intersection of open sets.
    <2>5. **$\mathcal{B} = \{B_J\}$ covers $X$:** For any $x \in X$, let $J(x) = \{i \mid x \in \overline{C}_i\}$. Since $\{C_i\}$ covers $X$, $J(x) \neq \varnothing$. By definition, $x \in \overline{C}_j \subseteq A_j$ for $j \in J(x)$ and $x \notin \overline{C}_k$ for $k \notin J(x)$, so $x \in B_{J(x)}$.
    <2>6. **Star refinement property:** Suppose $B_J \cap B_K \neq \varnothing$, and let $x \in B_J \cap B_K$.
    <2>7. Since $\{C_1, \dots, C_n\}$ covers $X$, $x \in C_{j_0} \subseteq \overline{C}_{j_0}$ for some $j_0$.
    <2>8. Because $x \in B_J$, $x \notin \overline{C}_k$ for all $k \notin J$, which forces $j_0 \in J$.
    <2>9. Symmetrically, $x \in B_K$ forces $j_0 \in K$.
    <2>10. Thus $j_0 \in J \cap K$.
    <2>11. By definition of $B_J$ and $B_K$, $B_J \subseteq A_{j_0}$ and $B_K \subseteq A_{j_0}$, so:
        $$B_J \cup B_K \subseteq A_{j_0} \in \mathcal{A}.$$

<1>3. Conclusion:
    Such an open star-refinement $\mathcal{B}$ exists whenever $X$ is metrizable or compact Hausdorff (and more generally, whenever $X$ is paracompact). Q.E.D.
:::
