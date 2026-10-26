---
schema: qual/card@1
id: P-TOP-WORKSHOP-HR-W2
kind: problem
title: A deformation retraction induces an isomorphism on fundamental groups
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the second warm-up problem in assets/attachments/day_4_homotopy_retractions.pdf.
---

::: {.problem}
Let $B\subseteq Y$ and let $p:Y\to B$ be a deformation retraction.
Prove that
\[
p_*:\pi_1(Y)\to\pi_1(B)
\]
is an isomorphism.
:::

Fix a basepoint $b_0\in B$ and let
\[
j:B\hookrightarrow Y
\]
be the inclusion.

::: pf

::: pf-step

Since $p$ is a deformation retraction,
\[
p\circ j
=
\operatorname{id}_B.
\]


::: pf-proof

A deformation retraction is, in particular, a retraction. Thus
\[
p(b)=b
\qquad
(b\in B),
\]
which is exactly the displayed identity.

:::

:::

::: pf-step

There is a homotopy
\[
H:Y\times I\to Y
\]
from
\[
\operatorname{id}_Y
\]
to
\[
j\circ p
\]
such that
\[
H(b,t)=b
\qquad
(b\in B, t\in I).
\]


::: pf-proof

This is the defining homotopy of a deformation retraction of $Y$ onto $B$.

:::

:::

::: pf-step

The homotopy in step <1>2 is a based homotopy at $b_0$.


::: pf-proof

Since $b_0\in B$, step <1>2 gives
\[
H(b_0,t)=b_0
\qquad
(t\in I).
\]
Thus the basepoint remains fixed throughout the homotopy.

:::

:::

::: pf-step

On fundamental groups,
\[
p_*\circ j_*
=
\operatorname{id}_{\pi_1(B,b_0)}.
\]


::: pf-proof

By functoriality and step <1>1,
\[
p_*\circ j_*
=
(p\circ j)_*
=
(\operatorname{id}_B)_*
=
\operatorname{id}_{\pi_1(B,b_0)}.
\]

:::

:::

::: pf-step

On fundamental groups,
\[
j_*\circ p_*
=
\operatorname{id}_{\pi_1(Y,b_0)}.
\]


::: pf-proof

By functoriality,
\[
j_*\circ p_*
=
(j\circ p)_*.
\]
By steps <1>2--<1>3, the based maps
\[
j\circ p
\qquad\text{and}\qquad
\operatorname{id}_Y
\]
are based-homotopic. Based-homotopic maps induce the same homomorphism on fundamental groups. Therefore
\[
(j\circ p)_*
=
(\operatorname{id}_Y)_*
=
\operatorname{id}_{\pi_1(Y,b_0)}.
\]

:::

:::

::: pf-step

The homomorphism
\[
p_*:
\pi_1(Y,b_0)
\longrightarrow
\pi_1(B,b_0)
\]
is an isomorphism with inverse $j_*$.


::: pf-proof

Steps <1>4 and <1>5 show that
\[
p_*\circ j_*
=
\operatorname{id}
\qquad\text{and}\qquad
j_*\circ p_*
=
\operatorname{id}.
\]
Hence $j_*$ is a two-sided inverse of $p_*$.

:::

:::

::: pf-qed

Step <1>6 is the required isomorphism.

:::

:::
