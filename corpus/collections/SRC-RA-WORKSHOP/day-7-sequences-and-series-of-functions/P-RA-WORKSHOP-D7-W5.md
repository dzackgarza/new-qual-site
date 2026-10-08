---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W5
kind: problem
title: Equicontinuity upgrades pointwise convergence to uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that if $\{f_n\}$ is an equicontinuous sequence of functions on a compact set $K$ and $f_n\to f$ pointwise on $K$, then $f_n\to f$ uniformly on $K$.
:::

::: {.solution}
<1>1. The pointwise limit $f$ is continuous on $K$.

::: {.proof}
Fix $z\in K$ and $\varepsilon>0$. Equicontinuity gives $r>0$ such that $|f_n(y)-f_n(z)|<\varepsilon/2$ for all $n$ whenever $y\in K$ and $d(y,z)<r$. Taking $n\to\infty$ at these fixed points gives $|f(y)-f(z)|\leq\varepsilon/2<\varepsilon$. Thus $f$ is continuous at $z$.
:::

<1>2. For every $\varepsilon>0$ and every $z\in K$, there exists $r_z>0$ such that for every $n$ and every $y\in K$ with $d(y,z)<r_z$,
\[
|f_n(y)-f_n(z)|<\varepsilon/3,
\qquad |f(y)-f(z)|\leq\varepsilon/3.
\]

::: {.proof}
Choose $r_z$ by equicontinuity with tolerance $\varepsilon/3$. The first inequality is its defining property. Taking limits in that inequality using pointwise convergence at $y$ and $z$ gives the second.
:::

<1>3. If $K\ne\varnothing$, there exist $z_1,\ldots,z_m\in K$ and $N\in\mathbb N$ such that
\[
K\subseteq\bigcup_{i=1}^m B(z_i,r_{z_i}/2),
\qquad |f_n(z_i)-f(z_i)|<\varepsilon/3
\quad(n\geq N,\ 1\leq i\leq m).
\]

::: {.proof}
The balls $B(z,r_z/2)$ cover $K$. Compactness gives a finite subcover. Pointwise convergence at each of its finitely many centers gives indices $N_i$ after which the displayed inequality holds; choose $N=\max_iN_i$. If $K$ is empty, uniform convergence is vacuous.
:::

<1>4. For every $\varepsilon>0$ there exists $N$ such that $|f_n(x)-f(x)|<\varepsilon$ for every $x\in K$ and $n\geq N$.

::: {.proof}
For nonempty $K$, choose the data of steps <1>2 and <1>3. Given $x\in K$, select $i$ with $d(x,z_i)<r_{z_i}/2$. For $n\geq N$, the triangle inequality gives
\[
\begin{aligned}
|f_n(x)-f(x)|
&\leq |f_n(x)-f_n(z_i)|+|f_n(z_i)-f(z_i)|\\
&\quad+|f(z_i)-f(x)|
<\varepsilon/3+\varepsilon/3+\varepsilon/3=\varepsilon.
\end{aligned}
\]
The first and third terms are bounded by step <1>2, and the middle term by step <1>3. For empty $K$, any $N$ works.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the definition of uniform convergence of $f_n$ to $f$ on $K$.
:::
:::
