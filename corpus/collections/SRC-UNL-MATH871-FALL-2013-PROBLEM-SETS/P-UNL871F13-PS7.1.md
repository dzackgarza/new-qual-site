---
schema: qual/card@1
id: P-UNL871F13-PS7.1
kind: problem
title: Separate a point from a closed set in a metrizable space
classification:
  areas: [topology]
  topics: [Separation Axioms, Metric Spaces]
relations: []
review: draft
---

::: {.problem}
Let $X$ be a metrizable space, let $p\in X$, and let $C\subseteq X$ be closed with $p\notin C$.
Prove that there are disjoint open sets $U,V\subseteq X$ such that
$$
p\in U,\qquad C\subseteq V.
$$
:::

::: {.solution}

Fix a metric
$$
d
$$
that induces the topology of $X$.

::: pf

::: {.pf-step #s1-1}

Since $C$ is closed and
$$
p\notin C,
$$
there exists
$$
\varepsilon>0
$$
such that
$$
B(p,\varepsilon)
\cap
C
=
\varnothing.
$$


::: pf-proof

Because $C$ is closed,
$$
X\setminus C
$$
is open.
Since
$$
p\in X\setminus C,
$$
the metric topology gives an
$$
\varepsilon>0
$$
with
$$
B(p,\varepsilon)
\subseteq
X\setminus C.
$$

:::

:::

::: {.pf-step #s1-2}

In particular,
$$
d(p,c)
\ge
\varepsilon
\qquad
(c\in C).
$$


::: pf-proof

If some
$$
c\in C
$$
satisfied
$$
d(p,c)<\varepsilon,
$$
then
$$
c\in B(p,\varepsilon),
$$
contradicting step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Define
$$
U
\coloneqq
B\left(p,\frac{\varepsilon}{3}\right)
$$
and
$$
V
\coloneqq
\bigcup_{c\in C}
B\left(c,\frac{\varepsilon}{3}\right).
$$
Then $U$ and $V$ are open,
$$
p\in U,
$$
and
$$
C\subseteq V.
$$


::: pf-proof

Both sets are unions of open balls.

Also
$$
d(p,p)=0<\frac{\varepsilon}{3},
$$
so
$$
p\in U.
$$

For every
$$
c\in C,
$$
one has
$$
c\in
B\left(c,\frac{\varepsilon}{3}\right)
\subseteq
V.
$$
Thus
$$
C\subseteq V.
$$

:::

:::

::: {.pf-step #s1-4}

The open sets $U$ and $V$ are disjoint.


::: pf-proof

Suppose, toward a contradiction, that
$$
x\in U\cap V.
$$
Then
$$
d(p,x)
<
\frac{\varepsilon}{3}.
$$
Because
$$
x\in V,
$$
there is some
$$
c\in C
$$
such that
$$
d(x,c)
<
\frac{\varepsilon}{3}.
$$
By the triangle inequality,
$$
\begin{aligned}
d(p,c)
&\le
d(p,x)+d(x,c)\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}\\
&=
\frac{2\varepsilon}{3}
<
\varepsilon.
\end{aligned}
$$
This contradicts step [](#s1-2){.pf-ref}.
Therefore
$$
U\cap V
=
\varnothing.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
p\in U,
\qquad
C\subseteq V,
\qquad
U\cap V=\varnothing,
}
$$
with $U$ and $V$ open.


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required separation.

:::

:::

:::
