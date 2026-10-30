---
schema: qual/card@1
id: P-UCLARA13F-11
kind: problem
title: 'An $L^2$-to-supremum norm bound forces finite dimension'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $S$ be a subspace of $C([0,1])$.
Write
$$
\norm{f}_\infty=\sup_{x\in[0,1]}\abs{f(x)},
\qquad
\norm{f}_2=\left(\int_0^1\abs{f(x)}^2\,dx\right)^{1/2}.
$$
Suppose there is $K\ge0$ such that
$$
\norm{f}_\infty\le K\norm{f}_2
$$
for every $f\in S$.
Show that $S$ is finite-dimensional.
:::

::: {.solution}

Argue by contradiction using an orthonormal sequence in the $L^2$ inner product.

::: pf

::: {.pf-step #s1-1}

Suppose that $S$ is infinite-dimensional.


::: pf-proof

This is the negation of the desired conclusion.

:::

:::

::: {.pf-step #s1-2}

There exists an infinite sequence $(f_n)$ in $S$ that is orthonormal for the $L^2$ inner product:
$$
\int_0^1 f_n(x)f_m(x)\,dx=\delta_{nm}.
$$


::: pf-proof

Inductively choose linearly independent vectors from the infinite-dimensional space $S$ and apply the Gram--Schmidt process using
$$
\langle f,g\rangle_2=\int_0^1f(x)g(x)\,dx.
$$
No nonzero continuous function has $L^2$ norm zero, so this is an inner product on $S$. Gram--Schmidt uses finite linear combinations, hence keeps every $f_n$ in $S$.

:::

:::

::: {.pf-step #s1-3}

For each $N\geq1$, define
$$
F_N(x)=\sum_{n=1}^N f_n(x)^2.
$$
Then
$$
\int_0^1F_N(x)\,dx=N.
$$


::: pf-proof

Each $f_n$ has $L^2$ norm $1$, so
$$
\int_0^1F_N
=\sum_{n=1}^N\int_0^1\abs{f_n}^2
=N.
$$

:::

:::

::: {.pf-step #s1-4}

Hence there exists $x_N\in[0,1]$ such that
$$
F_N(x_N)\geq N.
$$


::: pf-proof

If $F_N(x)<N$ for every $x$, continuity on the compact interval would give $\int_0^1F_N<N$, contradicting step [](#s1-3){.pf-ref}. Equivalently, the maximum of a nonnegative function is at least its average.

:::

:::

::: pf-step

Define coefficients
$$
c_n=f_n(x_N)
\qquad(1\leq n\leq N)
$$
and the function
$$
g_N=\sum_{n=1}^Nc_nf_n\in S.
$$


::: pf-proof

This is a finite linear combination of elements of the subspace $S$, so $g_N\in S$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
g_N(x_N)=F_N(x_N)
$$
and
$$
\norm{g_N}_2^2=F_N(x_N).
$$


::: pf-proof

By the definition of the coefficients,
$$
g_N(x_N)=\sum_{n=1}^Nf_n(x_N)^2=F_N(x_N).
$$
By orthonormality from step [](#s1-2){.pf-ref},
$$
\norm{g_N}_2^2
=\sum_{n=1}^N\abs{c_n}^2
=F_N(x_N).
$$

:::

:::

::: {.pf-step #s1-7}

The assumed norm inequality applied to $g_N$ gives
$$
F_N(x_N)
\leq K\sqrt{F_N(x_N)}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives
$$
F_N(x_N)=\abs{g_N(x_N)}\leq\norm{g_N}_\infty
\leq K\norm{g_N}_2
=K\sqrt{F_N(x_N)}.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
F_N(x_N)\leq K^2.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $F_N(x_N)\geq N>0$, so divide the inequality in step [](#s1-7){.pf-ref} by its positive square root and square the result.

:::

:::

::: {.pf-step #s1-9}

Steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref} imply
$$
N\leq K^2
$$
for every positive integer $N$, a contradiction.


::: pf-proof

Step [](#s1-4){.pf-ref} gives $N\leq F_N(x_N)$, and step [](#s1-8){.pf-ref} gives $F_N(x_N)\leq K^2$. Taking an integer $N>K^2$ is impossible.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{S\text{ is finite-dimensional}.}
$$


::: pf-proof

The assumption of infinite dimension in step [](#s1-1){.pf-ref} led to the contradiction in step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
