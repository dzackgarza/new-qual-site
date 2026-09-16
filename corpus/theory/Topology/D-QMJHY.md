---
schema: qual/card@1
id: D-QMJHY
kind: definition
title: Weak homotopy equivalence
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
A continuous map $f\colon X\to Y$ of topological spaces is a \dfn{weak homotopy equivalence} if $f_*\colon\pi_0(X)\to\pi_0(Y)$ is a bijection and, for every $x_0\in X$ and every $n\geq1$, the induced map on [[D-EUX36|homotopy groups]]
$$
f_*\colon\pi_n(X,x_0)\to\pi_n(Y,f(x_0))
$$
is an isomorphism [@Hat02, p. 352].
:::

::: {.theorem}
Let $f\colon X\to Y$ be a weak homotopy equivalence.

(a) For every $n$ and every abelian group $G$, $f_*\colon H_n(X;G)\to H_n(Y;G)$ and $f^*\colon H^n(Y;G)\to H^n(X;G)$ are isomorphisms [@Hat02, Prop. 4.21].

(b) (Whitehead) If $X$ and $Y$ are [[D-ZOU5G|CW complexes]], then $f$ is a [[D-HFR32|homotopy equivalence]] [@Hat02, Theorem 4.5].
:::
