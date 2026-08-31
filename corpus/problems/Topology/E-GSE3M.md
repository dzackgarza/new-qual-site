---
schema: qual/card@1
id: E-GSE3M
kind: exercise
title: The interval $[0,1]$ is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Euclidean Spaces
relations: []
review: draft
---

Show that $[0, 1]$ is connected.

::: {.solution}
::: {.concept}
[Reference](https://sites.math.washington.edu/~morrow/334_16/connected.pdf) [A potentially shorter proof](https://math.stackexchange.com/questions/934421/proof-of-that-every-interval-is-connected)
:::

<1>1. Suppose for contradiction that $I = [0,1]$ is disconnected, so $I = A \union B$ with $A, B$ nonempty, disjoint, and separated: $\cl_I(A) \intersect B = A \intersect \cl_I(B) = \emptyset$.
::: {.proof}
definition of a disconnection.
:::

<1>2. Relabel so that $0 \in A$, and set $s \da \sup A$.
::: {.proof}
$0$ lies in exactly one of $A, B$; swap the labels if needed. The supremum exists because $A \subseteq [0,1]$ is bounded above and $\RR$ has the least-upper-bound property.
:::

<1>3. $s \in A$.
<2>1. Suppose instead $s \in B$.
::: {.proof}
$s \in [0,1] = A \union B$, so if $s \notin A$ then $s \in B$.
:::
<2>2. Since $\cl_I(A) \intersect B = \emptyset$, the point $s \in B$ is not in $\cl_I(A)$, so there is a neighborhood $U$ of $s$ with $U \intersect A = \emptyset$.
::: {.proof}
a point outside the closure of $A$ has a neighborhood disjoint from $A$.
:::
<2>3. But $s = \sup A$ means every neighborhood of $s$ meets $A$: for any $\eps > 0$ there is $a \in A$ with $s - \eps < a \le s$.
::: {.proof}
if some neighborhood $(s-\eps, s+\eps)$ missed $A$, then $s - \eps$ would be an upper bound of $A$ smaller than $s$, contradicting that $s$ is the least upper bound.
:::
<2>4. <2>2 and <2>3 contradict each other, so $s \notin B$, hence $s \in A$.
::: {.proof}
<2>1.
:::

<1>4. $s = 1$.
<2>1. Since $A \intersect \cl_I(B) = \emptyset$, the point $s \in A$ is not in $\cl_I(B)$, so there is $\eps > 0$ with $(s - \eps, s + \eps) \intersect I \subseteq A$.
::: {.proof}
a point outside the closure of $B$ has a neighborhood disjoint from $B$; within $I$ that neighborhood lies entirely in $A$.
:::
<2>2. If $s < 1$, then $(s, s + \eps) \intersect I$ contains points of $A$ strictly larger than $s$.
::: {.proof}
take any $t$ with $s < t < \min(s + \eps, 1)$; then $t \in (s-\eps, s+\eps) \intersect I \subseteq A$.
:::
<2>3. This contradicts $s = \sup A$, so $s = 1$.
::: {.proof}
<2>2 produces an element of $A$ exceeding the supremum $s$.
:::

<1>5. Contradiction: $1 = s \in A$, but $B$ is nonempty.
<2>1. Since $B \neq \emptyset$, pick $b \in B \subseteq [0,1]$.
::: {.proof}
$B$ is nonempty by hypothesis.
:::
<2>2. $b \le 1 = s = \sup A$, so for every $\eps > 0$ there is $a \in A$ with $b - \eps < a \le b$.
::: {.proof}
$b$ is below the supremum of $A$, so $A$ meets every neighborhood of $b$.
:::
<2>3. Hence $b \in \cl_I(A)$, contradicting $\cl_I(A) \intersect B = \emptyset$.
::: {.proof}
<2>2 shows every neighborhood of $b$ meets $A$, which is the definition of $b \in \cl_I(A)$.
:::

<1>6. Therefore no disconnection of $[0,1]$ exists, so $[0,1]$ is connected.
::: {.proof}
<1>1 through <1>5.
:::
:::
