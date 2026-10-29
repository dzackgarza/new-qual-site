---
schema: qual/card@1
id: P-WESTOP03-05
kind: problem
title: Cardinality bound for connected normal $T_1$ spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: A second copy of the 2003 exam later in the same retained extraction recovers the bound that was garbled in the first copy.
---

::: {.problem}
Show that if $X$ is connected, normal, and $T_1$, then either
$$
|X|\le1
$$
or
$$
|X|\ge2^{\aleph_0}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume $|X|>1$, and choose distinct points
$$
a,b\in X.
$$


::: pf-proof

This is the only case not already covered by the alternative $|X|\leq1$.

:::

:::

::: {.pf-step #s1-2}

Since $X$ is $T_1$, the sets $\{a\}$ and $\{b\}$ are disjoint closed subsets of $X$.


::: pf-proof

In a $T_1$ space every singleton is closed, and $a\ne b$ makes the two singletons disjoint.

:::

:::

::: {.pf-step #s1-3}

By Urysohn's lemma, there exists a continuous function
$$
f:X\to[0,1]
$$
such that
$$
f(a)=0,
\qquad
f(b)=1.
$$


::: pf-proof

Urysohn's lemma states that in a normal space, any two disjoint closed subsets can be separated by a continuous $[0,1]$-valued function taking the values $0$ and $1$ on the respective closed sets. Apply it to the closed singletons from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The image $f(X)$ is connected.


::: pf-proof

Continuous images of connected spaces are connected, and $X$ is connected by hypothesis.

:::

:::

::: {.pf-step #s1-5}

Since
$$
0,1\in f(X)\subseteq[0,1]
$$
and $f(X)$ is connected, one has
$$
f(X)=[0,1].
$$


::: pf-proof

Connected subsets of $\RR$ are intervals. Any interval contained in $[0,1]$ and containing both endpoints $0$ and $1$ must contain every number between them, hence equals $[0,1]$.

:::

:::

::: {.pf-step #s1-6}

Thus $f$ is a surjection from $X$ onto $[0,1]$, so
$$
|X|\geq|[0,1]|.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives surjectivity. A surjection $X\to Y$ implies $|Y|\leq|X|$: choosing one preimage for each element of $Y$ gives an injection $Y\to X$ (equivalently, this is the standard cardinal comparison associated to a surjection).

:::

:::

::: {.pf-step #s1-7}

Since
$$
|[0,1]|=2^{\aleph_0},
$$
it follows that
$$
\boxed{|X|\geq2^{\aleph_0}.}
$$


::: pf-proof

The interval $[0,1]$ has the cardinality of the continuum, namely $2^{\aleph_0}$. Combine this with step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore every connected normal $T_1$ space satisfies
$$
\boxed{|X|\leq1\quad\text{or}\quad |X|\geq2^{\aleph_0}.}
$$


::: pf-proof

If $|X|\leq1$, the first alternative holds. If $|X|>1$, steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} prove the second.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is exactly the required dichotomy.

:::

:::

:::
