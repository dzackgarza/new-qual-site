---
schema: qual/card@1
id: P-6T7VU
kind: problem
title: Invariant factors of $R/(r)\oplus R/(s)$ over a PID
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Principal Ideal Domains
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
Let $R$ be a Principal Ideal Domain (PID), and let $r, s \in R \setminus \{0\}$ be non-zero elements.
Determine the **invariant factors** of the $R$-module:
$$M = R/(r) \oplus R/(s).$$
:::

::: {.solution}

Write $d=\gcd(r,s)$ and $l=\lcm(r,s)$, each defined up to a unit.

::: pf

::: {.pf-step #snf}
$M$ has presentation matrix $A=\begin{pmatrix}r&0\\0&s\end{pmatrix}$, whose Smith normal form is $\operatorname{diag}(d_1,d_2)$ with $d_1\mid d_2$, $d_1\sim\Delta_1$ and $d_1d_2\sim\Delta_2$, where $\Delta_k$ is the gcd of the $k\times k$ minors of $A$.

::: pf-proof
The relations $r\cdot e_1=0$ and $s\cdot e_2=0$ on the generators $e_1,e_2$ of $M$ give the presentation matrix $A$. Over a PID, the determinantal divisors $\Delta_k$ are invariant under invertible row and column operations, and for the diagonal Smith form $\operatorname{diag}(d_1,d_2)$ they are $d_1$ and $d_1d_2$.
:::

:::

::: {.pf-step #diag}
$d_1\sim d$ and $d_2\sim l$, so $M\cong R/(d)\oplus R/(l)$.

::: pf-proof
The $1\times1$ minors of $A$ are $r$, $s$ and $0$, so $\Delta_1\sim d$. The only $2\times2$ minor is $rs$, so $\Delta_2\sim rs$. Step [](#snf){.pf-ref} gives $d_1\sim d$ and $d_2\sim rs/d\sim l$, and $M\cong R/(d_1)\oplus R/(d_2)$.
:::

:::

::: pf-qed
The invariant factors are the non-unit diagonal entries of the Smith form, because a summand $R/(u)$ with $u$ a unit is zero. By step [](#diag){.pf-ref}, the invariant factors of $M$ are
$$
\boxed{d=\gcd(r,s)\ \text{and}\ l=\lcm(r,s)}
$$
up to units, where $d$ is omitted when $r$ and $s$ are coprime, and $l$ is also omitted when $r$ and $s$ are both units, in which case $M=0$.
:::

:::

:::
