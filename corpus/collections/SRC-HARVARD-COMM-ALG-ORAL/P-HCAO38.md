---
schema: qual/card@1
id: P-HCAO38
kind: problem
title: Nakayama's lemma and an example
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Jacobson Radical
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
State Nakayama's lemma.
Give an example of a ring and a nonzero ideal which satisfy its hypotheses.
:::

::: {.solution}
One standard form of Nakayama's lemma is the following.

::: pf

::: {.pf-step #nakayama-im-equals-m}
Let $R$ be a commutative ring, let $M$ be a finitely generated
$R$-module, and let $I\subseteq\operatorname{Jac}(R)$. If
\[
IM=M,
\]
then $M=0$.

::: pf-proof
Choose a minimal generating set $m_1,\ldots,m_r$ for $M$. If $r>0$, the
equality $IM=M$ gives
\[
m_r=a_1m_1+\cdots+a_rm_r
\]
with each $a_i\in I$. Thus
\[
(1-a_r)m_r=a_1m_1+\cdots+a_{r-1}m_{r-1}.
\]
Since $a_r\in\operatorname{Jac}(R)$, $1-a_r$ is a unit. Hence $m_r$ lies in
the span of the preceding generators, contradicting minimality. Therefore
$r=0$ and $M=0$.
:::

:::

::: pf-step
Equivalently, if $N\subseteq M$ and
\[
M=N+IM,
\]
with $M$ finitely generated and $I\subseteq\operatorname{Jac}(R)$, then
$M=N$.

::: pf-proof
Apply step [](#nakayama-im-equals-m){.pf-ref} to the finitely generated quotient $M/N$.
:::

:::

::: pf-step
A concrete nonzero ideal satisfying the hypotheses is
\[
I=(x)\subset R=k[x]_{(x)}.
\]

::: pf-proof
The localization $R=k[x]_{(x)}$ is a local ring with maximal ideal $(x)$.
For every local ring, its maximal ideal is the Jacobson radical. Thus the
nonzero ideal $I=(x)$ lies in $\operatorname{Jac}(R)$, as required in
Nakayama's lemma.
:::

:::

:::
:::
