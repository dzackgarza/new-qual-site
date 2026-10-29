---
schema: qual/card@1
id: P-AGXHWGLOBALSECEX
kind: problem
title: Global sections is left exact but not exact, and the exponential sequence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaf Cohomology
  - Exact Sequences
  - Global Sections
relations: []
review: draft
---

::: {.problem}
For any open $U \subseteq X$ show that the functor
$$
\Gamma\qty{U, {-}}: \Sh(X) \to \mathsf{Ab}\mathsf{Grp}
$$
is left exact, but need not be exact.
:::

::: {.solution}
Fix an open $U \subseteq X$ and an exact sequence of sheaves of abelian groups on $X$
$$
0 \to \mcf_1 \xrightarrow{f} \mcf_2 \xrightarrow{g} \mcf_3 \to 0
.$$
A sequence of sheaves is exact if and only if it is exact on every stalk.
For an open $W$, write $f_W\colon \mcf_1(W) \to \mcf_2(W)$ for the component of $f$ on $W$.

::: pf

::: {.pf-step #injective}
For every open $W \subseteq X$, the map $f_W$ is injective.

::: pf-proof
The kernel presheaf $W \mapsto \ker f_W$ is a sheaf, and its stalk at $p$ is $\ker f_p = 0$, because $f$ is injective on stalks.
A sheaf whose stalks all vanish is zero, by the identity axiom.
Hence $\ker f_W = 0$ for every open $W$.
:::

:::

::: {.pf-step #im-in-ker}
$\im f_U \subseteq \ker g_U$.

::: pf-proof
Let $s = f_U(r)$ with $r \in \mcf_1(U)$.
For every $p \in U$, the germ of $g_U(s)$ at $p$ is $g_p(f_p(r_p)) = 0$, because $g_p \circ f_p = 0$.
A section of $\mcf_3$ whose germs all vanish is $0$, so $g_U(s) = 0$.
:::

:::

::: {.pf-step #ker-in-im}
$\ker g_U \subseteq \im f_U$.

::: pf-proof
Let $s \in \mcf_2(U)$ with $g_U(s) = 0$.
For each $p \in U$, the germ $s_p$ lies in $\ker g_p = \im f_p$.
So there are an open neighborhood $W_p \subseteq U$ of $p$ and $t_p \in \mcf_1(W_p)$ with $f_{W_p}(t_p) = s|_{W_p}$, after shrinking $W_p$ so that the germ equality holds on all of $W_p$.
On $W_p \cap W_q$, the section $t_p - t_q$ has image $s - s = 0$ under $f_{W_p \cap W_q}$, which is injective by step [](#injective){.pf-ref}.
So the $t_p$ agree on overlaps and glue to $t \in \mcf_1(U)$.
The section $f_U(t) - s$ restricts to $0$ on every $W_p$, so $f_U(t) = s$ by the identity axiom for $\mcf_2$.
:::

:::

::: pf-step
$\Gamma(U, {-})$ is left exact: $0 \to \mcf_1(U) \xrightarrow{f_U} \mcf_2(U) \xrightarrow{g_U} \mcf_3(U)$ is exact.

::: pf-proof
Exactness at $\mcf_1(U)$ is step [](#injective){.pf-ref} with $W = U$, and exactness at $\mcf_2(U)$ is steps [](#im-in-ker){.pf-ref} and [](#ker-in-im){.pf-ref}.
:::

:::

::: pf-step
$\Gamma(U, {-})$ need not be exact.

::: pf-proof

::: {.pf-step #exp-sequence}
On $X = U = \units{\CC}$, the sequence
$$
0 \to \underline{\ZZ} \to \Hol_X \xrightarrow{\exp} \units{\Hol_X} \to 0, \qquad \exp(h) = e^{2\pi i h},
$$
is an exact sequence of sheaves of abelian groups.

::: pf-proof
Here $\units{\Hol_X}$ is the sheaf of nonvanishing holomorphic functions under multiplication.
A holomorphic $h$ with $e^{2\pi i h} = 1$ takes values in $\ZZ$ and is therefore locally constant, so the kernel of $\exp$ is $\underline{\ZZ}$.
Every nonvanishing holomorphic function has a holomorphic logarithm on a disk, so $\exp$ is surjective on stalks.
:::

:::

::: pf-step
The map $\exp\colon \Hol_X(X) \to \units{\Hol_X}(X)$ is not surjective, so $\Gamma(X, {-})$ does not carry the exact sequence of step [](#exp-sequence){.pf-ref} to an exact sequence.

::: pf-proof
If it were surjective, the identity function $z$ would equal $e^{2\pi i h}$ for some holomorphic $h$ on $\units{\CC}$.
Then $dz/z = 2\pi i\, h'(z)\, dz$ would be exact, so $\oint_{\abs{z} = 1} dz/z = 0$.
But this integral is $2\pi i \neq 0$.
:::

:::

:::

:::

:::
:::
