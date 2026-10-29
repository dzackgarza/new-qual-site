---
schema: qual/card@1
id: P-UCLARA12F-05
kind: problem
title: A quadratic identity under bounded L2 convergence
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
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $(f_n)$ be a sequence of functions $f_n:\RR^3\to\RR$ such that
\[
\sup_n\|f_n\|_{L^2}<\infty.
\]
Show that if $f_n$ converges almost everywhere to a function $f:\RR^3\to\RR$, then
\[
\int_{\RR^3}\left(|f_n|^2-|f_n-f|^2-|f|^2\right)\,dx\longrightarrow0.
\]
:::

::: {.solution}

Choose $M<\infty$ such that
$$
\|f_n\|_{L^2}\le M
$$
for every $n$.

::: pf

::: {.pf-step #s1-1}

The almost-everywhere limit $f$ belongs to $L^2(\RR^3)$.


::: pf-proof

By Fatou's lemma,
$$
\int_{\RR^3}|f|^2
\le
\liminf_{n\to\infty}
\int_{\RR^3}|f_n|^2
\le M^2.
$$

:::

:::

::: {.pf-step #s1-2}

The sequence $(f_n)$ converges weakly to $f$ in $L^2(\RR^3)$.


::: pf-proof

This is exactly the result of `P-UCLARA12F-01` applied with $p=2$: an almost-everywhere convergent sequence that is uniformly bounded in $L^p$, with $1<p<\infty$, converges weakly in $L^p$ to its almost-everywhere limit.

:::

:::

::: {.pf-step #s1-3}

For every $n$,
$$
|f_n|^2-|f_n-f|^2-|f|^2
=2f(f_n-f)
$$
almost everywhere.


::: pf-proof

Since the functions are real-valued,
$$
|f_n-f|^2
=|f_n|^2-2f_nf+|f|^2.
$$
Rearranging gives the displayed identity.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{
\int_{\RR^3}
\left(|f_n|^2-|f_n-f|^2-|f|^2\right)\,dx
\longrightarrow0.}
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref},
$$
\int_{\RR^3}
\left(|f_n|^2-|f_n-f|^2-|f|^2\right)
=2\int_{\RR^3}f(f_n-f).
$$
Since $f\in L^2$, it is an admissible test function for weak convergence. Step [](#s1-2){.pf-ref} therefore gives
$$
\int f f_n\to\int f^2,
$$
so the right-hand side tends to $0$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
