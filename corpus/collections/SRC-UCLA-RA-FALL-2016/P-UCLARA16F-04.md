---
schema: qual/card@1
id: P-UCLARA16F-04
kind: problem
title: $L^2$ is meager in $L^1([0,1])$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $L^1=L^1([0,1])$ be the space of integrable functions and $L^2=L^2([0,1])$ the space of square-integrable functions on $[0,1]$.
Then $L^2\subset L^1$.
Show that $L^2$ is a meager subset of $L^1$, i.e. $L^2$ can be written as a countable union of sets in $L^1$ that are closed and have empty interior in $L^1$.
:::

::: {.solution}
For each integer \(n\ge1\), define
\[
\boxed{
A_n
=
\left\{
f\in L^2([0,1]):
\|f\|_2\le n
\right\}.}
\]

<1>1. One has
\[
\boxed{
L^2([0,1])
=
\bigcup_{n=1}^{\infty}A_n}.
\]

::: {.proof}
If \(f\in L^2\), then \(\|f\|_2<\infty\), so choose an integer \(n\ge\|f\|_2\). Then \(f\in A_n\). The reverse inclusion is immediate from the definition of \(A_n\).
:::

We now regard every \(A_n\) as a subset of \(L^1([0,1])\).

## Closedness

<1>2. Let
\[
f_j\in A_n
\]
and suppose
\[
f_j\to f
\]
in \(L^1([0,1])\).

::: {.proof}
This is the setup for proving that \(A_n\) is closed in the \(L^1\)-topology.
:::

<1>3. There exists a subsequence
\[
(f_{j_k})
\]
such that
\[
\boxed{
f_{j_k}(x)\to f(x)}
\]
for almost every \(x\in[0,1]\).

::: {.proof}
From \(L^1\)-convergence, choose a subsequence satisfying
\[
\|f_{j_k}-f\|_1<2^{-k}.
\]
Then
\[
\sum_{k=1}^{\infty}
\|f_{j_k}-f\|_1
<
\infty.
\]
By Tonelli,
\[
\int_0^1
\sum_{k=1}^{\infty}
|f_{j_k}(x)-f(x)|
\,dx
<
\infty.
\]
Hence for almost every \(x\),
\[
\sum_k|f_{j_k}(x)-f(x)|<\infty,
\]
which implies
\[
f_{j_k}(x)-f(x)\to0.
\]
:::

<1>4. Fatou's lemma gives
\[
\int_0^1|f(x)|^2\,dx
\le
\liminf_{k\to\infty}
\int_0^1|f_{j_k}(x)|^2\,dx.
\]

::: {.proof}
By step <1>3,
\[
|f_{j_k}(x)|^2\to|f(x)|^2
\]
almost everywhere, and the integrands are nonnegative. Apply Fatou's lemma.
:::

<1>5. Since each \(f_{j_k}\in A_n\),
\[
\int_0^1|f_{j_k}|^2\,dx
\le
n^2.
\]

::: {.proof}
This is equivalent to
\[
\|f_{j_k}\|_2\le n.
\]
:::

<1>6. Therefore
\[
\boxed{
\int_0^1|f|^2\,dx
\le
n^2}.
\]

::: {.proof}
Combine steps <1>4--<1>5.
:::

<1>7. Hence
\[
\boxed{
f\in A_n}.
\]

::: {.proof}
Step <1>6 shows \(f\in L^2\) and
\[
\|f\|_2\le n.
\]
:::

<1>8. Thus \(A_n\) is closed in \(L^1([0,1])\).

::: {.proof}
Every \(L^1\)-limit of a sequence in \(A_n\) remains in \(A_n\) by steps <1>2--<1>7.
:::

## Empty interior

Fix
\[
f\in A_n
\]
and
\[
\varepsilon>0.
\]

<1>9. Define
\[
h(x)=x^{-1/2}
\qquad
(0<x\le1).
\]

::: {.proof}
This is a measurable function on \((0,1]\).
:::

<1>10. One has
\[
\boxed{
h\in L^1([0,1])}.
\]

::: {.proof}
\[
\int_0^1x^{-1/2}\,dx
=
2
<
\infty.
\]
:::

<1>11. One has
\[
\boxed{
h\notin L^2([0,1])}.
\]

::: {.proof}
\[
\int_0^1|h(x)|^2\,dx
=
\int_0^1\frac{dx}{x}
=
\infty.
\]
:::

<1>12. Choose
\[
\lambda>0
\]
so small that
\[
\boxed{
\lambda\|h\|_1<\varepsilon}.
\]

::: {.proof}
The number \(\|h\|_1=2\) is finite by step <1>10, so any
\[
0<\lambda<\varepsilon/2
\]
works.
:::

<1>13. Define
\[
\boxed{
g=f+\lambda h}.
\]

::: {.proof}
Since
\[
f\in L^2([0,1])\subseteq L^1([0,1])
\]
and \(h\in L^1\), the sum \(g\) belongs to \(L^1\).
:::

<1>14. One has
\[
\boxed{
\|g-f\|_1
=
\lambda\|h\|_1
<
\varepsilon}.
\]

::: {.proof}
By definition,
\[
g-f=\lambda h.
\]
Use step <1>12.
:::

<1>15. The function \(g\) does not belong to \(L^2([0,1])\).

::: {.proof}
Suppose \(g\in L^2\). Since \(f\in L^2\), their difference
\[
g-f
=
\lambda h
\]
would also lie in \(L^2\), because \(L^2\) is a vector space. Since \(\lambda\ne0\), this would imply \(h\in L^2\), contradicting step <1>11.
:::

<1>16. Hence
\[
\boxed{
g\notin A_n}.
\]

::: {.proof}
The set \(A_n\) is contained in \(L^2\), while step <1>15 gives \(g\notin L^2\).
:::

<1>17. Therefore every \(L^1\)-ball around every \(f\in A_n\) contains a point outside \(A_n\).

::: {.proof}
Given arbitrary \(\varepsilon>0\), steps <1>13--<1>16 construct \(g\) with
\[
\|g-f\|_1<\varepsilon
\]
but
\[
g\notin A_n.
\]
:::

<1>18. Thus
\[
\boxed{
\operatorname{int}_{L^1}(A_n)=\varnothing}.
\]

::: {.proof}
Step <1>17 is exactly the assertion that \(A_n\) has empty interior.
:::

<1>19. Since \(A_n\) is closed and has empty interior, it is nowhere dense in \(L^1\).

::: {.proof}
For a closed set,
\[
\overline{A_n}=A_n.
\]
Thus
\[
\operatorname{int}\overline{A_n}
=
\varnothing
\]
by step <1>18.
:::

<1>20. Finally,
\[
\boxed{
L^2([0,1])
=
\bigcup_{n=1}^{\infty}A_n}
\]
is a countable union of nowhere-dense subsets of \(L^1([0,1])\).

::: {.proof}
Use steps <1>1 and <1>19.
:::

<1>21. Therefore
\[
\boxed{
L^2([0,1])
\text{ is meager in }L^1([0,1]).}
\]

::: {.proof}
This is the definition of a meager set.
:::

<1>22. Q.E.D.

::: {.proof}
Step <1>21 is the required conclusion.
:::
:::
