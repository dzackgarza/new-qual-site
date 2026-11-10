---
schema: qual/card@1
id: P-AGH311PRIMESOFLOCAL
kind: problem
title: Primes of $\mco_P$ correspond to closed subvarieties through $P$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Rings
  - Prime Ideals
  - Subvarieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with Hartshorne I.3.11. The proof passes to an affine open neighborhood of P, applies the prime correspondence for localization at the maximal ideal of P, and then takes closure back in X.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked both directions of the affine-neighborhood and localization correspondences against independent published solutions; the closure/intersection step makes the correspondence global on X.'
---

::: {.problem}
Let $X$ be any variety and let $P \in X$.
Show that there is a one-to-one correspondence between the prime ideals of the local ring $\mco_P$ and the closed subvarieties of $X$ containing $P$.
:::

::: {.solution}
Choose an affine open neighborhood $U\subseteq X$ of $P$, and write
$$
A=A(U),
\qquad
\mathfrak m=I_U(P).
$$
Then
$$
\mco_P\cong A_{\mathfrak m}.
$$

::: pf

::: {.pf-step #s1}

Closed subvarieties of $X$ containing $P$ correspond bijectively to closed subvarieties of $U$ containing $P$.

::: pf-proof

If $Z\subseteq X$ is a closed subvariety containing $P$, then $Z\cap U$ is a nonempty open subset of the irreducible space $Z$, hence is irreducible; it is also closed in $U$ and contains $P$.

Conversely, let $W\subseteq U$ be a closed subvariety containing $P$.
Its closure $\overline{W}^{X}$ in $X$ is irreducible and closed, hence is a closed subvariety of $X$ containing $P$.
Because $U$ is open in $X$,
$$
\overline{W}^{X}\cap U=\overline{W}^{U}=W,
$$
the last equality using that $W$ is closed in $U$.
Likewise, for a closed subvariety $Z\subseteq X$, the nonempty open subset $Z\cap U$ is dense in $Z$, so
$$
\overline{Z\cap U}^{X}=Z.
$$
Thus intersection with $U$ and closure in $X$ are inverse operations.

:::

:::

::: {.pf-step #s2}

Closed subvarieties of $U$ containing $P$ correspond bijectively to prime ideals $\mathfrak p\subseteq A$ contained in $\mathfrak m$.

::: pf-proof

Since $U$ is affine, irreducible closed subsets of $U$ are exactly the sets
$$
Z_U(\mathfrak p)
$$
for prime ideals $\mathfrak p\subseteq A$, with inverse given by the vanishing ideal.
The point $P$ belongs to $Z_U(\mathfrak p)$ exactly when every element of $\mathfrak p$ vanishes at $P$, equivalently
$$
\mathfrak p\subseteq\mathfrak m.
$$
This gives the claimed restricted correspondence.

:::

:::

::: {.pf-step #s3}

Prime ideals of $A$ contained in $\mathfrak m$ correspond bijectively to prime ideals of $A_{\mathfrak m}$.

::: pf-proof

This is the prime correspondence for localization.
Explicitly,
$$
\mathfrak p\longmapsto \mathfrak p A_{\mathfrak m}
$$
sends every prime $\mathfrak p\subseteq\mathfrak m$ to a prime of $A_{\mathfrak m}$, while contraction
$$
\mathfrak q\longmapsto \mathfrak q\cap A
$$
sends a prime $\mathfrak q\subseteq A_{\mathfrak m}$ to a prime ideal of $A$ disjoint from $A\setminus\mathfrak m$, hence contained in $\mathfrak m$.
Extension and contraction are inverse under these conditions.

:::

:::

::: pf-qed

Using $\mco_P\cong A_{\mathfrak m}$, compose the bijections of steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.
Thus a prime $\mathfrak q\subseteq\mco_P$ corresponds to the closure in $X$ of
$$
Z_U(\mathfrak q\cap A),
$$
and every closed subvariety of $X$ through $P$ arises uniquely in this way.

:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 3.11, PDF p. 4: reduce to $X$ affine, where the irreducible varieties containing $P$ correspond to the prime ideals of $A(X)$ contained in the maximal ideal $M$ of $P$, that is, to the prime ideals of the localization $\mco_P$.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 3.11, PDF pp. 12--13: the map $X'\mapsto\mathfrak p_{X'}$, with a lemma that intersecting with an open subset $U$ and taking the closure in $X$ are inverse bijections between the irreducible closed subsets of $U$ and those of $X$ not contained in $X\setminus U$, which is then applied chart by chart.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.11, PDF p. 33: "this follows from properties of localization of the coordinate ring".
The proof above isolates the passage from $X$ to an affine neighborhood and from that neighborhood to the localization, which is the bijection Troiani states as a lemma and Egbert leaves to the reader.
Agree.
:::
