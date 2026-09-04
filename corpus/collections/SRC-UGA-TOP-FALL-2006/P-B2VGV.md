---
schema: qual/card@1
id: P-B2VGV
kind: problem
title: Connected and locally path-connected implies path-connected; the converse fails
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

::: {.problem}
\envlist

a. Prove that if the space $X$ is connected and locally path connected then $X$ is path connected.

b. Is the converse true?
Prove or give a counterexample.
:::

::: {.solution}
For (a), let $C$ be a path component of $X$.
We claim that $C$ is open.
If $x\in C$, local path connectedness gives a path-connected neighborhood $U_x$ of $x$.
Every point of $U_x$ can be joined to $x$ by a path in $U_x$, and $x$ can be joined to every point of $C$ represented in its path component.
Hence
\[
U_x\subseteq C.
\]
Thus every path component is open.

The path components partition $X$.
If there were at least two of them, then one path component $C$ and the union of all the others would be disjoint nonempty open sets whose union is $X$, contradicting connectedness.
Therefore $X$ has exactly one path component, so $X$ is path connected.

For (b), the converse is false.
Consider the comb space
\[
X=([0,1]\times\{0\})
\cup(\{0\}\times[0,1])
\cup\bigcup_{n\ge1}(\{1/n\}\times[0,1])
\subseteq\RR^2.
\]
It is path connected: every point on a vertical segment can first be joined vertically to the base $[0,1]\times\{0\}$, and the base joins all of the vertical segments to one another.

However, $X$ is not locally path connected at
\[
p=(0,1/2).
\]
Let
\[
U=X\cap B_{1/4}(p).
\]
Any neighborhood $V$ of $p$ in $X$ with $V\subseteq U$ contains points
\[
q_n=(1/n,1/2)
\]
for all sufficiently large $n$.
There is no path in $U$ from $p$ to any such $q_n$.
Indeed, a path in $X$ that avoids the base has second coordinate $>0$, so its first coordinate is a continuous map into
\[
\{0\}\cup\{1,1/2,1/3,\ldots\}.
\]
The image of an interval is connected, while this set contains no nontrivial connected subsets; hence the first coordinate must be constant.
A path from $p$ to $q_n$ therefore must meet the base, but $U$ does not meet the base.

Thus no neighborhood of $p$ contained in $U$ is path connected.
Hence the comb space is path connected but not locally path connected.
:::
