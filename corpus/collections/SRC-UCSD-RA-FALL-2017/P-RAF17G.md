---
schema: qual/card@1
id: P-RAF17G
kind: problem
title: "Precompactness of Sobolev-type unit balls in C([0,1])"
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
  note: Checked against Problem 7 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $AC([0,1])$ denote the absolutely continuous functions on $[0,1]$ with values in $\mathbb{R}$ and for $1 \leq p < \infty$, let
$$
\mathcal{C}_p := \{f \in AC([0,1]) : f(0) = 0 \text{ and } \int_{[0,1]} |f'(x)|^p\,dx \leq 1\}
$$
thought of as a subset of the Banach space $(C([0,1]), \|\cdot\|_u)$ where
$$
\|f\|_u := \max_{x \in [0,1]} |f(x)| \quad \forall f \in C([0,1]).
$$

1. Show $\mathcal{C}_p$ is precompact in $C([0,1])$ for all $p \in (1, \infty)$.

2. Is $\mathcal{C}_1$ precompact in $C([0,1])$?
   You must justify your conclusion here.
:::

::: solution
<1>1. Establish uniform boundedness and equicontinuity for $p>1$.
::: proof
Fix $p>1$ and let $q=p/(p-1)$. If $f\in\mathcal C_p$, then for $0\le x<y\le1$, absolute continuity gives
\[
f(y)-f(x)=\int_x^y f'(t)\,dt.
\]
By Hölder's inequality,
\[
|f(y)-f(x)|
\le
\left(\int_x^y|f'(t)|^p\,dt\right)^{1/p}
|y-x|^{1/q}
\le |y-x|^{1-1/p}.
\]
Thus the whole family has the common Hölder modulus
\[
|f(y)-f(x)|\le |y-x|^{1-1/p}.
\]
Also, since $f(0)=0$,
\[
|f(x)|\le x^{1-1/p}\le1,
\]
so $\mathcal C_p$ is uniformly bounded.
:::

<1>2. Apply Arzelà--Ascoli for $p>1$.
::: proof
The domain $[0,1]$ is compact. By Step 1, $\mathcal C_p$ is uniformly bounded and equicontinuous. Therefore the Arzelà--Ascoli theorem implies that its closure in $C([0,1])$ is compact. Hence
\[
\boxed{\mathcal C_p\text{ is precompact for every }p>1.}
\]
:::

<1>3. Show that $\mathcal C_1$ is not precompact.
::: proof
For $n\ge1$, define
\[
f_n(x):=\min(nx,1),
\qquad 0\le x\le1.
\]
Then $f_n$ is absolutely continuous, $f_n(0)=0$, and
\[
f_n'(x)=
\begin{cases}
n,&0<x<1/n,\\
0,&1/n<x<1,
\end{cases}
\]
almost everywhere. Therefore
\[
\int_0^1|f_n'(x)|\,dx=1,
\]
so $f_n\in\mathcal C_1$.

For every $x>0$,
\[
f_n(x)\longrightarrow1,
\]
while $f_n(0)=0$ for every $n$. Thus the pointwise limit is
\[
h(0)=0,
\qquad
h(x)=1\quad(x>0),
\]
which is discontinuous. Every subsequence has the same pointwise limit. If some subsequence converged uniformly, its uniform limit would be continuous and would have to equal this pointwise limit, a contradiction.

Hence $(f_n)$ has no uniformly convergent subsequence, so
\[
\boxed{\mathcal C_1\text{ is not precompact in }C([0,1]).}
\]
:::
:::
