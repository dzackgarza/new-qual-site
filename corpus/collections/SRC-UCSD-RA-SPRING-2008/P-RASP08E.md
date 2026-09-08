---
schema: qual/card@1
id: P-RASP08E
kind: problem
title: "Compactness of a bounded integral recursion"
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
  note: Checked against Problem 5 of the official UCSD Spring 2008 real-analysis qualifying exam. The card title was corrected because the source assumes only bounded Borel measurability, not a contraction hypothesis.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $F : \mathbb{C} \to \mathbb{C}$ be a bounded Borel measurable function, and $y_0 \in \mathbb{C}$.
Define a sequence of functions $f_n : [0,1] \to \mathbb{C}$ by the recursion $f_0(x) \equiv y_0$ and
$$
f_{n+1}(x) := y_0 + \int_0^x F(f_n(t))\,dt.
$$
Show that $f_n \in C([0,1])$, and there are $f \in C([0,1])$ and a subsequence $f_{n_k}$ such that $f_{n_k} \to f$ in $C([0,1])$.
:::


::: solution
<1>1. Show inductively that every $f_n$ is well defined and continuous.
::: proof
Let
\[
M:=\sup_{z\in\mathbb C}|F(z)|<\infty.
\]
The function $f_0\equiv y_0$ is continuous. Suppose $f_n$ is continuous. Then $f_n$ is Borel measurable, hence $F\circ f_n$ is Borel measurable. It is bounded by $M$, so it is Lebesgue integrable on $[0,1]$.

Therefore
\[
f_{n+1}(x)=y_0+\int_0^xF(f_n(t))\,dt
\]
is well defined for every $x\in[0,1]$. In fact $f_{n+1}$ is absolutely continuous, hence continuous. By induction,
\[
\boxed{f_n\in C([0,1])\text{ for every }n.}
\]
:::

<1>2. Establish uniform boundedness and equicontinuity.
::: proof
For $n\ge0$ and $x\in[0,1]$,
\[
|f_{n+1}(x)|
\le |y_0|+\int_0^x|F(f_n(t))|\,dt
\le |y_0|+M.
\]
Thus $(f_n)_{n\ge1}$ is uniformly bounded.

Also, for $x,y\in[0,1]$,
\[
\begin{aligned}
|f_{n+1}(x)-f_{n+1}(y)|
&=\left|\int_y^xF(f_n(t))\,dt\right|\\
&\le M|x-y|.
\end{aligned}
\]
Hence the family is equi-Lipschitz, and therefore equicontinuous.
:::

<1>3. Apply Arzelà--Ascoli.
::: proof
The interval $[0,1]$ is compact. By Step 2, the sequence $(f_n)_{n\ge1}$ is uniformly bounded and equicontinuous. The Arzelà--Ascoli theorem therefore gives a subsequence $(f_{n_k})$ and a continuous function $f\in C([0,1])$ such that
\[
\|f_{n_k}-f\|_\infty\longrightarrow0.
\]
Equivalently,
\[
\boxed{f_{n_k}\to f\text{ in }C([0,1]).}
\]
:::
:::
