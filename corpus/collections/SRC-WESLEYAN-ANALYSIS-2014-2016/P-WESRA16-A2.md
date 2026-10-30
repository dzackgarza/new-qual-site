---
schema: qual/card@1
id: P-WESRA16-A2
kind: problem
title: 'Measurability of the pointwise convergence set of measurable functions'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group A, problem A2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f_0,f_1,\dots:\RR^d\to\RR$ be Lebesgue measurable.
Prove that
$$
\{x:(f_0(x),f_1(x),\dots)\text{ converges}\}
$$
is measurable.

Hint: for $q\in\QQ$ and $n,k\in\NN$, let $C_{q,n,k}=\{x:\abs{f_n(x)-q}\le2^{-k}\}$.
:::

::: {.solution}

Let
$$
E=\{x\in\RR^d:(f_n(x))_{n\ge0}\text{ converges in }\RR\}.
$$

::: pf

::: {.pf-step #s1-1}

For every $m,n\ge0$ and $k\ge1$, the set
$$
E_{m,n,k}
=\left\{x:\abs{f_m(x)-f_n(x)}<\frac1k\right\}
$$
is Lebesgue measurable.


::: pf-proof

Since $f_m$ and $f_n$ are measurable, the function
$$
x\longmapsto f_m(x)-f_n(x)
$$
is measurable, and therefore so is its absolute value. Hence
$$
E_{m,n,k}
=\abs{f_m-f_n}^{-1}\left([0,1/k)\right)
$$
is measurable.

:::

:::

::: {.pf-step #s1-2}

Define
$$
C
=\bigcap_{k=1}^\infty
\bigcup_{N=0}^\infty
\bigcap_{m,n\ge N}E_{m,n,k}.
$$
Then $C$ is Lebesgue measurable.


::: pf-proof

Each $E_{m,n,k}$ is measurable by step [](#s1-1){.pf-ref}. The set $C$ is obtained from these sets by countable intersections and countable unions, so it is measurable.

:::

:::

::: {.pf-step #s1-3}

One has
$$
E=C.
$$


::: pf-proof

Fix $x\in\RR^d$. By completeness of $\RR$, the numerical sequence $(f_n(x))_{n\ge0}$ converges if and only if it is Cauchy.

The Cauchy condition says that for every $\varepsilon>0$ there exists $N$ such that
$$
\abs{f_m(x)-f_n(x)}<\varepsilon
$$
whenever $m,n\ge N$. It is enough to test the countable family $\varepsilon=1/k$, $k\ge1$. Thus $(f_n(x))$ is Cauchy if and only if
$$
\forall k\ge1\ \exists N\ge0\ \forall m,n\ge N,
\qquad
x\in E_{m,n,k},
$$
which is exactly the condition $x\in C$.

:::

:::

::: {.pf-step #s1-4}

The convergence set $E$ is measurable.


::: pf-proof

By step [](#s1-3){.pf-ref}, $E=C$, and step [](#s1-2){.pf-ref} shows that $C$ is measurable.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required measurability.

:::

:::

:::
