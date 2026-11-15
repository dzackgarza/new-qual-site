---
schema: qual/card@1
id: P-AGH513NONNORMALLOCUS
kind: problem
title: The nonnormal locus of a variety is a proper closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normal Varieties
  - Integral Closure
  - Local Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the requested direct proof and the finiteness-of-integral-closure hint with the retained Hartshorne I.5.13 transcription. The proof identifies the nonnormal locus on each affine chart with the support of the finite module Abar/A, using localization of normalization, and observes that this support omits the generic point.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.5.13,
    printed p. 38 (PDF p. 53 of the checked-in extraction). A. Shichijo,
    R.Hartshorne "Algebraic Geometry" 演習問題への解答 (2020/March), Chapter 1
    section 5, Exercise 5.13, printed pp. 11--12, read in the MinerU extraction
    tmp/sources/shitijyou-ch1-section5.md, is the only located treatment. It is
    not a complete published solution and is recorded as searched, not as one:
    it localizes to Y affine with ring A and K = Quot(A), takes the integral
    closure A-bar with generators g_i, and writes
    U = {P : {g_i} subset O_{P,Y}} = {P : A-bar subset O_{P,Y}}
      = intersection over i of Z_a(s_i)^c, where s_i is called the denominator
    of g_i; the three displays are said to be equivalent and U nonempty open
    ("明らか" / obvious). The third display is not well defined, a denominator of
    g_i in K being determined only up to a unit of A, and the openness of U is
    the closedness the exercise asks for, so that step is the assertion, the same
    gap the card's remark records in Egbert. What the source does prove is the
    identity Nor(Y) = U: U contained in Nor(Y) because localizing
    A subset A-bar subset O_{P,Y} at m_P gives O_{P,Y} = (A-bar)_{m_P}, which is
    integrally closed by Atiyah--Macdonald 5.12, and the reverse inclusion
    because an element of A-bar outside O_{P,Y} is integral but not in it. Those
    two inclusions are this card's step s2 localized, and they are not a proof of
    closedness. The card's closedness proof, through the annihilator of the finite
    module A-bar/A, is its own and is not in the source. Checked against the
    book: neither the source nor the card uses Theorem I.5.3, and both use only
    Theorem I.3.9A and the irreducibility of Y for nonemptiness.
---

::: {.problem}
It is a fact that any regular local ring is an integrally closed domain (Matsumura [2, Th. 36, p. 121]).
Thus we see from Theorem I.5.3 that any variety has a nonempty open subset of normal points ([[P-AGH317NORMAL]]).
In this exercise, show directly (without using Theorem I.5.3) that the set of nonnormal points of a variety is a proper closed subset (you will need the finiteness of integral closure: see Theorem I.3.9A).
:::

::: {.solution}
Let $X$ be a variety with function field $K=K(X)$.
Normality is a property of local rings, so we first work on an affine open $U \subseteq X$ with affine coordinate ring $A$.
Then $A$ is a finitely generated $k$-domain with fraction field $K$, and the points of $U$ correspond to the maximal ideals of $A$, with $\mco_P \cong A_{\mfm_P}$ [@Har77, Theorem I.3.2].
Let $\overline A$ denote the integral closure of $A$ in $K$.

::: pf

