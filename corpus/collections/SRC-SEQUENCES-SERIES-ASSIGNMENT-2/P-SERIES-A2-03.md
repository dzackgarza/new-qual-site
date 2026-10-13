---
schema: qual/card@1
id: P-SERIES-A2-03
kind: problem
title: $\limsup$ and $\liminf$ of a recursively defined sequence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the $\limsup$ and $\liminf$ of the sequence $\{a_n\}$ defined recursively by
\[
a_1=0,\qquad a_{2m}=\frac{a_{2m-1}}2,\qquad a_{2m+1}=\frac12+a_{2m}.
\]
Justify your answers with complete proofs.
:::

::: {.solution}
Define the even subsequence
\[
b_m=a_{2m}
\qquad(m\ge1).
\]

<1>1. One has
\[
\boxed{b_1=0}.
\]

::: {.proof}
By the recurrence,
\[
a_2=\frac{a_1}{2}=0.
\]
:::

<1>2. For \(m\ge2\),
\[
a_{2m-1}
=
\frac12+a_{2m-2}.
\]

::: {.proof}
Apply the odd-index recurrence with \(m-1\):
\[
a_{2(m-1)+1}
=
\frac12+a_{2(m-1)}.
\]
:::

<1>3. Therefore
\[
\boxed{
b_m
=
\frac14+\frac12b_{m-1}}
\qquad(m\ge2).
\]

::: {.proof}
Using the even-index recurrence and step <1>2,
\[
\begin{aligned}
b_m
&=
a_{2m}\\
&=
\frac{a_{2m-1}}2\\
&=
\frac12
\left(
\frac12+a_{2m-2}
\right)\\
&=
\frac14+\frac12b_{m-1}.
\end{aligned}
\]
:::

<1>4. The recurrence in step <1>3 can be rewritten as
\[
\boxed{
b_m-\frac12
=
\frac12
\left(
b_{m-1}-\frac12
\right)}.
\]

::: {.proof}
Subtract \(1/2\) from both sides:
\[
\frac14+\frac12b_{m-1}-\frac12
=
\frac12b_{m-1}-\frac14
=
\frac12\left(b_{m-1}-\frac12\right).
\]
:::

<1>5. Iterating,
\[
b_m-\frac12
=
\left(\frac12\right)^{m-1}
\left(
b_1-\frac12
\right).
\]

::: {.proof}
Apply step <1>4 repeatedly from index \(m\) down to index \(1\).
:::

<1>6. Since \(b_1=0\),
\[
\boxed{
a_{2m}
=
b_m
=
\frac12-\frac1{2^m}}.
\]

::: {.proof}
By step <1>5,
\[
b_m-\frac12
=
\left(\frac12\right)^{m-1}
\left(-\frac12\right)
=
-\frac1{2^m}.
\]
:::

<1>7. Hence
\[
\boxed{
a_{2m}\longrightarrow\frac12}.
\]

::: {.proof}
In step <1>6,
\[
2^{-m}\to0.
\]
:::

<1>8. For \(m\ge1\),
\[
a_{2m+1}
=
\frac12+a_{2m}.
\]

::: {.proof}
This is the odd-index recurrence from the problem.
:::

<1>9. Substituting step <1>6,
\[
\boxed{
a_{2m+1}
=
1-\frac1{2^m}}.
\]

::: {.proof}
\[
\frac12+
\left(
\frac12-\frac1{2^m}
\right)
=
1-\frac1{2^m}.
\]
:::

<1>10. Hence
\[
\boxed{
a_{2m+1}\longrightarrow1}.
\]

::: {.proof}
Again
\[
2^{-m}\to0.
\]
:::

<1>11. For every \(m\ge1\),
\[
a_{2m}<\frac12
\]
and
\[
a_{2m+1}<1.
\]

::: {.proof}
Both inequalities follow immediately from the positive correction terms in
steps <1>6 and <1>9.
:::

<1>12. Fix
\[
\varepsilon>0.
\]
There exists \(M_1\) such that for all \(m\ge M_1\),
\[
\frac12-\varepsilon
<
a_{2m}
<
\frac12+\varepsilon.
\]

::: {.proof}
This is convergence of the even subsequence from step <1>7.
:::

<1>13. There exists \(M_2\) such that for all \(m\ge M_2\),
\[
1-\varepsilon
<
a_{2m+1}
<
1+\varepsilon.
\]

::: {.proof}
This is convergence of the odd subsequence from step <1>10.
:::

<1>14. Therefore every sufficiently late term \(a_n\) satisfies
\[
\boxed{
a_n>\frac12-\varepsilon}.
\]

::: {.proof}
Choose
\[
M=\max(M_1,M_2).
\]
For late even terms use step <1>12. For late odd terms, step <1>13 gives
\[
a_{2m+1}>1-\varepsilon>\frac12-\varepsilon
\]
after decreasing \(\varepsilon\) if necessary; equivalently, one may use the
explicit formula in step <1>9, whose values are eventually above
\(1/2-\varepsilon\).
:::

<1>15. Infinitely many terms satisfy
\[
a_n<\frac12+\varepsilon.
\]

::: {.proof}
All sufficiently late even terms do so by step <1>12.
:::

<1>16. Hence
\[
\boxed{
\liminf_{n\to\infty}a_n=\frac12}.
\]

::: {.proof}
Step <1>14 shows that the eventual lower bound is at least
\[
1/2-\varepsilon
\]
for every \(\varepsilon>0\), while step <1>15 shows terms occur infinitely
often below
\[
1/2+\varepsilon.
\]
This is exactly the characterization of the liminf as \(1/2\).
:::

<1>17. Every sufficiently late term satisfies
\[
a_n<1+\varepsilon.
\]

::: {.proof}
Late odd terms satisfy this by step <1>13. Late even terms are below \(1/2\)
by step <1>11, hence also below \(1+\varepsilon\).
:::

<1>18. Infinitely many terms satisfy
\[
a_n>1-\varepsilon.
\]

::: {.proof}
All sufficiently late odd terms satisfy this by step <1>13.
:::

<1>19. Hence
\[
\boxed{
\limsup_{n\to\infty}a_n=1}.
\]

::: {.proof}
Step <1>17 gives the eventual upper bound \(1+\varepsilon\), while step
<1>18 gives infinitely many terms above \(1-\varepsilon\), for every
\(\varepsilon>0\).
:::

<1>20. Therefore
\[
\boxed{
\liminf a_n=\frac12,
\qquad
\limsup a_n=1}.
\]

::: {.proof}
Combine steps <1>16 and <1>19.
:::

<1>21. Q.E.D.

::: {.proof}
Step <1>20 gives both requested limits.
:::
:::
