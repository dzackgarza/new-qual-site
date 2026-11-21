---
schema: qual/card@1
id: E-MUN-3-12
kind: problem
title: Three order types on $\ZZ_+\times\ZZ_+$
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 12, printed p. 29: the three
    order relations (dictionary; x_0 - y_0 with y breaking ties; x_0 + y_0 with y
    breaking ties) on Z_+ x Z_+, asking which elements have immediate predecessors,
    whether there is a smallest element, and that the three order types differ. The
    stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.12,
    printed pp. 31-35 (tmp/sources/munkres-solutions-whitman.pdf). All three answers and
    all three order-type separations are his, including his Lemma 3.12.1 (an
    order-isomorphism preserves having a smallest element) and the counting of elements
    without an immediate predecessor that separates (i) from (iii).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked the "no immediate predecessor" cases of (ii) against the printed order: for
    (x,y) with x = 1 or y = 1 and (x_0,y_0) < (x,y), the card shows x_0 - y_0 < x - y
    (the alternative forces x_0 < 1 in the case x = 1 and y_0 < 1 in the case y = 1),
    which is what makes (x_0+1, y_0+1) lie strictly in between.
---

::: {.exercise}

Let $\ZZ_+$ denote the set of positive integers. Consider the following order relations on $\ZZ_+ \times \ZZ_+$:

(i) The dictionary order.

(ii) $(x_0, y_0) < (x_1, y_1)$ if either $x_0 - y_0 < x_1 - y_1$, or $x_0 - y_0 = x_1 - y_1$ and $y_0 < y_1$.

(iii) $(x_0, y_0) < (x_1, y_1)$ if either $x_0 + y_0 < x_1 + y_1$, or $x_0 + y_0 = x_1 + y_1$ and $y_0 < y_1$.

In these order relations, which elements have immediate predecessors? Does the set have a smallest element? Show that all three order types are different.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.12** (`tmp/sources/munkres-solutions-whitman.pdf`); the three answers, the case analyses and the separation of the order types are his. Throughout, an element has no immediate predecessor exactly when each element below it has something strictly between.

::: pf

