---
schema: qual/card@1
id: P-MIOKF
kind: problem
title: Proper subfields of $\CC$ isomorphic to $\CC$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Transcendence
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Can it happen that a proper subfield of $\CC$ is isomorphic to $\CC$?
How?
:::

::: {.solution}
Choose a transcendence basis $B$ of $\CC/\QQ$, so $\abs{B}=\trdeg_{\QQ}\CC=2^{\aleph_0}$. Fix $t\in B$, put $B_0=B\setminus\{t\}$, and let $K$ be the algebraic closure of $\QQ(B_0)$ in $\CC$, that is, the set of elements of $\CC$ algebraic over $\QQ(B_0)$.

::: pf

::: {.pf-step #proper}
$K$ is a proper subfield of $\CC$.

::: pf-proof
The element $t$ is transcendental over $\QQ(B_0)$ because $B$ is algebraically independent, so $t\notin K$.
:::

:::

::: {.pf-step #closed}
$K$ is algebraically closed of characteristic $0$ with $\trdeg_{\QQ}K=\trdeg_{\QQ}\CC$.

::: pf-proof
A root in $\CC$ of a polynomial over $K$ is algebraic over $K$, hence over $\QQ(B_0)$, so it lies in $K$; since $\CC$ is algebraically closed, $K$ is algebraically closed.
The set $B_0$ is a transcendence basis of $K/\QQ$, and $\abs{B_0}=\abs{B}$ because $B$ is infinite.
:::

:::

::: pf-step
$\boxed{\text{Yes}}$: $K\cong\CC$, so $K$ is a proper subfield of $\CC$ isomorphic to $\CC$.

::: pf-proof
Algebraically closed fields of the same characteristic and the same transcendence degree over the prime field are isomorphic: a bijection $B\to B_0$ extends to an isomorphism $\QQ(B)\to\QQ(B_0)$ and then to an isomorphism of their algebraic closures $\CC\to K$.
By steps [](#proper){.pf-ref} and [](#closed){.pf-ref}, this gives an injective but non-surjective field endomorphism of $\CC$.
:::

:::

:::

:::
