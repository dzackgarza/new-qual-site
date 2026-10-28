---
schema: qual/card@1
id: P-UCLAB16F-05
kind: problem
title: Multipliers preserving a finite $\mathbb Q$-span of complex numbers are algebraic
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Let $\alpha_1, \ldots, \alpha_n$ be complex numbers, and $V = \{\sum_{i=1}^n a_i \alpha_i \mid a_i \in \QQ\}$ be the vector subspace of $\CC$ spanned by them over the field of rational numbers, $\QQ$. Let $\beta$ be a complex number such that $\beta V \subset V$, where $\beta V = \{\beta v \mid v \in V\}$. Show that $\beta$ is the root of a degree $n$ polynomial with rational coefficients.
:::

::: {.remark}

As printed, the statement has the degenerate exception
\[
V=\{0\}.
\]
If
\[
\alpha_1=\cdots=\alpha_n=0,
\]
then
\[
\beta V\subseteq V
\]
for every complex number $\beta$, including transcendental ones.
Assume therefore that
\[
V\ne\{0\},
\]
which is the intended nondegenerate case.

:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The $\mathbb Q$-dimension of $V$ satisfies
\[
1\le \dim_{\mathbb Q}V\le n.
\]


::: pf-proof

The space $V$ is generated over $\mathbb Q$ by the $n$ vectors
\[
\alpha_1,\ldots,\alpha_n,
\]
so its dimension is at most $n$.
The assumption
\[
V\ne\{0\}
\]
gives positive dimension.

:::

:::

::: {.pf-step #s1-2}

Choose
\[
0\ne v\in V.
\]
Then for every integer $k\ge0$,
\[
\beta^kv\in V.
\]


::: pf-proof

The case $k=0$ is immediate.
If
\[
\beta^kv\in V,
\]
then the hypothesis
\[
\beta V\subseteq V
\]
gives
\[
\beta^{k+1}v
=
\beta(\beta^kv)
\in V.
\]
Thus the claim follows by induction.

:::

:::

::: {.pf-step #s1-3}

Let
\[
d=\dim_{\mathbb Q}V.
\]
Then the $d+1$ vectors
\[
v,\beta v,\beta^2v,\ldots,\beta^dv
\]
are linearly dependent over $\mathbb Q$.


::: pf-proof

All these vectors lie in $V$ by step [](#s1-2){.pf-ref}.
The vector space $V$ has dimension $d$, so any $d+1$ vectors in it are linearly dependent.

:::

:::

::: {.pf-step #s1-4}

There exist rational numbers
\[
c_0,\ldots,c_d,
\]
not all zero, such that
\[
\sum_{k=0}^d c_k\beta^kv=0.
\]


::: pf-proof

This is exactly the linear dependence supplied by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Since $v\ne0$,
\[
\sum_{k=0}^d c_k\beta^k=0.
\]


::: pf-proof

Factor the relation in step [](#s1-4){.pf-ref} inside the complex numbers:
\[
\left(
\sum_{k=0}^d c_k\beta^k
\right)v
=0.
\]
Because $v$ is a nonzero complex number, division by $v$ gives the displayed scalar equation.

:::

:::

::: {.pf-step #s1-6}

Thus $\beta$ is a root of a nonzero polynomial
\[
p(X)=\sum_{k=0}^d c_kX^k
\in\mathbb Q[X]
\]
of degree at most $d\le n$.


::: pf-proof

The coefficients are rational by step [](#s1-4){.pf-ref}, the polynomial is nonzero because the coefficients are not all zero, and step [](#s1-5){.pf-ref} gives
\[
p(\beta)=0.
\]
Its degree is at most $d$, and step [](#s1-1){.pf-ref} gives
\[
d\le n.
\]

:::

:::

::: {.pf-step #s1-7}

If a polynomial of degree exactly $n$ is required, define
\[
P(X)=X^{\,n-\deg p}p(X).
\]
Then
\[
\deg P=n
\]
and
\[
P(\beta)=0.
\]


::: pf-proof

The exponent
\[
n-\deg p
\]
is a nonnegative integer by step [](#s1-6){.pf-ref}.
Thus $P\in\mathbb Q[X]$ has degree exactly $n$.
Since
\[
p(\beta)=0,
\]
one also has
\[
P(\beta)=0.
\]

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} prove the intended statement under the necessary hypothesis
\[
V\ne\{0\},
\]
while the opening observation records the counterexample in the omitted zero-span case.

:::

:::

:::
