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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked against problem 8 of the official UGA Spring 2016 topology exam; corrected the card's introduced plural typo "in a surfaces" to "in a surface".
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the unsupported nontriviality assertion with an explicit homomorphism to a free group detecting the commutator.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified both claims independently in the genus-two surface-group presentation; the commutator survives in a free-group quotient and dies in the abelianization.
---

::: {.problem}
Give an example, with explanation, of a closed curve in a surface which is not nullhomotopic but is nullhomologous.
:::

::: {.solution}

::: pf

::: pf-step

Take the closed orientable genus-$2$ surface $\Sigma_2$, with
\[
\pi_1(\Sigma_2)
=\left\langle a_1,b_1,a_2,b_2
\mathrel{\Big|}
[a_1,b_1][a_2,b_2]=1
\right\rangle.
\]
Let $\gamma$ be a based closed curve representing the commutator $[a_1,b_1]$.

::: pf-proof

This is the standard one-relator presentation obtained from the usual $8$-gon model of $\Sigma_2$.
The word $[a_1,b_1]=a_1b_1a_1^{-1}b_1^{-1}$ is therefore represented by a closed loop on $\Sigma_2$.

:::

:::

::: {.pf-step #s2}

The curve $\gamma$ is not nullhomotopic.

::: pf-proof

Let $F(a,b)$ be the free group on $a,b$ and define on the generators
\[
a_1\longmapsto a,
\qquad
b_1\longmapsto b,
\qquad
a_2\longmapsto b,
\qquad
b_2\longmapsto a.
\]
The surface relator maps to
\[
[a,b][b,a]=[a,b][a,b]^{-1}=1,
\]
so these assignments induce a homomorphism
\[
\varphi:\pi_1(\Sigma_2)\longrightarrow F(a,b).
\]
But
\[
\varphi([a_1,b_1])=[a,b]\ne1,
\]
since the reduced word $aba^{-1}b^{-1}$ is nonempty in the free group.
Hence $[a_1,b_1]\ne1$ in $\pi_1(\Sigma_2)$, so $\gamma$ is not nullhomotopic.

:::

:::

::: {.pf-step #s3}

The curve $\gamma$ is nullhomologous.

::: pf-proof

For any path-connected space, the Hurewicz map identifies
\[
H_1(\Sigma_2;\ZZ)
\cong
\pi_1(\Sigma_2)^{\mathrm{ab}}.
\]
Every commutator maps to $0$ in an abelianization. Explicitly,
\[
[a_1,b_1]
\longmapsto
a_1+b_1-a_1-b_1
=0.
\]
Therefore $[\gamma]=0$ in $H_1(\Sigma_2;\ZZ)$.

:::

:::

::: pf-step

Thus $\gamma$ is a closed curve on a surface which is not nullhomotopic but is nullhomologous.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
