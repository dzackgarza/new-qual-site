---
schema: qual/card@1
id: P-UGA-CA-SPRING-2005-4
kind: problem
title: Laurent expansions of $z/(1-z^2)$ about one and infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read complex-analysis Problem 4 in the checked-in extraction of the combined January 2005 exam.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The statement of the Laurent theorem is a step with
    the coefficient formula and the uniqueness, and the two expansions are computed rather than quoted: the
    substitution $w=z-1$ with the partial-fraction split in the first annulus, and the geometric series in
    $1/z^2$ in the second. Both expansions were checked numerically against the closed form at $z=1.5$ and
    $z=2$. Not checked: the examination paper, which the collection retains as a problem file only; the
    statement is as transcribed on the card. No retained solution set covers the problem, so the argument is
    the card's own. No statement repair.
---

::: {.problem}
State the Laurent-series existence theorem.
Find the Laurent series of
$z/(1-z^2)$ on $0<\abs{z-1}<1$
and on $1<\abs{z}<\infty$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's provenance is the examination paper alone, so the argument is the card's own.

::: pf

::: {.pf-step #theorem}
If $f$ is holomorphic on the annulus $r<\abs{z-a}<R$, it has a Laurent expansion $f(z)=\sum_{n\in\ZZ}c_n(z-a)^n$ converging there, with
$$
c_n=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=\rho}\frac{f(\zeta)}{(\zeta-a)^{n+1}}d\zeta
$$
for any $\rho$ with $r<\rho<R$, and the coefficients are unique.

::: pf-proof
This is the Laurent expansion theorem: the coefficients given by the integral converge and the series equals $f$ on the annulus, by the Cauchy integral formula applied on a circle $\abs{\zeta-a}=\rho$ and expansion of the kernel $\frac{1}{\zeta-z}$ in powers of $\frac{z-a}{\zeta-a}$ on the two sides of $\abs{z-a}=\rho$. Uniqueness: two expansions with the same sum differ by a Laurent series vanishing identically, and multiplying by $(\zeta-a)^{-n-1}$ and integrating termwise over a circle isolates each coefficient.
:::

:::

::: {.pf-step #first}
On $0<\abs{z-1}<1$,
$$
\frac{z}{1-z^2}=-\frac{1}{2(z-1)}-\sum_{n\ge0}\frac{(-1)^n}{2^{n+2}}(z-1)^n .
$$

::: pf-proof
Put $w=z-1$, so $z=1+w$ and $1-z^2=1-(1+w)^2=-w(2+w)$. Then
$$
\frac{z}{1-z^2}=\frac{1+w}{-w(2+w)}=-\frac{1+w}{w(2+w)},
$$
and the partial-fraction identity $\frac{1+w}{w(2+w)}=\frac{1}{2w}+\frac{1}{2(2+w)}$ holds because $\frac{1}{2}(2+w)+\frac{1}{2}w=1+w$. Hence
$$
\frac{z}{1-z^2}=-\frac{1}{2w}-\frac{1}{4}\cdot\frac{1}{1+w/2},
$$
and for $0<\abs{w}<1$ the geometric series $\frac{1}{1+w/2}=\sum_{n\ge0}(-1)^n(w/2)^n$ converges, giving the display after substituting back $w=z-1$. This is a Laurent series in the annulus $0<\abs{z-1}<1$ with principal part $-\frac{1}{2(z-1)}$, a simple pole at $z=1$.
:::

:::

::: {.pf-step #second}
On $1<\abs{z}<\infty$,
$$
\frac{z}{1-z^2}=-\sum_{n\ge0}z^{-2n-1}.
$$

::: pf-proof
For $\abs{z}>1$ write
$$
\frac{z}{1-z^2}=-\frac{z}{z^2-1}=-\frac{1}{z}\cdot\frac{1}{1-z^{-2}}=-\frac1z\sum_{n\ge0}z^{-2n},
$$
the geometric series converging because $\abs{z^{-2}}<1$. Multiplying out gives $-\sum_{n\ge0}z^{-2n-1}$, a Laurent series on the annulus $1<\abs{z}<\infty$ with only negative powers. As a check, at $z=2$ the series is $-\frac12(1+\frac14+\frac1{16}+\cdots)=-\frac{2}{3}$, which equals $\frac{2}{1-4}$.
:::

:::

:::

:::
