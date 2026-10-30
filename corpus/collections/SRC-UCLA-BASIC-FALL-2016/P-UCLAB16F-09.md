---
schema: qual/card@1
id: P-UCLAB16F-09
kind: problem
title: Equicontinuity and uniform convergence on $[0,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 9 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let $f_n : [0, 1] \to \CC$ be a sequence of continuous functions.
Suppose $f_n$ converge pointwise.
Show that the sequence converges uniformly if and only if the collection of functions $\{f_n\}$ is equicontinuous.
:::

::: {.solution}

Let
$$
f(x)=\lim_{n\to\infty}f_n(x)
$$
for
$$
x\in[0,1].
$$

::: pf

::: {.pf-step #s1-1}

Suppose first that
$$
f_n\to f
$$
uniformly.
Then $f$ is continuous.


::: pf-proof

A uniform limit of continuous functions on a metric space is continuous.

:::

:::

::: {.pf-step #s1-2}

Under uniform convergence, the family
$$
\{f_n:n\ge1\}
$$
is equicontinuous.


::: pf-proof

Fix $\varepsilon>0$.
Choose $N$ such that
$$
\norm{f_n-f}_\infty<\frac{\varepsilon}{3}
$$
for every $n\ge N$.

By step [](#s1-1){.pf-ref}, $f$ is continuous on the compact interval $[0,1]$, hence uniformly continuous.
Choose $\delta_0>0$ such that
$$
\abs{x-y}<\delta_0
$$
implies
$$
\abs{f(x)-f(y)}<\frac{\varepsilon}{3}.
$$

For each of the finitely many functions
$$
f_1,\ldots,f_{N-1},
$$
uniform continuity on $[0,1]$ gives a number $\delta_j>0$ such that
$$
\abs{x-y}<\delta_j
$$
implies
$$
\abs{f_j(x)-f_j(y)}<\varepsilon.
$$
Set
$$
\delta
=
\min\{\delta_0,\delta_1,\ldots,\delta_{N-1}\}.
$$

If $n<N$, the desired estimate follows from the choice of $\delta_n$.
If $n\ge N$, then
$$
\begin{aligned}
\abs{f_n(x)-f_n(y)}
&\le
\abs{f_n(x)-f(x)}
+
\abs{f(x)-f(y)}
+
\abs{f(y)-f_n(y)}\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}\\
&=
\varepsilon.
\end{aligned}
$$
Thus one $\delta$ works for every $n$, proving equicontinuity.

:::

:::

::: {.pf-step #s1-3}

Conversely, suppose the family $\{f_n\}$ is equicontinuous.
Then the pointwise limit $f$ is continuous.


::: pf-proof

Fix $\varepsilon>0$.
By equicontinuity, choose $\delta>0$ such that
$$
\abs{x-y}<\delta
$$
implies
$$
\abs{f_n(x)-f_n(y)}<\frac{\varepsilon}{3}
$$
for every $n$.

Fix $x,y$ with
$$
\abs{x-y}<\delta.
$$
Taking $n\to\infty$ in
$$
\abs{f_n(x)-f_n(y)}<\frac{\varepsilon}{3}
$$
gives
$$
\abs{f(x)-f(y)}
\le
\frac{\varepsilon}{3}
<
\varepsilon.
$$
Thus $f$ is uniformly continuous, in particular continuous.

:::

:::

::: {.pf-step #s1-4}

Fix $\varepsilon>0$.
There exists $\delta>0$ such that
$$
\abs{x-y}<\delta
$$
implies both
$$
\abs{f_n(x)-f_n(y)}<\frac{\varepsilon}{3}
$$
for every $n$ and
$$
\abs{f(x)-f(y)}<\frac{\varepsilon}{3}.
$$


::: pf-proof

Use equicontinuity of the family for tolerance $\varepsilon/3$.
The same $\delta$ works for $f$ by the limiting argument in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

There exist finitely many points
$$
x_1,\ldots,x_m\in[0,1]
$$
such that every $x\in[0,1]$ satisfies
$$
\abs{x-x_j}<\delta
$$
for some $j$.


::: pf-proof

The open intervals
$$
(x-\delta,x+\delta),
\qquad
x\in[0,1],
$$
form an open cover of the compact interval $[0,1]$.
Choose a finite subcover and let its centers be $x_1,\ldots,x_m$.

:::

:::

::: {.pf-step #s1-6}

There exists $N$ such that for every $n\ge N$ and every
$$
j=1,\ldots,m,
$$
one has
$$
\abs{f_n(x_j)-f(x_j)}<\frac{\varepsilon}{3}.
$$


::: pf-proof

For each fixed $x_j$, pointwise convergence gives an index $N_j$ such that the displayed estimate holds for $n\ge N_j$.
Take
$$
N=\max_jN_j.
$$

:::

:::

::: {.pf-step #s1-7}

For every $n\ge N$ and every $x\in[0,1]$,
$$
\abs{f_n(x)-f(x)}<\varepsilon.
$$


::: pf-proof

Choose $x_j$ with
$$
\abs{x-x_j}<\delta
$$
as in step [](#s1-5){.pf-ref}.
Then steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref} give
$$
\begin{aligned}
\abs{f_n(x)-f(x)}
&\le
\abs{f_n(x)-f_n(x_j)}
+
\abs{f_n(x_j)-f(x_j)}
+
\abs{f(x_j)-f(x)}\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}\\
&=
\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

Thus equicontinuity plus pointwise convergence implies uniform convergence.


::: pf-proof

Step [](#s1-7){.pf-ref} is exactly the definition of uniform convergence.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
f_n\to f\text{ uniformly}
\iff
\{f_n\}\text{ is equicontinuous}
}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} proves the forward implication, and step [](#s1-8){.pf-ref} proves the reverse implication.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required equivalence.

:::

:::

:::
