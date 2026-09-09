---
schema: qual/card@1
id: P-EMRA5
kind: problem
title: "Banach-Zarecki characterizations of absolute continuity"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Real Analysis Problem 5 in the preserved Emory qualifying-exam compilation. The source omits the bounded-variation hypothesis needed for the stated equivalence; the card restores it and uses outer measure for arbitrary subsets.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f$ be a continuous function of bounded variation on $[0,1]$.
Show that the following statements are equivalent:

(a) $f$ is absolutely continuous.

(b) For any $\epsilon > 0$ there exists $\delta > 0$ such that $m^*(f(E)) < \epsilon$ for any set $E \subseteq [0,1]$ with $m^*(E) < \delta$.

(c) $m^*(f(E)) = 0$ for any set $E \subseteq [0,1]$ with $m^*(E) = 0$.
:::

::: {.solution}
<1>1. The bounded-variation hypothesis is necessary.
::: {.proof}
Continuity together with preservation of null sets does not by itself imply absolute continuity. For example, define
\[
u(0)=0,
\qquad
u(x)=x\sin(1/x)\quad(0<x\le1).
\]
For every $r>0$, $u$ is Lipschitz on $[r,1]$, while $u([0,r])\subseteq[-r,r]$; hence $u$ maps null sets to null sets. But $u$ has infinite variation near $0$, so it is not absolutely continuous. Thus the source statement needs the bounded-variation assumption restored above.
:::

<1>2. Absolute continuity implies (b).
::: {.proof}
Assume $f$ is absolutely continuous and let $\varepsilon>0$. By absolute continuity, choose $\delta>0$ such that for every finite pairwise disjoint family of intervals $I_j=[a_j,b_j]$ with
\[
\sum_j |I_j|<\delta,
\]
one has
\[
\sum_j |f(b_j)-f(a_j)|<\varepsilon.
\]

Let $E\subseteq[0,1]$ satisfy $m^*(E)<\delta$. Choose an open set $G\supseteq E$ with $m(G)<\delta$. Write the relative open set $G\cap[0,1]$ as a countable disjoint union of intervals $I_j$. On each closure $\overline I_j$, continuity gives points $u_j,v_j$ at which $f$ attains its minimum and maximum. Hence
\[
m^*(f(I_j))\le |f(v_j)-f(u_j)|.
\]
The intervals with endpoints $u_j,v_j$ are pairwise disjoint and have total length at most $m(G)<\delta$. Applying absolute continuity first to finite subfamilies and then passing to the limit gives
\[
m^*(f(E))
\le \sum_j m^*(f(I_j))
\le \sum_j |f(v_j)-f(u_j)|
\le \varepsilon.
\]
Thus (b) holds.
:::

<1>3. Condition (b) implies (c).
::: {.proof}
Let $E\subseteq[0,1]$ have $m^*(E)=0$. Given $\varepsilon>0$, choose the $\delta$ supplied by (b). Since $m^*(E)=0<\delta$, condition (b) gives
\[
m^*(f(E))<\varepsilon.
\]
As $\varepsilon$ is arbitrary, $m^*(f(E))=0$. Hence (c) holds.
:::

<1>4. Condition (c), together with continuity and bounded variation, implies absolute continuity.
::: {.proof}
Because $f$ has bounded variation, $f'$ exists almost everywhere and $f'\in L^1([0,1])$. Let
\[
D=\{x\in[0,1]: f'(x)\text{ exists}\};
\]
then $m([0,1]\setminus D)=0$, and by (c),
\[
m^*\bigl(f([0,1]\setminus D)\bigr)=0.
\]

We use the standard one-dimensional image estimate for functions of bounded variation:
\[
m^*(f(A))\le \int_A |f'(x)|\,dx
\tag{*}
\]
for every measurable $A\subseteq D$. This estimate follows by partitioning $A$ according to local bounds on the difference quotients of $f$ and applying the outer-measure definition on each piece; equivalently, it is the usual image-measure inequality in the proof of the Banach-Zarecki theorem.

Let $\varepsilon>0$. Since $|f'|\in L^1$, there is $\delta>0$ such that
\[
m(A)<\delta
\quad\Longrightarrow\quad
\int_A |f'|<\varepsilon
\]
for every measurable $A\subseteq[0,1]$.

Take finitely many pairwise disjoint intervals $I_k=[a_k,b_k]$ with
\[
\sum_k |I_k|<\delta.
\]
For each $k$, continuity implies that $f(I_k)$ is an interval, and therefore
\[
|f(b_k)-f(a_k)|\le m^*(f(I_k)).
\]
Using $I_k=(I_k\cap D)\cup(I_k\setminus D)$, condition (c), and (*),
\[
m^*(f(I_k))
\le m^*(f(I_k\cap D))+m^*(f(I_k\setminus D))
\le \int_{I_k}|f'|.
\]
Hence
\[
\sum_k |f(b_k)-f(a_k)|
\le \sum_k\int_{I_k}|f'|
=\int_{\bigcup_k I_k}|f'|
<\varepsilon.
\]
This is exactly the definition of absolute continuity. Thus (c) implies (a), and all three conditions are equivalent.
:::
:::
