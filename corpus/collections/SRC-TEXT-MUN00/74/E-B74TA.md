---
schema: qual/card@1
id: E-B74TA
kind: problem
title: Nonabelian fundamental groups of higher projective planes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §74 Exercise 7, printed p. 454. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved source is tmp/sources/gh-dyang5-MATH104-Topology-E-B74TA.md,
    read whole. David Yang, MATH104: Topology, Fall 2023, Homework 10, solves this exercise in
    HW/hw10.tex lines 35-70 of dyang5/MATH104-Topology at commit 12686a815d58f29aeaadb90a30449ae85c0a613f:
    the hint's homomorphism onto Z/2*Z/2, the relator going to 1, the induced map from the quotient of
    Theorem 74.4, and nonabelianness of the target. It is transcribed in the solution block with its commit
    and line range, and it replaces the card's own proof of the same argument. Two things were added to make
    the transcription stand on the book: the factorization step, which the source names "the Very Useful
    Lemma" and which is written out here as the universal property of the quotient, and the citation of
    Theorem 74.4 (printed p. 453) for the identification of G/N with the fundamental group. The source does
    not check the vertex hypothesis of Theorem 74.4, which the book leaves to the reader; the presentation is
    quoted as the theorem, so no such check is needed. Rejected in the search: mse 1103531, which has no
    answer.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 7, printed p. 454. The homomorphism of the printed hint sends the relator of Theorem 74.4 to a^2b^2 = 1 in C_2*C_2 and is onto it, and C_2*C_2 is nonabelian. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

If $m > 1$, show the fundamental group of the $m$-fold projective plane is not abelian.
[Hint: There is a homomorphism mapping this group onto the group $\ZZ/2 * \ZZ/2$.]
:::

::: {.solution}

The argument is that of **David Yang, *MATH104: Topology, Fall 2023*, Homework 10, solution to Section 74 Exercise 7**, in `HW/hw10.tex` lines 35--70 of the GitHub repository `dyang5/MATH104-Topology` at commit `12686a815d58f29aeaadb90a30449ae85c0a613f` (2024-05-04), https://github.com/dyang5/MATH104-Topology/blob/12686a815d58f29aeaadb90a30449ae85c0a613f/HW/hw10.tex#L35-L70; it carries out the exercise's printed hint, and each of its steps is checked below against Theorem 74.4.

Let $m>1$, let $G$ be the free group on $\alpha_{1},\ldots,\alpha_{m}$, and let $H=\ZZ/2*\ZZ/2=\langle\gamma,\delta\mid\gamma^{2}=\delta^{2}=1\rangle$. By Theorem 74.4, $\pi_{1}(P^{2}\#\cdots\#P^{2})\cong G/N$, where $N$ is the least normal subgroup of $G$ containing $\alpha_{1}^{2}\alpha_{2}^{2}\cdots\alpha_{m}^{2}$.

::: pf

::: {.pf-step #phi}
There is a homomorphism $\varphi:G\to H$ with $\varphi(\alpha_{1})=\gamma$ and $\varphi(\alpha_{i})=\delta$ for $i\ge2$.

::: pf-proof
$G$ is free on the $\alpha_{i}$ and $H$ is a group, so any assignment of an element of $H$ to each free generator extends uniquely to a homomorphism: that is the defining property of a free group on a system of free generators (§69).
:::

:::

::: {.pf-step #vanishes}
$\varphi$ vanishes on $N$, hence induces a homomorphism $\psi:G/N\to H$.

::: pf-proof
$\varphi(\alpha_{1}^{2}\alpha_{2}^{2}\cdots\alpha_{m}^{2})=\gamma^{2}\delta^{2}\cdots\delta^{2}=1$, since $\gamma^{2}=1$ and $\delta^{2}=1$ in $H$; so the normal generator of $N$ lies in $\ker\varphi$, and $\ker\varphi$, being a normal subgroup containing that element, contains $N$, the least normal subgroup containing it, by the definition of least normal subgroup. A homomorphism vanishing on a normal subgroup induces one on the quotient: the rule $\psi(gN)=\varphi(g)$ is well defined because $g_{1}N=g_{2}N$ gives $g_{1}g_{2}^{-1}\in N\subset\ker\varphi$, hence $\varphi(g_{1})=\varphi(g_{2})$, and it is a homomorphism because $\varphi$ is (§68).
:::

:::

::: {.pf-step #onto}
$\psi$ is onto, and $H$ is not abelian.

::: pf-proof
$\psi(\alpha_{1}N)=\gamma$ and $\psi(\alpha_{2}N)=\delta$, so the image contains the generating set $\{\gamma,\delta\}$ of $H$ and is all of $H$. For non-abelianness of $H=\ZZ/2*\ZZ/2$, the extension property of the free product gives a homomorphism $\theta:H\to S_{3}$ with $\theta(\gamma)=(12)$ and $\theta(\delta)=(13)$, since both these transpositions have order $2$; then $\theta(\gamma\delta)=(12)(13)=(132)$ while $\theta(\delta\gamma)=(13)(12)=(123)$, so $\gamma\delta\ne\delta\gamma$ and $H$ is not abelian.
:::

:::

::: {.pf-step #nonabelian}
$\pi_{1}(P^{2}\#\cdots\#P^{2})$ is not abelian.

::: pf-proof
Suppose that $G/N$ were abelian. Then any two of its elements commute, so for $g_{1},g_{2}\in G$ one has $g_{1}g_{2}N=g_{2}g_{1}N$ and hence, applying the homomorphism $\psi$,
$$
\psi(g_{1})\psi(g_{2})=\psi(g_{1}g_{2}N)=\psi(g_{2}g_{1}N)=\psi(g_{2})\psi(g_{1}).
$$
Every element of $H$ is $\psi(g)$ for some $g$, since $\psi$ is onto by step [](#onto){.pf-ref}, so every two elements of $H$ commute, contradicting the non-abelianness of $H$ there. So $G/N\cong\pi_{1}(P^{2}\#\cdots\#P^{2})$ is not abelian, as required for $m>1$.
:::

:::

:::
:::
