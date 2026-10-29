---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-10
kind: problem
title: The rational-translation quotient of R has the indiscrete topology
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Point-Set Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 10 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    The inverse image of an open quotient set is an open saturated subset of R.
    Any nonempty such set contains an interval, and density of Q gives a point
    of every rational-translation class in that interval; saturation therefore
    forces the inverse image to be all of R.
---

::: {.problem}
Construct a topological space $X$ by starting with $\RR$ with the usual topology and defining $x$ to be equivalent to $y$ if $x-y$ is rational.
Show that the resulting quotient or identification space $X$ has the indiscrete topology, that is, the only open sets are $\varnothing$ and $X$.
:::

::: {.solution}
Let
$$
q:\RR\longrightarrow X=\RR/\!\sim
$$
be the quotient map.

::: pf

::: {.pf-step #rational-in-interval}
Every nonempty open interval in $\RR$ contains a rational number.

::: pf-proof
Let $a<b$.
Choose $n\in\NN$ such that
$$
n(b-a)>1.
$$
Let
$$
m=\lfloor na\rfloor+1.
$$
Then
$$
na<m\le na+1<nb.
$$
Dividing by $n>0$ gives
$$
a<\frac mn<b.
$$
Since $m/n\in\QQ$, the interval $(a,b)$ contains a rational number.
:::

:::

::: {.pf-step #preimage-open-saturated}
If $W\subseteq X$ is open, then
$$
U=q^{-1}(W)
$$
is an open saturated subset of $\RR$.

::: pf-proof
By the definition of the quotient topology, $q^{-1}(W)$ is open in $\RR$.
It is saturated because if $x\in U$ and $y\sim x$, then
$$
q(y)=q(x)\in W,
$$
so $y\in q^{-1}(W)=U$.
:::

:::

::: {.pf-step #saturated-is-all}
Every nonempty open saturated subset $U\subseteq\RR$ is all of $\RR$.

::: pf-proof
Let $U$ be nonempty, open, and saturated.
Choose $x\in U$.
Since $U$ is open, there are real numbers $a<b$ such that
$$
x\in(a,b)\subseteq U.
$$

Take an arbitrary $y\in\RR$.
The interval
$$
(y-b,y-a)
$$
is nonempty because $a<b$.
By step [](#rational-in-interval){.pf-ref}, choose
$$
r\in\QQ\cap(y-b,y-a).
$$
The inequalities
$$
y-b<r<y-a
$$
are equivalent to
$$
a<y-r<b.
$$
Hence
$$
y-r\in(a,b)\subseteq U.
$$
Moreover,
$$
y-(y-r)=r\in\QQ,
$$
so
$$
y\sim y-r.
$$
Since $U$ is saturated and $y-r\in U$, it follows that $y\in U$.
The point $y$ was arbitrary, so $U=\RR$.
:::

:::

::: pf-step
The only open subsets of $X$ are $\varnothing$ and $X$.

::: pf-proof
Both $\varnothing$ and $X$ are open in every topology.

Conversely, let $W\subseteq X$ be a nonempty open set.
By surjectivity of $q$, its inverse image
$$
U=q^{-1}(W)
$$
is nonempty.
By step [](#preimage-open-saturated){.pf-ref} it is open and saturated, so step [](#saturated-is-all){.pf-ref} gives
$$
q^{-1}(W)=\RR.
$$
Applying $q$ and using surjectivity,
$$
W=q(q^{-1}(W))=q(\RR)=X.
$$
Thus every nonempty open subset is all of $X$, so the quotient topology is indiscrete.
:::

:::

:::

:::
