---
schema: qual/card@1
id: P-UCLARA16F-01
kind: problem
title: $L^1$ convergence from almost everywhere convergence and convergence of norms
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
We consider the space $L^1(\mu)$ of integrable functions on a measure space $(X,\mathcal M,\mu)$.
For $g\in L^1(\mu)$ let
$$
\lVert g\rVert_1=\int |g(x)|\,d\mu
$$
be the corresponding $L^1$-norm.
Suppose that $f$ and $f_n$, for $n\in\NN$, are functions in $L^1(\mu)$ such that

(i) $f_n(x)\to f(x)$ for $\mu$-almost every $x\in X$, and

(ii) $\lVert f_n\rVert_1\to\lVert f\rVert_1$.

Show that $\lVert f_n-f\rVert_1\to0$.
:::

::: {.solution}

Define
$$
g_n(x)
=
|f_n(x)|-|f_n(x)-f(x)|.
$$

::: pf

::: {.pf-step #s1-1}

For almost every $x\in X$,
$$
\boxed{
g_n(x)\to |f(x)|}.
$$


::: pf-proof

By hypothesis,
$$
f_n(x)\to f(x)
$$
for almost every $x$. Hence
$$
|f_n(x)|\to|f(x)|
$$
and
$$
|f_n(x)-f(x)|\to0.
$$
Subtract.

:::

:::

::: {.pf-step #s1-2}

For every $n$ and almost every $x$,
$$
\boxed{
|g_n(x)|
\le
|f(x)|}.
$$


::: pf-proof

Apply the reverse triangle inequality to the pair
$$
f_n(x)
\qquad\text{and}\qquad
f_n(x)-f(x):
$$
$$
\left|
|f_n(x)|
-
|f_n(x)-f(x)|
\right|
\le
|f(x)|.
$$
The left-hand side is $|g_n(x)|$.

:::

:::

::: {.pf-step #s1-3}

Since
$$
f\in L^1(\mu),
$$
the function $|f|$ is integrable.


::: pf-proof

This is exactly the definition of membership in $L^1(\mu)$.

:::

:::

::: {.pf-step #s1-4}

Therefore, by the dominated convergence theorem,
$$
\boxed{
\int g_n\,d\mu
\longrightarrow
\int |f|\,d\mu}.
$$


::: pf-proof

Use pointwise almost-everywhere convergence from step [](#s1-1){.pf-ref} and domination by the integrable function $|f|$ from steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For every $n$,
$$
\int g_n\,d\mu
=
\|f_n\|_1-\|f_n-f\|_1.
$$


::: pf-proof

By definition,
$$
g_n
=
|f_n|-|f_n-f|.
$$
Both terms are integrable because
$$
f_n,f\in L^1
$$
implies
$$
f_n-f\in L^1.
$$
Integrate term by term.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
\|f_n\|_1-\|f_n-f\|_1
\longrightarrow
\|f\|_1}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

By hypothesis,
$$
\boxed{
\|f_n\|_1\to\|f\|_1}.
$$


::: pf-proof

This is assumption (ii).

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\|f_n-f\|_1\to0}.
$$


::: pf-proof

From step [](#s1-6){.pf-ref},
$$
\|f_n-f\|_1
=
\|f_n\|_1
-
\left(
\|f_n\|_1-\|f_n-f\|_1
\right).
$$
The first term tends to $\|f\|_1$ by step [](#s1-7){.pf-ref}, and the parenthesized term tends to $\|f\|_1$ by step [](#s1-6){.pf-ref}. Their difference tends to $0$.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required $L^1$-convergence.

:::

:::

:::
