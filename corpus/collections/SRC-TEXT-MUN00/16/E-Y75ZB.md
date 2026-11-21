---
schema: qual/card@1
id: E-Y75ZB
kind: problem
title: A countable rational rectangle basis for the plane
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Bases
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 6, printed p. 92, with Theorem 15.1
    on printed p. 87 and Exercise 13.8(a); the collection is stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.6, printed p. 153.
    The reduction is his: the rational open intervals are a basis for R (Exercise 13.8(a)),
    so by Theorem 15.1 the products of two of them are a basis for the product topology on R
    x R, and that collection is exactly the one in the exercise. (tmp/sources/munkres-
    solutions-whitman.pdf).
---

::: {.exercise}

Show that the countable collection

$$
\theset{(a, b) \times (c, d) \mid a < b \text{ and } c < d, \text{ and } a, b, c, d \text{ rational}}
$$

is a basis for $\RR^2$.
:::

::: {.solution}

The reduction is **Dan Whitman**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.6, manual p. 153, PDF p. 156 (`tmp/sources/munkres-solutions-whitman.pdf`); the countability claims are checked here from the book's theorems. The statement was checked against Munkres, *Topology* (2000), §16 Exercise 6, printed p. 92, with §13 Exercise 8(a) on printed p. 83 and Theorem 15.1 on printed p. 86; the card's earlier page for Theorem 15.1, p. 87, is corrected, the theorem being stated on p. 86 and proved on p. 87.

Throughout,
$$
\mathcal{B}\coloneqq\theset{(a,b)\mid a<b\text{ and }a,b\in\QQ},\qquad
\mathcal{D}\coloneqq\theset{(a,b)\times(c,d)\mid a<b,\ c<d\text{ and }a,b,c,d\in\QQ}.
$$

::: pf

::: {.pf-step #rational-basis}
$\mathcal{B}$ is a countable basis for the standard topology of $\RR$.

::: pf-proof
§13 Exercise 8(a) (printed p. 83) shows, by the criterion of Lemma 13.2, that $\mathcal{B}$ is a basis for the topology of $\RR$. It is countable: $\QQ$ is countable by Theorem 7.5 (printed p. 48), a countable union of countable sets, applied to $\QQ=\QQ_{+}\cup\theset{0}\cup(-\QQ_{+})$ with $\QQ_{+}$ countable by Example 3 on the same page; $\QQ\times\QQ$ is countable by Theorem 7.6 (printed p. 49); $\mathcal{B}$ is in bijection with the subset $\theset{(a,b)\in\QQ\times\QQ\mid a<b}$ of $\QQ\times\QQ$, which is countable by Corollary 7.3 (printed p. 48).
:::

:::

::: {.pf-step #product-basis}
$\mathcal{D}$ is a basis for the product topology on $\RR\times\RR$.

::: pf-proof
By Theorem 15.1 (printed p. 86), if $\mathcal{B}$ is a basis for the topology of $X$ and $\mathcal{C}$ a basis for that of $Y$, then $\theset{B\times C\mid B\in\mathcal{B},\ C\in\mathcal{C}}$ is a basis for the topology of $X\times Y$. Taking $X=Y=\RR$ and $\mathcal{C}=\mathcal{B}$ gives $\mathcal{D}$ as soon as one writes each $B,C\in\mathcal{B}$ as $B=(a,b)$, $C=(c,d)$ with rational endpoints.
:::

:::

::: {.pf-step #countable}
$\mathcal{D}$ is countable.

::: pf-proof
$\mathcal{D}$ is the image of the countable set $\mathcal{B}\times\mathcal{B}$ under the map $(B,C)\mapsto B\times C$; $\mathcal{B}\times\mathcal{B}$ is countable by Theorem 7.6 (printed p. 49) and step [](#rational-basis){.pf-ref}, and a surjective image of a countable set is countable by Theorem 7.1 (printed p. 45).
:::

:::

::: pf-step
Therefore the displayed countable collection is a basis for $\RR^{2}$.

::: pf-proof
$\RR^{2}$ is $\RR\times\RR$ with the product topology, and $\mathcal{D}$ is the collection displayed in the statement; it is a basis by step [](#product-basis){.pf-ref} and countable by step [](#countable){.pf-ref}.
:::

:::

:::

:::
