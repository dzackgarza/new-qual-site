---
schema: qual/card@1
id: P-UNL871F13-PS3.2
kind: problem
title: Product and cofinite topologies on $\ZZ^2$
classification:
  areas: [topology]
  topics: [Product Topology]
relations: []
review: draft
---

::: {.problem}
Let $X=Y=\ZZ$, each with the finite-complement topology.
Let $\mathcal T_{prod}$ be the product topology on $X\times Y$, and let $\mathcal T_{fc}$ be the finite-complement topology on $X\times Y$.

Determine whether
$$
\mathcal T_{prod}=\mathcal T_{fc}.
$$
If equality fails, determine which, if either, of the containments
$$
\mathcal T_{prod}\subseteq\mathcal T_{fc},
\qquad
\mathcal T_{fc}\subseteq\mathcal T_{prod}
$$
holds, and prove your answer.
:::

::: {.solution}

Write
$$
Z=\ZZ\times\ZZ.
$$

::: pf

::: {.pf-step #s1-1}

Every cofinite-open subset of $Z$ is open in the product topology:
$$
\mathcal T_{\mathrm{fc}}
\subseteq
\mathcal T_{\mathrm{prod}}.
$$


::: pf-proof

Let
$$
O\in\mathcal T_{\mathrm{fc}}.
$$
If
$$
O=\varnothing,
$$
there is nothing to prove.

Otherwise,
$$
F
\coloneqq
Z\setminus O
$$
is finite.
Fix
$$
(x,y)\in O.
$$

Partition the forbidden points according to whether their first coordinate
equals $x$:
$$
F_1
\coloneqq
\{(a,b)\in F:a\ne x\},
\qquad
F_2
\coloneqq
\{(x,b)\in F\}.
$$
Define
$$
U
\coloneqq
\ZZ
\setminus
\{a:(a,b)\in F_1\}
$$
and
$$
V
\coloneqq
\ZZ
\setminus
\{b:(x,b)\in F_2\}.
$$

Only finitely many integers are removed from $U$ and $V$, so both are open
in the cofinite topology on $\ZZ$.
Also
$$
x\in U.
$$
Since
$$
(x,y)\notin F,
$$
one has
$$
y\in V.
$$
Thus
$$
(x,y)\in U\times V.
$$

We claim
$$
U\times V
\subseteq
O.
$$
Indeed, let
$$
(a,b)\in F.
$$
If
$$
a\ne x,
$$
then $a$ was removed from $U$.
If
$$
a=x,
$$
then $b$ was removed from $V$.
Hence no point of $F$ lies in $U\times V$.

Therefore every point of $O$ has a product-basic neighborhood contained in
$O$, so
$$
O\in\mathcal T_{\mathrm{prod}}.
$$

:::

:::

::: {.pf-step #s1-2}

The reverse containment fails.


::: pf-proof

Consider
$$
W
\coloneqq
(\ZZ\setminus\{0\})
\times
\ZZ.
$$
The set
$$
\ZZ\setminus\{0\}
$$
is cofinite-open in $X$, and
$$
\ZZ
$$
is open in $Y$.
Hence
$$
W
\in
\mathcal T_{\mathrm{prod}}.
$$

But
$$
Z\setminus W
=
\{0\}\times\ZZ,
$$
which is infinite.
Therefore $W$ is neither empty nor cofinite, so
$$
W\notin\mathcal T_{\mathrm{fc}}.
$$
Thus
$$
\mathcal T_{\mathrm{prod}}
\nsubseteq
\mathcal T_{\mathrm{fc}}.
$$

:::

:::

::: {.pf-step #s1-3}

Consequently
$$
\boxed{
\mathcal T_{\mathrm{fc}}
\subsetneq
\mathcal T_{\mathrm{prod}}.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives the containment, and step [](#s1-2){.pf-ref} proves it is strict.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the complete comparison of the two topologies.

:::

:::

:::
