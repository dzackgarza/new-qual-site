---
schema: qual/card@1
id: P-AGPICTORS
kind: problem
title: A variety with $\Pic(V) = \ZZ/3$, projective or otherwise
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Group
  - Torsion
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Poonen's question asking for a variety with Picard group $\ZZ/3$ and whether one can be projective.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Does there exist a variety $V$ with $\Pic(V) = \ZZ/3$?

Does there exist a *projective* variety with $\Pic(V) = \ZZ/3$?
:::

::: {.solution}
Let
\[
B=\mathbb P^1_k,
\qquad
L=\mathcal O_{\mathbb P^1}(3),
\]
let
\[
p:E=\operatorname{Tot}(L)\longrightarrow B
\]
be the total space of the line bundle, and let
\[
D\subseteq E
\]
be the zero section.  Put
\[
V=E\setminus D=L^\times.
\]

::: pf

::: {.pf-step #pic-b-pic-e-iso}
Pullback along $p$ gives an isomorphism
\[
\operatorname{Pic}(B)
\xrightarrow{\sim}
\operatorname{Pic}(E).
\]

::: pf-proof
The total space of a vector bundle over the regular scheme $B=\mathbb P^1$ is an affine-space bundle over $B$.  Homotopy invariance of the Picard group for regular schemes gives
\[
\operatorname{Pic}(B)
\cong
\operatorname{Pic}(E).
\]

The inverse is restriction to the zero section
\[
s:B\hookrightarrow E,
\]
because
\[
p\circ s=\operatorname{id}_B.
\]
:::

:::

::: {.pf-step #zero-section-class}
Under the identification in step [](#pic-b-pic-e-iso){.pf-ref}, the divisor class of the zero section $D$ corresponds to
\[
[L]=[\mathcal O_{\mathbb P^1}(3)]
\in\operatorname{Pic}(\mathbb P^1)\cong\mathbb Z.
\]

::: pf-proof
The zero section is an effective Cartier divisor in the smooth surface $E$.  Its divisor line bundle satisfies
\[
\mathcal O_E(D)|_D
\cong
N_{D/E}.
\]
The normal bundle of the zero section in the total space of $L$ is canonically $L$ itself.  Since restriction $s^*$ is the inverse of the pullback isomorphism in step [](#pic-b-pic-e-iso){.pf-ref}, the class $[D]$ corresponds to $[L]$.
:::

:::

::: {.pf-step #localization-sequence}
The localization sequence for the complement of $D$ gives
\[
\operatorname{Pic}(V)
\cong
\operatorname{Pic}(E)/\mathbb Z[D].
\]

::: pf-proof
Both $E$ and $V$ are regular integral schemes, so
\[
\operatorname{Pic}=\operatorname{Cl}
\]
on each.  Removing the prime divisor $D$ gives the divisor-class localization sequence
\[
\mathbb Z[D]
\longrightarrow
\operatorname{Cl}(E)
\longrightarrow
\operatorname{Cl}(V)
\longrightarrow0.
\]
Replacing class groups by Picard groups gives the displayed quotient.
:::

:::

::: {.pf-step #pic-v-z3}
Therefore
\[
\boxed{\operatorname{Pic}(V)\cong\mathbb Z/3\mathbb Z.}
\]

::: pf-proof
One has
\[
\operatorname{Pic}(\mathbb P^1)
\cong\mathbb Z,
\qquad
[\mathcal O(1)]\longmapsto1.
\]
By steps [](#pic-b-pic-e-iso){.pf-ref} and [](#zero-section-class){.pf-ref},
\[
\operatorname{Pic}(E)\cong\mathbb Z
\]
and the class $[D]$ corresponds to
\[
[\mathcal O(3)]=3.
\]
Hence step [](#localization-sequence){.pf-ref} gives
\[
\operatorname{Pic}(V)
\cong
\mathbb Z/3\mathbb Z.
\]
Thus such a variety does exist; $V=L^\times$ is a smooth quasi-projective surface.
:::

:::

::: {.pf-step #no-positive-dim-projective}
No positive-dimensional projective variety can have Picard group $\mathbb Z/3\mathbb Z$.

::: pf-proof
Suppose $X$ were a positive-dimensional projective variety with
\[
\operatorname{Pic}(X)\cong\mathbb Z/3\mathbb Z.
\]
Choose a very ample line bundle $A$ on $X$.  Every element of the Picard group is $3$-torsion, so
\[
A^{\otimes3}\cong\mathcal O_X.
\]

But a positive tensor power of a very ample line bundle is again very ample.  Thus $\mathcal O_X$ would be very ample.  The morphism defined by global sections of the trivial line bundle is constant on every geometrically connected component, so it cannot embed a positive-dimensional variety into projective space.  This is a contradiction.
:::

:::

::: {.pf-step #no-zero-dim-projective}
There is no zero-dimensional projective variety with Picard group $\mathbb Z/3\mathbb Z$ either.

::: pf-proof
A zero-dimensional variety is affine; if it is integral it is the spectrum of a finite field extension of $k$.  The Picard group of the spectrum of a field is zero.
:::

:::

::: {.pf-step #final-answer}
Hence
\[
\boxed{
\text{there are nonprojective varieties with }\operatorname{Pic}=\mathbb Z/3,
\text{ but no projective varieties with that Picard group.}
}
\]

::: pf-proof
Step [](#pic-v-z3){.pf-ref} supplies the example, and steps [](#no-positive-dim-projective){.pf-ref} and [](#no-zero-dim-projective){.pf-ref} rule out the projective case.
:::

:::

::: pf-qed
Step [](#final-answer){.pf-ref} answers both questions.
:::

:::
:::
