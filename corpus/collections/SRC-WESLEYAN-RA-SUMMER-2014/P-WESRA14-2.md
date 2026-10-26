---
schema: qual/card@1
id: P-WESRA14-2
kind: problem
title: 'Three theorem/definition statements with examples or uses'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Choose any three of the following and state/define them accurately.
For each definition give a quick example; for each theorem briefly indicate a use.

1. Monotone Convergence Theorem;

2. Radon–Nikodym Theorem;

3. Hahn Decomposition Theorem;

4. unimodularity of a locally compact Hausdorff topological group;

5. regular content.
:::

Choose items (1), (2), and (3).

::: pf

::: pf-step

**Monotone Convergence Theorem.**

Let
\[
(X,\mathcal M,\mu)
\]
be a measure space and let
\[
0\le f_1\le f_2\le\cdots
\]
be measurable functions such that
\[
f_n(x)\uparrow f(x)
\]
for almost every
\[
x\in X.
\]
Then
\[
\boxed{
\int_X f\,d\mu
=
\lim_{n\to\infty}
\int_X f_n\,d\mu,
}
\]
where either side is allowed to be
\[
+\infty.
\]


::: pf-proof

This is the standard Beppo Levi monotone convergence theorem.
The nonnegativity and monotonicity hypotheses are essential to this exact
formulation.

:::

:::

::: pf-step

A standard use of monotone convergence is to justify interchange of
an infinite sum and an integral for nonnegative measurable functions.


::: pf-proof

If
\[
g_k\ge0
\]
are measurable, define
\[
f_n
=
\sum_{k=1}^n g_k.
\]
Then
\[
f_n\uparrow
\sum_{k=1}^{\infty}g_k.
\]
Hence
\[
\int_X
\sum_{k=1}^{\infty}g_k
\,d\mu
=
\sum_{k=1}^{\infty}
\int_X g_k\,d\mu.
\]
This is Tonelli's theorem for a countable sum in its simplest form.

:::

:::

::: pf-step

**Radon--Nikodym Theorem.**

Let
\[
(X,\mathcal M)
\]
be a measurable space, let
\[
\mu
\]
be a
\[
\sigma\text{-finite}
\]
positive measure, and let
\[
\nu
\]
be a
\[
\sigma\text{-finite}
\]
positive measure satisfying
\[
\nu\ll\mu.
\]
Then there exists a measurable function
\[
h:X\to[0,\infty]
\]
such that
\[
\boxed{
\nu(E)
=
\int_E h\,d\mu
}
\]
for every
\[
E\in\mathcal M.
\]
The function $h$ is unique
\[
\mu\text{-almost everywhere}
\]
and is denoted
\[
\frac{d\nu}{d\mu}.
\]


::: pf-proof

This is the standard
\[
\sigma\text{-finite}
\]
positive-measure form of the Radon--Nikodym theorem.
There is an analogous version for finite signed or complex measures.

:::

:::

::: pf-step

A standard use of Radon--Nikodym is to represent absolutely
continuous measures by densities.


::: pf-proof

If
\[
\nu\ll\lambda
\]
on
\[
\mathbb R
\]
with
\[
\lambda
\]
Lebesgue measure, then there is a measurable
\[
h\ge0
\]
such that
\[
\nu(E)
=
\int_E h(x)\,dx.
\]
Thus the measure can be recovered from the density
\[
h
=
\frac{d\nu}{d\lambda}.
\]
This is the measure-theoretic foundation of probability density functions.

:::

:::

::: pf-step

**Hahn Decomposition Theorem.**

Let
\[
\nu
\]
be a signed measure on
\[
(X,\mathcal M).
\]
Then there exist disjoint measurable sets
\[
P,N\in\mathcal M
\]
such that
\[
X=P\sqcup N,
\]
with the following properties:

- every measurable
  \[
  E\subseteq P
  \]
  satisfies
  \[
  \nu(E)\ge0;
  \]
- every measurable
  \[
  E\subseteq N
  \]
  satisfies
  \[
  \nu(E)\le0.
  \]


::: pf-proof

The sets $P$ and $N$ are called a positive set and a negative set for
$\nu$.
The decomposition is unique up to
\[
\nu\text{-null}
\]
sets in the standard sense.

:::

:::

::: pf-step

A standard use of Hahn decomposition is the Jordan decomposition of
a signed measure.


::: pf-proof

Given a Hahn decomposition
\[
X=P\sqcup N,
\]
define
\[
\nu^+(E)
\coloneqq
\nu(E\cap P)
\]
and
\[
\nu^-(E)
\coloneqq
-\nu(E\cap N).
\]
Then
\[
\nu^+,
\nu^-
\]
are positive measures and
\[
\boxed{
\nu
=
\nu^+-\nu^-.
}
\]
This is the Jordan decomposition of $\nu$.

:::

:::

::: pf-qed

Steps <1>1--<1>2 give one theorem and a use,
steps <1>3--<1>4 give a second theorem and a use,
and steps <1>5--<1>6 give a third theorem and a use.

:::

:::
