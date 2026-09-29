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
---

::: {.problem}
Show that the free product $G * H$ of nontrivial groups $G$ and $H$ has trivial center, and that the only elements of $G * H$ of finite order are the conjugates of finite-order elements of $G$ and $H$.
:::

::: {.solution}

::: pf

::: pf-step

Every element of $G * H$ has a unique reduced word form $g_1 h_1 g_2 h_2 \cdots$ with $g_i \in G \setminus \{1\}$, $h_i \in H \setminus \{1\}$ (alternating, no adjacent factors from the same group).

::: pf-proof

normal form theorem for free products.

:::

:::

::: {.pf-step #s2}

Let $w \in Z(G * H)$ be a nontrivial central element, written in reduced form.

::: pf-proof

suppose the center is nontrivial.

:::

:::

::: {.pf-step #s3}

If $w$ has length $\ge 2$, then conjugating by a nontrivial element of the group of the first factor changes the word, contradicting centrality.

::: pf-proof

e.g. if $w$ starts with $g_1 \in G$, then for $h \in H \setminus \{1\}$, $h w h^{-1}$ has a different reduced form than $w$ (the first factor changes), so $h w h^{-1} \ne w$.

:::

:::

::: {.pf-step #s4}

If $w$ has length $1$, say $w = g_1 \in G$, then for $h \in H \setminus \{1\}$, $h g_1 h^{-1} \ne g_1$.

::: pf-proof

$h g_1 h^{-1}$ is a reduced word of length $3$, not equal to the length-$1$ word $g_1$.

:::

:::

::: {.pf-step #s5}

Hence no nontrivial element is central, so $Z(G * H) = 1$.

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Let $w \in G * H$ have finite order, with reduced form $w = a_1 a_2 \cdots a_n$.

::: pf-proof

take a finite-order element.

:::

:::

::: {.pf-step #s7}

If $n \ge 2$, then $w$ is cyclically reduced (after conjugation) and $w^k$ has reduced length $kn$ for all $k \ge 1$, so $w^k \ne 1$.

::: pf-proof

the reduced form of $w^k$ is the concatenation of $k$ copies of the cyclically reduced form, of length $kn > 0$.

:::

:::

::: {.pf-step #s8}

Hence $n = 1$, so $w$ is conjugate to an element of $G$ or of $H$.

::: pf-proof

Step [](#s7){.pf-ref} (a finite-order element must have length $1$, i.e. lie in a single factor, up to conjugation).

:::

:::

::: {.pf-step #s9}

Therefore the finite-order elements of $G * H$ are exactly the conjugates of finite-order elements of $G$ and $H$.

::: pf-proof

Steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s5){.pf-ref} and [](#s9){.pf-ref}.

:::

:::

:::
