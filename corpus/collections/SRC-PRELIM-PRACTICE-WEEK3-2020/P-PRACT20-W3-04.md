---
schema: qual/card@1
id: P-PRACT20-W3-04
kind: problem
title: Binomial series for $(1+x)^\alpha$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 1-2 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the Taylor series of (1+x)^alpha at 0 for real alpha, which is what the card asks
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's computation of the k-th derivative and the resulting series with the product of the falling factorials is transcribed, with the radius of convergence and the polynomial case noted as on the printed page.
---

::: {.problem}
Let $\alpha \in \RR$. Find the Taylor Series for $(1 + x)^{\alpha}$ around $x = 0$.
:::

::: {.solution}

Let $\alpha\in\RR$ and $f(x)=(1+x)^\alpha$, taken on $(-1,1)$.

::: pf

::: {.pf-step #derivatives}

$f^{(k)}(x)=\alpha(\alpha-1)\cdots(\alpha-(k-1))(1+x)^{\alpha-k}$ for every
$k\ge1$, and $f^{(k)}(0)=\prod_{\ell=0}^{k-1}(\alpha-\ell)$.

::: pf-proof

Induction on $k$: for $k=1$ the power rule gives $\alpha(1+x)^{\alpha-1}$. If
the formula holds for $k$ then differentiating gives $k$ more factors
$\alpha-(k-1)$ and the exponent decreases by one, giving the formula for
$k+1$. Evaluating at $0$ uses $(1+0)^{\alpha-k}=1$; for $k=0$ the empty
product is $1$, giving $f(0)=1$.

:::

:::

::: {.pf-step #series}

$\boxed{(1+x)^\alpha=\sum_{k\ge0}\Big(\prod_{\ell=0}^{k-1}(\alpha-\ell)\Big)\frac{x^k}{k!}}$
for $\abs x<1$.

::: pf-proof

The Taylor series at $0$ is $\sum_k\frac{f^{(k)}(0)}{k!}x^k$, which by step
[](#derivatives){.pf-ref} is the displayed series. It converges for $\abs
x<1$, either by the ratio test on the coefficients
$\frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$, whose ratio tends to $1$, or
by the binomial theorem for real exponents; inside that interval the sum
equals $(1+x)^\alpha$, and the identity extends the polynomial case. If
$\alpha\in\NN$ the factors vanish for $k>\alpha$ and the series is the finite
binomial expansion, matching the remark in the printed solution.

:::

:::

:::


:::
