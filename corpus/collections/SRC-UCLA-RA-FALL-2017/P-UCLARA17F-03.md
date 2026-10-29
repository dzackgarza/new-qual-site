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
Problem 3. Let $\{\mu_n\}$ denote a sequence of Borel probability measures on $\RR$. For $n\in\NN$ and $x\in\RR$ define
\[
F_n(x):=\mu_n(( -\infty,x]).
\]
Suppose the sequence $\{F_n\}$ converges uniformly on $\RR$. Show that for every bounded continuous function $f:\RR\to\RR$, the numbers
\[
\int_{\RR} f(x)\,d\mu_n(x)
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

::: pf

::: {.pf-step #s1-1}

Choose \(N_0\) such that for every \(n\ge N_0\),
\[
\boxed{
\sup_{x\in\RR}
|F_n(x)-F_{N_0}(x)|
<
\delta}
\]
where \(\delta>0\) will be chosen below.


::: pf-proof

Uniform convergence implies the uniform Cauchy property. Fix one sufficiently late index \(N_0\) and compare all later functions to \(F_{N_0}\).

:::

:::

::: pf-step

There exists \(R>0\) such that
\[
\boxed{
F_{N_0}(-R)<\delta}
\]
and
\[
\boxed{
1-F_{N_0}(R)<\delta}.
\]


::: pf-proof

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

:::

::: {.pf-step #s1-3}

For every \(n\ge N_0\),
\[
\boxed{
F_n(-R)<2\delta}.
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
F_n(-R)
\le
F_{N_0}(-R)+\delta
<
2\delta.
\]

:::

:::

::: {.pf-step #s1-4}

For every \(n\ge N_0\),
\[
\boxed{
1-F_n(R)<2\delta}.
\]


::: pf-proof

Again by step [](#s1-1){.pf-ref},
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

:::

::: {.pf-step #s1-5}

Therefore, for every \(n\ge N_0\),
\[
\boxed{
\mu_n((-\infty,-R])
+
\mu_n((R,\infty))
<
4\delta}.
\]


::: pf-proof

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
Use steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Since \(f\) is uniformly continuous on \([-R,R]\), there exists a partition
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


::: pf-proof

Uniform continuity gives \(\rho>0\) such that
\[
|x-y|<\rho
\Longrightarrow
|f(x)-f(y)|<\varepsilon/8
\]
for \(x,y\in[-R,R]\). Choose a partition of mesh \(<\rho\).

:::

:::

::: {.pf-step #s1-7}

For every \(x\in(-R,R]\),
\[
\boxed{
|f(x)-s(x)|<\eta}.
\]


::: pf-proof

If
\[
x\in(x_{j-1},x_j],
\]
then both \(x\) and \(\xi_j\) lie in the same partition interval, whose oscillation is \(<\eta\) by step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For every \(n\ge N_0\),
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


::: pf-proof

Split the integral of \(|f-s|\) into
\[
(-R,R]
\]
and its complement.

On \((-R,R]\), step [](#s1-7){.pf-ref} gives
\[
|f-s|<\eta,
\]
so the contribution is at most \(\eta\).

Outside \((-R,R]\), one has \(s=0\) and
\[
|f|\le M.
\]
By step [](#s1-5){.pf-ref}, the outside mass is \(<4\delta\), so the tail contribution is \(<4M\delta\).

:::

:::

::: {.pf-step #s1-9}

By the choices of \(\eta\) and \(\delta\),
\[
\boxed{
\eta+4M\delta
<
\frac{\varepsilon}{4}}.
\]


::: pf-proof

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

:::

::: {.pf-step #s1-10}

One has
\[
\boxed{
\mu_n((x_{j-1},x_j])
=
F_n(x_j)-F_n(x_{j-1})}.
\]


::: pf-proof

By the definition of the distribution function,
\[
F_n(b)-F_n(a)
=
\mu_n((a,b]).
\]

:::

:::

::: pf-step

Therefore
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


::: pf-proof

Substitute step [](#s1-10){.pf-ref} into the step-function integral.

:::

:::

::: {.pf-step #s1-12}

The sequence
\[
\left(
\int s\,d\mu_n
\right)
\]
is Cauchy.


::: pf-proof

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

:::

::: {.pf-step #s1-13}

Hence there exists \(N_1\ge N_0\) such that for \(n,m\ge N_1\),
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


::: pf-proof

Use step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

For \(n,m\ge N_1\),
\[
\left|
\int f\,d\mu_n
-
\int f\,d\mu_m
\right|
<
\varepsilon.
\]


::: pf-proof

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
The first and third terms are \(<\varepsilon/4\) by steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}, and the middle term is \(<\varepsilon/2\) by step [](#s1-13){.pf-ref}.

:::

:::

::: pf-step

Thus
\[
\boxed{
\left(
\int_{\RR}f\,d\mu_n
\right)
\text{ is Cauchy in }\RR}.}
\]


::: pf-proof

Step [](#s1-14){.pf-ref} is the Cauchy criterion.

:::

:::

::: {.pf-step #s1-16}

Therefore
\[
\boxed{
\int_{\RR}f\,d\mu_n
\text{ converges as }n\to\infty}.}
\]


::: pf-proof

The real numbers are complete.

:::

:::

::: pf-qed

Step [](#s1-16){.pf-ref} is the required conclusion.

:::

:::

:::
