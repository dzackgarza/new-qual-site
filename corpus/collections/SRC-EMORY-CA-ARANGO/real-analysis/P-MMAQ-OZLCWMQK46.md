---
schema: qual/card@1
id: P-MMAQ-OZLCWMQK46
kind: problem
title: Absolute continuity and image-measure conditions for a continuous function
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 5 in both preserved Arango Emory qualifying-problem compilations. The source asks to prove three conditions equivalent, but condition (3), Lusin's N-property, does not imply absolute continuity without an additional bounded-variation hypothesis. The card is corrected to ask for the valid implications and a counterexample to the claimed equivalence.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $f:[0,1]\to\mathbb R$ be continuous. Consider:

1. $f$ is absolutely continuous.
2. For every $\varepsilon>0$ there exists $\delta>0$ such that
   \[
   m(E)<\delta\quad\Longrightarrow\quad m^*(f(E))<\varepsilon
   \]
   for every $E\subseteq[0,1]$.
3. $m(E)=0$ implies $m^*(f(E))=0$ for every $E\subseteq[0,1]$.

The source asks to prove that these three conditions are equivalent. Determine whether that claim is correct. Prove every implication asserted below and, if the equivalence fails, give a counterexample.
:::

::: solution
<1>1. Absolute continuity implies the small-image condition.
::: proof
Assume $f$ is absolutely continuous. Then $f'\in L^1([0,1])$ and
\[
f(y)-f(x)=\int_x^y f'(t)\,dt
\]
for all $0\le x<y\le1$.

Fix $\varepsilon>0$. By absolute continuity of the Lebesgue integral, choose $\eta>0$ such that
\[
m(U)<\eta\quad\Longrightarrow\quad \int_U|f'|<\varepsilon
\]
for every measurable $U\subseteq[0,1]$. Put $\delta=\eta/2$.

Let $E\subseteq[0,1]$ with $m^*(E)<\delta$. Choose an open set $U\supseteq E$ with $m(U)<\eta$. Write the relative open set $U\cap[0,1]$ as a countable disjoint union of intervals $I_j$. For each $j$,
\[
\operatorname{diam} f(I_j)
\le \int_{I_j}|f'(t)|\,dt,
\]
because every difference $|f(y)-f(x)|$ with $x,y\in I_j$ is bounded by that integral. Hence
\[
\begin{aligned}
m^*(f(E))
&\le \sum_j m^*(f(E\cap I_j))\\
&\le \sum_j \operatorname{diam} f(I_j)\\
&\le \sum_j\int_{I_j}|f'|\\
&=\int_U|f'|<\varepsilon.
\end{aligned}
\]
Thus (1) implies (2).
:::

<1>2. The small-image condition implies Lusin's $N$-property.
::: proof
Assume (2), and let $E\subseteq[0,1]$ satisfy $m(E)=0$. Given $\varepsilon>0$, let $\delta$ be supplied by (2). Since $m(E)=0<\delta$,
\[
m^*(f(E))<\varepsilon.
\]
As $\varepsilon>0$ is arbitrary,
\[
m^*(f(E))=0.
\]
Hence (2) implies (3).
:::

<1>3. Condition (3) does not imply absolute continuity.
::: proof
Define
\[
f(0)=0,
\qquad
f(x)=x\sin(x^{-2})\quad(0<x\le1).
\]
This function is continuous on $[0,1]$.

First we prove that it satisfies (3). Let $E\subseteq[0,1]$ have measure zero and fix $a\in(0,1)$. On $[a,1]$, the function $f$ is $C^1$, hence Lipschitz. Therefore
\[
m^*(f(E\cap[a,1]))=0.
\]
On the other hand, $|f(x)|\le x$, so
\[
f(E\cap[0,a])\subseteq[-a,a]
\]
and therefore
\[
m^*(f(E\cap[0,a]))\le2a.
\]
Consequently
\[
m^*(f(E))\le2a.
\]
Letting $a\downarrow0$ gives $m^*(f(E))=0$. Thus $f$ has Lusin's $N$-property.

Now set
\[
t_k=\left(\frac\pi2+k\pi\right)^{-1/2},\qquad k\ge0.
\]
Then $t_k\downarrow0$ and
\[
f(t_k)=(-1)^k t_k.
\]
For the partition containing $0,t_N,t_{N-1},\ldots,t_0$ in increasing order, the variation is at least
\[
\sum_{k=0}^{N-1}|f(t_k)-f(t_{k+1})|
=\sum_{k=0}^{N-1}(t_k+t_{k+1}).
\]
Since $t_k\asymp k^{-1/2}$, this tends to $\infty$. Hence $f$ has unbounded variation on $[0,1]$.

Every absolutely continuous function on a compact interval has bounded variation, so $f$ is not absolutely continuous. Thus (3) does not imply (1), and the source's claimed equivalence is false as written.
:::

<1>4. State the standard corrected theorem.
::: proof
The Banach--Zarecki theorem states that a real-valued function on a compact interval is absolutely continuous if and only if it is continuous, has bounded variation, and has Lusin's $N$-property. Therefore the missing bounded-variation hypothesis is exactly what prevents condition (3) from characterizing absolute continuity in the source statement.
:::
:::
