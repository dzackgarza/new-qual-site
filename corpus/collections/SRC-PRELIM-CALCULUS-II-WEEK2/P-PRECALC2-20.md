---
schema: qual/card@1
id: P-PRECALC2-20
kind: problem
title: Convergence of $\sum_n 1/(3\sqrt{3}\sqrt[3]{3}\cdots\sqrt[n]{3})$
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
  note: Retranscribed the garbled series of Problem 20 on page 7 of Week2_solns.pdf, restoring the cube and n-th roots, and added a remark on the source's plus signs in the general denominator.
---

::: {.problem}
Does the series
\[
\frac{1}{3} + \frac{1}{3\sqrt{3}} + \frac{1}{3\sqrt{3}\sqrt[3]{3}} + \cdots + \frac{1}{3\sqrt{3}\sqrt[3]{3} + \cdots + \sqrt[n]{3}} + \cdots
\]
converge or diverge?
:::

::: {.remark}
The general denominator in the source is printed as $3\sqrt{3}\sqrt[3]{3} + \cdots + \sqrt[n]{3}$, with plus signs; the pattern of the first three terms and the source's solution, which writes the series as $\sum_{n=1}^{\infty} 3^{-H_n}$ with $H_n = \sum_{k=1}^{n} \frac{1}{k}$, show that the intended $n$-th denominator is the product $3\sqrt{3}\sqrt[3]{3}\cdots\sqrt[n]{3}$.
:::

::: {.solution}
Let
\[
H_n=\sum_{k=1}^{n}\frac1k.
\]

<1>1. The intended \(n\)th denominator is
\[
3\sqrt3\sqrt[3]3\cdots\sqrt[n]3.
\]

::: {.proof}
The first displayed terms show a product pattern, and the source solution
rewrites the denominator as \(3^{H_n}\). This agrees with the remark already
recorded on the card.
:::

<1>2. Therefore the \(n\)th term is
\[
\boxed{
a_n
=
\frac1{3^{H_n}}}.
\]

::: {.proof}
Each factor satisfies
\[
\sqrt[k]3
=
3^{1/k}.
\]
Hence
\[
3\sqrt3\sqrt[3]3\cdots\sqrt[n]3
=
3^{1+1/2+\cdots+1/n}
=
3^{H_n}.
\]
:::

<1>3. For every \(n\ge1\),
\[
\boxed{
H_n\ge\int_1^{n+1}\frac{dx}{x}
=
\log(n+1)}.
\]

::: {.proof}
The function
\[
x\mapsto\frac1x
\]
is decreasing. Hence for each integer \(k\ge1\),
\[
\frac1k
\ge
\int_k^{k+1}\frac{dx}{x}.
\]
Summing from \(k=1\) to \(n\) gives the result.
:::

<1>4. Since \(3>1\), step <1>3 implies
\[
3^{H_n}
\ge
3^{\log(n+1)}.
\]

::: {.proof}
The function \(x\mapsto3^x\) is increasing.
:::

<1>5. One has
\[
\boxed{
3^{\log(n+1)}
=
(n+1)^{\log3}}.
\]

::: {.proof}
Using \(a^b=e^{b\log a}\),
\[
3^{\log(n+1)}
=
e^{(\log3)(\log(n+1))}
=
(n+1)^{\log3}.
\]
:::

<1>6. Therefore
\[
\boxed{
a_n
\le
\frac1{(n+1)^{\log3}}}.
\]

::: {.proof}
Combine steps <1>2, <1>4, and <1>5, then take reciprocals.
:::

<1>7. The exponent satisfies
\[
\boxed{\log3>1}.
\]

::: {.proof}
Since
\[
3>e,
\]
taking logarithms gives
\[
\log3>\log e=1.
\]
:::

<1>8. Hence
\[
\sum_{n=1}^{\infty}
\frac1{(n+1)^{\log3}}
\]
converges.

::: {.proof}
This is a \(p\)-series with
\[
p=\log3>1
\]
by step <1>7.
:::

<1>9. Therefore the original series
\[
\boxed{
\sum_{n=1}^{\infty}
\frac1{3^{H_n}}
}
\]
converges.

::: {.proof}
The terms are nonnegative, and step <1>6 bounds them above by the terms of
the convergent series in step <1>8. Apply the comparison test.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 gives the requested convergence decision.
:::
:::
