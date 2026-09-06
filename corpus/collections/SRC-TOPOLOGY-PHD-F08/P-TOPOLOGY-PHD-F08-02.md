---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-02
kind: problem
title: Complete subspaces of complete metric spaces
classification:
  areas:
  - topology
  topics:
  - Completeness
  - Metric Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 2 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    For the closed direction, a Cauchy sequence in Y converges in X and its
    limit remains in Y. For the converse, approximated each closure point x by
    y_n in Y with d(x,y_n)<1/n; completeness gives a limit in Y, and uniqueness
    of metric limits identifies it with x.
---

::: {.problem}
Prove that in a complete metric space $(X,d)$ a subspace $Y$ of $X$ is complete if and only if it is a closed subspace of $X$.
:::

::: {.solution}
Equip $Y$ with the metric obtained by restricting $d$ to $Y\times Y$.

<1>1. If $Y$ is closed in $X$, then $Y$ is complete.
::: {.proof}
Let
\[
(y_n)_{n\ge1}
\]
be a Cauchy sequence in $Y$.
Because the metric on $Y$ is the restriction of $d$, the same sequence is Cauchy in $X$.
Since $X$ is complete, there is some $x\in X$ such that
\[
y_n\longrightarrow x
\]
in $X$.

Every limit of a sequence from $Y$ lies in the closure $\overline Y$.
Since $Y$ is closed,
\[
\overline Y=Y,
\]
so $x\in Y$.
The convergence $y_n\to x$ in $X$ is exactly convergence in the restricted metric on $Y$.
Thus every Cauchy sequence in $Y$ converges to a point of $Y$, so $Y$ is complete.
:::

<1>2. Assume $Y$ is complete and let $x\in\overline Y$.
There is a sequence $(y_n)$ in $Y$ satisfying
\[
d(x,y_n)<\frac1n
\]
for every $n\ge1$.
::: {.proof}
Since $x\in\overline Y$, every open ball centered at $x$ meets $Y$.
For each $n\ge1$, choose
\[
y_n\in Y\cap B(x,1/n).
\]
Then by definition of the ball,
\[
d(x,y_n)<\frac1n.
\]
:::

<1>3. The sequence $(y_n)$ from <1>2 is Cauchy in $Y$.
::: {.proof}
Let $\varepsilon>0$.
Choose $N$ such that
\[
\frac2N<\varepsilon.
\]
If $m,n\ge N$, then the triangle inequality and <1>2 give
\[
d(y_m,y_n)
\le d(y_m,x)+d(x,y_n)
<\frac1m+\frac1n
\le\frac2N
<\varepsilon.
\]
Hence $(y_n)$ is Cauchy.
:::

<1>4. There is a point $y\in Y$ such that
\[
y_n\longrightarrow y.
\]
::: {.proof}
By <1>3, $(y_n)$ is Cauchy in $Y$.
Since $Y$ is complete by assumption, it converges in $Y$ to some $y\in Y$.
:::

<1>5. The limit $y$ from <1>4 equals $x$.
::: {.proof}
By <1>2,
\[
d(x,y_n)<\frac1n,
\]
so
\[
y_n\longrightarrow x
\]
in $X$.
By <1>4, the same sequence converges to $y$ in $Y$, hence also in $X$.
For every $n$,
\[
d(x,y)
\le d(x,y_n)+d(y_n,y).
\]
Both terms on the right tend to $0$, so
\[
d(x,y)=0.
\]
Therefore $x=y$.
:::

<1>6. If $Y$ is complete, then $Y$ is closed in $X$.
::: {.proof}
Let $x\in\overline Y$.
By <1>2--<1>5, $x=y$ for some $y\in Y$.
Thus
\[
\overline Y\subseteq Y.
\]
The reverse inclusion always holds, so
\[
\overline Y=Y.
\]
Hence $Y$ is closed.
:::

<1>7. Consequently, for a subspace $Y$ of a complete metric space $X$,
\[
\boxed{Y\text{ is complete}\iff Y\text{ is closed in }X.}
\]
::: {.proof}
The forward implication is <1>6 and the reverse implication is <1>1.
:::
:::
