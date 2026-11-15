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

The proof below is that of David Yang, *MATH104: Topology, Fall 2023*, Homework 10, solution to Section 74 Exercise 7, in `HW/hw10.tex` lines 35--70 of the GitHub repository `dyang5/MATH104-Topology` at commit 12686a815d58f29aeaadb90a30449ae85c0a613f (2024-05-04), https://github.com/dyang5/MATH104-Topology/blob/12686a815d58f29aeaadb90a30449ae85c0a613f/HW/hw10.tex#L35-L70. It carries out the exercise's printed hint.

Let $m>1$, let $G$ be the free group on $\alpha_1,\dots,\alpha_m$, and let $H=\ZZ/2*\ZZ/2=\langle\gamma,\delta\mid\gamma^2=\delta^2=1\rangle$. Define a homomorphism $\varphi:G\to H$ on the free generators by $\varphi(\alpha_1)=\gamma$ and $\varphi(\alpha_i)=\delta$ for $i\ge2$. Then
$$
\varphi(\alpha_1^2\alpha_2^2\cdots\alpha_m^2)=\gamma^2\delta^2\cdots\delta^2=1,
$$
so $\varphi$ vanishes on the least normal subgroup $N$ of $G$ containing $\alpha_1^2\alpha_2^2\cdots\alpha_m^2$. It therefore induces $\psi:G/N\to H$ by $\psi(gN)=\varphi(g)$, which is well defined because $g_1g_2^{-1}\in N$ gives $\varphi(g_1)\varphi(g_2)^{-1}=\varphi(g_1g_2^{-1})=1$, and is a homomorphism because $\varphi$ is; this is the universal property of the quotient map $G\to G/N$, which Yang quotes as "the Very Useful Lemma".

By Theorem 74.4 (printed p. 453), $G/N\cong\pi_1(P^{2\#m})$; the map $\psi$ is onto, since $\gamma=\psi(\alpha_1N)$ and $\delta=\psi(\alpha_2N)$; and $H$ is not abelian, since the reduced words $(\gamma,\delta)$ and $(\delta,\gamma)$ are distinct in the free product. Were $\pi_1(P^{2\#m})$ abelian then every two of its elements would commute, so $\psi(g_1)$ and $\psi(g_2)$ would commute for all $g_1,g_2$, contrary to $\gamma\delta\ne\delta\gamma$; hence $\pi_1(P^{2\#m})$ is not abelian.
:::
