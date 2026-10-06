---
schema: qual/card@1
id: P-WESRA03-II4
kind: problem
title: Epsilon-delta absolute continuity for finite measures
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Absolute Continuity]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 4 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf.
---

::: {.problem}
Let $(X,\mathcal A)$ be a measurable space, and let $\mu$ and $\nu$ be finite measures on it.
Assume that for every $A\in\mathcal A$,
\[
\mu(A)=0\implies \nu(A)=0.
\]
Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
\mu(A)<\delta\implies \nu(A)<\varepsilon.
\]
:::

::: {.solution}
Suppose, toward a contradiction, that the asserted \(\varepsilon\)-\(\delta\)
statement is false.

<1>1. Then there exists
\[
\varepsilon_0>0
\]
such that for every \(\delta>0\), there is a measurable set \(A\) with
\[
\mu(A)<\delta
\]
but
\[
\nu(A)\ge\varepsilon_0.
\]

::: {.proof}
This is exactly the negation of
\[
\forall\varepsilon>0\ \exists\delta>0\
\forall A\in\mathcal A:
\mu(A)<\delta\Rightarrow\nu(A)<\varepsilon.
\]
:::

<1>2. For each \(n\ge1\), choose
\[
A_n\in\mathcal A
\]
such that
\[
\boxed{
\mu(A_n)<2^{-n}}
\]
and
\[
\boxed{
\nu(A_n)\ge\varepsilon_0}.
\]

::: {.proof}
Apply step <1>1 with
\[
\delta=2^{-n}.
\]
:::

<1>3. Define
\[
\boxed{
B_n=\bigcup_{k=n}^{\infty}A_k}.
\]

::: {.proof}
This is a countable union of measurable sets, hence measurable.
:::

<1>4. The sequence \((B_n)\) is decreasing:
\[
\boxed{
B_{n+1}\subseteq B_n}.
\]

::: {.proof}
The union defining \(B_{n+1}\) omits the first set \(A_n\) from the union
defining \(B_n\).
:::

<1>5. By countable subadditivity,
\[
\mu(B_n)
\le
\sum_{k=n}^{\infty}\mu(A_k).
\]

::: {.proof}
Apply countable subadditivity of the measure \(\mu\) to the union in step
<1>3.
:::

<1>6. Using step <1>2,
\[
\mu(B_n)
<
\sum_{k=n}^{\infty}2^{-k}
=
2^{1-n}.
\]

::: {.proof}
The geometric tail satisfies
\[
\sum_{k=n}^{\infty}2^{-k}
=
\frac{2^{-n}}{1-1/2}
=
2^{1-n}.
\]
:::

<1>7. Hence
\[
\boxed{
\mu(B_n)\longrightarrow0}.
\]

::: {.proof}
Step <1>6 gives
\[
0\le\mu(B_n)<2^{1-n}\to0.
\]
Apply the squeeze theorem.
:::

<1>8. Let
\[
\boxed{
B=\bigcap_{n=1}^{\infty}B_n}.
\]
Then
\[
\boxed{\mu(B)=0}.
\]

::: {.proof}
Since
\[
B\subseteq B_n
\]
for every \(n\),
\[
0\le\mu(B)\le\mu(B_n).
\]
Use step <1>7.
:::

<1>9. By the assumed absolute continuity,
\[
\boxed{\nu(B)=0}.
\]

::: {.proof}
The hypothesis says
\[
\mu(A)=0
\Rightarrow
\nu(A)=0
\]
for every measurable \(A\). Apply it to \(A=B\) using step <1>8.
:::

<1>10. For every \(n\),
\[
A_n\subseteq B_n.
\]

::: {.proof}
The union defining \(B_n\) includes the term \(A_n\).
:::

<1>11. Therefore
\[
\boxed{
\nu(B_n)\ge\nu(A_n)\ge\varepsilon_0}.
\]

::: {.proof}
Measures are monotone, so step <1>10 gives
\[
\nu(B_n)\ge\nu(A_n).
\]
Apply step <1>2.
:::

<1>12. Since \(\nu\) is finite,
\[
\nu(B_1)<\infty.
\]

::: {.proof}
The measure \(\nu\) is finite on the whole space \(X\), so
\[
\nu(B_1)\le\nu(X)<\infty.
\]
:::

<1>13. By continuity from above,
\[
\boxed{
\nu(B_n)\longrightarrow\nu(B)}.
\]

::: {.proof}
The sets \(B_n\) decrease by step <1>4, and the first one has finite
\(\nu\)-measure by step <1>12. The continuity-from-above theorem for measures
therefore gives
\[
\nu\left(\bigcap_{n=1}^{\infty}B_n\right)
=
\lim_{n\to\infty}\nu(B_n).
\]
The intersection is \(B\).
:::

<1>14. Steps <1>11 and <1>13 imply
\[
\boxed{
\nu(B)\ge\varepsilon_0}.
\]

::: {.proof}
Every term of the sequence \(\nu(B_n)\) is at least \(\varepsilon_0\), so
its limit is also at least \(\varepsilon_0\).
:::

<1>15. Steps <1>9 and <1>14 contradict one another.

::: {.proof}
Step <1>9 gives
\[
\nu(B)=0,
\]
while step <1>14 gives
\[
\nu(B)\ge\varepsilon_0>0.
\]
:::

<1>16. Therefore the negation in step <1>1 is impossible.

::: {.proof}
It leads to the contradiction in step <1>15.
:::

<1>17. Hence for every \(\varepsilon>0\), there exists \(\delta>0\) such
that
\[
\boxed{
\mu(A)<\delta
\Longrightarrow
\nu(A)<\varepsilon}
\]
for every measurable \(A\).

::: {.proof}
This is the logical negation of the impossible statement in step <1>1.
:::

<1>18. Q.E.D.

::: {.proof}
Step <1>17 is the required conclusion.
:::
:::
