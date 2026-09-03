---
schema: qual/card@1
id: E-CTM3H
kind: problem
title: Where the countable intersection property breaks the Tychonoff argument
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Consider the three statements:

(i) If $X$ is a set and $\mathcal{A}$ is a collection of subsets of $X$ having the countable intersection property, then there is a collection $\mathcal{D}$ of subsets of $X$ such that $\mathcal{D} \supset \mathcal{A}$ and $\mathcal{D}$ is maximal with respect to the countable intersection property.

(ii) Suppose $\mathcal{D}$ is maximal with respect to the countable intersection property.
Then countable intersections of elements of $\mathcal{D}$ are in $\mathcal{D}$.
Furthermore, if $A$ is a subset of $X$ that intersects every element of $\mathcal{D}$, then $A$ is an element of $\mathcal{D}$.

(iii) Products of Lindelöf spaces are Lindelöf.

(a) Show that (i) and (ii) together imply (iii).

(b) Show that (ii) holds.

(c) Products of Lindelöf spaces need not be Lindelöf (see §30). Therefore (i) does not hold.
If one attempts to generalize the proof of Lemma 37.1 to the countable intersection property, at what point does the proof break down?
:::

::: {.solution}
**(a).**

<1>1. Let $\{X_\alpha\}$ be a family of Lindelöf spaces, and let $\mathcal{U}$ be an open cover of $X = \prod_\alpha X_\alpha$.
::: {.proof}
setup.
:::

<1>2. Suppose $X$ is not Lindelöf, so $\mathcal{U}$ has no countable subcover.
::: {.proof}
assume for contradiction.
:::

<1>3. The collection $\mathcal{A} = \{X - U : U \in \mathcal{U}\}$ has the countable intersection property.
::: {.proof}
if $\bigcap_{i=1}^{\infty} (X - U_i) = \varnothing$, then $\{U_i\}$ would be a countable subcover, contradicting <1>2.
:::

<1>4. By (i), extend $\mathcal{A}$ to a maximal collection $\mathcal{D}$ with the countable intersection property.
::: {.proof}
(i).
:::

<1>5. By (ii), $\mathcal{D}$ is closed under countable intersections, and any set meeting every element of $\mathcal{D}$ is in $\mathcal{D}$.
::: {.proof}
(ii).
:::

<1>6. For each $\alpha$, the projections $\pi_\alpha(D)$ for $D \in \mathcal{D}$ have the countable intersection property in $X_\alpha$, so (by Lindelöfness of $X_\alpha$) there is a point $x_\alpha$ in the closure of every $\pi_\alpha(D)$.
::: {.proof}
Lindelöfness implies the countable intersection property of closed sets has nonempty intersection.
:::

<1>7. The point $x = (x_\alpha)$ lies in $\overline{D}$ for every $D \in \mathcal{D}$, so every neighborhood of $x$ meets every $D \in \mathcal{D}$.
::: {.proof}
<1>6.
:::

<1>8. By (ii), every neighborhood of $x$ is in $\mathcal{D}$, so $x \in \bigcap_{D \in \mathcal{D}} \overline{D}$, contradicting that $\mathcal{D}$ contains $X - U$ for each $U \in \mathcal{U}$ (so $\bigcap_{D \in \mathcal{D}} \overline{D} = \varnothing$ since $\mathcal{U}$ covers $X$).
::: {.proof}
<1>7 and the fact that $\mathcal{U}$ covers $X$.
:::

<1>9. Contradiction, so $X$ is Lindelöf.
::: {.proof}
<1>8.
:::

**(b).**

<1>1. Let $\mathcal{D}$ be maximal with the countable intersection property.
::: {.proof}
setup.
:::

<1>2. If $D_1, D_2, \ldots \in \mathcal{D}$, then $\bigcap_i D_i \in \mathcal{D}$.
::: {.proof}
if $\bigcap_i D_i \notin \mathcal{D}$, then by maximality $\mathcal{D} \cup \{\bigcap_i D_i\}$ fails the countable intersection property, so there are $E_1, E_2, \ldots \in \mathcal{D}$ with $(\bigcap_i D_i) \cap \bigcap_j E_j = \varnothing$; but then $D_1, D_2, \ldots, E_1, E_2, \ldots$ is a countable subcollection of $\mathcal{D}$ with empty intersection, contradicting the countable intersection property of $\mathcal{D}$.
:::

<1>3. If $A$ meets every element of $\mathcal{D}$, then $A \in \mathcal{D}$.
::: {.proof}
if $A \notin \mathcal{D}$, then by maximality $\mathcal{D} \cup \{A\}$ fails the countable intersection property, so there are $D_1, D_2, \ldots \in \mathcal{D}$ with $A \cap \bigcap_i D_i = \varnothing$; but $\bigcap_i D_i \in \mathcal{D}$ by <1>2, contradicting that $A$ meets every element of $\mathcal{D}$.
:::

<1>4. Hence (ii) holds.
::: {.proof}
<1>2 and <1>3.
:::

**(c).**

<1>1. The proof of Lemma 37.1 (for the finite intersection property) uses Zorn's lemma to extend $\mathcal{A}$ to a maximal collection with the finite intersection property.
::: {.proof}
recall the structure of the proof.
:::

<1>2. The breakdown occurs in the Zorn's-lemma step: the union of a chain of collections with the finite intersection property again has the finite intersection property, but the union of a chain of collections with the *countable* intersection property need not have the countable intersection property.
::: {.proof}
a countable intersection of elements of the union may involve one element from each of countably many different collections in the chain, and there is no single collection in the chain containing all of them.
:::

<1>3. Hence Zorn's lemma cannot be applied to extend $\mathcal{A}$ to a maximal collection with the countable intersection property, so (i) fails.
::: {.proof}
<1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>9 (a), <1>4 (b), <1>3 (c).
:::
:::
