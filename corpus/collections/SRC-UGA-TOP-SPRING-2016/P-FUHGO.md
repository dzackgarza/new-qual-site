---
schema: qual/card@1
id: P-FUHGO
kind: problem
title: A closed curve on a surface that is nullhomologous but not nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Give an example, with explanation, of a closed curve in a surfaces which is not nullhomotopic but is nullhomologous.
:::

::: {.solution}
<1>1. Take the genus-$2$ surface $\Sigma_2$, with $\pi_1(\Sigma_2) = \langle a_1, b_1, a_2, b_2 \mid [a_1, b_1][a_2, b_2] \rangle$.
Proof: standard presentation of the fundamental group of a genus-$2$ surface.

<1>2. The commutator $[a_1, b_1] = a_1 b_1 a_1^{-1} b_1^{-1}$ is not nullhomotopic.
Proof: $[a_1, b_1] \neq 1$ in $\pi_1(\Sigma_2)$ (it is a nontrivial element of the free group on $a_1, b_1$).

<1>3. But $[a_1, b_1]$ is nullhomologous.
Proof: $H_1(\Sigma_2) = \pi_1(\Sigma_2)^{\text{ab}} = \ZZ^4$ (free abelian on $a_1, b_1, a_2, b_2$), and the image of $[a_1, b_1]$ in the abelianization is $a_1 + b_1 - a_1 - b_1 = 0$, so $[a_1, b_1]$ is nullhomologous.

<1>4. Hence $[a_1, b_1]$ is a closed curve that is not nullhomotopic but is nullhomologous.
Proof: <1>2 and <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
