---
schema: qual/card@1
id: P-WESTOP12-1
kind: problem
title: Examples and impossibilities relating homotopy, retracts, and low-dimensional homology
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For path-connected spaces $X$ and $Y$, give an explicit example satisfying each possible statement below, or state that no such example exists:

1. $X\simeq Y$ but $X\not\cong Y$.
2. $X\simeq Y$, but neither is a deformation retract of the other.
3. $X$ is a deformation retract of $Y$, but $X\not\simeq Y$.
4. $X$ is a retract of $Y$, but not a deformation retract of $Y$.
5. $X$ is a deformation retract of $Y$, but not a retract of $Y$.
6. $X\simeq Y$ but $\pi_1(X)\not\cong\pi_1(Y)$.
7. $\pi_1(X)\cong\pi_1(Y)$ but $X\not\simeq Y$.
8. $X$ is a deformation retract of $Y$ but $\pi_1(X)\not\cong\pi_1(Y)$.
9. $X$ is contractible but $\pi_1(X)$ is nontrivial.
10. $\pi_1(X)$ is trivial but $X$ is not contractible.
11. $H_1(X)\cong H_1(Y)$ but $\pi_1(X)\not\cong\pi_1(Y)$.
12. $\pi_1(X)\cong\pi_1(Y)$ but $H_1(X)\not\cong H_1(Y)$.
13. $H_2(X)\cong H_2(Y)$ but $\pi_1(X)\not\cong\pi_1(Y)$.
14. $\pi_1(X)\cong\pi_1(Y)$ but $H_2(X)\not\cong H_2(Y)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (1) is possible.
Take
\[
X=\{*\},
\qquad
Y=[0,1].
\]


::: pf-proof

Both spaces are contractible, so
\[
X\simeq Y.
\]
They are not homeomorphic because one has one point and the other has
infinitely many.

:::

:::

::: {.pf-step #s1-2}

Statement (2) is possible as literally stated.
Take two disjoint copies of the circle:
\[
X=S^1\times\{0\},
\qquad
Y=S^1\times\{1\}.
\]


::: pf-proof

They are homeomorphic, hence homotopy equivalent.
Neither is a subset of the other, so neither can be a deformation retract
of the other.

:::

:::

::: {.pf-step #s1-3}

Statement (3) is impossible.


::: pf-proof

If $X$ is a deformation retract of $Y$, the inclusion
\[
i:X\hookrightarrow Y
\]
and the retraction
\[
r:Y\to X
\]
satisfy
\[
r\circ i=\operatorname{id}_X
\]
and
\[
i\circ r\simeq\operatorname{id}_Y.
\]
Thus $i$ and $r$ are homotopy inverses, so
\[
X\simeq Y.
\]

:::

:::

::: {.pf-step #s1-4}

Statement (4) is possible.
Take
\[
X=S^1
\]
as the circle summand of
\[
Y=S^1\vee S^2.
\]


::: pf-proof

Collapse the $S^2$ summand to the wedge point.
This gives a retraction
\[
r:Y\to X.
\]

If $X$ were a deformation retract of $Y$, then step [](#s1-3){.pf-ref} would imply
\[
X\simeq Y.
\]
But
\[
H_2(X)=0
\]
while
\[
H_2(Y)\cong\ZZ.
\]
Hence the retraction is not a deformation retraction.

:::

:::

::: {.pf-step #s1-5}

Statement (5) is impossible.


::: pf-proof

A deformation retraction is, by definition, a retraction together with a
homotopy fixing the retract.
Thus every deformation retract is a retract.

:::

:::

::: {.pf-step #s1-6}

Statement (6) is impossible.


::: pf-proof

Homotopy equivalent path-connected spaces have isomorphic fundamental
groups.
Homotopy inverse maps induce mutually inverse homomorphisms on
\[
\pi_1.
\]

:::

:::

::: {.pf-step #s1-7}

Statement (7) is possible.
Take
\[
X=\{*\},
\qquad
Y=S^2.
\]


::: pf-proof

Both fundamental groups are trivial:
\[
\pi_1(X)=0=\pi_1(Y).
\]
But
\[
H_2(X)=0,
\qquad
H_2(Y)\cong\ZZ.
\]
Therefore $X$ and $Y$ cannot be homotopy equivalent.

:::

:::

::: {.pf-step #s1-8}

Statement (8) is impossible.


::: pf-proof

By step [](#s1-3){.pf-ref}, a deformation retract is a homotopy equivalence.
By step [](#s1-6){.pf-ref}, homotopy-equivalent spaces have isomorphic fundamental
groups.

:::

:::

::: {.pf-step #s1-9}

Statement (9) is impossible.


::: pf-proof

If $X$ is contractible, then
\[
X\simeq\{*\}.
\]
Homotopy invariance of the fundamental group gives
\[
\pi_1(X)\cong0.
\]

:::

:::

::: {.pf-step #s1-10}

Statement (10) is possible.
Take
\[
X=S^2.
\]


::: pf-proof

The sphere is simply connected:
\[
\pi_1(S^2)=0.
\]
It is not contractible because
\[
H_2(S^2)\cong\ZZ\ne0.
\]

:::

:::

::: {.pf-step #s1-11}

Statement (11) is possible.
Take
\[
X=S^1\vee S^1,
\qquad
Y=T^2.
\]


::: pf-proof

For the wedge,
\[
\pi_1(X)\cong F_2,
\]
while
\[
\pi_1(Y)\cong\ZZ^2.
\]
These groups are not isomorphic because the first is nonabelian and the
second is abelian.

However,
\[
H_1(X)
\cong
F_2^{\mathrm{ab}}
\cong
\ZZ^2
\cong
H_1(Y).
\]

:::

:::

::: {.pf-step #s1-12}

Statement (12) is impossible.


::: pf-proof

For every path-connected space $Z$,
\[
H_1(Z;\ZZ)
\cong
\pi_1(Z)^{\mathrm{ab}}.
\]
Hence an isomorphism
\[
\pi_1(X)\cong\pi_1(Y)
\]
induces an isomorphism of abelianizations and therefore
\[
H_1(X)\cong H_1(Y).
\]

:::

:::

::: {.pf-step #s1-13}

Statement (13) is possible.
Take
\[
X=S^1,
\qquad
Y=\{*\}.
\]


::: pf-proof

Both second homology groups vanish:
\[
H_2(S^1)=0=H_2(\{*\}).
\]
But
\[
\pi_1(S^1)\cong\ZZ
\]
and
\[
\pi_1(\{*\})=0.
\]

:::

:::

::: {.pf-step #s1-14}

Statement (14) is possible.
Take
\[
X=\{*\},
\qquad
Y=S^2.
\]


::: pf-proof

Both fundamental groups are trivial, while
\[
H_2(X)=0
\]
and
\[
H_2(Y)\cong\ZZ.
\]

:::

:::

::: pf-step

The complete classification is
\[
\boxed{
\begin{array}{c|cccccccccccccc}
\text{statement}
&1&2&3&4&5&6&7&8&9&10&11&12&13&14\\
\hline
\text{possible?}
&Y&Y&N&Y&N&N&Y&N&N&Y&Y&N&Y&Y
\end{array}
}
\]


::: pf-proof

This table collects steps [](#s1-1){.pf-ref} through [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Each possible statement has an explicit example and each impossible
statement has a proof of impossibility above.

:::

:::

:::
