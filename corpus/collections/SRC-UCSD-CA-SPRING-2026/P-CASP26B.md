---
schema: qual/card@1
id: P-CASP26B
kind: problem
title: '$\abs{f(1/45)}<1$ for an even holomorphic $f$ on $\DD$ with $f(0)=0$ and $\abs f<2000$'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. f even and f(0) = 0 give a zero of order at least 2 at 0, so
    f = z^2 g with g holomorphic on the disc; on each circle |z| = r the bound |f| < 2000 gives
    |g| < 2000/r^2, and the maximum principle on the disc of radius r then passes |g| <= 2000 to the
    limit, including at 0. Hence |f(1/45)| = (1/45)^2 |g(1/45)| <= 2000/2025 < 1. Checked that the
    evenness is what produces the double zero (f' odd, so f'(0) = 0) and that no Schwarz lemma is
    needed: the estimate is immediate from the factorisation, which is what the closing step says.
---

::: {.problem}
Let $f : \DD \to \CC$ be holomorphic such that

(i) $f(0) = 0$;

(ii) $\abs{f(z)} < 2000$ for all $z \in \DD$;

(iii) $f(z) = f(-z)$ for all $z \in \DD$.

Prove that $\abs{f\bigl(\frac{1}{45}\bigr)} < 1$.
:::

::: {.solution}
::: pf

::: {.pf-step #factor}
$f(z)=z^2g(z)$ for a holomorphic $g$ on $\DD$.

::: pf-proof
Write $f(z)=\sum_{n\ge0}a_nz^n$ on $\DD$. By (i), $a_0=0$. By (iii) and uniqueness of the power series, $a_n=0$ for every odd $n$, so $a_1=0$. Take $g(z)=\sum_{k\ge0}a_{2k+2}z^{2k}$.
:::

:::

::: {.pf-step #bound}
$\abs{g}\le2000$ on $\DD$.

::: pf-proof
Fix $z\in\DD$ and $\abs{z}<r<1$. By (ii), $\abs{g(w)}=\abs{f(w)}/r^2<2000/r^2$ for $\abs{w}=r$. The maximum modulus principle on $\overline{B(0,r)}$ gives $\abs{g(z)}\le2000/r^2$. Let $r\to1$.
:::

:::

::: pf-qed
By steps [](#factor){.pf-ref} and [](#bound){.pf-ref}, $\abs{f(1/45)}\le2000/45^2=2000/2025<1$.
:::

:::
:::
