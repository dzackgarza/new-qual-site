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
Fix a basepoint $x_0\in A$ and let $i\colon A\hookrightarrow S^2$ be the inclusion.
Suppose $r\colon S^2\to A$ is a retraction.

<1>1. $r_*\circ i_*=\operatorname{id}_{\pi_1(A,x_0)}$.

::: {.proof}
A retraction onto $A$ restricts to the identity on $A$, so $r\circ i=\operatorname{id}_A$ and $r(x_0)=x_0$.
By functoriality of $\pi_1$, $r_*\circ i_*=(r\circ i)_*=\operatorname{id}_{\pi_1(A,x_0)}$.
:::

<1>2. $i_*\colon\pi_1(A,x_0)\to\pi_1(S^2,x_0)$ is the zero homomorphism.

::: {.proof}
Its codomain $\pi_1(S^2,x_0)$ is trivial.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, $r_*\circ i_*=0$.
By step <1>1, the same composite is the identity of $\pi_1(A,x_0)\cong\pi_1(S^1)\cong\ZZ$, which is nontrivial.
This contradiction shows that no retraction $S^2\to A$ exists.
:::
:::
