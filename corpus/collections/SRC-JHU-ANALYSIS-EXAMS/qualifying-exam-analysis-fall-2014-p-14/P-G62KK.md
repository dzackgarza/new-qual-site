---
schema: qual/card@1
id: P-G62KK
kind: problem
title: 'Egoroff''s theorem for a dominated sequence, proved without invoking Egoroff'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 7 of the Fall 2014 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

1. Prove the following statement without using Ergoroff’s Theorem: Suppose $\{ f _ { k } \} _ { k = 1 } ^ { \infty }$ is a sequence of measurable functions defined on a measurable set $E ,$ $f _ { k }  f$ a.e. on E and there exists $g \in L ^ { 1 } ( E )$ such that $| f _ { k } | \le g$ for all k. Given $\epsilon > 0$ , there exists a closed set $A _ { \epsilon }$ such that $m ( E \backslash A _ { \epsilon } ) < \epsilon$ and $f _ { k }  f$ uniformly on $A _ { \epsilon }$

::: solution
<1>1. Control the tail suprema in $L^1$.
::: proof
After modifying $f$ on the null set where convergence fails, we may assume $f_k(x)\to f(x)$ for every $x\in E$. Since $|f_k|\le g$, passage to the pointwise limit gives $|f|\le g$.

For $N\ge1$, define
\[
h_N(x):=\sup_{k\ge N}|f_k(x)-f(x)|.
\]
Then each $h_N$ is measurable,
\[
0\le h_{N+1}\le h_N\le 2g,
\]
and $h_N(x)\downarrow0$ for every $x\in E$. Since $g\in L^1(E)$, dominated convergence gives
\[
\int_E h_N\,dm\longrightarrow0.
\]
:::

<1>2. Remove a set of arbitrarily small measure on which the tail bounds are bad.
::: proof
Fix $\varepsilon>0$. For each $j\ge1$, choose $N_j$ increasing so that
\[
\int_E h_{N_j}\,dm<\frac{\varepsilon}{2^{j+2}j}.
\]
Set
\[
B_j:=\{x\in E:h_{N_j}(x)>1/j\}.
\]
By Chebyshev's inequality,
\[
m(B_j)
\le j\int_E h_{N_j}\,dm
<\frac{\varepsilon}{2^{j+2}}.
\]
Hence, with
\[
B:=\bigcup_{j=1}^\infty B_j,
\]
we have
\[
m(B)<\frac\varepsilon2.
\]
On $E\setminus B$, for every $j$ and every $k\ge N_j$,
\[
|f_k(x)-f(x)|\le h_{N_j}(x)\le\frac1j.
\]
Thus $f_k\to f$ uniformly on $E\setminus B$.
:::

<1>3. Replace the measurable good set by a closed good set.
::: proof
By inner regularity of Lebesgue measure, there exists a closed set
\[
A_\varepsilon\subset E\setminus B
\]
such that
\[
m\bigl((E\setminus B)\setminus A_\varepsilon\bigr)<\frac\varepsilon2.
\]
Therefore
\[
m(E\setminus A_\varepsilon)
\le m(B)+m\bigl((E\setminus B)\setminus A_\varepsilon\bigr)
<\varepsilon.
\]
Since uniform convergence on a set passes to every subset, $f_k\to f$ uniformly on $A_\varepsilon$.

Hence there is a closed set $A_\varepsilon\subset E$ with
\[
m(E\setminus A_\varepsilon)<\varepsilon
\]
such that $f_k\to f$ uniformly on $A_\varepsilon$, as required.
:::
:::
