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
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "PDF page 15 identifies this as Spring 2014 problem 1, not Fall 2014 problem 7. Restored the convergence arrows and compared the unrestricted measurable set and closed good-set conclusion."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Excluded the original exceptional null set before the tail-supremum argument and supplied closed-set approximation valid also for infinite-measure E; did not modify the original sequence or its limit."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Spring 2014 problem 1 is the only occurrence of this statement in the JHU packet; merged the duplicate card P-8XT02 and kept its tail-set proof as a second solution."
---

::: problem
Prove the following without using Egoroff's theorem. Let
$(f_k)$ be measurable functions on a Lebesgue-measurable set
$E\subset\mathbb R^d$, with $f_k\to f$ almost everywhere
on $E$. Suppose $g\in L^1(E)$ and $|f_k|\leq g$ for every
$k$. For each $\varepsilon>0$, prove that there is a closed
set $A_\varepsilon\subseteq E$ with
$m(E\setminus A_\varepsilon)<\varepsilon$ such that
$f_k\to f$ uniformly on $A_\varepsilon$.
:::

::: solution
<1>1. Control the tail suprema in $L^1$.
::: proof
Choose a measurable null set $Z\subset E$ outside which
the given convergence holds and $g$ is finite. On
$E_0=E\setminus Z$, passage to the limit gives $|f|\leq g$.
We leave every value of the original functions unchanged.

For $N\ge1$, define
\[
h_N(x):=\begin{cases}
\sup_{k\ge N}|f_k(x)-f(x)|,&x\in E_0,\\
0,&x\in Z.
\end{cases}
\]
Then each $h_N$ is measurable,
\[
0\le h_{N+1}\le h_N\le 2g,
\]
The displayed domination holds almost everywhere, and
$h_N\downarrow0$ everywhere by its definition on $Z$.
Since $g\in L^1(E)$, dominated convergence gives [@Fol13]
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
B:=Z\cup\bigcup_{j=1}^\infty B_j,
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
Put $F=E\setminus B$ and $H=\mathbb R^d\setminus F$.
For each positive integer $j$, the measurable set
$H_j=H\cap[-j,j]^d$ has finite measure. Outer regularity
gives an open $O_j\supset H_j$ with
$m(O_j\setminus H_j)<\varepsilon/2^{j+1}$ [@Fol13].
Then $O=\bigcup_jO_j$ is open and contains $H$, and
$$
m(O\setminus H)\leq\sum_{j=1}^\infty m(O_j\setminus H_j)
<\varepsilon/2.
$$
Consequently $A_\varepsilon=\mathbb R^d\setminus O$ is
closed, lies in $F$, and satisfies
$m(F\setminus A_\varepsilon)<\varepsilon/2$.
This construction does not assume $m(E)<\infty$.
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

::: {.solution}
<1>1. At each accuracy level, the bad tail sets have finite measure decreasing to zero.

::: proof
Choose a measurable null set $Z\subset E$ outside which
$f_k(x)\to f(x)$ and $g$ is finite. Put $E_0=E\setminus Z$.
On $E_0$, the bound on $f_k$ implies $|f|\leq g$.
No function values need to be changed.

For positive integers $j,N$, define
\[
B_{N,j}
:=\bigcup_{k\ge N}
\left\{x\in E_0:|f_k(x)-f(x)|\ge \frac1j\right\}.
\]
For fixed $j$, the sets $B_{N,j}$ decrease as $N\to\infty$. Pointwise convergence gives
\[
\bigcap_{N=1}^\infty B_{N,j}=\varnothing.
\]
Also, because $|f_k|,|f|\le g$,
\[
B_{1,j}\subseteq\left\{x\in E:g(x)\ge\frac1{2j}\right\}.
\]
Chebyshev's inequality gives
\[
m(B_{1,j})
\le 2j\int_E g<\infty.
\]
Hence continuity from above of measure yields [@Fol13]
\[
m(B_{N,j})\longrightarrow0
\qquad(N\to\infty).
\]
:::

<1>2. Removing a set of small measure gives uniform convergence.

::: proof
Choose $N_j$ so that
\[
m(B_{N_j,j})<\frac{\epsilon}{2^{j+2}}.
\]
Set
\[
B:=Z\cup\bigcup_{j=1}^\infty B_{N_j,j}.
\]
Then
\[
m(B)<\frac\epsilon2.
\]

On $E\setminus B$, convergence is uniform. Indeed, given $\eta>0$, choose $j$ with $1/j<\eta$. If $k\ge N_j$ and $x\in E\setminus B$, then $x\notin B_{N_j,j}$, so
\[
|f_k(x)-f(x)|<\frac1j<\eta.
\]
:::

<1>3. The good set contains a closed subset with arbitrarily small measure loss.

::: proof
Let $\mathbb R^d$ be the ambient Euclidean space, and put
$F=E\setminus B$ and $H=\mathbb R^d\setminus F$.
For each positive integer $j$, use finite-measure outer
regularity to choose an open $O_j\supset H\cap[-j,j]^d$
whose excess measure is less than $\epsilon/2^{j+1}$
[@Fol13]. The open set $O=\bigcup_jO_j$ contains $H$, and
$$
m(O\setminus H)
\leq\sum_j m\bigl(O_j\setminus(H\cap[-j,j]^d)\bigr)
<\epsilon/2.
$$
Its complement $A_\epsilon=\mathbb R^d\setminus O$ is
closed, contained in $F$, and satisfies
$m(F\setminus A_\epsilon)<\epsilon/2$. This holds whether
or not $E$ has finite measure.
Then
\[
m(E\setminus A_\epsilon)
\le m(B)+m\bigl((E\setminus B)\setminus A_\epsilon\bigr)
<\epsilon,
\]
and uniform convergence on $E\setminus B$ implies uniform convergence on $A_\epsilon$.
:::
:::
