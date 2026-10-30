---
schema: qual/card@1
id: P-TOP-WORKSHOP-HR-W1
kind: problem
title: A retraction induces a surjection on fundamental groups
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the first warm-up problem in assets/attachments/Revised_packet_-_Homotopy_and_Retractions.pdf.
---

::: {.problem}
Let $A\subseteq X$ and let $r:X\to A$ be a retraction.
Prove that
$$
r_*:\pi_1(X)\to\pi_1(A)
$$
is surjective.
:::

::: {.solution}

Fix a basepoint $a_0\in A$ and let
$$
i:A\hookrightarrow X
$$
be the inclusion.

::: pf

::: {.pf-step #s1-1}

Both $i$ and $r$ preserve the basepoint $a_0$, and
$$
r\circ i
=
\operatorname{id}_A.
$$


::: pf-proof

Because $r$ is a retraction onto $A$,
$$
r(a)=a
\qquad
(a\in A).
$$
In particular,
$$
r(a_0)=a_0.
$$
The inclusion also fixes $a_0$, and for every $a\in A$,
$$
(r\circ i)(a)
=
r(a)
=
a.
$$
Thus $r\circ i=\operatorname{id}_A$ as based maps.

:::

:::

::: {.pf-step #s1-2}

The induced homomorphisms on fundamental groups satisfy
$$
r_*\circ i_*
=
\operatorname{id}_{\pi_1(A,a_0)}.
$$


::: pf-proof

Functoriality of the fundamental group gives
$$
(r\circ i)_*
=
r_*\circ i_*.
$$
By step [](#s1-1){.pf-ref},
$$
r\circ i
=
\operatorname{id}_A,
$$
so
$$
r_*\circ i_*
=
(\operatorname{id}_A)_*
=
\operatorname{id}_{\pi_1(A,a_0)}.
$$

:::

:::

::: {.pf-step #s1-3}

The homomorphism
$$
r_*:
\pi_1(X,a_0)
\longrightarrow
\pi_1(A,a_0)
$$
is surjective.


::: pf-proof

Let
$$
[\gamma]\in\pi_1(A,a_0).
$$
By step [](#s1-2){.pf-ref},
$$
[\gamma]
=
(r_*\circ i_*)([\gamma])
=
r_*\bigl(i_*([\gamma])\bigr).
$$
Thus every element of $\pi_1(A,a_0)$ lies in the image of $r_*$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required surjectivity.

:::

:::

:::
