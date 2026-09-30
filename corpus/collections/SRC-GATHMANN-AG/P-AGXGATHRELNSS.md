---
schema: qual/card@1
id: P-AGXGATHRELNSS
kind: problem
title: Relative Nullstellensatz over the coordinate ring of a variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Coordinate Rings
  - Radical Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Gathmann 1.23 in the retained native problem source at revision
    7eafedfc0 and compared the three parts and concluding correspondence with
    the current card. The retained source gives the exercise statement but no
    worked solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the proof. Checked both preimage identities, the passage from the
    affine-space Nullstellensatz inclusion to the relative radical inclusion,
    and both inverse identities in the inclusion-reversing correspondence.
---

::: {.problem}
Let $Y\subset \AA^n/k$ be an affine variety and define $A(Y)$ by the quotient
\[
\pi: k[x_1,\cdots, x_n] \to A(Y) \definedas k[x_1, \cdots, x_n]/I(Y)
.\]

a. Show that $V_Y(J) = V(\pi^{-1}(J))$ for every $J\normal A(Y)$.

b. Show that $\pi^{-1} (I_Y(X)) = I(X)$ for every affine subvariety $X\subseteq Y$.

c. Using the fact that $I(V(J)) \subset \sqrt{J}$ for every $J\normal k[x_1, \cdots, x_n]$, deduce that $I_Y(V_Y(J)) \subset \sqrt{J}$ for every $J\normal A(Y)$.

Conclude that there is an inclusion-reversing bijection
\[
\correspond{\text{Affine subvarieties}\\ \text{of } Y} \iff \correspond{\text{Radical ideals} \\ \text{in } A(Y)}
.\]
:::

::: {.solution}
Put
$$
S=k[x_1,\ldots,x_n],
\qquad
A=A(Y)=S/I(Y).
$$
For $g\in A$ and $y\in Y$, the value $g(y)$ is well defined: any two lifts
of $g$ to $S$ differ by an element of $I(Y)$ and therefore agree on $Y$.

::: pf

::: {.pf-step #vy-equals-v-preimage}
(a) For every ideal $J\normal A$,
$$
\boxed{V_Y(J)=V(\pi^{-1}(J)).}
$$

::: pf-proof
Since
$$
I(Y)=\ker\pi\subseteq\pi^{-1}(J),
$$
every point of $V(\pi^{-1}(J))$ lies in
$$
V(I(Y))=Y.
$$
For $y\in Y$,
$$
\begin{aligned}
y\in V_Y(J)
&\iff g(y)=0 &&\text{for every }g\in J\\
&\iff f(y)=0 &&\text{for every }f\in\pi^{-1}(J)\\
&\iff y\in V(\pi^{-1}(J)).
\end{aligned}
$$
The middle equivalence follows because every $g\in J$ has a lift
$f\in\pi^{-1}(J)$ and evaluation of $g$ at $y$ is evaluation of any such
lift.
:::

:::

::: {.pf-step #preimage-iy-equals-i}
(b) For every affine subvariety $X\subseteq Y$,
$$
\boxed{\pi^{-1}(I_Y(X))=I(X).}
$$

::: pf-proof
For $f\in S$,
$$
\begin{aligned}
f\in\pi^{-1}(I_Y(X))
&\iff \pi(f)\in I_Y(X)\\
&\iff \pi(f)(x)=0 &&\text{for every }x\in X\\
&\iff f(x)=0 &&\text{for every }x\in X\\
&\iff f\in I(X).
\end{aligned}
$$
:::

:::

::: {.pf-step #iy-vy-subset-radical}
(c) For every ideal $J\normal A$,
$$
\boxed{I_Y(V_Y(J))\subseteq\sqrt J}.
$$

::: pf-proof
Let
$$
g\in I_Y(V_Y(J))
$$
and choose a lift $f\in S$ with $\pi(f)=g$. By step [](#preimage-iy-equals-i){.pf-ref},
$$
f\in\pi^{-1}\bigl(I_Y(V_Y(J))\bigr)
=I(V_Y(J)).
$$
By step [](#vy-equals-v-preimage){.pf-ref},
$$
V_Y(J)=V(\pi^{-1}(J)),
$$
so
$$
f\in I\bigl(V(\pi^{-1}(J))\bigr).
$$
Applying the given affine-space Nullstellensatz inclusion to the ideal
$\pi^{-1}(J)\normal S$ gives
$$
f\in\sqrt{\pi^{-1}(J)}.
$$
Hence $f^m\in\pi^{-1}(J)$ for some $m\ge1$, and therefore
$$
g^m=\pi(f)^m=\pi(f^m)\in J.
$$
Thus $g\in\sqrt J$.
:::

:::

::: {.pf-step #inverse-correspondence}
The assignments
$$
X\longmapsto I_Y(X),
\qquad
J\longmapsto V_Y(J)
$$
restrict to mutually inverse correspondences between affine subvarieties of
$Y$ and radical ideals of $A$.

::: pf-proof
First, $I_Y(X)$ is radical for every affine subvariety $X\subseteq Y$. If
$$
g^m\in I_Y(X),
$$
then $g(x)^m=0$ for every $x\in X$, hence $g(x)=0$ for every $x\in X$ and
therefore $g\in I_Y(X)$.

For every $X\subseteq Y$, steps [](#vy-equals-v-preimage){.pf-ref} and [](#preimage-iy-equals-i){.pf-ref} give
$$
V_Y(I_Y(X))
=V\bigl(\pi^{-1}(I_Y(X))\bigr)
=V(I(X))
=X.
$$
The last equality holds because $X$ is an affine subvariety: if
$X=V(K)$, then $K\subseteq I(X)$ gives $V(I(X))\subseteq V(K)=X$, while
the reverse inclusion follows directly from the definition of $I(X)$.

Conversely, for every ideal $J\normal A$ one always has
$$
J\subseteq I_Y(V_Y(J)).
$$
If $J$ is radical, step [](#iy-vy-subset-radical){.pf-ref} gives
$$
I_Y(V_Y(J))
\subseteq
\sqrt J
=J.
$$
Hence
$$
I_Y(V_Y(J))=J
$$
for every radical ideal $J$.

Thus the two assignments are inverse on the stated classes.
:::

:::

::: {.pf-step #inclusion-reversing}
The bijection in step [](#inverse-correspondence){.pf-ref} reverses inclusions.

::: pf-proof
If $X_1\subseteq X_2$, every function vanishing on $X_2$ vanishes on
$X_1$, so
$$
I_Y(X_2)\subseteq I_Y(X_1).
$$
If $J_1\subseteq J_2$, every common zero of $J_2$ is a common zero of
$J_1$, so
$$
V_Y(J_2)\subseteq V_Y(J_1).
$$
This proves that the bijection is inclusion reversing.
:::

:::

::: pf-qed
Steps [](#vy-equals-v-preimage){.pf-ref}, [](#preimage-iy-equals-i){.pf-ref} and [](#iy-vy-subset-radical){.pf-ref} prove (a)--(c). Steps [](#inverse-correspondence){.pf-ref} and [](#inclusion-reversing){.pf-ref} establish the concluding
inclusion-reversing bijection.
:::

:::
:::
