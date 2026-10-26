---
schema: qual/card@1
id: P-MAXAT-6-09
kind: problem
title: Maxim algebraic topology 6.9
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 9 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that $\mathbb { C P } ^ { 2 n }$ is not an oriented boundary.
(Hint: use the Pontrjagin number)
:::

Let
\[
M=\mathbb{CP}^{2n},
\qquad n\geq1,
\]
and let
\[
x\in H^2(M;\mathbb Z)
\]
be the positive generator, normalized by
\[
\langle x^{2n},[M]\rangle=1.
\]

::: pf

::: pf-step

The total Pontryagin class of $M$ is
\[
p(TM)=(1+x^2)^{2n+1}.
\]


::: pf-proof

The complex Euler sequence gives the stable complex-bundle identity
\[
T\mathbb{CP}^{2n}\oplus\varepsilon^1_{\mathbb C}
\cong(2n+1)\gamma^*,
\]
where $c_1(\gamma^*)=x$. The underlying real bundle of $\gamma^*$ has total Pontryagin class $1+x^2$. Pontryagin classes are stable and multiplicative, giving the formula.

:::

:::

::: pf-step

In particular,
\[
p_n(TM)=\binom{2n+1}{n}x^{2n}.
\]


::: pf-proof

Expand the formula in step <1>1:
\[
(1+x^2)^{2n+1}
=\sum_{j=0}^{2n+1}\binom{2n+1}{j}x^{2j}.
\]
The degree-$4n$ component is obtained at $j=n$ and is exactly $p_n$.

:::

:::

::: pf-step

Hence the Pontryagin number
\[
\langle p_n(TM),[M]\rangle
\]
is nonzero:
\[
\langle p_n(TM),[M]\rangle
=\binom{2n+1}{n}\ne0.
\]


::: pf-proof

Substitute step <1>2 and use the normalization
\[
\langle x^{2n},[M]\rangle=1.
\]
The binomial coefficient is a positive integer.

:::

:::

::: pf-step

Every Pontryagin number of an oriented boundary is zero.


::: pf-proof

Suppose a closed oriented $4n$-manifold $N$ is the oriented boundary of a compact oriented $(4n+1)$-manifold $W$. Along the boundary,
\[
TW|_N\cong TN\oplus\varepsilon^1,
\]
so stability and naturality give
\[
p_i(TN)=i^*p_i(TW),
\]
where $i:N\hookrightarrow W$. Thus every degree-$4n$ polynomial $P(p_1(TN),\ldots,p_n(TN))$ is the restriction of the corresponding class on $W$. Its characteristic number is
\[
\langle i^*P,[N]\rangle.
\]
Since $[N]=\partial[W,N]$, the Kronecker pairing with a restricted absolute cohomology class vanishes by the cohomological boundary formula. Hence every Pontryagin number of $N$ is zero.

:::

:::

::: pf-step

Therefore $\mathbb{CP}^{2n}$ cannot be an oriented boundary.


::: pf-proof

If $M=\mathbb{CP}^{2n}$ bounded orientably, step <1>4 would force
\[
\langle p_n(TM),[M]\rangle=0.
\]
Step <1>3 computes the same integer as the nonzero value $\binom{2n+1}{n}$, a contradiction.

:::

:::

::: pf-step

Thus
\[
\boxed{\mathbb{CP}^{2n}\text{ is not an oriented boundary}.}
\]


::: pf-proof

This is the conclusion of step <1>5.

:::

:::

::: pf-qed

Step <1>6 proves the required oriented non-bordism statement.

:::

:::
