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
$$
p_*:\pi_1(Y)\to\pi_1(B)
$$
is an isomorphism.
:::

::: {.solution}

Fix a basepoint $b_0\in B$ and let
$$
j:B\hookrightarrow Y
$$
be the inclusion.

::: pf

::: {.pf-step #s1-1}

Since $p$ is a deformation retraction,
$$
p\circ j
=
\operatorname{id}_B.
$$


::: pf-proof

A deformation retraction is, in particular, a retraction. Thus
$$
p(b)=b
\qquad
(b\in B),
$$
which is exactly the displayed identity.

:::

:::

::: {.pf-step #s1-2}

There is a homotopy
$$
H:Y\times I\to Y
$$
from
$$
\operatorname{id}_Y
$$
to
$$
j\circ p
$$
such that
$$
H(b,t)=b
\qquad
(b\in B, t\in I).
$$


::: pf-proof

This is the defining homotopy of a deformation retraction of $Y$ onto $B$.

:::

:::

::: {.pf-step #s1-3}

The homotopy in step [](#s1-2){.pf-ref} is a based homotopy at $b_0$.


::: pf-proof

Since $b_0\in B$, step [](#s1-2){.pf-ref} gives
$$
H(b_0,t)=b_0
\qquad
(t\in I).
$$
Thus the basepoint remains fixed throughout the homotopy.

:::

:::

::: {.pf-step #s1-4}

On fundamental groups,
$$
p_*\circ j_*
=
\operatorname{id}_{\pi_1(B,b_0)}.
$$


::: pf-proof

By functoriality and step [](#s1-1){.pf-ref},
$$
p_*\circ j_*
=
(p\circ j)_*
=
(\operatorname{id}_B)_*
=
\operatorname{id}_{\pi_1(B,b_0)}.
$$

:::

:::

::: {.pf-step #s1-5}

On fundamental groups,
$$
j_*\circ p_*
=
\operatorname{id}_{\pi_1(Y,b_0)}.
$$


::: pf-proof

By functoriality,
$$
j_*\circ p_*
=
(j\circ p)_*.
$$
By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, the based maps
$$
j\circ p
\qquad\text{and}\qquad
\operatorname{id}_Y
$$
are based-homotopic. Based-homotopic maps induce the same homomorphism on fundamental groups. Therefore
$$
(j\circ p)_*
=
(\operatorname{id}_Y)_*
=
\operatorname{id}_{\pi_1(Y,b_0)}.
$$

:::

:::

::: {.pf-step #s1-6}

The homomorphism
$$
p_*:
\pi_1(Y,b_0)
\longrightarrow
\pi_1(B,b_0)
$$
is an isomorphism with inverse $j_*$.


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} show that
$$
p_*\circ j_*
=
\operatorname{id}
\qquad\text{and}\qquad
j_*\circ p_*
=
\operatorname{id}.
$$
Hence $j_*$ is a two-sided inverse of $p_*$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required isomorphism.

:::

:::

:::
