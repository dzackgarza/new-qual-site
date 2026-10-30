---
schema: qual/card@1
id: P-UCLARA11F-01
kind: problem
title: Egorov theorem on almost-uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Egorov
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(f_n)$ be measurable functions on $[0,1]$ converging almost everywhere to a measurable function $f$.
Prove that for every $\varepsilon>0$ there exists a measurable set $E\subseteq[0,1]$ with $\lambda(E)<\varepsilon$ such that $f_n\to f$ uniformly on $[0,1]\setminus E$.
:::

::: {.solution}

Fix
$$
\varepsilon>0.
$$

For each integer $m\ge1$ and $N\ge1$, define
$$
\boxed{
A_{m,N}
=
\bigcup_{n\ge N}
\left\{
x\in[0,1]:
\abs{f_n(x)-f(x)}\ge\frac1m
\right\}.}
$$

::: pf

::: pf-step

Each set $A_{m,N}$ is measurable.


::: pf-proof

The functions $f_n$ and $f$ are measurable, so
$$
\abs{f_n-f}
$$
is measurable. Hence each set
$$
\left\{\abs{f_n-f}\ge\frac1m\right\}
$$
is measurable, and a countable union of measurable sets is measurable.

:::

:::

::: {.pf-step #s1-2}

For fixed $m$, the sets $A_{m,N}$ decrease with $N$:
$$
\boxed{
A_{m,N+1}\subseteq A_{m,N}}.
$$


::: pf-proof

The union defining $A_{m,N+1}$ runs over the smaller index set
$$
\{n\ge N+1\}\subseteq\{n\ge N\}.
$$

:::

:::

::: {.pf-step #s1-3}

For fixed $m$,
$$
\bigcap_{N=1}^{\infty}A_{m,N}
$$
is contained in the set where $f_n$ fails to converge to $f$.


::: pf-proof

If
$$
x\in\bigcap_N A_{m,N},
$$
then for every $N$ there exists $n\ge N$ such that
$$
\abs{f_n(x)-f(x)}\ge\frac1m.
$$
Thus the difference does not eventually stay below $1/m$, so $f_n(x)\not\to f(x)$.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
\lambda\left(
\bigcap_{N=1}^{\infty}A_{m,N}
\right)=0}.
$$


::: pf-proof

The sequence converges to $f$ almost everywhere, so the failure set has Lebesgue measure zero. Apply step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Because
$$
A_{m,1}\subseteq[0,1],
$$
one has
$$
\lambda(A_{m,1})\le1<\infty.
$$


::: pf-proof

Lebesgue measure of $[0,1]$ is $1$.

:::

:::

::: {.pf-step #s1-6}

By continuity from above of measure,
$$
\boxed{
\lambda(A_{m,N})\longrightarrow0
\qquad(N\to\infty)}
$$
for every fixed $m$.


::: pf-proof

The sets decrease by step [](#s1-2){.pf-ref}, the first has finite measure by step [](#s1-5){.pf-ref}, and their intersection has measure zero by step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For each $m\ge1$, choose $N_m$ such that
$$
\boxed{
\lambda(A_{m,N_m})
<
\frac{\varepsilon}{2^m}}.
$$


::: pf-proof

This is possible by step [](#s1-6){.pf-ref}.

:::

:::

::: pf-step

Define
$$
\boxed{
E
=
\bigcup_{m=1}^{\infty}
A_{m,N_m}}.
$$


::: pf-proof

This is a countable union of measurable sets, hence measurable.

:::

:::

::: {.pf-step #s1-9}

The exceptional set satisfies
$$
\boxed{
\lambda(E)<\varepsilon}.
$$


::: pf-proof

By countable subadditivity and step [](#s1-7){.pf-ref},
$$
\lambda(E)
\le
\sum_{m=1}^{\infty}
\lambda(A_{m,N_m})
<
\sum_{m=1}^{\infty}
\frac{\varepsilon}{2^m}
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-10}

For every $m\ge1$, every $x\in F$, and every $n\ge N_m$,
$$
\boxed{
\abs{f_n(x)-f(x)}<\frac1m}.
$$


::: pf-proof

Since
$$
x\notin E,
$$
one has
$$
x\notin A_{m,N_m}.
$$
By definition of $A_{m,N_m}$, this means there is no $n\ge N_m$ for which
$$
\abs{f_n(x)-f(x)}\ge\frac1m.
$$

:::

:::

::: pf-step

Let
$$
\delta>0.
$$
Choose $m$ so large that
$$
\frac1m<\delta.
$$


::: pf-proof

The sequence $1/m$ tends to $0$.

:::

:::

::: {.pf-step #s1-12}

Then for every
$$
n\ge N_m
$$
and every
$$
x\in F,
$$
$$
\boxed{
\abs{f_n(x)-f(x)}<\delta}.
$$


::: pf-proof

By step [](#s1-10){.pf-ref},
$$
\abs{f_n(x)-f(x)}<\frac1m<\delta.
$$

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
f_n\to f
\text{ uniformly on }
[0,1]\setminus E}.
$$


::: pf-proof

Step [](#s1-12){.pf-ref} is exactly the definition of uniform convergence on $F$: for the given $\delta>0$, the single index $N_m$ works simultaneously for every $x\in F$.

:::

:::

::: {.pf-step #s1-14}

Thus for every $\varepsilon>0$, there exists a measurable set $E\subseteq[0,1]$ with
$$
\boxed{\lambda(E)<\varepsilon}
$$
such that $f_n\to f$ uniformly on
$$
\boxed{[0,1]\setminus E}.
$$


::: pf-proof

The measure estimate is step [](#s1-9){.pf-ref} and uniform convergence is step [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the required conclusion.

:::

:::

:::
