---
schema: qual/card@1
id: P-APAS20A
kind: problem
title: Extremal dimensions of $\ker(\phi^2)$ and $\ker((\phi-\mathrm{id})^2)$ from partial matrix data
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $\phi\colon\CC^8\to\CC^8$ be a linear map whose matrix with respect to the standard basis is of the form
$$
\begin{pmatrix}
1 & * & * & * & * & * & * & * \\
0 & 1 & * & * & * & * & * & * \\
0 & 0 & 1 & * & * & * & * & * \\
0 & 0 & 0 & 1 & * & * & * & * \\
0 & 0 & 0 & 0 & 0 & * & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & * & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & * \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix},
$$
where $*$ represents an unknown value.
Suppose moreover that we are told
$$
\dim\ker\phi=2,\qquad
\dim\ker(\phi-\mathrm{id})=2,\qquad
\phi^5-2\phi^4+\phi^3=0.
$$
Determine, with proof, the maximum and minimum possible values of
$$
\dim\ker(\phi^2)\qquad\text{and}\qquad\dim\ker\bigl((\phi-\mathrm{id})^2\bigr).
$$
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Jordan-form count is completed, with the spectral decomposition, the two block constraints and the resulting dimensions as separate steps.

Let $N_{0}=\ker\phi^{4}$ and $N_{1}=\ker(\phi-\mathrm{id})^{4}$.

::: pf

::: {.pf-step #charpoly}
$\chi_{\phi}(t)=t^{4}(t-1)^{4}$, and $\CC^{8}=N_{0}\oplus N_{1}$ with $\dim N_{0}=\dim N_{1}=4$.

::: pf-proof
The matrix is upper triangular with diagonal entries $1,1,1,1,0,0,0,0$, so the characteristic polynomial is $t^{4}(t-1)^{4}$ and the two eigenvalues are $0,1$. By the primary decomposition (or the Jordan form) $\CC^{8}$ is the direct sum of the generalized eigenspaces, whose dimensions are the multiplicities, $4$ each.
:::

:::

::: {.pf-step #conditions}
$\phi^{3}(\phi-\mathrm{id})^{2}=0$; hence on $N_{0}$ the nilpotent $\phi$ satisfies $\phi^{3}=0$ and on $N_{1}$ one has $(\phi-\mathrm{id})^{2}=0$; also $\dim\ker\phi=2$ and $\dim\ker(\phi-\mathrm{id})=2$.

::: pf-proof
The hypothesis is $\phi^{5}-2\phi^{4}+\phi^{3}=\phi^{3}(\phi-1)^{2}=0$. Since $\phi$ is invertible on $N_{1}$ and $\phi-1$ is invertible on $N_{0}$ (the eigenvalues there are $1$ and $0$ respectively), the identity forces $\phi^{3}=0$ on $N_{0}$ and $(\phi-1)^{2}=0$ on $N_{1}$. Moreover $\ker\phi\subseteq N_{0}$ (a $\phi$-fixed vector is killed by $\phi^{4}$) and $\ker(\phi-1)\subseteq N_{1}$, so $\dim\ker\phi=2$ is the number of Jordan blocks of $\restrictionof{\phi}{N_{0}}$ and $\dim\ker(\phi-1)=2$ that of $\restrictionof{\phi}{N_{1}}$.
:::

:::

::: {.pf-step #zero-part}
$\dim\ker\phi^{2}=3$ or $4$; both occur.

::: pf-proof
$\restrictionof{\phi}{N_{0}}$ is nilpotent on a $4$-dimensional space with exactly $2$ Jordan blocks, each of size $\le3$ (by $\phi^{3}=0$). The block-size partitions of $4$ into exactly $2$ parts, each at most $3$, are $(3,1)$ and $(2,2)$. For a nilpotent with block sizes $s_{1},\dots,s_{r}$ one has $\dim\ker\phi^{k}=\sum_{i}\min(k,s_{i})$, so $\dim\ker\phi^{2}$ is $2+1=3$ for $(3,1)$ and $2+2=4$ for $(2,2)$; both are realised by upper triangular matrices with the given shape.
:::

:::

::: {.pf-step #one-part}
$\dim\ker(\phi-\mathrm{id})^{2}=4$; it is both the maximum and the minimum.

::: pf-proof
On $N_{1}$, $\phi-\mathrm{id}$ is nilpotent with exactly $2$ Jordan blocks (from $\dim\ker(\phi-\mathrm{id})=2$) on a $4$-dimensional space, each of size $\le2$ (by $(\phi-1)^{2}=0$). The only partition of $4$ into exactly $2$ parts, each at most $2$, is $(2,2)$, so $\dim\ker(\phi-1)^{2}=\sum_{i}\min(2,s_{i})=2+2=4$ necessarily.
:::

:::

::: {.pf-qed}
$\dim\ker(\phi^{2})$ lies in $\{3,4\}$, with maximum $4$ and minimum $3$ (step [](#zero-part){.pf-ref}); $\dim\ker\big((\phi-\mathrm{id})^{2}\big)=4$ necessarily, so its maximum and minimum coincide (step [](#one-part){.pf-ref}).
:::

:::

:::
