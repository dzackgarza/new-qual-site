---
schema: qual/card@1
id: P-UCLARA17F-03
kind: problem
title: Uniform convergence of distribution functions implies weak convergence of measures
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
Problem 3. Let $\{\mu_n\}$ denote a sequence of Borel probability measures on $\mathbb R$. For $n\in\mathbb N$ and $x\in\mathbb R$ define
\[
F_n(x):=\mu_n(( -\infty,x]).
\]
Suppose the sequence $\{F_n\}$ converges uniformly on $\mathbb R$. Show that for every bounded continuous function $f:\mathbb R\to\mathbb R$, the numbers
\[
\int_{\mathbb R} f(x)\,d\mu_n(x)
\]
converge as $n\to\infty$.
:::

::: {.solution}
Let
\[
M=\|f\|_\infty.
\]

If \(M=0\), then \(f\equiv0\) and the conclusion is immediate. Assume henceforth
\[
M>0.
\]

We will show that
\[
\left(
\int f\,d\mu_n
\right)
\]
is a Cauchy sequence.

Fix
\[
\varepsilon>0.
\]

Since \(F_n\) converges uniformly, it is uniformly Cauchy.

<1>1. Choose \(N_0\) such that for every \(n\ge N_0\),
\[
\boxed{
\sup_{x\in\mathbb R}
|F_n(x)-F_{N_0}(x)|
<
\delta}
\]
where \(\delta>0\) will be chosen below.

::: {.proof}
Uniform convergence implies the uniform Cauchy property. Fix one sufficiently late index \(N_0\) and compare all later functions to \(F_{N_0}\).
:::

Choose
\[
\boxed{
\delta<\frac{\varepsilon}{32M}}.
\]

<1>2. There exists \(R>0\) such that
\[
\boxed{
F_{N_0}(-R)<\delta}
\]
and
\[
\boxed{
1-F_{N_0}(R)<\delta}.
\]

::: {.proof}
Since \(F_{N_0}\) is the distribution function of a probability measure,
\[
F_{N_0}(x)\to0
\quad(x\to-\infty)
\]
and
\[
F_{N_0}(x)\to1
\quad(x\to+\infty).
\]
:::

<1>3. For every \(n\ge N_0\),
\[
\boxed{
F_n(-R)<2\delta}.
\]

::: {.proof}
By step <1>1,
\[
F_n(-R)
\le
F_{N_0}(-R)+\delta
<
2\delta.
\]
:::

<1>4. For every \(n\ge N_0\),
\[
\boxed{
1-F_n(R)<2\delta}.
\]

::: {.proof}
Again by step <1>1,
\[
F_n(R)
>
F_{N_0}(R)-\delta,
\]
so
\[
1-F_n(R)
<
1-F_{N_0}(R)+\delta
<
2\delta.
\]
:::

<1>5. Therefore, for every \(n\ge N_0\),
\[
\boxed{
\mu_n((-\infty,-R])
+
\mu_n((R,\infty))
<
4\delta}.
\]

::: {.proof}
By definition,
\[
\mu_n((-\infty,-R])
=
F_n(-R)
\]
and
\[
\mu_n((R,\infty))
=
1-F_n(R).
\]
Use steps <1>3--<1>4.
:::

Now approximate \(f\) on \([-R,R]\).

<1>6. Since \(f\) is uniformly continuous on \([-R,R]\), there exists a partition
\[
-R=x_0<x_1<\cdots<x_J=R
\]
such that the oscillation of \(f\) on each interval
\[
[x_{j-1},x_j]
\]
is less than
\[
\boxed{\eta=\frac{\varepsilon}{8}}.
\]

::: {.proof}
Uniform continuity gives \(\rho>0\) such that
\[
|x-y|<\rho
\Longrightarrow
|f(x)-f(y)|<\varepsilon/8
\]
for \(x,y\in[-R,R]\). Choose a partition of mesh \(<\rho\).
:::

For each \(j\), choose
\[
\xi_j\in[x_{j-1},x_j]
\]
and set
\[
c_j=f(\xi_j).
\]

Define the step function
\[
s(x)
=
\begin{cases}
c_j,&x\in(x_{j-1},x_j],\ 1\le j\le J,\\
0,&x\le-R\text{ or }x>R.
\end{cases}
\]

<1>7. For every \(x\in(-R,R]\),
\[
\boxed{
|f(x)-s(x)|<\eta}.
\]

