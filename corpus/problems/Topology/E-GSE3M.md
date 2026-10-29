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

Write $I = [0,1]$.

::: pf

::: {.pf-step #s1}

Suppose for contradiction that $I = A \union B$ with $A, B$ nonempty, disjoint, and both closed in $I$.

::: pf-proof

This is a disconnection of $I$. Each of $A$ and $B$ is the complement in $I$ of the other, so each is also open in $I$.

:::

:::

::: {.pf-step #s2}

Relabel so that $0 \in A$, and set $T \coloneqq \theset{t \in I \suchthat [0,t] \subseteq A}$ and $s \coloneqq \sup T$.

::: pf-proof

The point $0$ lies in exactly one of $A, B$; swap the labels if needed. Then $0 \in T$, so $T$ is nonempty and bounded above by $1$, and the supremum exists by the least-upper-bound property of $\RR$.

:::

:::

::: {.pf-step #s3}

$[0,s] \subseteq A$.

::: pf-proof

If $0 \le t < s$, some $t' \in T$ satisfies $t' > t$, so $t \in [0,t'] \subseteq A$. Thus $[0,s) \subseteq A$. If $s = 0$, then $s \in A$ by step [](#s2){.pf-ref}. If $s > 0$, then $s$ is a limit of points of $[0,s) \subseteq A$, and $A$ is closed in $I$, so $s \in A$.

:::

:::

::: {.pf-step #s4}

$s = 1$.

::: pf-proof

Suppose $s < 1$. Since $s \in A$ and $A$ is open in $I$ (step [](#s1){.pf-ref}), there is $\varepsilon > 0$ with $(s - \varepsilon, s + \varepsilon) \intersect I \subseteq A$. Put $t = \min(s + \varepsilon/2, 1) > s$. By step [](#s3){.pf-ref}, $[0,t] = [0,s] \union (s,t] \subseteq A$, so $t \in T$ and $t > \sup T$, which is impossible.

:::

:::

::: pf-step

No disconnection of $I$ exists, so $[0,1]$ is connected.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give $I = [0,1] \subseteq A$, so $B = I \setminus A$ is empty, contradicting step [](#s1){.pf-ref}.

:::

:::

:::

:::

::: {.remark}
Further reading: [notes on connectedness](https://sites.math.washington.edu/~morrow/334_16/connected.pdf) and [a discussion of proofs that intervals are connected](https://math.stackexchange.com/questions/934421/proof-of-that-every-interval-is-connected).
:::
