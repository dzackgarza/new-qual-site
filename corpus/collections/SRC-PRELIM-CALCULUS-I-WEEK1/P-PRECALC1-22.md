---
schema: qual/card@1
id: P-PRECALC1-22
kind: problem
title: Limit of $\sum_{k=n+1}^{2n}\frac1k$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the limit of Problem 22 on page 5 of Week1_solns.pdf.
---

::: {.problem}
Calculate $\displaystyle\lim_{n \to \infty} \sum_{k=n+1}^{2n} \frac{1}{k}$.
:::

::: {.solution}
<1>1. Reindex the sum by writing
\[
k=n+j,
\qquad
1\le j\le n.
\]

::: {.proof}
As \(k\) runs from \(n+1\) to \(2n\), the integer \(j=k-n\) runs from
\(1\) to \(n\).
:::

<1>2. Then
\[
\sum_{k=n+1}^{2n}\frac1k
=
\sum_{j=1}^{n}\frac1{n+j}.
\]

::: {.proof}
Substitute \(k=n+j\).
:::

<1>3. Factor \(n\) from each denominator:
\[
\boxed{
\sum_{k=n+1}^{2n}\frac1k
=
\frac1n
\sum_{j=1}^{n}
\frac1{1+j/n}}.
\]

::: {.proof}
\[
\frac1{n+j}
=
\frac1n
\frac1{1+j/n}.
\]
:::

<1>4. The expression in step <1>3 is the right-endpoint Riemann sum for
\[
f(x)=\frac1{1+x}
\]
on \([0,1]\).

::: {.proof}
The interval width is
\[
\Delta x=\frac1n,
\]
and the right endpoints are
\[
x_j=\frac jn.
\]
Thus
\[
\frac1n
\sum_{j=1}^{n}
f(j/n)
\]
is exactly the right-endpoint Riemann sum.
:::

<1>5. Since \(f\) is continuous on \([0,1]\),
\[
\lim_{n\to\infty}
\frac1n
\sum_{j=1}^{n}
\frac1{1+j/n}
=
\int_0^1\frac{dx}{1+x}.
\]

::: {.proof}
Riemann sums of a continuous function converge to its definite integral.
:::

<1>6. Evaluate the integral:
\[
\int_0^1\frac{dx}{1+x}
=
\left[
\log(1+x)
\right]_0^1.
\]

::: {.proof}
An antiderivative of \(1/(1+x)\) is \(\log(1+x)\).
:::

<1>7. Therefore
\[
\boxed{
\int_0^1\frac{dx}{1+x}
=
\log2}.
\]

::: {.proof}
\[
\log2-\log1
=
\log2.
\]
:::

<1>8. Hence
\[
\boxed{
\lim_{n\to\infty}
\sum_{k=n+1}^{2n}\frac1k
=
\log2}.
\]

::: {.proof}
Combine steps <1>3--<1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested limit.
:::
:::