::: {.pf-step #criterion}

An element $p$ has an immediate predecessor exactly when the set of elements below $p$ has a greatest element.

::: pf-proof

An immediate predecessor of $p$ is an element $q<p$ such that no element lies strictly between $q$ and $p$; so $q$ is a greatest element of $\{r:r<p\}$, and conversely a greatest element of that set has nothing between it and $p$ and is therefore an immediate predecessor. Hence $p$ has none exactly when every $r<p$ has some $s$ with $r<s<p$.

:::

:::

::: {.pf-step #table}

The answers for the three orders are as tabulated.

::: pf-proof

$$
\begin{array}{c|l|l}
\text{order} & \text{immediate predecessor} & \text{smallest element}\\ \hline
\text{(i)} & \text{every }(x,y)\text{ with }y>1,\text{ namely }(x,y-1);\ \text{none with }y=1 & (1,1)\\
\text{(ii)} & \text{every }(x,y)\text{ with }x>1,\ y>1,\text{ namely }(x-1,y-1);\ \text{none with }x=1\text{ or }y=1 & \text{none}\\
\text{(iii)} & \text{every }(x,y)\ne(1,1);\ \text{none other} & (1,1)
\end{array}
$$
The three rows are established in steps [](#orderi){.pf-ref}, [](#orderii){.pf-ref} and [](#orderiii){.pf-ref} respectively.

:::

:::

::: {.pf-step #orderi}

For the dictionary order (i), $(1,1)$ is smallest; $(x,y)$ with $y>1$ has the immediate predecessor $(x,y-1)$; nothing of the form $(x,1)$ has an immediate predecessor.

::: pf-proof

Here $(x_{0},y_{0})<(x_{1},y_{1})$ means $x_{0}<x_{1}$, or $x_{0}=x_{1}$ and $y_{0}<y_{1}$. Given any $(x,y)$: if $x>1$ then $(1,1)<(x,y)$ in the first clause; if $x=1$ then $y\ge1$ and $y>1$ gives $(1,1)<(1,y)$ in the second. So $(1,1)$ is smallest. If $y_{1}>1$ then $(x_{1},y_{1}-1)<(x_{1},y_{1})$, and an element strictly between would have $x_{2}=x_{1}$ (since $x_{1}<x_{2}$ would put it above $(x_{1},y_{1})$ itself) and $y_{1}-1<y_{2}<y_{1}$, impossible in $\ZZ_{+}$. If instead $y_{1}=1$ and $(x_{0},y_{0})<(x_{1},1)$, then $x_{0}<x_{1}$, since $y_{0}<1$ is impossible in $\ZZ_{+}$; then $(x_{0},y_{0})<(x_{0},y_{0}+1)<(x_{1},1)$, so no element below $(x_{1},1)$ is greatest and by step [](#criterion){.pf-ref} it has no immediate predecessor.

:::

:::

::: {.pf-step #orderii}

For order (ii), there is no smallest element; $(x,y)$ with $x>1$, $y>1$ has the immediate predecessor $(x-1,y-1)$; no element with $x=1$ or $y=1$ has one.

::: pf-proof

Write $\delta(x,y)=x-y$. Since $(x,y+1)$ has $\delta=x-y-1<x-y$, it lies below $(x,y)$, so no element is smallest in this order. Suppose $x_{1}>1$ and $y_{1}>1$: then $(x_{1}-1,y_{1}-1)$ has the same $\delta$ as $(x_{1},y_{1})$ and a smaller second coordinate, so it is below; an element strictly between would have to share that $\delta$ (otherwise $(x_{1},y_{1})$ would be below it) and then $y_{1}-1<y_{2}<y_{1}$, impossible. Suppose $x_{1}=1$ or $y_{1}=1$ and $(x_{0},y_{0})<(x_{1},y_{1})$: then necessarily $\delta(x_{0},y_{0})<\delta(x_{1},y_{1})$, because the equal-value alternative would force $y_{0}<y_{1}=1$ when $y_{1}=1$, and when $x_{1}=1$ would force $x_{0}=\delta(x_{0},y_{0})+y_{0}<(1-y_{1})+y_{1}=1$, contradicting $x_{0}\in\ZZ_{+}$. Then $(x_{0}+1,y_{0}+1)$ has the same $\delta$ as $(x_{0},y_{0})$ and a larger second coordinate, so $(x_{0},y_{0})<(x_{0}+1,y_{0}+1)$, while $\delta(x_{0},y_{0})<\delta(x_{1},y_{1})$ gives $(x_{0}+1,y_{0}+1)<(x_{1},y_{1})$. Hence no element below $(x_{1},y_{1})$ is greatest.

:::

:::

::: {.pf-step #orderiii}

For order (iii), $(1,1)$ is smallest and has no predecessor; every other element has an immediate predecessor.

::: pf-proof

Write $\sigma(x,y)=x+y$. For $(x,y)\ne(1,1)$ either $x>1$, and then $\sigma(1,1)=2\le1+y<\sigma(x,y)$, or $y>1$ and $2\le x+1<\sigma(x,y)$; in both cases $(1,1)<(x,y)$, so $(1,1)$ is smallest, and it has no predecessor since nothing is below it. If $y_{1}=1$ then $x_{1}>1$ (as $(x_{1},y_{1})\ne(1,1)$) and $(1,x_{1}-1)$ has sum $x_{1}<x_{1}+y_{1}$, hence is below; an element strictly between would satisfy $\sigma(x_{2},y_{2})<x_{1}+1$ (the alternative forcing $y_{2}<y_{1}=1$, impossible) and $x_{1}+1=x_{1}+y_{1}\le\sigma(x_{2},y_{2})$, a contradiction. If $y_{1}>1$ then $(x_{1}+1,y_{1}-1)$ has the same sum $\sigma(x_{1},y_{1})$ and second coordinate $y_{1}-1<y_{1}$, hence is below; an element strictly between would satisfy $x_{1}+y_{1}\le\sigma(x_{2},y_{2})\le\sigma(x_{1},y_{1})$, hence equal sums, and then $y_{1}-1<y_{2}<y_{1}$, impossible.

:::

:::

::: {.pf-step #distinct}

No two of the three orders have the same order type.

::: pf-proof

An order isomorphism carries a smallest element to a smallest element, and carries the set of elements with no immediate predecessor onto the corresponding set, since having an immediate predecessor is the non-emptiness of an order interval and is expressed by the order relation alone. Orders (i) and (iii) have a smallest element while (ii) has none, by steps [](#orderi){.pf-ref}, [](#orderii){.pf-ref} and [](#orderiii){.pf-ref}, so (ii) is isomorphic to neither of the others. In (i) the elements without an immediate predecessor are those with $y=1$, infinitely many, whereas in (iii) there is exactly one, the smallest element; an order isomorphism would be a bijection between these two sets, and no bijection exists between an infinite set and a one-element set. Hence
$$
\boxed{\text{the three orders have pairwise distinct order types.}}
$$

:::

:::

:::

:::
