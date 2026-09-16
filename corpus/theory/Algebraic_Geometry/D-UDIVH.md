---
schema: qual/card@1
id: D-UDIVH
kind: definition
title: Support of a section and of a sheaf, and why only one is closed
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Support
relations:
- kind: uses
  target: D-0QSI0
review: draft
prompts:
- Define the support of a section, and of a sheaf.
- Why is $\supp(s)$ closed?
- Give a sheaf whose support is not closed.
---

::: {.definition}
For $s \in \mcf(U)$,
\[
\supp(s) \da \ts{ p \in U \st s_p \neq 0 \text{ in } \mcf_p } .
\]
For a sheaf $\mcf$ on $X$,
\[
\supp(\mcf) \da \ts{ p \in X \st \mcf_p \neq 0 } .
\]
:::

::: {.proposition}
$\supp(s)$ is closed in $U$, and $\supp(\mcf)$ need not be closed in $X$.
:::

::: {.proof}
The complement of $\supp(s)$ is open: if $s_p = 0$ then some representative already vanishes, so $\ro{s}{V} = 0$ on a neighborhood $V \ni p$, and then $s_q = 0$ for every $q \in V$.

For the second claim, take $X = \spec \ZZ_{(p)}$, a two-point space $\ts{\eta, \mfm}$ with $\ts{\eta}$ open and not closed, and let $j : \ts{\eta} \injects X$ be that open point.
Then $\mcf \da j_! \ul{\ZZ}$ has $\mcf_\eta = \ZZ$ and $\mcf_\mfm = 0$, so $\supp(\mcf) = \ts{\eta}$, which is not closed.
:::

::: {.proposition}
Let $X$ be a scheme and $\mcf$ a quasicoherent $\OO_X$-module of finite type.
Then $\supp(\mcf)$ is closed, and on an affine open $\Spec A$ with $\mcf|_{\Spec A} \cong \tilde{M}$ it is $V(\operatorname{Ann}_A M)$.
:::

::: {.remark}
The asymmetry is worth stating as a rule, because the two definitions look identical.
Vanishing of a *fixed* section is an open condition: one section propagates outward from a point where it dies.
Vanishing of the whole stalk is not, because different points may be killed by unrelated sections with no common neighborhood.

Extension by zero is exactly the construction that exploits the gap.
For $j$ an open immersion, $j_!$ produces a sheaf supported on $U$ — not on $\cl_X(U)$ — which is why $j_!$ is the functor to reach for when a computation must not spread to the boundary.
By contrast, for $i$ a closed immersion $i_*$ has closed support, and that is the case where support behaves as intuition predicts.
:::
