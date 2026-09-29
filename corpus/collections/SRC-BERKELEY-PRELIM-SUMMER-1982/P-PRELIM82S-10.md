---
schema: qual/card@1
id: P-PRELIM82S-10
kind: problem
title: Limsup growth of a finite sum of complex power sequences
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    After normalizing by the largest modulus, the upper bound is immediate.
    Grouping equal unit-modulus terms gives a finite exponential sum whose
    Cesàro mean square tends to the positive sum of the squared
    multiplicities. Hence that sum is bounded away from zero infinitely
    often, while all smaller-modulus terms tend to zero. This yields the
    matching lower limsup bound.
---

::: {.problem}
For complex numbers $\alpha_1,\ldots,\alpha_k$, prove that
\[
\limsup_{n\to\infty}
\left|\sum_{j=1}^k\alpha_j^n\right|^{1/n}
=\max_{1\le j\le k}|\alpha_j|.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Put
$$
R=\max_{1\leq j\leq k}\abs{\alpha_j}.
$$
If $R=0$, then the asserted identity holds.

::: pf-proof

If $R=0$, then every $\alpha_j=0$. Hence
$$
\sum_{j=1}^k\alpha_j^n=0
$$
for every $n\geq1$, so both sides of the required identity are zero.

:::

:::

::: {.pf-step #s2}

Assume henceforth that $R>0$ and define
$$
\beta_j=\frac{\alpha_j}{R}
\qquad
(1\leq j\leq k).
$$
Then
$$
\max_j\abs{\beta_j}=1.
$$

::: pf-proof

By the definition of $R$,
$$
\abs{\beta_j}
=
\frac{\abs{\alpha_j}}{R}
\leq1
$$
for every $j$, and equality holds for at least one $j$.

:::

:::

::: {.pf-step #s3}

One has
$$
\limsup_{n\to\infty}
\abs{\sum_{j=1}^k\beta_j^n}^{1/n}
\leq1.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\abs{\sum_{j=1}^k\beta_j^n}
\leq
\sum_{j=1}^k\abs{\beta_j}^n
\leq k.
$$
Therefore
$$
\abs{\sum_{j=1}^k\beta_j^n}^{1/n}
\leq k^{1/n},
$$
and $k^{1/n}\to1$.

:::

:::

::: {.pf-step #s4}

Let $\zeta_1,\ldots,\zeta_m$ be the distinct values among the
$\beta_j$ satisfying $\abs{\beta_j}=1$, and let $c_r$ be the multiplicity
of $\zeta_r$. Define
$$
S_n=\sum_{r=1}^m c_r\zeta_r^n.
$$
Then
$$
\lim_{N\to\infty}
\frac1N\sum_{n=1}^N\abs{S_n}^2
=
\sum_{r=1}^m c_r^2
>0.
$$

::: pf-proof

::: {.pf-step #s4-1}

For $r\neq s$,
$$
\lim_{N\to\infty}
\frac1N\sum_{n=1}^N
(\zeta_r\overline{\zeta_s})^n
=0.
$$

::: pf-proof

Since the $\zeta_r$ are distinct and have modulus one,
$$
q=\zeta_r\overline{\zeta_s}
$$
satisfies $\abs{q}=1$ and $q\neq1$. Thus
$$
\frac1N\sum_{n=1}^Nq^n
=
\frac{q(1-q^N)}{N(1-q)},
$$
whose modulus is at most
$$
\frac{2}{N\abs{1-q}}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s4-2}

The asserted mean-square limit holds.

::: pf-proof

Expanding the square gives
$$
\frac1N\sum_{n=1}^N\abs{S_n}^2
=
\sum_{r,s=1}^m
c_r c_s
\left(
\frac1N\sum_{n=1}^N
(\zeta_r\overline{\zeta_s})^n
\right).
$$
For $r=s$, the parenthesized average equals $1$. For $r\neq s$, it tends
to zero by step [](#s4-1){.pf-ref}. Hence the limit is
$$
\sum_{r=1}^m c_r^2.
$$
This number is positive because step [](#s2){.pf-ref} ensures that at least one
$\beta_j$ has modulus one, so $m\geq1$.

:::

:::

::: pf-qed

Step [](#s4-2){.pf-ref} proves the claim of step [](#s4){.pf-ref}.

:::

:::

:::

::: {.pf-step #s5}

There is a constant $\delta>0$ such that
$$
\abs{S_n}\geq2\delta
$$
for infinitely many positive integers $n$.

::: pf-proof

Set
$$
A=\sum_{r=1}^m c_r^2>0.
$$
By step [](#s4){.pf-ref},
$$
\frac1N\sum_{n=1}^N\abs{S_n}^2\longrightarrow A.
$$
If $\abs{S_n}<\sqrt{A/2}$ for all sufficiently large $n$, then the
Cesàro means of $\abs{S_n}^2$ would have limsup at most $A/2$, a
contradiction. Thus
$$
\abs{S_n}\geq\sqrt{A/2}
$$
for infinitely many $n$. Taking
$$
\delta=\frac12\sqrt{A/2}
$$
gives the claim.

:::

:::

::: {.pf-step #s6}

If
$$
T_n
=
\sum_{\abs{\beta_j}<1}\beta_j^n,
$$
then $T_n\to0$.

::: pf-proof

The sum is finite, and each summand tends to zero because its base has
modulus strictly smaller than one. Hence their sum tends to zero.

:::

:::

::: {.pf-step #s7}

For infinitely many $n$,
$$
\abs{\sum_{j=1}^k\beta_j^n}\geq\delta.
$$

::: pf-proof

By grouping the terms of modulus one according to equal values,
$$
\sum_{j=1}^k\beta_j^n=S_n+T_n.
$$
Step [](#s5){.pf-ref} gives infinitely many $n$ with $\abs{S_n}\geq2\delta$, while
step [](#s6){.pf-ref} gives $\abs{T_n}<\delta$ for all sufficiently large $n$.
Therefore infinitely many of the indices from step [](#s5){.pf-ref} also satisfy
$$
\abs{S_n+T_n}
\geq
\abs{S_n}-\abs{T_n}
\geq\delta.
$$

:::

:::

::: {.pf-step #s8}

One has
$$
\limsup_{n\to\infty}
\abs{\sum_{j=1}^k\beta_j^n}^{1/n}
\geq1.
$$

::: pf-proof

Along the infinite subsequence from step [](#s7){.pf-ref},
$$
\abs{\sum_{j=1}^k\beta_j^n}^{1/n}
\geq
\delta^{1/n}.
$$
Since $\delta^{1/n}\to1$, the limsup is at least $1$.

:::

:::

::: {.pf-step #s9}

Therefore
$$
\limsup_{n\to\infty}
\abs{\sum_{j=1}^k\beta_j^n}^{1/n}
=1.
$$

::: pf-proof

The upper bound is step [](#s3){.pf-ref} and the lower bound is step [](#s8){.pf-ref}.

:::

:::

::: {.pf-step #s10}

The required value is
$$
\boxed{
\limsup_{n\to\infty}
\abs{\sum_{j=1}^k\alpha_j^n}^{1/n}
=
\max_{1\leq j\leq k}\abs{\alpha_j}
}.
$$

::: pf-proof

For $R>0$, step [](#s2){.pf-ref} gives
$$
\sum_{j=1}^k\alpha_j^n
=
R^n\sum_{j=1}^k\beta_j^n.
$$
Hence
$$
\abs{\sum_{j=1}^k\alpha_j^n}^{1/n}
=
R\abs{\sum_{j=1}^k\beta_j^n}^{1/n}.
$$
Taking limsups and using step [](#s9){.pf-ref} yields the stated equality. The case
$R=0$ was proved in step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s10){.pf-ref} is the desired identity.

:::

:::

:::
