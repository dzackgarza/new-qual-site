---
schema: qual/card@1
id: P-UNL871F13-PS2.1
kind: problem
title: Included-point and finite-complement topologies on $\RR$ are not homeomorphic
classification:
  areas: [topology]
  topics: [General Topology]
relations: []
review: draft
---

::: {.problem}
Let $X=Y=\RR$.
Give $X$ the included-point topology with included point $0$, and give $Y$ the finite-complement topology.
Determine whether $(X,\mathcal T_{ip})$ and $(Y,\mathcal T_{fc})$ are homeomorphic, and prove your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In the finite-complement topology on
$$
Y=\RR,
$$
every singleton is closed.


::: pf-proof

For any
$$
y\in Y,
$$
the complement
$$
Y\setminus\{y\}
$$
has finite complement, namely
$$
\{y\}.
$$
Hence
$$
Y\setminus\{y\}
$$
is open.
Therefore
$$
\{y\}
$$
is closed.
Thus
$$
(Y,\mathcal T_{fc})
$$
is a
$$
T_1
$$
space.

:::

:::

::: {.pf-step #s1-2}

In the included-point topology on
$$
X=\RR
$$
with included point $0$, the singleton
$$
\{0\}
$$
is not closed.


::: pf-proof

By definition, the open sets are
$$
\varnothing
$$
and all subsets of $X$ that contain the distinguished point
$$
0.
$$

The complement of
$$
\{0\}
$$
is
$$
X\setminus\{0\}.
$$
This set is nonempty and does not contain
$$
0,
$$
so it is not open in the included-point topology.
Hence
$$
\{0\}
$$
is not closed.
Therefore
$$
(X,\mathcal T_{ip})
$$
is not
$$
T_1.
$$

:::

:::

::: {.pf-step #s1-3}

The property of being
$$
T_1
$$
is preserved by homeomorphism.


::: pf-proof

Let
$$
h:Z\to W
$$
be a homeomorphism.
If every singleton in $Z$ is closed, then for
$$
w\in W,
$$
write
$$
w=h(z).
$$
Then
$$
\{w\}
=
h(\{z\}).
$$
Since a homeomorphism maps closed sets to closed sets,
$$
\{w\}
$$
is closed.
Thus $W$ is $T_1$.
The converse follows from $h^{-1}$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
(X,\mathcal T_{ip})
\not\cong
(Y,\mathcal T_{fc}).
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
(Y,\mathcal T_{fc})
$$
is $T_1$.
By step [](#s1-2){.pf-ref},
$$
(X,\mathcal T_{ip})
$$
is not $T_1$.
Step [](#s1-3){.pf-ref} says homeomorphic spaces must agree on this property.
Hence no homeomorphism exists.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
