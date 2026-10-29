---
schema: qual/card@1
id: P-WESTOP09-II1
kind: problem
title: Simple connectivity, retractions, and deformation retracts on fundamental groups
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove or disprove each statement:

1. If $A\subseteq X$ and $X$ is simply connected, then $A$ is simply connected.
2. If $r:X\to A$ is a retraction, then
   \[
   r_*:\pi_1(X)\to\pi_1(A)
   \]
   is surjective.
3. If $A$ is a deformation retract of $X$ and $i:A\hookrightarrow X$ is inclusion, then
   \[
   i_*:\pi_1(A)\to\pi_1(X)
   \]
   is an isomorphism.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement 1 is
\[
\boxed{\mathrm{False}}.
\]


::: pf-proof

Take
\[
X=D^2
\qquad\text{and}\qquad
A=S^1=\partial D^2.
\]
The disk $D^2$ is contractible and therefore simply connected, whereas
\[
\pi_1(S^1)\cong\ZZ
\]
is nontrivial. Thus a subspace of a simply connected space need not be simply
connected.

:::

:::

::: pf-step

Statement 2 is
\[
\boxed{\mathrm{True}}.
\]


::: pf-proof

Let $i:A\hookrightarrow X$ be the inclusion and choose a basepoint
$a_0\in A$. Since $r$ is a retraction,
\[
r\circ i=\operatorname{id}_A.
\]
Passing to fundamental groups gives
\[
r_*\circ i_*
=(r\circ i)_*
=(\operatorname{id}_A)_*
=\operatorname{id}_{\pi_1(A,a_0)}.
\]
Thus every element $\alpha\in\pi_1(A,a_0)$ satisfies
\[
\alpha=r_*(i_*(\alpha)),
\]
so $r_*$ is surjective.

:::

:::

::: {.pf-step #s1-3}

Statement 3 is
\[
\boxed{\mathrm{True}}.
\]


::: pf-proof

Let $r:X\to A$ be the deformation retraction and let $i:A\hookrightarrow X$
be inclusion. Then
\[
r\circ i=\operatorname{id}_A,
\]
and the deformation retraction gives a homotopy
\[
i\circ r\simeq\operatorname{id}_X
\]
that fixes $A$ pointwise. With a basepoint $a_0\in A$, this is a based
homotopy, so
\[
r_*\circ i_*=\operatorname{id}_{\pi_1(A,a_0)}
\]
and
\[
i_*\circ r_*=\operatorname{id}_{\pi_1(X,a_0)}.
\]
Hence $i_*$ and $r_*$ are inverse isomorphisms. In particular,
\[
\boxed{i_*:\pi_1(A,a_0)\xrightarrow{\sim}\pi_1(X,a_0)}.
\]

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} settle the three statements.

:::

:::

:::
