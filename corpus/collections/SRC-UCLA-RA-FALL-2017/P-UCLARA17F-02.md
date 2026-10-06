---
schema: qual/card@1
id: P-UCLARA17F-02
kind: problem
title: Bounded almost everywhere convergent sequences in $L^2([0,1])$ converge weakly
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 2. Let $\{f_n\}$ denote a bounded sequence in $L^2([0,1])$. Suppose the sequence $\{f_n\}$ also converges almost everywhere. Show that then $\{f_n\}$ converges in the weak topology on $L^2([0,1])$.
:::

::: {.solution}
Let
\[
f_n(x)\to f(x)
\]
for almost every \(x\in[0,1]\), and assume
\[
\sup_n\|f_n\|_2\le M.
\]

<1>1. The limit \(f\) belongs to \(L^2([0,1])\) and satisfies
\[
\boxed{\|f\|_2\le M}.
\]

::: {.proof}
By Fatou's lemma,
\[
\int_0^1|f|^2
\le
\liminf_{n\to\infty}
\int_0^1|f_n|^2
\le
M^2.
\]
:::

Define
\[
h_n=f_n-f.
\]

<1>2. One has
\[
\boxed{
h_n(x)\to0}
\]
for almost every \(x\).

::: {.proof}
This is immediate from the assumed a.e. convergence \(f_n\to f\).
:::

<1>3. The sequence \((h_n)\) is uniformly bounded in \(L^2\):
\[
\boxed{
\|h_n\|_2\le2M}.
\]

::: {.proof}
By the triangle inequality and step <1>1,
\[
\|h_n\|_2
\le
\|f_n\|_2+\|f\|_2
\le
M+M
=
2M.
\]
:::

We first prove that
\[
h_n\to0
\quad\text{in }L^1([0,1]).
\]

Fix \(\varepsilon>0\).

<1>4. Choose \(\delta>0\) so small that
\[
\boxed{
2M\sqrt\delta<\frac{\varepsilon}{2}}.
\]

::: {.proof}
The left-hand side tends to \(0\) as \(\delta\downarrow0\).
:::

<1>5. By Egorov's theorem, there exists a measurable set
\[
E\subset[0,1]
\]
with
\[
|E|<\delta
\]
such that \(h_n\to0\) uniformly on
\[
[0,1]\setminus E.
\]

::: {.proof}
The underlying measure space has finite measure, and \(h_n\to0\) almost everywhere by step <1>2.
:::

<1>6. For sufficiently large \(n\),
\[
\boxed{
\sup_{x\in[0,1]\setminus E}|h_n(x)|
<
\frac{\varepsilon}{2}}.
\]

::: {.proof}
Use the uniform convergence from step <1>5.
:::

<1>7. Hence for all sufficiently large \(n\),
\[
\int_{[0,1]\setminus E}
|h_n(x)|\,dx
<
\frac{\varepsilon}{2}.
\]

::: {.proof}
The complement has measure at most \(1\), so
\[
\int_{[0,1]\setminus E}|h_n|
\le
\sup_{[0,1]\setminus E}|h_n|
\cdot
|[0,1]\setminus E|
<
\frac{\varepsilon}{2}.
\]
:::

<1>8. On \(E\),
\[
\int_E|h_n|
\le
\|h_n\|_2\,|E|^{1/2}.
\]

::: {.proof}
Apply Cauchy--Schwarz:
\[
\int_E|h_n|
=
\int_E|h_n|\cdot1
\le
\left(
\int_E|h_n|^2
\right)^{1/2}
|E|^{1/2}.
\]
:::

<1>9. Therefore
\[
\int_E|h_n|
<
\frac{\varepsilon}{2}
\]
for every \(n\).

::: {.proof}
Use step <1>3, the bound \(|E|<\delta\), and step <1>4:
\[
\int_E|h_n|
\le
2M\sqrt{|E|}
<
2M\sqrt\delta
<
\frac{\varepsilon}{2}.
\]
:::

<1>10. Hence
\[
\boxed{
\|h_n\|_1\to0}.
\]

::: {.proof}
For all sufficiently large \(n\),
\[
\|h_n\|_1
=
\int_{[0,1]\setminus E}|h_n|
+
\int_E|h_n|
<
\varepsilon
\]
by steps <1>7 and <1>9.
:::

Now let
\[
g\in L^2([0,1]).
\]

<1>11. For \(R>0\), define the truncation
\[
g_R
=
g\,\mathbf 1_{\{|g|\le R\}}.
\]

::: {.proof}
This is a measurable bounded function.
:::

<1>12. One has
\[
\boxed{
g_R\in L^\infty\cap L^2}
\]
and
\[
\boxed{
\|g-g_R\|_2\to0}
\]
as \(R\to\infty\).

::: {.proof}
The function \(g_R\) is bounded by \(R\), hence lies in \(L^\infty\), and clearly lies in \(L^2\).

Moreover,
\[
|g-g_R|^2
=
|g|^2\mathbf 1_{\{|g|>R\}}
\to0
\]
pointwise and is dominated by \(|g|^2\in L^1\). Dominated convergence gives the \(L^2\)-convergence.
:::

<1>13. For fixed \(R\),
\[
\boxed{
\int_0^1h_n g_R\to0}.
\]

::: {.proof}
Since \(g_R\in L^\infty\),
\[
\left|
\int h_n g_R
\right|
\le
\|g_R\|_\infty
\|h_n\|_1.
\]
Apply step <1>10.
:::

<1>14. For every \(n\),
\[
\left|
\int_0^1
h_n(g-g_R)
\right|
\le
2M\,\|g-g_R\|_2.
\]

::: {.proof}
By Cauchy--Schwarz and step <1>3,
\[
\left|
\int h_n(g-g_R)
\right|
\le
\|h_n\|_2
\|g-g_R\|_2
\le
2M\|g-g_R\|_2.
\]
:::

<1>15. Given \(\varepsilon>0\), choose \(R\) so large that
\[
2M\|g-g_R\|_2
<
\frac{\varepsilon}{2}.
\]

::: {.proof}
Use the convergence in step <1>12.
:::

<1>16. For this fixed \(R\), choose \(N\) so large that for \(n\ge N\),
\[
\left|
\int h_n g_R
\right|
<
\frac{\varepsilon}{2}.
\]

::: {.proof}
Use step <1>13.
:::

<1>17. Then for \(n\ge N\),
\[
\left|
\int_0^1h_n g
\right|
<
\varepsilon.
\]

::: {.proof}
Split:
\[
\int h_n g
=
\int h_n g_R
+
\int h_n(g-g_R),
\]
and use steps <1>14--<1>16.
:::

<1>18. Therefore
\[
\boxed{
\int_0^1f_n g
\to
\int_0^1f g}
\]
for every \(g\in L^2([0,1])\).

::: {.proof}
Since
\[
h_n=f_n-f,
\]
step <1>17 says
\[
\int h_n g\to0.
\]
:::

<1>19. Hence
\[
\boxed{
f_n\rightharpoonup f
\text{ weakly in }L^2([0,1]).}
\]

::: {.proof}
Step <1>18 is exactly the definition of weak convergence in the Hilbert space \(L^2([0,1])\).
:::

<1>20. Q.E.D.

::: {.proof}
Step <1>19 is the required conclusion.
:::
:::
