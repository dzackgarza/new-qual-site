---
schema: qual/card@1
id: P-BKS12-2A
kind: problem
title: A finite group is not the union of conjugates of a proper subgroup
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 1 of the retained Spring 2012 solution PDF and independently reviewed the normalizer-counting argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the number of distinct conjugates, the common-identity overlap bound, and the comparison with the subgroup index.
---

::: {.problem}
For G a finite group, H a proper subgroup, show that $G \neq \bigcup \{ g H g ^ { - 1 } ; g \in G \}$
:::

::: {.solution}
Let
$$
N\coloneqq N_G(H)
=
\{g\in G:gHg^{-1}=H\}
$$
be the normalizer of $H$.

::: pf

::: {.pf-step #conjugate-count}
The number of distinct conjugates of $H$ in $G$ is
$$
k=[G:N].
$$

::: pf-proof
The group $G$ acts by conjugation on the set of subgroups of $G$. The
stabilizer of $H$ under this action is exactly $N_G(H)=N$. The
orbit-stabilizer theorem therefore gives the stated number of conjugates.
:::

:::

::: {.pf-step #k-bound}
One has
$$
k\leq[G:H].
$$

::: pf-proof
Every element of $H$ normalizes $H$, so
$$
H\subseteq N.
$$
Hence
$$
[G:N]\leq[G:H].
$$
Apply step [](#conjugate-count){.pf-ref}.
:::

:::

::: {.pf-step #union-bound}
The union of all conjugates of $H$ has cardinality at most
$$
1+k(\abs{H}-1).
$$

::: pf-proof
Every conjugate $gHg^{-1}$ has exactly $\abs{H}$ elements and contains the
identity element. Count the identity once, and then allow at most
$\abs{H}-1$ additional elements from each of the $k$ conjugates. Further
overlaps can only decrease the size of the union.
:::

:::

::: {.pf-step #union-strictly-smaller}
The union of the conjugates has strictly fewer than $\abs{G}$
elements.

::: pf-proof
By steps [](#k-bound){.pf-ref} and [](#union-bound){.pf-ref},
$$
\begin{aligned}
\abs{
\bigcup_{g\in G}gHg^{-1}
}
&\leq
1+[G:H](\abs{H}-1)\\
&=
1+\abs{G}-[G:H].
\end{aligned}
$$
Since $H$ is proper,
$$
[G:H]\geq2.
$$
Therefore
$$
1+\abs{G}-[G:H]
<
\abs{G}.
$$
:::

:::

::: {.pf-step #conclusion}
Consequently,
$$
\boxed{
G\neq\bigcup_{g\in G}gHg^{-1}
}.
$$

::: pf-proof
The set on the right has strictly smaller cardinality than $G$ by step
[](#union-strictly-smaller){.pf-ref}.
:::

:::

::: pf-qed
Step [](#conclusion){.pf-ref} is the required conclusion.
:::

:::

:::
