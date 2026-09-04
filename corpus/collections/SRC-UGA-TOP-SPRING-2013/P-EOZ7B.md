---
schema: qual/card@1
id: P-EOZ7B
kind: problem
title: A space is connected iff its only clopen subsets are $\emptyset$ and $X$, and
  the intermediate value theorem
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Restored the source word "open" in the definition of connectedness; its omission changed the mathematical statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked both directions of the clopen characterization and the direct intermediate-value separation argument.
---

::: {.problem}
Recall that a topological space is said to be **connected** if there does not exist a pair $U, V$ of disjoint nonempty open subsets whose union is $X$.

a. Prove that $X$ is connected if and only if the only subsets of $X$ that are both open and closed are $X$ and the empty set.

b. Suppose that $X$ is connected and let $f : X \to \RR$ be a continuous map.
If $a$ and $b$ are two points of $X$ and $r$ is a point of $\RR$ lying between $f (a)$ and $f (b)$ show that there exists a point $c$ of $X$ such that $f (c) = r$.
:::

::: {.solution}
<1>1. If \(X\) is connected, then its only subsets that are both open and closed are \(\varnothing\) and \(X\).
::: {.proof}
Let \(A\subseteq X\) be both open and closed.
Then
\[
X\setminus A
\]
is open because \(A\) is closed.
If \(A\) were neither \(\varnothing\) nor \(X\), then
\[
A
\qquad\text{and}\qquad
X\setminus A
\]
would be disjoint nonempty open subsets of \(X\) whose union is \(X\), contradicting connectedness.
Hence
\[
A=\varnothing
\qquad\text{or}\qquad
A=X.
\]
:::

<1>2. Conversely, if the only clopen subsets of \(X\) are \(\varnothing\) and \(X\), then \(X\) is connected.
::: {.proof}
Suppose \(X\) were disconnected.
Then there would be disjoint nonempty open sets \(U,V\subseteq X\) with
\[
X=U\cup V.
\]
Since they are disjoint and cover \(X\),
\[
U=X\setminus V.
\]
Because \(V\) is open, \(U\) is closed; it is open by assumption.
Thus \(U\) is a clopen subset different from both \(\varnothing\) and \(X\), a contradiction.
:::

<1>3. Therefore
\[
\boxed{X\text{ is connected}\iff\varnothing\text{ and }X\text{ are its only clopen subsets}.}
\]
::: {.proof}
Combine <1>1 and <1>2.
:::

<1>4. Let \(X\) be connected and let \(f:X\to\mathbb R\) be continuous.
If \(r\) lies between \(f(a)\) and \(f(b)\), then there exists \(c\in X\) such that
\[
f(c)=r.
\]
::: {.proof}
If \(r=f(a)\) or \(r=f(b)\), take \(c=a\) or \(c=b\). Otherwise, after interchanging \(a\) and \(b\) if necessary, assume
\[
f(a)<r<f(b).
\]
Suppose no point of \(X\) maps to \(r\). Define
\[
U=f^{-1}(({-}\infty,r)),
\qquad
V=f^{-1}((r,\infty)).
\]
Continuity of \(f\) makes \(U\) and \(V\) open.
They are disjoint, and the assumption
\[
r\notin f(X)
\]
shows that
\[
X=U\cup V.
\]
Moreover,
\[
a\in U,
\qquad
b\in V,
\]
so both are nonempty.
This is a separation of \(X\), contradicting connectedness.
Therefore some \(c\in X\) satisfies \(f(c)=r\).
:::
:::
