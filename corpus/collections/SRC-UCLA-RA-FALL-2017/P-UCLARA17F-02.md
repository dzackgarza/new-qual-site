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
$$
f_n(x)\to f(x)
$$
for almost every $x\in[0,1]$, and assume
$$
\sup_n\norm{f_n}_2\le M.
$$

::: pf

::: {.pf-step #s1-1}

The limit $f$ belongs to $L^2([0,1])$ and satisfies
$$
\boxed{\norm{f}_2\le M}.
$$


::: pf-proof

By Fatou's lemma,
$$
\int_0^1\abs{f}^2
\le
\liminf_{n\to\infty}
\int_0^1\abs{f_n}^2
\le
M^2.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
h_n(x)\to0}
$$
for almost every $x$.


::: pf-proof

This is immediate from the assumed a.e. convergence $f_n\to f$.

:::

:::

::: {.pf-step #s1-3}

The sequence $(h_n)$ is uniformly bounded in $L^2$:
$$
\boxed{
\norm{h_n}_2\le2M}.
$$


::: pf-proof

By the triangle inequality and step [](#s1-1){.pf-ref},
$$
\norm{h_n}_2
\le
\norm{f_n}_2+\norm{f}_2
\le
M+M
=
2M.
$$

:::

:::

::: {.pf-step #s1-4}

Choose $\delta>0$ so small that
$$
\boxed{
2M\sqrt\delta<\frac{\varepsilon}{2}}.
$$


::: pf-proof

The left-hand side tends to $0$ as $\delta\downarrow0$.

:::

:::

::: {.pf-step #s1-5}

By Egorov's theorem, there exists a measurable set
$$
E\subset[0,1]
$$
with
$$
\setmeasure{E}<\delta
$$
such that $h_n\to0$ uniformly on
$$
[0,1]\setminus E.
$$


::: pf-proof

The underlying measure space has finite measure, and $h_n\to0$ almost everywhere by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

For sufficiently large $n$,
$$
\boxed{
\sup_{x\in[0,1]\setminus E}\abs{h_n(x)}
<
\frac{\varepsilon}{2}}.
$$


::: pf-proof

Use the uniform convergence from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Hence for all sufficiently large $n$,
$$
\int_{[0,1]\setminus E}
\abs{h_n(x)}\,dx
<
\frac{\varepsilon}{2}.
$$


::: pf-proof

The complement has measure at most $1$, so
$$
\int_{[0,1]\setminus E}\abs{h_n}
\le
\sup_{[0,1]\setminus E}\abs{h_n}
\cdot
\setmeasure{[0,1]\setminus E}
<
\frac{\varepsilon}{2}.
$$

:::

:::

::: pf-step

On $E$,
$$
\int_E\abs{h_n}
\le
\norm{h_n}_2\,\setmeasure{E}^{1/2}.
$$


::: pf-proof

Apply Cauchy--Schwarz:
$$
\int_E\abs{h_n}
=
\int_E\abs{h_n}\cdot1
\le
\left(
\int_E\abs{h_n}^2
\right)^{1/2}
\setmeasure{E}^{1/2}.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\int_E\abs{h_n}
<
\frac{\varepsilon}{2}
$$
for every $n$.


::: pf-proof

Use step [](#s1-3){.pf-ref}, the bound $\setmeasure{E}<\delta$, and step [](#s1-4){.pf-ref}:
$$
\int_E\abs{h_n}
\le
2M\sqrt{\setmeasure{E}}
<
2M\sqrt\delta
<
\frac{\varepsilon}{2}.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{
\norm{h_n}_1\to0}.
$$


::: pf-proof

For all sufficiently large $n$,
$$
\norm{h_n}_1
=
\int_{[0,1]\setminus E}\abs{h_n}
+
\int_E\abs{h_n}
<
\varepsilon
$$
by steps [](#s1-7){.pf-ref} and [](#s1-9){.pf-ref}.

:::

:::

::: pf-step

For $R>0$, define the truncation
$$
g_R
=
g\,\mathbf 1_{\{\abs{g}\le R\}}.
$$


::: pf-proof

This is a measurable bounded function.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\boxed{
g_R\in L^\infty\cap L^2}
$$
and
$$
\boxed{
\norm{g-g_R}_2\to0}
$$
as $R\to\infty$.


::: pf-proof

The function $g_R$ is bounded by $R$, hence lies in $L^\infty$, and clearly lies in $L^2$.

Moreover,
$$
\abs{g-g_R}^2
=
\abs{g}^2\mathbf 1_{\{\abs{g}>R\}}
\to0
$$
pointwise and is dominated by $\abs{g}^2\in L^1$. Dominated convergence gives the $L^2$-convergence.

:::

:::

::: {.pf-step #s1-13}

For fixed $R$,
$$
\boxed{
\int_0^1h_n g_R\to0}.
$$


::: pf-proof

Since $g_R\in L^\infty$,
$$
\abs{
\int h_n g_R
}
\le
\norm{g_R}_\infty
\norm{h_n}_1.
$$
Apply step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

For every $n$,
$$
\abs{
\int_0^1
h_n(g-g_R)
}
\le
2M\,\norm{g-g_R}_2.
$$


::: pf-proof

By Cauchy--Schwarz and step [](#s1-3){.pf-ref},
$$
\abs{
\int h_n(g-g_R)
}
\le
\norm{h_n}_2
\norm{g-g_R}_2
\le
2M\norm{g-g_R}_2.
$$

:::

:::

::: {.pf-step #s1-15}

Given $\varepsilon>0$, choose $R$ so large that
$$
2M\norm{g-g_R}_2
<
\frac{\varepsilon}{2}.
$$


::: pf-proof

Use the convergence in step [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

For this fixed $R$, choose $N$ so large that for $n\ge N$,
$$
\abs{
\int h_n g_R
}
<
\frac{\varepsilon}{2}.
$$


::: pf-proof

Use step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Then for $n\ge N$,
$$
\abs{
\int_0^1h_n g
}
<
\varepsilon.
$$


::: pf-proof

Split:
$$
\int h_n g
=
\int h_n g_R
+
\int h_n(g-g_R),
$$
and use steps [](#s1-14){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
\int_0^1f_n g
\to
\int_0^1f g}
$$
for every $g\in L^2([0,1])$.


::: pf-proof

Since
$$
h_n=f_n-f,
$$
step [](#s1-17){.pf-ref} says
$$
\int h_n g\to0.
$$

:::

:::

::: {.pf-step #s1-19}

Hence
$$
\boxed{
f_n\rightharpoonup f
\text{ weakly in }L^2([0,1]).}
$$


::: pf-proof

Step [](#s1-18){.pf-ref} is exactly the definition of weak convergence in the Hilbert space $L^2([0,1])$.

:::

:::

::: pf-qed

Step [](#s1-19){.pf-ref} is the required conclusion.

:::

:::

:::
