---
schema: qual/card@1
id: P-WESRA13A-II5
kind: problem
title: 'Monotonicity versus positivity of the derivative — partially extractor-defective'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Direct inspection of the retained PDF page resolves subpart (a) as asking whether strict increase implies $F'>0$ almost everywhere.
---

::: {.problem}
Consider the following questions for functions $F:[0,1]\to\RR$.

(a) Suppose $F$ is strictly increasing.
Must $F'(x)>0$ almost everywhere?

(b) Suppose $F'(x)>0$ almost everywhere.
Must $F$ be strictly increasing?
:::

::: {.solution}

::: pf

::: pf-step

There exists a compact nowhere-dense set $K\subset[0,1]$ with positive Lebesgue measure.


::: pf-proof

Take the Smith--Volterra--Cantor set, obtained by successively removing middle open intervals whose total length is $1/2$. It is closed, hence compact; its measure is $1/2$; and the lengths of its remaining interval components tend to zero, so it contains no nonempty interval and is therefore nowhere dense.

:::

:::

::: {.pf-step #s1-2}

Let
$$
A=[0,1]\setminus K,
\qquad
F(x)=\int_0^x\mathbf1_A(t)\,dt.
$$
Then $F$ is strictly increasing.


::: pf-proof

Let $0\leq x<y\leq1$. Since $K$ is nowhere dense, the nonempty open interval $(x,y)$ contains a nonempty open subinterval $J$ disjoint from $K$. Thus $J\subseteq A$, and consequently
$$
F(y)-F(x)
=\int_x^y\mathbf1_A(t)\,dt
=m(A\cap(x,y))
\geq m(J)>0.
$$
Hence $F(y)>F(x)$ for every $x<y$.

:::

:::

::: {.pf-step #s1-3}

The function $F$ from step [](#s1-2){.pf-ref} does not satisfy $F'(x)>0$ almost everywhere.


::: pf-proof

The function $F$ is absolutely continuous, so by the fundamental theorem of calculus for Lebesgue integrals,
$$
F'(x)=\mathbf1_A(x)
$$
for almost every $x\in[0,1]$. Since $K$ has positive measure and $\mathbf1_A=0$ on $K$, one has $F'(x)=0$ on a set of positive measure. Thus strict increase does not imply $F'>0$ almost everywhere. This answers part (a) negatively.

:::

:::

::: {.pf-step #s1-4}

Let $C:[0,1]\to[0,1]$ be the Cantor function and define
$$
G(x)=x-2C(x).
$$
Then
$$
G'(x)=1
$$
for almost every $x\in[0,1]$.


::: pf-proof

The Cantor function is differentiable with derivative $0$ almost everywhere. At every point where $C'(x)=0$,
$$
G'(x)=1-2C'(x)=1.
$$
Hence $G'(x)=1>0$ almost everywhere.

:::

:::

::: {.pf-step #s1-5}

The function $G$ is not strictly increasing.


::: pf-proof

The Cantor function satisfies $C(0)=0$ and $C(1)=1$. Therefore
$$
G(0)=0,
\qquad
G(1)=1-2=-1.
$$
Since $0<1$ but $G(0)>G(1)$, the function $G$ is not increasing, and in particular is not strictly increasing. Thus $F'>0$ almost everywhere does not imply strict increase. This answers part (b) negatively.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give a counterexample to part (a), and steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give a counterexample to part (b).

:::

:::

:::
