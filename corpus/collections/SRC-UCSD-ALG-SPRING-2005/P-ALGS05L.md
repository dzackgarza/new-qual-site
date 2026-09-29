---
schema: qual/card@1
id: P-ALGS05L
kind: problem
title: "Statement and proof of the Hilbert Basis Theorem"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
State and prove the Hilbert Basis Theorem.
:::

::: {.solution}
**Goal.** State and prove the Hilbert Basis Theorem.

::: pf

::: pf-step
Statement: if $R$ is a Noetherian ring, then $R[x]$ is Noetherian.

::: pf-proof
this is the Hilbert Basis Theorem.
:::

:::

::: {.pf-step #s2}
Proof.

::: pf-proof

::: pf-step
Let $I \subseteq R[x]$ be an ideal; we show $I$ is finitely generated.

::: pf-proof
it suffices to show every ideal of $R[x]$ is finitely generated.
:::

:::

::: pf-step
For each $d \ge 0$, let $L_d \subseteq R$ be the set of leading coefficients of polynomials in $I$ of degree $d$, together with $0$.

::: pf-proof
define the ideal of leading coefficients.
:::

:::

::: pf-step
$L_d$ is an ideal of $R$.

::: pf-proof
the leading coefficients are closed under addition and multiplication by $R$ (multiply a polynomial by a constant, or add two polynomials of the same degree).
:::

:::

::: pf-step
$L_0 \subseteq L_1 \subseteq L_2 \subseteq \cdots$ is an ascending chain.

::: pf-proof
if $a$ is the leading coefficient of a degree-$d$ polynomial $p \in I$, then $xp \in I$ has degree $d+1$ and leading coefficient $a$, so $L_d \subseteq L_{d+1}$.
:::

:::

::: pf-step
Since $R$ is Noetherian, the chain stabilizes: $L_d = L_N$ for all $d \ge N$.

::: pf-proof
the ascending chain condition on ideals of $R$.
:::

:::

::: pf-step
Each $L_d$ ($d \le N$) is finitely generated, say by $a_{d,1}, \dots, a_{d,m_d}$.

::: pf-proof
$R$ is Noetherian, so each ideal $L_d$ is finitely generated.
:::

:::

::: pf-step
Choose polynomials $p_{d,j} \in I$ of degree $d$ with leading coefficient $a_{d,j}$.

::: pf-proof
by definition of $L_d$.
:::

:::

::: {.pf-step #s2-8}
The finite set $\theset{p_{d,j} : 0 \le d \le N, 1 \le j \le m_d}$ generates $I$.

::: pf-proof
given $p \in I$ of degree $d$, induct on $d$: if $d \le N$, subtract an $R[x]$-linear combination of the $p_{d,j}$ to reduce the leading coefficient to $0$ (lowering the degree); if $d > N$, use $L_d = L_N$ to reduce the leading coefficient using the degree-$N$ generators, lowering the degree; induction terminates.
:::

:::

::: pf-step
Hence $I$ is finitely generated, so $R[x]$ is Noetherian.

::: pf-proof
step [](#s2-8){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
step [](#s2){.pf-ref} proves the theorem.
:::

:::
:::
