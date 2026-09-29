---
schema: qual/card@1
id: E-HAT-1.1-18
kind: problem
title: Attaching cells of dimension $\geq 2$ gives surjection on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - CW Complexes
  - Cell Attachments
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Applied Lemma 1.15 to the standard two-open-set cover of a cell attachment and then iterated the one-cell result over the CW skeleta.
---

::: {.problem}
Using Lemma 1.15, show that if a space $X$ is obtained from a path-connected subspace $A$ by attaching a cell $e^n$ with $n \geq 2$, then the inclusion $A \hookrightarrow X$ induces a surjection on $\pi_1$.
Apply this to show:

(a) The wedge sum $S^1 \lor S^2$ has fundamental group $\mathbb{Z}$.

(b) For a path-connected CW complex $X$ the inclusion map $X^1 \hookrightarrow X$ of its 1 skeleton induces a surjection $\pi_1(X^1) \longrightarrow \pi_1(X)$.
[For the case that $X$ has infinitely many cells, see Proposition A.1 in the Appendix.]
:::

::: {.solution}
Let
\[
X=A\cup_\varphi D^n,
\qquad n\ge2,
\]
where the boundary sphere $S^{n-1}=\partial D^n$ is attached to the path-connected space $A$ by $\varphi$.

::: pf

::: {.pf-step #s1}

There is an open cover $X=U\cup V$ such that $U$ deformation retracts onto $A$, $V$ is contractible, and $U\cap V$ is path connected.

::: pf-proof

Choose a smaller closed ball $B\subset\operatorname{int}D^n$ about the center.
The image in $X$ of
\[
D^n\setminus B
\]
deformation retracts radially onto the attaching sphere, hence together with $A$ gives a neighborhood that deformation retracts onto $A$.
After slightly enlarging this neighborhood in the quotient, call it $U$.

Take $V$ to be the image of a slightly larger open ball about the center, joined by a thin radial tube to a chosen point of the attaching sphere and then by a thin tube in $A$ to the basepoint.
This $V$ is contractible.
Its overlap with $U$ deformation retracts onto a sphere with a tube attached to the basepoint.
Since
\[
n-1\ge1,
\]
the sphere $S^{n-1}$ is path connected, so $U\cap V$ is path connected.
Both $U$ and $V$ may be chosen path connected and to contain the basepoint.

:::

:::

::: {.pf-step #s2}

Every loop in $X$ based at $x_0\in A$ is homotopic to a product of loops, each lying entirely in $U$ or entirely in $V$.

::: pf-proof

Apply Lemma 1.15 to the cover $X=U\cup V$ from step [](#s1){.pf-ref}.
Its hypotheses hold because $U$ and $V$ are path connected, both contain $x_0$, and $U\cap V$ is path connected.

:::

:::

::: {.pf-step #s3}

Every factor lying in $V$ is null-homotopic in $X$, while every factor lying in $U$ is homotopic in $X$ to a loop in $A$.

::: pf-proof

The first assertion follows from contractibility of $V$.
For the second, use the deformation retraction
\[
U\simeq A
\]
from step [](#s1){.pf-ref}, chosen to fix the basepoint.

:::

:::

::: {.pf-step #s4}

The inclusion-induced homomorphism
\[
i_*:\pi_1(A,x_0)\longrightarrow\pi_1(X,x_0)
\]
is surjective.

::: pf-proof

Let $[\gamma]\in\pi_1(X,x_0)$.
By step [](#s2){.pf-ref}, $\gamma$ is homotopic to a product of loops in $U$ and $V$.
By step [](#s3){.pf-ref}, discard the null-homotopic $V$ factors and replace every $U$ factor by a loop in $A$.
Thus $[\gamma]$ is represented by a product of loops in $A$, hence lies in the image of $i_*$.

:::

:::

::: {.pf-step #s5}

For $S^1\vee S^2$, the inclusion
\[
S^1\hookrightarrow S^1\vee S^2
\]
induces a surjection on fundamental groups.

::: pf-proof

The wedge $S^1\vee S^2$ is obtained from $S^1$ by attaching a $2$-cell by the constant attaching map.
Apply step [](#s4){.pf-ref}.

:::

:::

::: pf-step

The same inclusion also induces an injection, hence
\[
\pi_1(S^1\vee S^2)\cong\mathbb Z.
\]

::: pf-proof

Collapse the $S^2$ summand to the wedge point.
This gives a retraction
\[
r:S^1\vee S^2\to S^1.
\]
If $i:S^1\hookrightarrow S^1\vee S^2$ is the inclusion, then
\[
r\circ i=\operatorname{id}_{S^1},
\]
so
\[
r_*\circ i_*=\operatorname{id}_{\pi_1(S^1)}.
\]
Thus $i_*$ is injective.
Together with step [](#s5){.pf-ref} it is an isomorphism, and
\[
\pi_1(S^1)\cong\mathbb Z.
\]

:::

:::

::: {.pf-step #s7}

If $X$ is a finite path-connected CW complex, then
\[
\pi_1(X^1)\longrightarrow\pi_1(X)
\]
is surjective.

::: pf-proof

Starting with $X^1$, form $X^2$ by attaching the $2$-cells one at a time.
Each attachment induces a surjection on $\pi_1$ by step [](#s4){.pf-ref}, so the composite
\[
\pi_1(X^1)\twoheadrightarrow\pi_1(X^2)
\]
is surjective.
Then attach the $3$-cells one at a time, and continue through all higher dimensions.
At every step the cell dimension is at least $2$, so step [](#s4){.pf-ref} applies.
The composite map
\[
\pi_1(X^1)\longrightarrow\pi_1(X)
\]
is therefore surjective.

:::

:::

::: pf-step

The same conclusion holds for an arbitrary path-connected CW complex.

::: pf-proof

Every loop has compact image.
By Proposition A.1, a compact subset of a CW complex is contained in a finite subcomplex.
Hence any loop in $X$ lies in a finite subcomplex $K\subseteq X$.
Applying step [](#s7){.pf-ref} to $K$ shows that the loop class comes from $\pi_1(K^1)$, and
\[
K^1\subseteq X^1.
\]
Thus every element of $\pi_1(X)$ lies in the image of $\pi_1(X^1)$.

:::

:::

:::

:::
