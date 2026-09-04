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
<1>1. If $X$ is locally path connected, every path component of $X$ is open.
::: {.proof}
Let $C$ be a path component and let $x\in C$.
Local path connectedness gives a path-connected neighborhood $U_x$ of $x$.
Every point of $U_x$ can be joined to $x$ by a path in $U_x$, so every point of $U_x$ lies in the same path component as $x$.
Hence
\[
U_x\subseteq C.
\]
Since this holds at every $x\in C$, the component $C$ is open.
:::

<1>2. If $X$ is connected and locally path connected, then $X$ is path connected.
::: {.proof}
The path components partition $X$, and by <1>1 every component is open.
If there were at least two components, one component and the union of all the others would be disjoint nonempty open sets whose union is $X$, contradicting connectedness.
Thus $X$ has one path component.
:::

<1>3. The comb space
\[
X=([0,1]\times\{0\})
\cup(\{0\}\times[0,1])
\cup\bigcup_{n\ge1}(\{1/n\}\times[0,1])
\subseteq\RR^2.
\]
is path connected.
::: {.proof}
Every point on a vertical segment can be joined vertically to the base $[0,1]\times\{0\}$.
The base is itself path connected and meets every vertical segment.
Concatenating these paths joins any two points of $X$.
:::

<1>4. The comb space in <1>3 is not locally path connected at
\[
p=(0,1/2).
\]
::: {.proof}
Let
\[
U=X\cap B_{1/4}(p).
\]
This neighborhood does not meet the base $[0,1]\times\{0\}$.
Any neighborhood $V$ of $p$ in $X$ with $V\subseteq U$ contains points
\[
q_n=(1/n,1/2)
\]
for all sufficiently large $n$.

There is no path in $U$ from $p$ to such a $q_n$.
Indeed, a path in $X$ that avoids the base has positive second coordinate, so its first coordinate is a continuous map from an interval into
\[
\{0\}\cup\{1,1/2,1/3,\ldots\}.
\]
The image must be connected, but every connected subset of this subset of $\RR$ is a singleton.
Thus the first coordinate must be constant.
A path from $p$ to $q_n$ would therefore have to meet the base, contrary to the choice of $U$.

Therefore $U$ contains no path-connected neighborhood of $p$, so $X$ is not locally path connected at $p$.
:::

<1>5. The converse in part (b) is false.
::: {.proof}
By <1>3 the comb space is path connected, while by <1>4 it is not locally path connected.
:::
:::
