---
schema: qual/card@1
id: P-WESRA03-II1
kind: problem
title: Integration against a nonnegative function defines a measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 1 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf.
---

::: {.problem}
Let $f\ge 0$ on the Lebesgue measure space $(\RR,\mathcal B(\RR),m)$.
Prove that the set function
\[
A\longmapsto \int_A f\,dm
\]
is a measure.
:::

::: {.solution}

Define
\[
\mu_f(A)
=
\int_A f\,dm
=
\int_{\RR}\mathbf 1_A f\,dm
\]
for every Borel set
\[
A\in\mathcal B(\RR).
\]

::: pf

::: {.pf-step #s1-1}

For every Borel set \(A\),
\[
\boxed{\mu_f(A)\in[0,\infty]}.
\]


::: pf-proof

Since
\[
f\ge0
\]
and
\[
\mathbf 1_A\ge0,
\]
the function
\[
\mathbf 1_Af
\]
is nonnegative and measurable. Its Lebesgue integral therefore lies in
\([0,\infty]\).

:::

:::

::: {.pf-step #s1-2}

One has
\[
\boxed{\mu_f(\varnothing)=0}.
\]


::: pf-proof

The indicator of the empty set is the zero function:
\[
\mathbf 1_{\varnothing}=0.
\]
Hence
\[
\mu_f(\varnothing)
=
\int_{\RR}0\cdot f\,dm
=
0.
\]

:::

:::

::: pf-step

Let
\[
A_1,A_2,\dots
\]
be pairwise disjoint Borel sets, and set
\[
A=\bigcup_{n=1}^{\infty}A_n.
\]


::: pf-proof

A countable union of Borel sets is Borel, so \(A\in\mathcal B(\RR)\).

:::

:::

::: {.pf-step #s1-4}

For every \(N\ge1\),
\[
\boxed{
\mathbf 1_{\bigcup_{n=1}^{N}A_n}
=
\sum_{n=1}^{N}\mathbf 1_{A_n}}.
\]


::: pf-proof

Because the sets \(A_n\) are pairwise disjoint, at each point \(x\) at most
one of the indicators \(\mathbf 1_{A_n}(x)\) is equal to \(1\). Thus the sum
is \(1\) exactly when \(x\) belongs to the finite union.

:::

:::

::: {.pf-step #s1-5}

Multiplying by \(f\),
\[
\boxed{
\mathbf 1_{\bigcup_{n=1}^{N}A_n}f
=
\sum_{n=1}^{N}\mathbf 1_{A_n}f}.
\]


::: pf-proof

Multiply the identity from step [](#s1-4){.pf-ref} by the nonnegative measurable function
\(f\).

:::

:::

::: {.pf-step #s1-6}

The sequence
\[
g_N
=
\mathbf 1_{\bigcup_{n=1}^{N}A_n}f
\]
is nondecreasing and converges pointwise to
\[
\mathbf 1_Af.
\]


::: pf-proof

The finite unions
\[
\bigcup_{n=1}^{N}A_n
\]
increase with \(N\), so their indicators increase pointwise to
\[
\mathbf 1_{\bigcup_{n=1}^{\infty}A_n}
=
\mathbf 1_A.
\]
Since \(f\ge0\), multiplication by \(f\) preserves the inequalities and the
pointwise limit.

:::

:::

::: {.pf-step #s1-7}

By the monotone convergence theorem,
\[
\mu_f(A)
=
\lim_{N\to\infty}
\int_{\RR}g_N\,dm.
\]


::: pf-proof

Step [](#s1-6){.pf-ref} gives a monotone increasing sequence of nonnegative measurable
functions converging pointwise to \(\mathbf 1_Af\). Apply the monotone
convergence theorem:
\[
\int_{\RR}\mathbf 1_Af\,dm
=
\lim_{N\to\infty}\int_{\RR}g_N\,dm.
\]

:::

:::

::: {.pf-step #s1-8}

For every \(N\),
\[
\int_{\RR}g_N\,dm
=
\sum_{n=1}^{N}\mu_f(A_n).
\]


::: pf-proof

By step [](#s1-5){.pf-ref} and finite additivity of the Lebesgue integral,
\[
\begin{aligned}
\int_{\RR}g_N\,dm
&=
\int_{\RR}
\sum_{n=1}^{N}\mathbf 1_{A_n}f\,dm\\
&=
\sum_{n=1}^{N}
\int_{\RR}\mathbf 1_{A_n}f\,dm\\
&=
\sum_{n=1}^{N}\mu_f(A_n).
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-9}

Therefore
\[
\boxed{
\mu_f\!\left(
\bigcup_{n=1}^{\infty}A_n
\right)
=
\sum_{n=1}^{\infty}\mu_f(A_n)}.
\]


::: pf-proof

Combine steps [](#s1-7){.pf-ref} and [](#s1-8){.pf-ref}:
\[
\begin{aligned}
\mu_f(A)
&=
\lim_{N\to\infty}
\sum_{n=1}^{N}\mu_f(A_n)\\
&=
\sum_{n=1}^{\infty}\mu_f(A_n).
\end{aligned}
\]
The equality is valid in \([0,\infty]\).

:::

:::

::: {.pf-step #s1-10}

Hence
\[
\boxed{
A\longmapsto\int_A f\,dm
}
\]
is a measure on
\[
(\RR,\mathcal B(\RR)).
\]


::: pf-proof

By step [](#s1-1){.pf-ref} the set function is nonnegative, by step [](#s1-2){.pf-ref} it vanishes on
the empty set, and by step [](#s1-9){.pf-ref} it is countably additive on pairwise disjoint
Borel sets. These are exactly the defining axioms of a measure.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
