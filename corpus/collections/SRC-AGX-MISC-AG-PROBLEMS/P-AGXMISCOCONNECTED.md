---
schema: qual/card@1
id: P-AGXMISCOCONNECTED
kind: problem
title: $\OO_Y \to \pi_* \OO_X$ is an isomorphism exactly when $Y$ is integrally closed in $K(X)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Integral Closure
  - Stein Factorisation
relations:
- kind: related-to
  target: T-MORSTEIN
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Proved the corrected statement under the hypotheses recorded in the
    existing remark, including normality of X. On each affine open V=Spec A,
    identified Gamma(pi^{-1}V,O_X) with the integral closure of A in K(X)
    using properness for finiteness and normality for the reverse inclusion.
---

::: {.problem}
Show that given $\pi: X \rightarrow Y$, $Y$ is integrally closed in $K(X)$ over $K(Y)$ if and only if $\OO_{Y} \rightarrow \pi_{*} \OO_{X}$ is an isomorphism (i.e., $\pi$ is $\OO$-connected).
:::

::: {.solution}
Assume that $X$ and $Y$ are
integral Noetherian schemes, $\pi:X\to Y$ is proper and dominant, and
$X$ is normal. Say that $Y$ is integrally closed in $K(X)$ if
$\OO_Y(V)$ is integrally closed in $K(X)$ for every affine open
$V\subseteq Y$. Dominance gives an inclusion
$$
K(Y)\subseteq K(X).
$$

::: pf

::: {.pf-step #finite-algebra-b}
Let
$$
V=\Spec A\subseteq Y
$$
be a nonempty affine open and put
$$
U=\pi^{-1}(V),
\qquad
B=\Gamma(U,\OO_X).
$$
Then $B$ is a finite $A$-algebra contained in $K(X)$.

::: pf-proof
The restricted morphism
$$
\pi_U:U\longrightarrow V
$$
is proper. By proper pushforward of coherent sheaves, or equivalently the
finite part of Stein factorisation [[T-MORSTEIN]],
$$
(\pi_U)_*\OO_U
$$
is a coherent $\OO_V$-algebra. Since $V$ is affine, this means
$$
B=\Gamma(U,\OO_U)
$$
is a finite $A$-module.

Because $\pi$ is dominant and $V$ is nonempty, $U$ is a nonempty open
subset of the integral scheme $X$. Every regular function on $U$
determines a rational function on $X$, giving an injection
$$
B\injects K(X).
$$
:::

:::

::: {.pf-step #b-integral-over-a}
Every element of $B$ is integral over $A$.

::: pf-proof
By step [](#finite-algebra-b){.pf-ref}, $B$ is finite as an $A$-module. Every element of a finite
$A$-algebra is integral over $A$. Therefore
$$
B
\subseteq
\overline A^{\,K(X)},
$$
where $\overline A^{\,K(X)}$ denotes the integral closure of $A$ in
$K(X)$.
:::

:::

::: {.pf-step #integral-elements-in-b}
Since $X$ is normal, every element of $K(X)$ integral over $A$
belongs to $B$.

::: pf-proof
Let
$$
\alpha\in K(X)
$$
be integral over $A$. Thus $\alpha$ satisfies a monic equation
$$
\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0=0,
\qquad
a_i\in A.
$$

Fix $x\in U$. The map
$$
A\longrightarrow\OO_{X,x}
$$
induced by $\pi$ carries the same equation into $\OO_{X,x}$. Hence
$\alpha$ is integral over $\OO_{X,x}$. Since $X$ is normal,
$\OO_{X,x}$ is integrally closed in $K(X)$, so
$$
\alpha\in\OO_{X,x}.
$$

This holds for every $x\in U$. Thus $\alpha$ is regular in a neighborhood
of every point of $U$. These local representatives are all the same
rational function and therefore agree on overlaps, so they glue to a
section of $\OO_X(U)$. Hence
$$
\alpha\in B.
$$
Therefore
$$
\overline A^{\,K(X)}
\subseteq B.
$$
:::

:::

::: {.pf-step #gamma-equals-integral-closure}
Consequently,
$$
\boxed{
\Gamma(\pi^{-1}V,\OO_X)
=
\overline{\Gamma(V,\OO_Y)}^{\,K(X)}
}
$$
for every nonempty affine open $V\subseteq Y$.

::: pf-proof
Step [](#b-integral-over-a){.pf-ref} gives
$$
B\subseteq\overline A^{\,K(X)},
$$
and step [](#integral-elements-in-b){.pf-ref} gives the reverse inclusion.
:::

:::

::: {.pf-step #forward-implication-connected}
If $Y$ is integrally closed in $K(X)$, then
$$
\OO_Y\xrightarrow{\sim}\pi_*\OO_X.
$$

::: pf-proof
By hypothesis, for every nonempty affine open
$$
V=\Spec A\subseteq Y,
$$
the ring $A$ is integrally closed in $K(X)$:
$$
A=\overline A^{\,K(X)}.
$$
Step [](#gamma-equals-integral-closure){.pf-ref} therefore gives
$$
\Gamma(V,\OO_Y)
=
A
=
\Gamma(\pi^{-1}V,\OO_X)
=
\Gamma(V,\pi_*\OO_X).
$$
These identifications are induced by the natural sheaf map and are
compatible with restriction. Hence that map is an isomorphism.
:::

:::

::: {.pf-step #converse-implication-connected}
Conversely, if
$$
\OO_Y\xrightarrow{\sim}\pi_*\OO_X,
$$
then $Y$ is integrally closed in $K(X)$.

::: pf-proof
Let
$$
V=\Spec A\subseteq Y
$$
be nonempty affine. The sheaf isomorphism gives
$$
A
=
\Gamma(V,\OO_Y)
\cong
\Gamma(\pi^{-1}V,\OO_X)
=B.
$$
By step [](#gamma-equals-integral-closure){.pf-ref},
$$
B=\overline A^{\,K(X)}.
$$
Therefore
$$
A=\overline A^{\,K(X)}.
$$
Since this holds on every affine open, $Y$ is integrally closed in
$K(X)$.
:::

:::

::: {.pf-step #equivalence-statement}
Under these hypotheses,
$$
\boxed{
Y\text{ is integrally closed in }K(X)
\iff
\OO_Y\xrightarrow{\sim}\pi_*\OO_X.
}
$$

::: pf-proof
Step [](#forward-implication-connected){.pf-ref} proves the forward implication and step [](#converse-implication-connected){.pf-ref} proves the reverse
implication.
:::

:::

::: pf-qed
Step [](#equivalence-statement){.pf-ref} is the asserted equivalence.
:::

:::

:::

::: {.remark}
The problem states no hypotheses on $X$, $Y$, or $\pi$. The solution assumes $X$ and $Y$ integral Noetherian, $\pi$ proper and dominant, so that $K(Y) \subseteq K(X)$, and $X$ normal.
The implication from $\OO_Y \cong \pi_* \OO_X$ to integral closedness fails without normality of $X$.
Let $Y$ be the cuspidal cubic $V(y^2 - x^3)$ and $\pi = \id_Y$.
Then $\OO_Y \to \pi_* \OO_X$ is an isomorphism, but $t = y/x \in K(Y)$ satisfies $t^2 = x$, so it is integral over $\OO_Y$ and does not lie in $\OO_Y$.
:::
