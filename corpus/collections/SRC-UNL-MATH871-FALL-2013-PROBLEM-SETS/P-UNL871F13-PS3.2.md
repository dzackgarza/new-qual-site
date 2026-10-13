---
schema: qual/card@1
id: P-UNL871F13-PS3.2
kind: problem
title: Product and cofinite topologies on $\mathbb Z^2$
classification:
  areas: [topology]
  topics: [Product Topology]
relations: []
review: draft
---

::: {.problem}
Let $X=Y=\mathbb Z$, each with the finite-complement topology.
Let $\mathcal T_{prod}$ be the product topology on $X\times Y$, and let $\mathcal T_{fc}$ be the finite-complement topology on $X\times Y$.

Determine whether
\[
\mathcal T_{prod}=\mathcal T_{fc}.
\]
If equality fails, determine which, if either, of the containments
\[
\mathcal T_{prod}\subseteq\mathcal T_{fc},
\qquad
\mathcal T_{fc}\subseteq\mathcal T_{prod}
\]
holds, and prove your answer.
:::

::: {.solution}
Write
\[
Z=\mathbb Z\times\mathbb Z.
\]

<1>1. Every cofinite-open subset of $Z$ is open in the product topology:
\[
\mathcal T_{mathrm{fc}}
\subseteq
\mathcal T_{mathrm{prod}}.
\]

::: {.proof}
Let
\[
O\in\mathcal T_{mathrm{fc}}.
\]
If
\[
O=\varnothing,
\]
there is nothing to prove.

Otherwise,
\[
F
\coloneqq
Z\setminus O
\]
is finite.
Fix
\[
(x,y)\in O.
\]

Partition the forbidden points according to whether their first coordinate
equals $x$:
\[
F_1
\coloneqq
\{(a,b)\in F:a\ne x\},
\qquad
F_2
\coloneqq
\{(x,b)\in F\}.
\]
Define
\[
U
\coloneqq
\mathbb Z
\setminus
\{a:(a,b)\in F_1\}
\]
and
\[
V
\coloneqq
\mathbb Z
\setminus
\{b:(x,b)\in F_2\}.
\]

Only finitely many integers are removed from $U$ and $V$, so both are open
in the cofinite topology on $\mathbb Z$.
Also
\[
x\in U.
\]
Since
\[
(x,y)\notin F,
\]
one has
\[
y\in V.
\]
Thus
\[
(x,y)\in U\times V.
\]

We claim
\[
U\times V
\subseteq
O.
\]
Indeed, let
\[
(a,b)\in F.
\]
If
\[
a\ne x,
\]
then $a$ was removed from $U$.
If
\[
a=x,
\]
then $b$ was removed from $V$.
Hence no point of $F$ lies in $U\times V$.

Therefore every point of $O$ has a product-basic neighborhood contained in
$O$, so
\[
O\in\mathcal T_{mathrm{prod}}.
\]
:::

<1>2. The reverse containment fails.

::: {.proof}
Consider
\[
W
\coloneqq
(\mathbb Z\setminus\{0\})
\times
\mathbb Z.
\]
The set
\[
\mathbb Z\setminus\{0\}
\]
is cofinite-open in $X$, and
\[
\mathbb Z
\]
is open in $Y$.
Hence
\[
W
\in
\mathcal T_{mathrm{prod}}.
\]

But
\[
Z\setminus W
=
\{0\}\times\mathbb Z,
\]
which is infinite.
Therefore $W$ is neither empty nor cofinite, so
\[
W\notin\mathcal T_{mathrm{fc}}.
\]
Thus
\[
\mathcal T_{mathrm{prod}}
\nsubseteq
\mathcal T_{mathrm{fc}}.
\]
:::

<1>3. Consequently
\[
\boxed{
\mathcal T_{mathrm{fc}}
\subsetneq
\mathcal T_{mathrm{prod}}.
}
\]

::: {.proof}
Step <1>1 gives the containment, and step <1>2 proves it is strict.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the complete comparison of the two topologies.
:::
:::
