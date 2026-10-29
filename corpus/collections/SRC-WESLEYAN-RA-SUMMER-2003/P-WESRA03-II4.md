---
schema: qual/card@1
id: P-WESRA03-II4
kind: problem
title: Epsilon-delta absolute continuity for finite measures
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Absolute Continuity]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 4 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf.
---

::: {.problem}
Let $(X,\mathcal A)$ be a measurable space, and let $\mu$ and $\nu$ be finite measures on it.
Assume that for every $A\in\mathcal A$,
$$
\mu(A)=0\implies \nu(A)=0.
$$
Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\mu(A)<\delta\implies \nu(A)<\varepsilon.
$$
:::

::: {.solution}

Suppose, toward a contradiction, that the asserted $\varepsilon$-$\delta$
statement is false.

::: pf

::: {.pf-step #s1-1}

Then there exists
$$
\varepsilon_0>0
$$
such that for every $\delta>0$, there is a measurable set $A$ with
$$
\mu(A)<\delta
$$
but
$$
\nu(A)\ge\varepsilon_0.
$$


::: pf-proof

This is exactly the negation of
$$
\forall\varepsilon>0\ \exists\delta>0\
\forall A\in\mathcal A:
\mu(A)<\delta\Rightarrow\nu(A)<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-2}

For each $n\ge1$, choose
$$
A_n\in\mathcal A
$$
such that
$$
\boxed{
\mu(A_n)<2^{-n}}
$$
and
$$
\boxed{
\nu(A_n)\ge\varepsilon_0}.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} with
$$
\delta=2^{-n}.
$$

:::

:::

::: {.pf-step #s1-3}

Define
$$
\boxed{
B_n=\bigcup_{k=n}^{\infty}A_k}.
$$


::: pf-proof

This is a countable union of measurable sets, hence measurable.

:::

:::

::: {.pf-step #s1-4}

The sequence $(B_n)$ is decreasing:
$$
\boxed{
B_{n+1}\subseteq B_n}.
$$


::: pf-proof

The union defining $B_{n+1}$ omits the first set $A_n$ from the union
defining $B_n$.

:::

:::

::: pf-step

By countable subadditivity,
$$
\mu(B_n)
\le
\sum_{k=n}^{\infty}\mu(A_k).
$$


::: pf-proof

Apply countable subadditivity of the measure $\mu$ to the union in step
[](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Using step [](#s1-2){.pf-ref},
$$
\mu(B_n)
<
\sum_{k=n}^{\infty}2^{-k}
=
2^{1-n}.
$$


::: pf-proof

The geometric tail satisfies
$$
\sum_{k=n}^{\infty}2^{-k}
=
\frac{2^{-n}}{1-1/2}
=
2^{1-n}.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\mu(B_n)\longrightarrow0}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives
$$
0\le\mu(B_n)<2^{1-n}\to0.
$$
Apply the squeeze theorem.

:::

:::

::: {.pf-step #s1-8}

Let
$$
\boxed{
B=\bigcap_{n=1}^{\infty}B_n}.
$$
Then
$$
\boxed{\mu(B)=0}.
$$


::: pf-proof

Since
$$
B\subseteq B_n
$$
for every $n$,
$$
0\le\mu(B)\le\mu(B_n).
$$
Use step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

By the assumed absolute continuity,
$$
\boxed{\nu(B)=0}.
$$


::: pf-proof

The hypothesis says
$$
\mu(A)=0
\Rightarrow
\nu(A)=0
$$
for every measurable $A$. Apply it to $A=B$ using step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

For every $n$,
$$
A_n\subseteq B_n.
$$


::: pf-proof

The union defining $B_n$ includes the term $A_n$.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
\nu(B_n)\ge\nu(A_n)\ge\varepsilon_0}.
$$


::: pf-proof

Measures are monotone, so step [](#s1-10){.pf-ref} gives
$$
\nu(B_n)\ge\nu(A_n).
$$
Apply step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Since $\nu$ is finite,
$$
\nu(B_1)<\infty.
$$


::: pf-proof

The measure $\nu$ is finite on the whole space $X$, so
$$
\nu(B_1)\le\nu(X)<\infty.
$$

:::

:::

::: {.pf-step #s1-13}

By continuity from above,
$$
\boxed{
\nu(B_n)\longrightarrow\nu(B)}.
$$


::: pf-proof

The sets $B_n$ decrease by step [](#s1-4){.pf-ref}, and the first one has finite
$\nu$-measure by step [](#s1-12){.pf-ref}. The continuity-from-above theorem for measures
therefore gives
$$
\nu\left(\bigcap_{n=1}^{\infty}B_n\right)
=
\lim_{n\to\infty}\nu(B_n).
$$
The intersection is $B$.

:::

:::

::: {.pf-step #s1-14}

Steps [](#s1-11){.pf-ref} and [](#s1-13){.pf-ref} imply
$$
\boxed{
\nu(B)\ge\varepsilon_0}.
$$


::: pf-proof

Every term of the sequence $\nu(B_n)$ is at least $\varepsilon_0$, so
its limit is also at least $\varepsilon_0$.

:::

:::

::: {.pf-step #s1-15}

Steps [](#s1-9){.pf-ref} and [](#s1-14){.pf-ref} contradict one another.


::: pf-proof

Step [](#s1-9){.pf-ref} gives
$$
\nu(B)=0,
$$
while step [](#s1-14){.pf-ref} gives
$$
\nu(B)\ge\varepsilon_0>0.
$$

:::

:::

::: pf-step

Therefore the negation in step [](#s1-1){.pf-ref} is impossible.


::: pf-proof

It leads to the contradiction in step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Hence for every $\varepsilon>0$, there exists $\delta>0$ such
that
$$
\boxed{
\mu(A)<\delta
\Longrightarrow
\nu(A)<\varepsilon}
$$
for every measurable $A$.


::: pf-proof

This is the logical negation of the impossible statement in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-17){.pf-ref} is the required conclusion.

:::

:::

:::