::: {.proof}
If
\[
x\in(x_{j-1},x_j],
\]
then both \(x\) and \(\xi_j\) lie in the same partition interval, whose oscillation is \(<\eta\) by step <1>6.
:::

<1>8. For every \(n\ge N_0\),
\[
\boxed{
\left|
\int f\,d\mu_n
-
\int s\,d\mu_n
\right|
\le
\eta+4M\delta}.
\]

::: {.proof}
Split the integral of \(|f-s|\) into
\[
(-R,R]
\]
and its complement.

On \((-R,R]\), step <1>7 gives
\[
|f-s|<\eta,
\]
so the contribution is at most \(\eta\).

Outside \((-R,R]\), one has \(s=0\) and
\[
|f|\le M.
\]
By step <1>5, the outside mass is \(<4\delta\), so the tail contribution is \(<4M\delta\).
:::

<1>9. By the choices of \(\eta\) and \(\delta\),
\[
\boxed{
\eta+4M\delta
<
\frac{\varepsilon}{4}}.
\]

::: {.proof}
One has
\[
\eta=\frac{\varepsilon}{8}
\]
and
\[
4M\delta
<
4M\frac{\varepsilon}{32M}
=
\frac{\varepsilon}{8}.
\]
Thus the sum is \(<\varepsilon/4\).
:::

For the step function,
\[
\int s\,d\mu_n
=
\sum_{j=1}^{J}
c_j
\mu_n((x_{j-1},x_j]).
\]

<1>10. One has
\[
\boxed{
\mu_n((x_{j-1},x_j])
=
F_n(x_j)-F_n(x_{j-1})}.
\]

::: {.proof}
By the definition of the distribution function,
\[
F_n(b)-F_n(a)
=
\mu_n((a,b]).
\]
:::

<1>11. Therefore
\[
\boxed{
\int s\,d\mu_n
=
\sum_{j=1}^{J}
c_j
\bigl(
F_n(x_j)-F_n(x_{j-1})
\bigr)}.
\]

::: {.proof}
Substitute step <1>10 into the step-function integral.
:::

<1>12. The sequence
\[
\left(
\int s\,d\mu_n
\right)
\]
is Cauchy.

::: {.proof}
Since \(F_n\) converges uniformly, it is uniformly Cauchy. For \(n,m\),
\[
\begin{aligned}
\left|
\int s\,d\mu_n
-
\int s\,d\mu_m
\right|
&\le
\sum_{j=1}^{J}
|c_j|
\Bigl(
|F_n(x_j)-F_m(x_j)|\\
&\qquad\qquad+
|F_n(x_{j-1})-F_m(x_{j-1})|
\Bigr)\\
&\le
2JM
\sup_x|F_n(x)-F_m(x)|.
\end{aligned}
\]
The final quantity tends to \(0\) as \(n,m\to\infty\).
:::

<1>13. Hence there exists \(N_1\ge N_0\) such that for \(n,m\ge N_1\),
\[
\boxed{
\left|
\int s\,d\mu_n
-
\int s\,d\mu_m
\right|
<
\frac{\varepsilon}{2}}.
\]

::: {.proof}
Use step <1>12.
:::

<1>14. For \(n,m\ge N_1\),
\[
\left|
\int f\,d\mu_n
-
\int f\,d\mu_m
\right|
<
\varepsilon.
\]

::: {.proof}
Insert the step-function integrals:
\[
\begin{aligned}
\left|
\int f\,d\mu_n-\int f\,d\mu_m
\right|
&\le
\left|
\int f\,d\mu_n-\int s\,d\mu_n
\right|\\
&\quad+
\left|
\int s\,d\mu_n-\int s\,d\mu_m
\right|\\
&\quad+
\left|
\int s\,d\mu_m-\int f\,d\mu_m
\right|.
\end{aligned}
\]
The first and third terms are \(<\varepsilon/4\) by steps <1>8--<1>9, and the middle term is \(<\varepsilon/2\) by step <1>13.
:::

<1>15. Thus
\[
\boxed{
\left(
\int_{\mathbb R}f\,d\mu_n
\right)
\text{ is Cauchy in }\mathbb R}.}
\]

::: {.proof}
Step <1>14 is the Cauchy criterion.
:::

<1>16. Therefore
\[
\boxed{
\int_{\mathbb R}f\,d\mu_n
\text{ converges as }n\to\infty}.}
\]

::: {.proof}
The real numbers are complete.
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>16 is the required conclusion.
:::
:::
