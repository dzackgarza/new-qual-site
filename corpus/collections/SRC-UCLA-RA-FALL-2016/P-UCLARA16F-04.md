---
schema: qual/card@1
id: P-UCLARA16F-04
kind: problem
title: $L^2$ is meager in $L^1([0,1])$
classification:
  areas:
  - real-analysis
  topics:
  - Baire Category
  - L¹
  - L²
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

For each integer $n\ge1$, define
$$
\boxed{
A_n
=
\left\{
f\in L^2([0,1]):
\norm{f}_2\le n
\right\}.}
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{
L^2([0,1])
=
\bigcup_{n=1}^{\infty}A_n}.
$$


::: pf-proof

If $f\in L^2$, then $\norm{f}_2<\infty$, so choose an integer $n\ge\norm{f}_2$. Then $f\in A_n$. The reverse inclusion is immediate from the definition of $A_n$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
f_j\in A_n
$$
and suppose
$$
f_j\to f
$$
in $L^1([0,1])$.


::: pf-proof

This is the setup for proving that $A_n$ is closed in the $L^1$-topology.

:::

:::

::: {.pf-step #s1-3}

There exists a subsequence
$$
(f_{j_k})
$$
such that
$$
\boxed{
f_{j_k}(x)\to f(x)}
$$
for almost every $x\in[0,1]$.


::: pf-proof

From $L^1$-convergence, choose a subsequence satisfying
$$
\norm{f_{j_k}-f}_1<2^{-k}.
$$
Then
$$
\sum_{k=1}^{\infty}
\norm{f_{j_k}-f}_1
<
\infty.
$$
By Tonelli,
$$
\int_0^1
\sum_{k=1}^{\infty}
\abs{f_{j_k}(x)-f(x)}
\,dx
<
\infty.
$$
Hence for almost every $x$,
$$
\sum_k\abs{f_{j_k}(x)-f(x)}<\infty,
$$
which implies
$$
f_{j_k}(x)-f(x)\to0.
$$

:::

:::

::: {.pf-step #s1-4}

Fatou's lemma gives
$$
\int_0^1\abs{f(x)}^2\,dx
\le
\liminf_{k\to\infty}
\int_0^1\abs{f_{j_k}(x)}^2\,dx.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\abs{f_{j_k}(x)}^2\to\abs{f(x)}^2
$$
almost everywhere, and the integrands are nonnegative. Apply Fatou's lemma.

:::

:::

::: {.pf-step #s1-5}

Since each $f_{j_k}\in A_n$,
$$
\int_0^1\abs{f_{j_k}}^2\,dx
\le
n^2.
$$


::: pf-proof

This is equivalent to
$$
\norm{f_{j_k}}_2\le n.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\int_0^1\abs{f}^2\,dx
\le
n^2}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
f\in A_n}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} shows $f\in L^2$ and
$$
\norm{f}_2\le n.
$$

:::

:::

::: pf-step

Thus $A_n$ is closed in $L^1([0,1])$.


::: pf-proof

Every $L^1$-limit of a sequence in $A_n$ remains in $A_n$ by steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: pf-step

Define
$$
h(x)=x^{-1/2}
\qquad
(0<x\le1).
$$


::: pf-proof

This is a measurable function on $(0,1]$.

:::

:::

::: {.pf-step #s1-10}

One has
$$
\boxed{
h\in L^1([0,1])}.
$$


::: pf-proof

$$
\int_0^1x^{-1/2}\,dx
=
2
<
\infty.
$$

:::

:::

::: {.pf-step #s1-11}

One has
$$
\boxed{
h\notin L^2([0,1])}.
$$


::: pf-proof

$$
\int_0^1\abs{h(x)}^2\,dx
=
\int_0^1\frac{dx}{x}
=
\infty.
$$

:::

:::

::: {.pf-step #s1-12}

Choose
$$
\lambda>0
$$
so small that
$$
\boxed{
\lambda\norm{h}_1<\varepsilon}.
$$


::: pf-proof

The number $\norm{h}_1=2$ is finite by step [](#s1-10){.pf-ref}, so any
$$
0<\lambda<\varepsilon/2
$$
works.

:::

:::

::: {.pf-step #s1-13}

Define
$$
\boxed{
g=f+\lambda h}.
$$


::: pf-proof

Since
$$
f\in L^2([0,1])\subseteq L^1([0,1])
$$
and $h\in L^1$, the sum $g$ belongs to $L^1$.

:::

:::

::: {.pf-step #s1-14}

One has
$$
\boxed{
\norm{g-f}_1
=
\lambda\norm{h}_1
<
\varepsilon}.
$$


::: pf-proof

By definition,
$$
g-f=\lambda h.
$$
Use step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

The function $g$ does not belong to $L^2([0,1])$.


::: pf-proof

Suppose $g\in L^2$. Since $f\in L^2$, their difference
$$
g-f
=
\lambda h
$$
would also lie in $L^2$, because $L^2$ is a vector space. Since $\lambda\ne0$, this would imply $h\in L^2$, contradicting step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

Hence
$$
\boxed{
g\notin A_n}.
$$


::: pf-proof

The set $A_n$ is contained in $L^2$, while step [](#s1-15){.pf-ref} gives $g\notin L^2$.

:::

:::

::: {.pf-step #s1-17}

Therefore every $L^1$-ball around every $f\in A_n$ contains a point outside $A_n$.


::: pf-proof

Given arbitrary $\varepsilon>0$, steps [](#s1-13){.pf-ref} through [](#s1-16){.pf-ref} construct $g$ with
$$
\norm{g-f}_1<\varepsilon
$$
but
$$
g\notin A_n.
$$

:::

:::

::: {.pf-step #s1-18}

Thus
$$
\boxed{
\operatorname{int}_{L^1}(A_n)=\varnothing}.
$$


::: pf-proof

Step [](#s1-17){.pf-ref} is exactly the assertion that $A_n$ has empty interior.

:::

:::

::: {.pf-step #s1-19}

Since $A_n$ is closed and has empty interior, it is nowhere dense in $L^1$.


::: pf-proof

For a closed set,
$$
\overline{A_n}=A_n.
$$
Thus
$$
\operatorname{int}\overline{A_n}
=
\varnothing
$$
by step [](#s1-18){.pf-ref}.

:::

:::

::: pf-step

Finally,
$$
\boxed{
L^2([0,1])
=
\bigcup_{n=1}^{\infty}A_n}
$$
is a countable union of nowhere-dense subsets of $L^1([0,1])$.


::: pf-proof

Use steps [](#s1-1){.pf-ref} and [](#s1-19){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

Therefore
$$
\boxed{
L^2([0,1])
\text{ is meager in }L^1([0,1]).}
$$


::: pf-proof

This is the definition of a meager set.

:::

:::

::: pf-qed

Step [](#s1-21){.pf-ref} is the required conclusion.

:::

:::

:::
