---
schema: qual/card@1
id: E-HAT-1.2-1
kind: problem
title: Free product of nontrivial groups has trivial center and only conjugates of finite-order elements have finite order
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Free Groups
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The center argument claimed conjugation changes the first letter, and the torsion argument used cyclic reduction without proving it; both rewritten from the reduced-word normal form.
---

::: {.problem}
Show that the free product $G * H$ of nontrivial groups $G$ and $H$ has trivial center, and that the only elements of $G * H$ of finite order are the conjugates of finite-order elements of $G$ and $H$.
:::

::: {.solution}
Every element of $G*H$ has a unique reduced word $a_1a_2\cdots a_n$, where each $a_i$ is a nontrivial element of $G$ or of $H$ and consecutive letters lie in different factors; $n$ is its length.

::: pf

::: {.pf-step #s1}

$Z(G*H)=1$.

::: pf-proof

Let $w=a_1\cdots a_n\ne1$ be reduced, and by symmetry let $a_1\in G$.
Choose $h\in H\setminus\{1\}$.
The word $ha_1\cdots a_n$ is reduced, so $hw$ has first letter $h\in H$.
If $a_n\in G$, then $a_1\cdots a_nh$ is reduced; if $a_n\in H$, then $n\ge2$ and $wh$ reduces to $a_1\cdots a_{n-1}(a_nh)$ or $a_1\cdots a_{n-1}$.
In every case $wh$ is reduced with first letter $a_1\in G$.
By uniqueness of reduced words, $hw\ne wh$, so $w$ is not central.

:::

:::

::: {.pf-step #s2}

Every $w\in G*H$ is conjugate to an element $v$ that lies in $G$ or in $H$, or that is a reduced word of even length $m\ge2$, whose first and last letters lie in different factors.

::: pf-proof

Induct on the length $n$ of $w$.
If $n\le1$, take $v=w$.
If $n\ge2$ and $a_1,a_n$ lie in different factors, then $n$ is even; take $v=w$.
Otherwise $a_1,a_n$ lie in one factor and $n\ge3$, and $a_1^{-1}wa_1=a_2\cdots a_{n-1}(a_na_1)$ has length at most $n-1$; apply induction.

:::

:::

::: {.pf-step #s3}

An element $v$ of the last kind in step [](#s2){.pf-ref} has infinite order.

::: pf-proof

The last letter of $v$ and the first letter of $v$ lie in different factors, so the concatenation of $k$ copies of the reduced word of $v$ is reduced.
Hence $v^k$ has length $km>0$, and $v^k\ne1$ for every $k\ge1$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives the trivial center.
If $w$ has finite order, its conjugate $v$ of step [](#s2){.pf-ref} has finite order, so by step [](#s3){.pf-ref} $v$ lies in $G$ or in $H$, and $w$ is a conjugate of a finite-order element of $G$ or of $H$.
Conversely every conjugate of a finite-order element has finite order.

:::

:::

:::
