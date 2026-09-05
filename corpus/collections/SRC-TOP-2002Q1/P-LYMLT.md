---
schema: qual/card@1
id: P-LYMLT
kind: problem
title: No retraction from $S^2$ onto an equatorial circle
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homology
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section B, problem B3 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    A retraction would split the equatorial inclusion on fundamental groups,
    forcing the identity of pi_1(S^1) = Z to factor through pi_1(S^2) = 0.
---

::: {.problem}
Let $X$ be the 2-sphere, and $A \subseteq X$ the equatorial circle in $X$.
Show that there is no retraction $r : X \to A$.
:::

::: {.solution}
Fix a basepoint $x_0\in A$ and let
\[
i:A\hookrightarrow S^2
\]
be the inclusion.

<1>1. If a retraction $r:S^2\to A$ existed, then
\[
r\circ i=\operatorname{id}_A.
\]
::: {.proof}
By definition, a retraction onto $A$ restricts to the identity on $A$.
In particular $r(x_0)=x_0$, so both $i$ and $r$ are based at $x_0$.
:::

<1>2. Applying the fundamental-group functor to <1>1 would give
\[
r_*\circ i_*
=\operatorname{id}_{\pi_1(A,x_0)}.
\]
::: {.proof}
Functoriality gives
\[
(r\circ i)_*=r_*\circ i_*.
\]
By <1>1, $r\circ i=\operatorname{id}_A$, whose induced map on $\pi_1(A,x_0)$ is the identity.
:::

<1>3. But $i_*$ is the zero homomorphism.
::: {.proof}
Since
\[
\pi_1(S^2,x_0)=0,
\]
the homomorphism
\[
i_*:\pi_1(A,x_0)\longrightarrow\pi_1(S^2,x_0)
\]
has trivial codomain and is therefore zero.
:::

<1>4. This is impossible, so no retraction exists.
::: {.proof}
By <1>3,
\[
r_*\circ i_*=0.
\]
By <1>2 the same composite would have to be the identity on
\[
\pi_1(A,x_0)\cong\pi_1(S^1)\cong\mathbb Z,
\]
which is nontrivial.
This contradiction proves that no retraction $S^2\to A$ exists.
:::
:::
