---
schema: qual/card@1
id: E-GSE3M
kind: problem
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

::: {.problem}
Show that $[0, 1]$ is connected.
:::

::: {.solution}
::: {.concept}
[Reference](https://sites.math.washington.edu/~morrow/334_16/connected.pdf) [A potentially shorter proof](https://math.stackexchange.com/questions/934421/proof-of-that-every-interval-is-connected)
:::

::: pf

::: {.pf-step #s1}

Suppose for contradiction that $I = [0,1]$ is disconnected, so $I = A \union B$ with $A, B$ nonempty, disjoint, and separated: $\cl_I(A) \intersect B = A \intersect \cl_I(B) = \emptyset$.

::: pf-proof

definition of a disconnection.

:::

:::

::: {.pf-step #s2}

Relabel so that $0 \in A$, and set $s \definedas \sup A$.

::: pf-proof

$0$ lies in exactly one of $A, B$; swap the labels if needed. The supremum exists because $A \subseteq [0,1]$ is bounded above and $\RR$ has the least-upper-bound property.

:::

:::

::: {.pf-step #s3}

$s \in A$.

::: pf-proof

::: {.pf-step #s3-1}

Suppose instead $s \in B$.

::: pf-proof

$s \in [0,1] = A \union B$, so if $s \notin A$ then $s \in B$.

:::

:::

::: {.pf-step #s3-2}

Since $\cl_I(A) \intersect B = \emptyset$, the point $s \in B$ is not in $\cl_I(A)$, so there is a neighborhood $U$ of $s$ with $U \intersect A = \emptyset$.

::: pf-proof

a point outside the closure of $A$ has a neighborhood disjoint from $A$.

:::

:::

::: {.pf-step #s3-3}

But $s = \sup A$ means every neighborhood of $s$ meets $A$: for any $\eps > 0$ there is $a \in A$ with $s - \eps < a \le s$.

::: pf-proof

if some neighborhood $(s-\eps, s+\eps)$ missed $A$, then $s - \eps$ would be an upper bound of $A$ smaller than $s$, contradicting that $s$ is the least upper bound.

:::

:::

::: pf-step

Steps [](#s3-2){.pf-ref} and [](#s3-3){.pf-ref} contradict each other, so $s \notin B$, hence $s \in A$.

::: pf-proof

Step [](#s3-1){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s4}

$s = 1$.

::: pf-proof

::: pf-step

Since $A \intersect \cl_I(B) = \emptyset$, the point $s \in A$ is not in $\cl_I(B)$, so there is $\eps > 0$ with $(s - \eps, s + \eps) \intersect I \subseteq A$.

::: pf-proof

a point outside the closure of $B$ has a neighborhood disjoint from $B$; within $I$ that neighborhood lies entirely in $A$.

:::

:::

::: {.pf-step #s4-2}

If $s < 1$, then $(s, s + \eps) \intersect I$ contains points of $A$ strictly larger than $s$.

::: pf-proof

take any $t$ with $s < t < \min(s + \eps, 1)$; then $t \in (s-\eps, s+\eps) \intersect I \subseteq A$.

:::

:::

::: pf-step

This contradicts $s = \sup A$, so $s = 1$.

::: pf-proof

Step [](#s4-2){.pf-ref} produces an element of $A$ exceeding the supremum $s$.

:::

:::

:::

:::

::: {.pf-step #s5}

Contradiction: $1 = s \in A$, but $B$ is nonempty.

::: pf-proof

::: pf-step

Since $B \neq \emptyset$, pick $b \in B \subseteq [0,1]$.

::: pf-proof

$B$ is nonempty by hypothesis.

:::

:::

::: {.pf-step #s5-2}

$b \le 1 = s = \sup A$, so for every $\eps > 0$ there is $a \in A$ with $b - \eps < a \le b$.

::: pf-proof

$b$ is below the supremum of $A$, so $A$ meets every neighborhood of $b$.

:::

:::

::: pf-step

Hence $b \in \cl_I(A)$, contradicting $\cl_I(A) \intersect B = \emptyset$.

::: pf-proof

Step [](#s5-2){.pf-ref} shows every neighborhood of $b$ meets $A$, which is the definition of $b \in \cl_I(A)$.

:::

:::

:::

:::

::: pf-step

Therefore no disconnection of $[0,1]$ exists, so $[0,1]$ is connected.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
