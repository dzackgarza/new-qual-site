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
