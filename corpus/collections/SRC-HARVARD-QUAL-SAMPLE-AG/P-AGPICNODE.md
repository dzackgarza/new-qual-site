---
schema: qual/card@1
id: P-AGPICNODE
kind: problem
title: $\Pic(k[t^2,t^3])$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Group
  - Singularities
  - Normalization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's question computing $\Pic(k[t^2,t^3])$ from its normalization $k[t]$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Calculate $\Pic(k[t^2,t^3])$, where $k[t^2,t^3] \subseteq k[t]$.
:::

::: {.solution}
Put
\[
A=k[t^2,t^3],
\qquad
B=k[t].
\]
The inclusion $A\subseteq B$ is the normalization of the cuspidal affine curve.

::: pf

::: pf-step
The conductor of $A\subseteq B$ is
\[
I=t^2B=(t^2,t^3)\subseteq A.
\]

::: pf-proof
Every monomial $t^n$ with $n\ge2$ lies in $A$.  Thus
\[
t^2B\subseteq A,
\]
and multiplication by any element of $t^2B$ sends $B$ into $A$.

Conversely, if
\[
b=a_0+a_1t+a_2t^2+\cdots\in B
\]
lies in the conductor, then in particular $b\in A$, so $a_1=0$.  Also $bt\in A$, which forces $a_0=0$.  Hence $b\in t^2B$.  Therefore the conductor is exactly $I=t^2B$.
:::

:::

::: pf-step
The conductor square has quotients
\[
A/I\cong k,
\qquad
B/I\cong k[t]/(t^2).
\]

::: pf-proof
Modulo $(t^2,t^3)$, every element of $A$ reduces to its constant term, giving $A/I\cong k$.  In $B=k[t]$, the ideal is $(t^2)$, giving the second quotient.
:::

:::

::: {.pf-step #conductor-exact-sequence}
The conductor square gives an exact sequence
\[
B^*\times(A/I)^*
\longrightarrow
(B/I)^*
\longrightarrow
\operatorname{Pic}(A)
\longrightarrow
\operatorname{Pic}(B)\times\operatorname{Pic}(A/I)
\longrightarrow
\operatorname{Pic}(B/I).
\]

::: pf-proof
The conductor square
\[
\begin{array}{ccc}
\operatorname{Spec}(B/I)&\longrightarrow&\operatorname{Spec}B\\
\downarrow&&\downarrow\\
\operatorname{Spec}(A/I)&\longrightarrow&\operatorname{Spec}A
\end{array}
\]
is a Milnor patching square.  The Mayer--Vietoris sequence for units and line bundles gives the displayed exact segment.
:::

:::

::: {.pf-step #picard-groups-vanish}
The three Picard groups on the right of step [](#conductor-exact-sequence){.pf-ref} vanish.

::: pf-proof
The ring
\[
B=k[t]
\]
is a principal ideal domain, so
\[
\operatorname{Pic}(B)=0.
\]
The ring $A/I\cong k$ is a field, so its Picard group is zero.  The ring
\[
B/I\cong k[t]/(t^2)
\]
is local Artinian, and every rank-one projective module over a local ring is free, so its Picard group is also zero.
:::

:::

::: {.pf-step #pic-a-quotient}
Hence
\[
\operatorname{Pic}(A)
\cong
(B/I)^*/\operatorname{im}\bigl(B^*\times(A/I)^*\bigr).
\]

::: pf-proof
This is exactness of step [](#conductor-exact-sequence){.pf-ref} together with the vanishing in step [](#picard-groups-vanish){.pf-ref}.
:::

:::

::: {.pf-step #unit-computation}
One has
\[
(B/I)^*
=\{a+bt\pmod{t^2}:a\in k^*,\ b\in k\}
=k^*\cdot(1+kt),
\]
and the image of
\[
B^*\times(A/I)^*
\]
is exactly the subgroup of constant units $k^*$.

::: pf-proof
An element $a+bt$ of $k[t]/(t^2)$ is a unit exactly when $a\ne0$, and then
\[
a+bt=a\left(1+\frac ba t\right).
\]

Both
\[
B^*=k^*
\qquad\text{and}\qquad
(A/I)^*=k^*.
\]
The patching map sends a pair of constants to their ratio in $(B/I)^*$, so its image is precisely $k^*$.
:::

:::

::: {.pf-step #final-picard-computation}
Therefore
\[
\boxed{
\operatorname{Pic}(k[t^2,t^3])
\cong
1+kt
\cong
(k,+).
}
\]

::: pf-proof
Steps [](#pic-a-quotient){.pf-ref} and [](#unit-computation){.pf-ref} give
\[
\operatorname{Pic}(A)
\cong
(B/I)^*/k^*
\cong
1+kt.
\]
Modulo $t^2$,
\[
(1+at)(1+bt)=1+(a+b)t,
\]
so the map
\[
k\longrightarrow1+kt,
\qquad
a\longmapsto1+at
\]
is an isomorphism from the additive group of $k$ to this multiplicative unit subgroup.
:::

:::

::: pf-qed
Step [](#final-picard-computation){.pf-ref} is the required Picard-group calculation.
:::

:::
:::
