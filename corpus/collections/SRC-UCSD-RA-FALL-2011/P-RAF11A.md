---
schema: qual/card@1
id: P-RAF11A
kind: problem
title: "Density of measurable sets with uniform lower density"
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
  note: Checked against Problem 1 of the official UCSD Fall 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
(a) Let $E \subseteq [0,1]$ be Lebesgue measurable.
Suppose there exists a fixed $\epsilon > 0$ such that $|E \cap (a,b)| \geq \epsilon|a - b|$ for all intervals $(a,b) \subseteq [0,1]$.
Show that one must have $|E| = 1$.

(b) Give an example of a Lebesgue measurable set $E \subseteq [0,1]$ with $0 < |E| < 1$ and $|E \cap (a,b)| > 0$ for all nontrivial intervals $(a,b) \subseteq [0,1]$.
Explain why this example does not contradict part (a) above.
:::

::: solution
<1>1. Prove part (a) by the Lebesgue density theorem.
::: proof
Suppose, toward a contradiction, that
\[
|E|<1.
\]
Then
\[
|[0,1]\setminus E|>0.
\]
By the Lebesgue density theorem, for almost every
\[
x\in [0,1]\setminus E,
\]
the set $[0,1]\setminus E$ has density $1$ at $x$. Choose such an $x$ in the interior $(0,1)$. Then
\[
\frac{|E\cap(x-r,x+r)|}{2r}\longrightarrow0
\]
as $r\downarrow0$.

But for all sufficiently small $r>0$, the interval $(x-r,x+r)$ lies in $[0,1]$, and the hypothesis gives
\[
|E\cap(x-r,x+r)|\ge \varepsilon(2r).
\]
Hence
\[
\frac{|E\cap(x-r,x+r)|}{2r}\ge\varepsilon,
\]
contradicting the density limit above. Therefore
\[
\boxed{|E|=1.}
\]
:::

<1>2. Construct a dense measurable set of intermediate measure.
::: proof
Enumerate the rationals in $[0,1]$ as
\[
\{q_n:n\ge1\}.
\]
Choose positive radii $r_n$ such that
\[
\sum_{n=1}^\infty 2r_n<\frac12,
\]
and define
\[
E:=\bigcup_{n=1}^\infty
\bigl((q_n-r_n,q_n+r_n)\cap[0,1]\bigr).
\]
Then $E$ is open in $[0,1]$ and dense there. Also
\[
0<|E|\le\sum_{n=1}^\infty2r_n<\frac12<1.
\]

Let $(a,b)\subset[0,1]$ be nontrivial. Choose a rational $q_n\in(a,b)$. Since $q_n\in E$ and $E$ is open, there exists $\delta>0$ such that
\[
(q_n-\delta,q_n+\delta)\subset E\cap(a,b).
\]
Therefore
\[
|E\cap(a,b)|>0.
\]
:::

<1>3. Explain why this does not contradict part (a).
::: proof
Part (a) requires one fixed constant $\varepsilon>0$ such that
\[
|E\cap(a,b)|\ge\varepsilon|a-b|
\]
for every interval. The set in Step 2 only guarantees that each intersection has some positive measure; it gives no uniform lower bound on the relative proportion.

Indeed, if such a uniform $\varepsilon$ existed, part (a) would force $|E|=1$, contradicting the construction. Thus there is no contradiction.
:::
:::
