---
schema: qual/card@1
id: P-WESTOP08-II1
kind: problem
title: Examples and impossibilities relating homotopy, retracts, and low homology groups
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For connected spaces $X,Y$, give an example satisfying each statement below or state that no example exists:

1. $X\simeq Y$ but $X\not\cong Y$.
2. $X\simeq Y$, but neither is a deformation retract of the other.
3. $X$ is a deformation retract of $Y$, but $X\not\simeq Y$.
4. $X\simeq Y$ but $\pi_1(X)\not\cong\pi_1(Y)$.
5. $\pi_1(X)\cong\pi_1(Y)$ but $X\not\simeq Y$.
6. $X$ is a retract of $Y$, but not a deformation retract of $Y$.
7. $X$ is a deformation retract of $Y$, but not a retract of $Y$.
8. $X$ is a deformation retract of $Y$, but $\pi_1(X)\not\cong\pi_1(Y)$.
9. $H_1(X)\cong H_1(Y)$ but $\pi_1(X)\not\cong\pi_1(Y)$.
10. $\pi_1(X)\cong\pi_1(Y)$ but $H_1(X)\not\cong H_1(Y)$.
11. $H_2(X)\cong H_2(Y)$ but $\pi_1(X)\not\cong\pi_1(Y)$.
12. $\pi_1(X)\cong\pi_1(Y)$ but $H_2(X)\not\cong H_2(Y)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (1) is possible:
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
They are not homeomorphic because $X$ has one point and $Y$ has more than
one point.

:::

:::

