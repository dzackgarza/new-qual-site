---
schema: qual/card@1
id: P-BKS14-8A
kind: problem
title: A group of order $48$ has a normal subgroup of order $16$ or $8$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the coset action, containment of its kernel in a Sylow 2-subgroup, and the resulting order possibilities.
---

::: {.problem}
Let $G$ be a group of order $48$. Show that $G$ contains a normal subgroup of order $16$ or $8$.
:::

::: {.solution}
Let $P$ be a Sylow $2$-subgroup of $G$.

<1>1. One has
$$
\abs{P}=16
$$
and
$$
[G:P]=3.
$$

::: {.proof}
Since
$$
\abs{G}=48=2^4\cdot3,
$$
a Sylow $2$-subgroup has order $2^4=16$. Its index is therefore
$$
\frac{48}{16}=3.
$$
:::

<1>2. Left multiplication on the set of left cosets
$$
G/P
$$
defines a homomorphism
$$
\rho:G\longrightarrow S_3.
$$

::: {.proof}
There are three left cosets by step <1>1. For $g\in G$, define
$$
\rho(g)(xP)
\coloneqq
(gx)P.
$$
This is a permutation of the coset set, and
$$
\rho(gh)=\rho(g)\rho(h)
$$
because left multiplication is associative.
:::

<1>3. Let
$$
K\coloneqq\ker\rho.
$$
Then $K$ is a normal subgroup of $G$.

::: {.proof}
The kernel of every group homomorphism is normal.
:::

<1>4. One has
$$
K\subseteq P.
$$

::: {.proof}
Every element $k\in K$ fixes every coset, in particular the coset $P$.
Thus
$$
kP=P.
$$
This is equivalent to $k\in P$.
:::

<1>5. The index
$$
[G:K]
$$
divides $6$.

::: {.proof}
By the first isomorphism theorem,
$$
G/K
\cong
\operatorname{im}\rho.
$$
The image is a subgroup of $S_3$, whose order is $6$. Therefore
$$
[G:K]
=
\abs{\operatorname{im}\rho}
$$
divides $6$.
:::

<1>6. The order of $K$ is either
$$
16
$$
or
$$
8.
$$

::: {.proof}
By step <1>4, $K$ is a subgroup of the $2$-group $P$, so
$$
\abs{K}
$$
is a power of $2$ dividing $16$.

By step <1>5,
$$
\abs{K}
=
\frac{48}{[G:K]},
$$
where
$$
[G:K]\in\{1,2,3,6\}.
$$
Thus the possible values from this formula are
$$
48,\ 24,\ 16,\ 8.
$$
The only powers of $2$ among them are $16$ and $8$.
:::

<1>7. Therefore $G$ contains a normal subgroup of order
$$
\boxed{16\text{ or }8}.
$$

::: {.proof}
The subgroup $K$ is normal by step <1>3 and has one of the two required
orders by step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
