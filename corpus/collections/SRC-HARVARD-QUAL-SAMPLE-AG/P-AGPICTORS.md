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

<1>1. Pullback along $p$ gives an isomorphism
\[
\operatorname{Pic}(B)
\xrightarrow{\sim}
\operatorname{Pic}(E).
\]
::: {.proof}
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

<1>2. Under the identification in <1>1, the divisor class of the zero section $D$ corresponds to
\[
[L]=[\mathcal O_{\mathbb P^1}(3)]
\in\operatorname{Pic}(\mathbb P^1)\cong\mathbb Z.
\]
::: {.proof}
The zero section is an effective Cartier divisor in the smooth surface $E$.  Its divisor line bundle satisfies
\[
\mathcal O_E(D)|_D
\cong
N_{D/E}.
\]
The normal bundle of the zero section in the total space of $L$ is canonically $L$ itself.  Since restriction $s^*$ is the inverse of the pullback isomorphism in <1>1, the class $[D]$ corresponds to $[L]$.
:::

<1>3. The localization sequence for the complement of $D$ gives
\[
\operatorname{Pic}(V)
\cong
\operatorname{Pic}(E)/\mathbb Z[D].
\]
::: {.proof}
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

<1>4. Therefore
\[
\boxed{\operatorname{Pic}(V)\cong\mathbb Z/3\mathbb Z.}
\]
::: {.proof}
One has
\[
\operatorname{Pic}(\mathbb P^1)
\cong\mathbb Z,
\qquad
[\mathcal O(1)]\longmapsto1.
\]
By <1>1 and <1>2,
\[
\operatorname{Pic}(E)\cong\mathbb Z
\]
and the class $[D]$ corresponds to
\[
[\mathcal O(3)]=3.
\]
Hence <1>3 gives
\[
\operatorname{Pic}(V)
\cong
\mathbb Z/3\mathbb Z.
\]
Thus such a variety does exist; $V=L^\times$ is a smooth quasi-projective surface.
:::

<1>5. No positive-dimensional projective variety can have Picard group $\mathbb Z/3\mathbb Z$.
::: {.proof}
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

<1>6. There is no zero-dimensional projective variety with Picard group $\mathbb Z/3\mathbb Z$ either.
::: {.proof}
A zero-dimensional variety is affine; if it is integral it is the spectrum of a finite field extension of $k$.  The Picard group of the spectrum of a field is zero.
:::

<1>7. Hence
\[
\boxed{
\text{there are nonprojective varieties with }\operatorname{Pic}=\mathbb Z/3,
\text{ but no projective varieties with that Picard group.}
}
\]
::: {.proof}
Step <1>4 supplies the example, and steps <1>5--<1>6 rule out the projective case.
:::

<1>8. Q.E.D.
::: {.proof}
Step <1>7 answers both questions.
:::
:::
