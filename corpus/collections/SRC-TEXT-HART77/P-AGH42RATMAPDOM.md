---
schema: qual/card@1
id: P-AGH42RATMAPDOM
kind: problem
title: Largest open set on which a rational map is a morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Maps
  - Morphisms
  - Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with Hartshorne I.4.2 and the immediately preceding definition of rational map. Equivalent representatives agree on their common domain, so their morphisms glue on arbitrary unions.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked continuity, pullback of regular functions, and maximality against Hartshorne I.4 and independent chapter notes.'
---

::: {.problem}
Let $\varphi$ be a rational map from a variety $X$ to a variety $Y$.
Show that there is a largest open set on which $\varphi$ is represented by a morphism.
One says that the rational map is defined at the points of that open set.
:::

::: {.solution}
Let $\varphi:X\dashrightarrow Y$ be the given rational map.

::: pf

::: {.pf-step #s1}

Any two representatives of $\varphi$ glue on the union of their domains.

::: pf-proof

Let
$$
\varphi_U:U\to Y,
\qquad
\varphi_V:V\to Y
$$
be two representatives.
By the definition of a rational map,
$$
\varphi_U\restrict_{U\cap V}=\varphi_V\restrict_{U\cap V}.
$$
Hence the piecewise rule
$$
\psi(x)=
\begin{cases}
\varphi_U(x),&x\in U,\\
\varphi_V(x),&x\in V
\end{cases}
$$
is well-defined on $U\cup V$.

It is continuous: for every open $W\subseteq Y$,
$$
\psi^{-1}(W)
=\varphi_U^{-1}(W)\cup\varphi_V^{-1}(W),
$$
which is open in $U\cup V$.

Let $h$ be regular on an open subset $W\subseteq Y$.
On
$$
\psi^{-1}(W)\cap U
$$
the pullback $h\circ\psi$ equals the regular function $h\circ\varphi_U$, and similarly on the open subset $\psi^{-1}(W)\cap V$.
These opens cover $\psi^{-1}(W)$, so regularity being local shows that $h\circ\psi$ is regular.
Thus $\psi$ is a morphism.

:::

:::

::: {.pf-step #s2}

Let
$$
D(\varphi)
=\bigcup\{U\subseteq X:U\text{ is open and }\varphi\text{ is represented by a morphism }U\to Y\}.
$$
Then the representatives glue to a morphism
$$
\varphi_D:D(\varphi)\to Y.
$$

::: pf-proof

The set $D(\varphi)$ is open as a union of opens.
On pairwise overlaps all representatives agree by the equivalence relation defining the rational map.
Therefore they define a single set map $\varphi_D$ on the union.

Every point of $D(\varphi)$ lies in one representative domain $U$, and on that open neighborhood $\varphi_D$ equals the morphism $\varphi_U$.
The morphism condition is local on the source, so $\varphi_D$ is a morphism.

:::

:::

::: {.pf-step #s3}

The open set $D(\varphi)$ is the unique largest open subset on which $\varphi$ is represented by a morphism.

::: pf-proof

Step [](#s2){.pf-ref} shows that $\varphi$ is represented on $D(\varphi)$.
If $W\subseteq X$ is any other open subset on which $\varphi$ is represented by a morphism, then $W$ is one of the opens in the union defining $D(\varphi)$.
Hence
$$
W\subseteq D(\varphi).
$$
Thus $D(\varphi)$ is the largest such open set.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} construct the maximal domain of definition and its representing morphism.

:::

:::

:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 4.2, PDF p. 6: "A map is regular if and only if it is regular in a neighborhood of each point, so the conclusion follows as in 4.1."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 4.2, PDF p. 15: he first proves the gluing statement for morphisms $U_1,U_2\to Y$ agreeing on $U_1\cap U_2$, by pulling back regular functions and gluing them with the previous exercise, then applies it to representatives of two rational maps.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.4.2, PDF p. 39: "see 4.1".
The proof above states the gluing of two morphisms with continuity and the pullback of regular functions as separate verifications and then takes the union over every representing morphism, which is Troiani's route with the maximality step written out; Borcherds and Egbert leave it to 4.1.
Agree.
:::
