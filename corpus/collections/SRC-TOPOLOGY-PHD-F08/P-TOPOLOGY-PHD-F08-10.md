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
Construct a topological space $X$ by starting with $\mathbb R$ with the usual topology and defining $x$ to be equivalent to $y$ if $x-y$ is rational.
Show that the resulting quotient or identification space $X$ has the indiscrete topology, that is, the only open sets are $\varnothing$ and $X$.
:::

::: {.solution}
Let
\[
q:\mathbb R\longrightarrow X=\mathbb R/\!\sim
\]
be the quotient map.

<1>1. Every nonempty open interval in $\mathbb R$ contains a rational number.
::: {.proof}
Let $a<b$.
Choose $n\in\mathbb N$ such that
\[
n(b-a)>1.
\]
Let
\[
m=\lfloor na\rfloor+1.
\]
Then
\[
na<m\le na+1<nb.
\]
Dividing by $n>0$ gives
\[
a<\frac mn<b.
\]
Since $m/n\in\mathbb Q$, the interval $(a,b)$ contains a rational number.
:::

<1>2. If $W\subseteq X$ is open, then
\[
U=q^{-1}(W)
\]
is an open saturated subset of $\mathbb R$.
::: {.proof}
By the definition of the quotient topology, $q^{-1}(W)$ is open in $\mathbb R$.
It is saturated because if $x\in U$ and $y\sim x$, then
\[
q(y)=q(x)\in W,
\]
so $y\in q^{-1}(W)=U$.
:::

<1>3. Every nonempty open saturated subset $U\subseteq\mathbb R$ is all of $\mathbb R$.
::: {.proof}
Let $U$ be nonempty, open, and saturated.
Choose $x\in U$.
Since $U$ is open, there are real numbers $a<b$ such that
\[
x\in(a,b)\subseteq U.
\]

Take an arbitrary $y\in\mathbb R$.
The interval
\[
(y-b,y-a)
\]
is nonempty because $a<b$.
By <1>1, choose
\[
r\in\mathbb Q\cap(y-b,y-a).
\]
The inequalities
\[
y-b<r<y-a
\]
are equivalent to
\[
a<y-r<b.
\]
Hence
\[
y-r\in(a,b)\subseteq U.
\]
Moreover,
\[
y-(y-r)=r\in\mathbb Q,
\]
so
\[
y\sim y-r.
\]
Since $U$ is saturated and $y-r\in U$, it follows that $y\in U$.
The point $y$ was arbitrary, so $U=\mathbb R$.
:::

<1>4. The only open subsets of $X$ are $\varnothing$ and $X$.
::: {.proof}
Both $\varnothing$ and $X$ are open in every topology.

Conversely, let $W\subseteq X$ be a nonempty open set.
By surjectivity of $q$, its inverse image
\[
U=q^{-1}(W)
\]
is nonempty.
By <1>2 it is open and saturated, so <1>3 gives
\[
q^{-1}(W)=\mathbb R.
\]
Applying $q$ and using surjectivity,
\[
W=q(q^{-1}(W))=q(\mathbb R)=X.
\]
Thus every nonempty open subset is all of $X$, so the quotient topology is indiscrete.
:::
:::
