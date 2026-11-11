---
schema: qual/card@1
id: E-FS62I
kind: problem
title: A direct sum of two cyclic groups does not determine their orders
classification:
  areas:
  - topology
  topics:
  - Free Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §69 Exercise 4, printed p. 425. Proof transcribed from "Solutions to exercises for Mathematics
    205A", University of California, Riverside, Part 9 (Fall 2014), §69 Exercise 4, the set's printed p. 4,
    which uses 2, 3 and 5 to get Z/30 two ways; the card exhibits the example on Z/30 and proves the
    relatively-prime step of the hint rather than citing the Chinese remainder theorem, so the proof is closed
    against the book. Checked against Corollary 67.3 (printed p. 409) and the definition of direct sum
    (printed p. 407). The card's title previously said the factors are not determined by the direct sum, which
    is the reverse of what is shown; the group, not the sum, is what fails to determine the orders.
---

::: {.exercise}

Show that if $G = G_1 \oplus G_2$, where $G_1$ and $G_2$ are cyclic of orders $m$ and $n$, respectively, then $m$ and $n$ are not uniquely determined by $G$ in general.
[Hint: If $m$ and $n$ are relatively prime, show that $G$ is cyclic of order $mn$.]
:::

::: {.solution}

::: pf

::: pf-step

If $\gcd(m,n)=1$ then $\ZZ/m\ZZ\oplus\ZZ/n\ZZ\cong\ZZ/mn\ZZ$.

::: pf-proof

The element $(1,1)$ has order $k$ exactly when $k\equiv0 \pmod m$ and $k\equiv0\pmod n$, that is when $mn\mid k$ by coprimality. So $(1,1)$ has order $mn$, which equals the order of the group $\ZZ/m\ZZ\oplus\ZZ/n\ZZ$; hence the cyclic subgroup it generates is the whole group.

:::

:::

::: pf-step

$\ZZ/30\ZZ$ is the direct sum of cyclic groups in two ways with different orders.

::: pf-proof

$30=6\cdot5$ with $\gcd(6,5)=1$ and $30=2\cdot15$ with $\gcd(2,15)=1$, so step 1 gives

$$
\ZZ/30\ZZ\cong\ZZ/6\ZZ\oplus\ZZ/5\ZZ,\qquad \ZZ/30\ZZ\cong\ZZ/2\ZZ\oplus\ZZ/15\ZZ .
$$

The pair of orders $(6,5)$ differs from the pair $(2,15)$, while both direct sums are the same group $\ZZ/30\ZZ$.

:::

:::

::: pf-step

The orders are therefore not determined by $G$.

::: pf-proof

Take $G=\ZZ/30\ZZ$. If $G=G_1\oplus G_2$ with $G_1\cong\ZZ/6\ZZ$, $G_2\cong\ZZ/5\ZZ$ and also $G=H_1\oplus H_2$ with $H_1\cong\ZZ/2\ZZ$, $H_2\cong\ZZ/15\ZZ$, both decompositions hold by step 2, and no function of the isomorphism class of $G$ alone can return the pair $(6,5)$ in the first case and the pair $(2,15)$ in the second, since the isomorphism class is the same.

:::

:::

::: pf-qed

The pair of orders of the two cyclic summands is not determined by the group.

:::

:::
:::
