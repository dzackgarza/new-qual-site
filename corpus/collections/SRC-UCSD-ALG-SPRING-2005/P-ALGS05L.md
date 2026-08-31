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

::: problem
State and prove the Hilbert Basis Theorem.
:::

::: {.solution}
**Goal.** State and prove the Hilbert Basis Theorem.

<1>1. Statement: if $R$ is a Noetherian ring, then $R[x]$ is Noetherian.
::: {.proof}
this is the Hilbert Basis Theorem.
:::

<1>2. Proof.
<2>1. Let $I \subseteq R[x]$ be an ideal; we show $I$ is finitely generated.
::: {.proof}
it suffices to show every ideal of $R[x]$ is finitely generated.
:::
<2>2. For each $d \ge 0$, let $L_d \subseteq R$ be the set of leading coefficients of polynomials in $I$ of degree $d$, together with $0$.
::: {.proof}
define the ideal of leading coefficients.
:::
<2>3. $L_d$ is an ideal of $R$.
::: {.proof}
the leading coefficients are closed under addition and multiplication by $R$ (multiply a polynomial by a constant, or add two polynomials of the same degree).
:::
<2>4. $L_0 \subseteq L_1 \subseteq L_2 \subseteq \cdots$ is an ascending chain.
::: {.proof}
if $a$ is the leading coefficient of a degree-$d$ polynomial $p \in I$, then $xp \in I$ has degree $d+1$ and leading coefficient $a$, so $L_d \subseteq L_{d+1}$.
:::
<2>5. Since $R$ is Noetherian, the chain stabilizes: $L_d = L_N$ for all $d \ge N$.
::: {.proof}
the ascending chain condition on ideals of $R$.
:::
<2>6. Each $L_d$ ($d \le N$) is finitely generated, say by $a_{d,1}, \dots, a_{d,m_d}$.
::: {.proof}
$R$ is Noetherian, so each ideal $L_d$ is finitely generated.
:::
<2>7. Choose polynomials $p_{d,j} \in I$ of degree $d$ with leading coefficient $a_{d,j}$.
::: {.proof}
by definition of $L_d$.
:::
<2>8. The finite set $\theset{p_{d,j} : 0 \le d \le N, 1 \le j \le m_d}$ generates $I$.
::: {.proof}
given $p \in I$ of degree $d$, induct on $d$: if $d \le N$, subtract an $R[x]$-linear combination of the $p_{d,j}$ to reduce the leading coefficient to $0$ (lowering the degree); if $d > N$, use $L_d = L_N$ to reduce the leading coefficient using the degree-$N$ generators, lowering the degree; induction terminates.
:::
<2>9. Hence $I$ is finitely generated, so $R[x]$ is Noetherian.
::: {.proof}
<1>2.8.
:::

<1>3. Q.E.D.
::: {.proof}
<1>2 proves the theorem.
:::
:::
