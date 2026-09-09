---
schema: qual/card@1
id: P-RAF11B
kind: problem
title: "Weak topology on infinite-dimensional Banach spaces"
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
  note: Checked against Problem 2 of the official UCSD Fall 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
(a) Let $X$ be an infinite dimensional Banach space.
Prove that $X$ endowed with the weak topology is not a complete metric space.

Hint: Begin by showing that any norm bounded set in $X$ is nowhere dense in the weak topology.

(b) Let $X$ be a Banach space and $X^*$ its dual.
Suppose that there exists countably many linear functionals $L_n \in X^*$ with the following property: any sequence $x_j, x \in X$ converges weakly $x_j \to x$ iff $L_n(x_j) \to L_n(x)$ for all $n$.
Show that $X$ must be finite dimensional.

Hint: Consider the function $d(x,y) = \sum_n 2^{-n} \frac{|L_n(x-y)|}{1 + |L_n(x-y)|}$.
:::

::: solution
<1>1. Norm-bounded sets have empty weak interior in infinite dimension.
::: proof
Let $B\subset X$ be norm bounded. Suppose a weakly open neighborhood of some $x_0\in B$ were contained in $B$. Then there would exist $f_1,\dots,f_N\in X^*$ and $\varepsilon>0$ such that
\[
U:=\{x\in X:|f_j(x-x_0)|<\varepsilon\text{ for }1\le j\le N\}
\subset B.
\]
Because $X$ is infinite dimensional,
\[
M:=\bigcap_{j=1}^N\ker f_j
\]
contains a nonzero vector $v$. For every scalar $t$,
\[
x_0+tv\in U,
\]
while
\[
\|x_0+tv\|\to\infty
\]
as $|t|\to\infty$. This contradicts norm boundedness of $B$. Hence every norm-bounded set has empty weak interior.
:::

<1>2. Prove part (a) by Baire category.
::: proof
For each integer $n\ge1$, the closed norm ball
\[
B_n:=\{x\in X:\|x\|\le n\}
\]
is weakly closed. Indeed, by Hahn--Banach,
\[
\|x\|=\sup_{\|f\|\le1}|f(x)|,
\]
so $B_n$ is an intersection of weakly closed sets.

By Step 1, $B_n$ has empty weak interior, hence is nowhere dense in the weak topology. But
\[
X=\bigcup_{n=1}^\infty B_n.
\]
If the weak topology were induced by a complete metric, the Baire Category Theorem would forbid a complete metric space from being a countable union of closed nowhere dense sets. Therefore, for infinite-dimensional $X$, the weak topology is not a complete metric topology.
:::

<1>3. The function in the hint is a metric whose convergent sequences are exactly the weakly convergent sequences.
::: proof
Define
\[
d(x,y)=\sum_{n=1}^\infty2^{-n}
\frac{|L_n(x-y)|}{1+|L_n(x-y)|}.
\]
The series converges uniformly because each summand is at most $2^{-n}$. If $d(x,y)=0$, then
\[
L_n(x-y)=0
\]
for every $n$. The constant sequence $x_j=x$ would then satisfy
\[
L_n(x_j)\to L_n(y)
\]
for every $n$, so by hypothesis $x_j\rightharpoonup y$. But a constant sequence converges weakly only to its constant value, hence $x=y$. Thus $d$ is a genuine metric.

For completeness, the triangle inequality follows from the subadditivity of
\[
q(t):=\frac{t}{1+t},\qquad t\ge0.
\]
Indeed, for $a,b\ge0$,
\[
q(a+b)\le q(a)+q(b),
\]
and
\[
|L_n(x-z)|\le |L_n(x-y)|+|L_n(y-z)|.
\]
Applying $q$ and summing with weights $2^{-n}$ gives
\[
d(x,z)\le d(x,y)+d(y,z).
\]

For a sequence $(x_j)$,
\[
d(x_j,x)\to0
\]
if and only if
\[
L_n(x_j)\to L_n(x)
\]
for every $n$: one direction follows termwise, and the other by dominated convergence for the summable series. By hypothesis, this is equivalent to weak convergence.
:::

<1>4. Show that $d$ metrizes the weak topology.
::: proof
Each function
\[
x\longmapsto d(x,x_0)
\]
is weakly continuous, because it is the uniform limit of finite sums of continuous functions of the weakly continuous coordinates $L_n$. Hence every $d$-ball is weakly open, so the $d$-topology is contained in the weak topology.

Suppose the inclusion were strict. Then there would be a weakly open set $U$ and a point $x\in U$ such that no $d$-ball centered at $x$ is contained in $U$. Choose
\[
x_j\notin U,
\qquad
d(x_j,x)<\frac1j.
\]
Then $x_j\to x$ in $d$, hence by Step 3 $x_j\rightharpoonup x$. Since $U$ is weakly open and contains $x$, eventually $x_j\in U$, a contradiction. Thus the two topologies coincide.
:::

<1>5. A normed space with metrizable weak topology is finite dimensional.
::: proof
Since the weak topology is metrizable, it has a countable neighborhood base $(U_m)$ at $0$. For each $m$, choose a basic weak neighborhood
\[
V_m
=\{x:|f_{m,j}(x)|<\varepsilon_m,\ 1\le j\le N_m\}
\subset U_m.
\]
Let $\mathcal F$ be the countable collection of all functionals $f_{m,j}$.

Fix any $f\in X^*$. The set
\[
W_f:=\{x:|f(x)|<1\}
\]
is a weak neighborhood of $0$, so some $U_m\subset W_f$. Hence $V_m\subset W_f$. If
\[
x\in\bigcap_{j=1}^{N_m}\ker f_{m,j},
\]
then $tx\in V_m$ for every scalar $t$, so $|t f(x)|<1$ for every $t$. Thus $f(x)=0$. Therefore
\[
\bigcap_{j=1}^{N_m}\ker f_{m,j}\subseteq\ker f.
\]
It follows by elementary linear algebra that
\[
f\in\operatorname{span}\{f_{m,1},\dots,f_{m,N_m}\}.
\]
Consequently $X^*$ is spanned by the countable set $\mathcal F$.

But $X^*$ is a Banach space. If it were infinite dimensional and countably Hamel-dimensional, it would be a countable union of finite-dimensional closed subspaces, contradicting Baire category. Hence $X^*$ is finite dimensional.

Finally, Hahn--Banach implies that any finite linearly independent family in $X$ gives rise to the same number of linearly independent continuous functionals. Thus
\[
\dim X\le\dim X^*<\infty.
\]
Therefore $X$ is finite dimensional.
:::
:::