::: {.pf-step #s1-2}

Statement (2) is possible as literally stated.

Take two disjoint copies of the same connected space, for example
\[
X=S^1\times\{0\},
\qquad
Y=S^1\times\{1\}
\]
inside
\[
S^1\times\RR.
\]


::: pf-proof

The two spaces are homeomorphic, hence homotopy equivalent.

However, a deformation retract relation
\[
X\subseteq Y
\]
or
\[
Y\subseteq X
\]
requires literal inclusion.
Here the two copies are disjoint, so neither is a deformation retract of the
other.

Thus the statement is possible.
This also records that “is a deformation retract of” depends on a chosen
inclusion, unlike homotopy equivalence.

:::

:::

::: {.pf-step #s1-3}

Statement (3) is impossible.


::: pf-proof

If $X$ is a deformation retract of $Y$, then there is a retraction
\[
r:Y\to X
\]
and a homotopy
\[
\operatorname{id}_Y
\simeq
i\circ r
\]
fixing $X$, where
\[
i:X\hookrightarrow Y
\]
is the inclusion.
Also
\[
r\circ i
=
\operatorname{id}_X.
\]
Hence
\[
i
\]
and
\[
r
\]
are homotopy inverses, so
\[
X\simeq Y.
\]

:::

:::

::: {.pf-step #s1-4}

Statement (4) is impossible.


::: pf-proof

Homotopy-equivalent connected spaces have isomorphic fundamental groups.
Indeed, homotopy inverse maps induce mutually inverse homomorphisms on
\[
\pi_1.
\]

:::

:::

::: {.pf-step #s1-5}

Statement (5) is possible:
\[
X=\{*\},
\qquad
Y=S^2.
\]


::: pf-proof

Both fundamental groups are trivial:
\[
\pi_1(X)=0
=
\pi_1(S^2).
\]
But
\[
H_2(X)=0,
\qquad
H_2(S^2)\cong\ZZ.
\]
Homotopy-equivalent spaces have isomorphic homology groups, so
\[
X\not\simeq Y.
\]

:::

:::

::: {.pf-step #s1-6}

Statement (6) is possible:
\[
X=S^1,
\qquad
Y=S^1\vee S^2,
\]
with $X$ the $S^1$ wedge summand.


::: pf-proof

Define
\[
r:S^1\vee S^2\to S^1
\]
to be the identity on the $S^1$ summand and to collapse the whole $S^2$
summand to the wedge point.
Then
\[
r|_{S^1}
=
\operatorname{id}_{S^1},
\]
so $X$ is a retract of $Y$.

If $X$ were a deformation retract of $Y$, then step [](#s1-3){.pf-ref} would give
\[
X\simeq Y.
\]
But
\[
H_2(X)=0
\]
while
\[
H_2(Y)
\cong
H_2(S^1\vee S^2)
\cong
\ZZ.
\]
Thus they are not homotopy equivalent, so the retraction is not a
deformation retraction.

:::

:::

::: {.pf-step #s1-7}

Statement (7) is impossible.


::: pf-proof

A deformation retraction is, by definition, a retraction together with an
additional homotopy.
Thus every deformation retract is automatically a retract.

:::

:::

::: {.pf-step #s1-8}

Statement (8) is impossible.


::: pf-proof

If $X$ is a deformation retract of $Y$, then
\[
X\simeq Y
\]
by step [](#s1-3){.pf-ref}.
Hence
\[
\pi_1(X)
\cong
\pi_1(Y)
\]
by homotopy invariance of the fundamental group.

:::

:::

::: {.pf-step #s1-9}

Statement (9) is possible:
\[
X=S^1\vee S^1,
\qquad
Y=T^2=S^1\times S^1.
\]


::: pf-proof

For the wedge,
\[
\pi_1(X)
\cong
F_2,
\]
the free group on two generators.
For the torus,
\[
\pi_1(Y)
\cong
\ZZ^2.
\]
These groups are not isomorphic because
\[
F_2
\]
is nonabelian while
\[
\ZZ^2
\]
is abelian.

However,
\[
H_1(X)
\cong
F_2^{\mathrm{ab}}
\cong
\ZZ^2,
\]
and
\[
H_1(Y)
\cong
\ZZ^2.
\]
Thus the first homology groups are isomorphic while the fundamental groups
are not.

:::

:::

::: {.pf-step #s1-10}

Statement (10) is impossible.


::: pf-proof

For every path-connected space $Z$,
\[
H_1(Z;\ZZ)
\cong
\pi_1(Z)^{\mathrm{ab}}.
\]
Therefore an isomorphism
\[
\pi_1(X)
\cong
\pi_1(Y)
\]
induces an isomorphism of abelianizations, hence
\[
H_1(X)
\cong
H_1(Y).
\]

:::

:::

::: {.pf-step #s1-11}

Statement (11) is possible:
\[
X=S^1,
\qquad
Y=\{*\}.
\]


::: pf-proof

Both second homology groups vanish:
\[
H_2(S^1)=0
=
H_2(\{*\}).
\]
But
\[
\pi_1(S^1)
\cong
\ZZ,
\qquad
\pi_1(\{*\})=0.
\]
Thus the fundamental groups are not isomorphic.

:::

:::

::: {.pf-step #s1-12}

Statement (12) is possible:
\[
X=\{*\},
\qquad
Y=S^2.
\]


::: pf-proof

As in step [](#s1-5){.pf-ref},
\[
\pi_1(X)
=
0
=
\pi_1(Y),
\]
while
\[
H_2(X)=0
\]
and
\[
H_2(Y)
\cong
\ZZ.
\]

:::

:::

::: pf-step

The complete classification is therefore
\[
\boxed{
\begin{array}{c|cccccccccccc}
\text{statement}
&1&2&3&4&5&6&7&8&9&10&11&12\\
\hline
\text{possible?}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{no}
&\mathrm{no}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{no}
&\mathrm{no}
&\mathrm{yes}
&\mathrm{no}
&\mathrm{yes}
&\mathrm{yes}
\end{array}
}
\]


::: pf-proof

This table collects steps [](#s1-1){.pf-ref} through [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-12){.pf-ref} give either an explicit example or an impossibility proof
for every requested statement.

:::

:::

:::
