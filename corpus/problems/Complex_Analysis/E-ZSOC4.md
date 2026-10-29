---
schema: qual/card@1
id: E-ZSOC4
kind: problem
title: A Blaschke factor is an involution
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Let psi_a be a Blaschke factor" without defining it; the statement defines psi_a(z) = (a-z)/(1-conj(a) z) for a in the unit disc, the factor the solution uses.'
---

::: {.exercise}
For $a\in\DD$, let $\psi_a(z) \coloneqq \dfrac{a-z}{1-\bar a z}$ be a Blaschke factor.
Use the Schwarz lemma to prove that $\psi_a \circ \psi_a = \id_\DD$.
:::

::: {.solution}

::: pf

::: {.pf-step #maps-disc}
$\psi_a$ is holomorphic on a neighborhood of $\overline{\DD}$ and maps $\DD$ into $\DD$.

::: pf-proof
The only pole of $\psi_a$ is $1/\bar a$, which lies outside $\overline{\DD}$ because $\abs{a}<1$ (there is no pole when $a=0$).
For $\abs{z}=1$, $\abs{1-\bar a z} = \abs{z}\,\abs{\bar z-\bar a} = \abs{\overline{z-a}} = \abs{a-z}$, so $\abs{\psi_a(z)}=1$.
Since $\psi_a$ is not constant, the maximum modulus principle gives $\abs{\psi_a}<1$ on $\DD$.
:::

:::

::: pf-step
$\psi_a\circ\psi_a = \id_\DD$.

::: pf-proof
Let $g \coloneqq \psi_a\circ\psi_a$.
By step [](#maps-disc){.pf-ref}, $g$ is a holomorphic map $\DD\to\DD$, and $g(0)=\psi_a(a)=0$.
If $a=0$, then $\psi_0(z)=-z$ and $g=\id_\DD$.
If $a\neq 0$, then $g(a)=\psi_a(0)=a$, so $\abs{g(a)}=\abs{a}$ at a point $a\neq 0$, and the equality case of the Schwarz lemma gives $g(z)=\lambda z$ for some $\abs{\lambda}=1$.
Then $a=g(a)=\lambda a$ forces $\lambda=1$.
:::

:::

:::

:::
