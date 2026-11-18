---
schema: qual/card@1
id: E-4T2MK
kind: problem
title: Connected fibers over a connected base connect the total space
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 11, printed p. 152, with Lemma 23.2
    and Theorem 23.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.11, PDF p. 3. A connected fibre meeting one
    side of a would-be separation of X lies in it, so the sides are saturated, and being
    open and saturated they have open images that would separate Y. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that a fibre meeting an open set lies in it
    (Lemma 23.2), that such an open set is saturated, and that the images of a separation
    are a separation of the quotient, against Munkres §23 Exercise 11, printed p. 152.
    positron0802, Chapter 3 Exercise 23.11, PDF p. 3. The printed statement needed no
    repair.
---

::: {.exercise}

Let $p: X \to Y$ be a quotient map.
Show that if each set $p^{-1}(\theset{y})$ is connected, and if $Y$ is connected, then $X$ is connected.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.11, PDF p. 3** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the saturation argument is theirs.

::: pf

::: {.pf-step #saturated}
Let $U$ be open in $X$ and suppose that $U$ meets a fibre $p^{-1}(\{y\})$; then $p^{-1}(\{y\})\subset U$.

::: pf-proof
The fibre $p^{-1}(\{y\})$ is connected by hypothesis, and it meets $U$ in some point. If it also met $X-U$, then $U\cap p^{-1}(\{y\})$ and $(X-U)\cap p^{-1}(\{y\})$ would be two disjoint nonempty open sets of the subspace $p^{-1}(\{y\})$ whose union is that fibre, a separation of a connected space. So the fibre lies in $U$. This is Lemma 23.2 applied to the subspace $p^{-1}(\{y\})$.
:::

:::

::: {.pf-step #preimage}
If $U\subset X$ and $p^{-1}(\{y\})\subset U$ for every $y\in p(U)$, then $U=p^{-1}\big(p(U)\big)$, that is, $U$ is saturated.

::: pf-proof
For any $U$ one has $U\subset p^{-1}\big(p(U)\big)$: if $x\in U$ then $p(x)\in p(U)$, so $x$ lies in the preimage. Conversely, if $x\in p^{-1}\big(p(U)\big)$ then $p(x)=p(x')$ for some $x'\in U$; the fibre of $p(x)$ contains $x'$, hence is the fibre of a point of $p(U)$, hence lies in $U$ by step [](#saturated){.pf-ref}; so $x\in U$.
:::

:::

::: {.pf-step #separation}
If $X=U\cup V$ is a separation, then $p(U)$ and $p(V)$ form a separation of $Y$.

::: pf-proof
$U$ and $V$ are disjoint nonempty open sets. By steps [](#saturated){.pf-ref} and [](#preimage){.pf-ref} both are saturated, so $p(U)$ and $p(V)$ are open in $Y$ because $p$ is a quotient map. They are nonempty because $p$ is surjective and $U$, $V$ are nonempty; they are disjoint because a common point $y$ would have a point of $U$ and a point of $V$ in the fibre $p^{-1}(\{y\})$, contradicting $U\cap V=\varnothing$; and $p(U)\cup p(V)=p(U\cup V)=Y$.
:::

:::

::: {.pf-step}
$X$ is connected.

::: pf-proof
If $X$ had a separation, step [](#separation){.pf-ref} would produce one of $Y$, contradicting the connectedness of $Y$. So $X$ has no separation and is connected.
:::

:::

:::
:::