::: {.pf-step #s1}

The $A$-module
$$
M=\overline A/A
$$
is finite.

::: pf-proof

By the finiteness of integral closure [@Har77, Theorem I.3.9A], applied with the finite extension $K/K$, the ring $\overline A$ is a finite $A$-module.
Its quotient $M$ is therefore finite as well.

:::

:::

::: {.pf-step #s2}

For a prime $\mathfrak p$ of $A$, the local ring $A_{\mathfrak p}$ is integrally closed if and only if
$$
M_{\mathfrak p}=0.
$$

::: pf-proof

Integral closure commutes with localization:
$$
\overline{A_{\mathfrak p}}
=
(\overline A)_{\mathfrak p}
\subseteq K.
$$
Indeed, localization of an integral extension is integral.
Conversely, if $u\in K$ is integral over $A_{\mathfrak p}$, choose one denominator $s\notin\mathfrak p$ for all coefficients of a monic equation for $u$ of degree $n$.
Multiplying that equation by $s^n$ shows that $v=su$ satisfies a monic equation with coefficients in $A$.
Thus $v\in\overline A$ and
$$
u=v/s\in(\overline A)_{\mathfrak p}.
$$

Consequently $A_{\mathfrak p}$ is integrally closed exactly when $A_{\mathfrak p}=(\overline A)_{\mathfrak p}$.
The localized exact sequence
$$
0\longrightarrow A_{\mathfrak p}
\longrightarrow(\overline A)_{\mathfrak p}
\longrightarrow M_{\mathfrak p}
\longrightarrow0
$$
shows that this equality is equivalent to $M_{\mathfrak p}=0$.

:::

:::

::: {.pf-step #s3}

The set of nonnormal points of $U$ is the closed subset
$$
\boxed{Z(\Ann_A M) \subseteq U.}
$$

::: pf-proof

By step [](#s2){.pf-ref}, a point $P \in U$ is nonnormal exactly when $M_{\mfm_P}\neq 0$.
For a finite module, $M_{\mfm}=0$ exactly when $\Ann_A M \not\subseteq \mfm$.
Indeed, if generators $m_1,\ldots,m_s$ of $M$ all vanish after localization at $\mfm$, choose $a_i\notin\mfm$ with $a_im_i=0$; then $a_1\cdots a_s\in\Ann_A M\sm\mfm$.
The converse is immediate.
So $P$ is nonnormal exactly when $\Ann_A M\subseteq\mfm_P$, that is, when $P\in Z(\Ann_A M)$.

The same set is described in A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.13, printed pp. 11--12, as $U=\theset{P\in Y \st \overline A\subseteq\mco_{P,Y}}$, and his two inclusions there prove that $U$ is the normal locus. His openness of $U$, an intersection of the complements of the zero sets of "the denominators $s_i$" of generators of $\overline A$, is asserted and the denominators are not well defined, so it is not a proof of closedness; the annihilator argument above is what makes the set closed.

:::

:::

::: {.pf-step #s4}

This closed subset is proper.

::: pf-proof

The localization of $A$ at the zero prime is $K$, which is integrally closed, so $M_{(0)}=0$ by step [](#s2){.pf-ref}.
The argument of step [](#s3){.pf-ref} with $\mfm$ replaced by $(0)$ gives a nonzero $a\in\Ann_A M$.
Then $Z(\Ann_A M)\subseteq Z(a)$, which is a proper closed subset of $U$ because $a$ is a nonzero element of the coordinate ring.

:::

:::

::: {.pf-step #s5}

The nonnormal locus of $X$ is a proper closed subset of $X$.

::: pf-proof

Cover $X$ by affine opens $U_1,\ldots,U_N$ [@Har77, Proposition I.4.3].
Normality of a point is a property of its local ring, which does not change when it is computed in an open neighborhood.
So the nonnormal locus $N$ of $X$ satisfies $N\intersect U_i=Z(\Ann_{A_i} M_i)$ in the notation of step [](#s3){.pf-ref} for $U_i$.
Each intersection is closed in $U_i$, so $N$ is closed in $X$.
By step [](#s4){.pf-ref}, $N\intersect U_1$ is a proper subset of $U_1$, so $N\neq X$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} to [](#s4){.pf-ref} prove that the nonnormal locus of an affine variety is a proper closed subset, and step [](#s5){.pf-ref} extends this to any variety.

:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), gives no solution to 5.13.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 5.13.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.5.13, PDF p. 50: assume $X$ affine; the integral closure is finitely generated by $f_1,\ldots,f_n$; "$\mco_x$ is integrally closed iff the image of $f_i$ is in $\mco_x$ for all $i$"; "a finite intersection of nonempty opens is nonempty open, and rational functions are defined on such", so the normal locus is nonempty open.
Egbert's sketch asserts what the exercise asks for: that the condition "$f_i\in\mco_x$ for all $i$" cuts out an open set, and that the intersection over $i$ is nonempty, are both steps. The proof above supplies them: on an affine chart the nonnormal locus is the support $Z(\operatorname{Ann}_AM)$ of the finite module $M=\overline A/A$, which is closed because $M_{\mathfrak m}=0$ exactly when $\operatorname{Ann}_AM\not\subseteq\mathfrak m$, and proper because $M_{(0)}=0$ makes $\operatorname{Ann}_AM$ nonzero.

A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.13, printed pp. 11--12, proves that the normal locus is $U=\theset{P \st \overline A\subseteq\mco_{P,Y}}$, by the two inclusions step [](#s3){.pf-ref} names, and then treats the openness of $U$ as obvious, writing it as an intersection of complements of zero sets of "the denominators" of generators of $\overline A$. That is the step at issue: a denominator in $K$ is defined only up to a unit of $A$, and the openness of $U$ is the closedness of the nonnormal locus. The source is therefore cited here for the identification of the normal locus and not for its closedness, which is proved on this card.
:::
