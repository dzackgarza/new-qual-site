---
schema: qual/card@1
id: P-PRACT20-W3-08
kind: problem
title: Maclaurin series of $f(x)/(1-x)$
classification:
  areas:
  - prelim
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 3 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the Maclaurin series of f(x) divided by (1-x) under the same hypothesis of convergence on (-1,1), and the printed solution gives the same answer
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's coefficient recurrence is transcribed and solved by induction, with the convergence clause stated.
---

::: {.problem}
Assume that $f(x) = \sum_{n=0}^{\infty} a_{n} x^{n}$ converges on $(-1, 1)$. Find the Maclaurin series for $g(x) = f(x)/(1 - x)$.
:::

::: {.solution}

Let $f(x)=\sum_{n\ge0}a_nx^n$ converge on $(-1,1)$ and let $g(x)=f(x)/(1-x)$;
seek $g(x)=\sum_{n\ge0}b_nx^n$.

::: pf

::: {.pf-step #recurrence}

The coefficients satisfy $b_0=a_0$ and $b_n=a_n+b_{n-1}$ for $n\ge1$, hence
$b_n=a_0+a_1+\cdots+a_n$.

::: pf-proof

$(1-x)\sum_{n\ge0}b_nx^n=b_0+\sum_{n\ge1}(b_n-b_{n-1})x^n$ by collecting the
coefficient of $x^n$, which is $b_n-b_{n-1}$ for $n\ge1$. Equating with $\sum
a_nx^n$ coefficient by coefficient, legitimate since both sides are power
series converging on a common interval, gives $b_0=a_0$ and $b_n-b_{n-1}=a_n$.
Induction then gives $b_n=a_0+\cdots+a_n$: the base is $b_0=a_0$, and
$b_n=a_n+b_{n-1}=a_n+a_0+\cdots+a_{n-1}$.

:::

:::

::: {.pf-step #convergence}

$\displaystyle\sum_{n\ge0}\Big(\sum_{k=0}^na_k\Big)x^n$ converges on $(-1,1)$,
and its sum is $g(x)$.

::: pf-proof

For $\abs x<1$ and $N$ fixed the partial sums are bounded by $\sum_{k\le
N}\abs{a_k}$, and $\sum_k\abs{a_k}r^k<\infty$ for each $r<1$ inside the
interval of convergence; the standard summability of $\frac{1}{1-x}$ then
gives convergence of the coefficientwise-cumulative series on $(-1,1)$, which
the printed solution asserts and which follows, for instance, from the product
formula for power series. Its sum is $(1-x)^{-1}f(x)=g(x)$ by step
[](#recurrence){.pf-ref}.

:::

:::

::: {.pf-step #series}

$\boxed{g(x)=\displaystyle\sum_{n\ge0}\Big(\sum_{k=0}^na_k\Big)x^n}$ on
$(-1,1)$.

::: pf-proof

Steps [](#recurrence){.pf-ref} and [](#convergence){.pf-ref} identify the
coefficients of the Maclaurin series of $g$ as the running sums of those of
$f$, and give its convergence on the same interval. The printed solution
states the same conclusion and adds the general Cauchy product formula, by
which a product of two power series convergent on a common interval has
coefficients $\sum_{k=0}^nc_kd_{n-k}$, the case at hand being $c_n=a_n$ and
$d_n=1$.

:::

:::

:::


:::
