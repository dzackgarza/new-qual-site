---
schema: qual/card@1
id: P-WESRA15-4
kind: problem
title: 'A large closed set containing no rationals'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. Flash renders the interval delimiters as braces; the irrational-subset and measure-$>3/4$ requirements determine $[0,1]$.
---

::: {.problem}
Let
$$
E=[0,1]\setminus\QQ.
$$
Construct a closed set $F\subset E$ whose Lebesgue measure exceeds $3/4$.
:::

::: {.solution}

::: pf

::: pf-step

Enumerate the rational numbers in $[0,1]$ as
$$
\QQ\cap[0,1]=\{q_1,q_2,\ldots\}.
$$
For each $n\ge1$, let
$$
I_n=
\left(
q_n-2^{-n-4},
q_n+2^{-n-4}
\right).
$$


::: pf-proof

The rationals are countable, so the displayed enumeration exists. Each $I_n$ is an open interval containing $q_n$ and has length
$$
\abs{I_n}=2^{-n-3}.
$$

:::

:::

::: {.pf-step #s1-2}

The open set
$$
U=\bigcup_{n=1}^{\infty}I_n
$$
contains every rational number in $[0,1]$ and satisfies
$$
m(U)\le\frac18.
$$


::: pf-proof

Every $q_n$ belongs to $I_n$, so
$$
\QQ\cap[0,1]\subseteq U.
$$
By countable subadditivity of Lebesgue measure,
$$
\begin{aligned}
m(U)
&\le
\sum_{n=1}^{\infty}m(I_n)\\
&=
\sum_{n=1}^{\infty}2^{-n-3}\\
&=\frac18.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Define
$$
F=[0,1]\setminus U.
$$
Then $F$ is closed and
$$
F\subseteq E=[0,1]\setminus\QQ.
$$


::: pf-proof

The set $U$ is open, so $U^c$ is closed. Hence
$$
F=[0,1]\cap U^c
$$
is closed in $\RR$. By step [](#s1-2){.pf-ref}, every rational point of $[0,1]$ lies in $U$, so no rational point belongs to $F$. Thus $F\subseteq E$.

:::

:::

::: {.pf-step #s1-4}

The set $F$ satisfies
$$
\boxed{m(F)>\frac34}.
$$


::: pf-proof

Because $F$ and $U\cap[0,1]$ partition $[0,1]$,
$$
m(F)
=1-m(U\cap[0,1])
\ge
1-m(U).
$$
Step [](#s1-2){.pf-ref} therefore gives
$$
m(F)\ge1-\frac18=\frac78>\frac34.
$$

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} give a closed set $F\subset E$ with the required measure.

:::

:::

:::
