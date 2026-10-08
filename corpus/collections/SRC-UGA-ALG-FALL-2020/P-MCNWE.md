---
schema: qual/card@1
id: P-MCNWE
kind: problem
title: Galois extensions, $\Gal(x^3-7/\QQ)$, and subfields of the splitting field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
a. Define what it means for a finite extension of fields $E$ over $F$ to be a *Galois* extension.

b. Determine the Galois group of $f(x) = x^3 - 7$ over $\QQ$, and justify your answer carefully.

c. Find all subfields of the splitting field of $f(x)$ over $\QQ$.
:::

::: {.solution}
<1>1. A finite extension is Galois if and only if it is normal and separable.

::: {.proof}
This is the definition. Equivalently, it is the splitting field of a separable polynomial over the base field.
:::

Put $\alpha=\sqrt[3]{7}$, and let $\zeta$ be a primitive cube root of unity.

<1>2. The splitting field and its Galois group are
\[
\boxed{L=\mathbb Q(\alpha,\zeta),\qquad
\operatorname{Gal}(L/\mathbb Q)\cong S_3}.
\]

::: {.proof}
The roots of $x^3-7$ are $\alpha,\zeta\alpha,\zeta^2\alpha$, so $L$ is its splitting field. Eisenstein's criterion at $7$ gives $[\mathbb Q(\alpha):\mathbb Q]=3$. Since $\mathbb Q(\alpha)$ is real and $\zeta$ is not, $[L:\mathbb Q(\alpha)]=2$, hence $[L:\mathbb Q]=6$. In characteristic zero the splitting field is Galois. Its Galois group permutes the three distinct roots faithfully, embedding in $S_3$. Because both groups have order six, this embedding is an isomorphism.

Explicit automorphisms are
\[
\sigma(\alpha)=\zeta\alpha,\quad \sigma(\zeta)=\zeta,
\qquad
\tau(\alpha)=\alpha,\quad\tau(\zeta)=\zeta^2.
\]
They correspond respectively to $(123)$ and $(23)$ on the ordered roots $(\alpha,\zeta\alpha,\zeta^2\alpha)$, so they generate the Galois group with $\sigma^3=\tau^2=1$ and $\tau\sigma\tau=\sigma^{-1}$.
:::

<1>3. The complete list of intermediate fields between $\mathbb Q$ and $L$ is
\[
\boxed{\mathbb Q,\quad \mathbb Q(\zeta),\quad
\mathbb Q(\alpha),\quad \mathbb Q(\zeta\alpha),\quad
\mathbb Q(\zeta^2\alpha),\quad L}.
\]

::: {.proof}
The six subgroups of $S_3$ are the trivial subgroup, $S_3$, the unique subgroup $\langle\sigma\rangle$ of order three, and the three subgroups $\langle\tau\rangle$, $\langle\sigma\tau\rangle$, and $\langle\sigma^2\tau\rangle$ of order two. By the Galois correspondence, their fixed fields have degrees six, one, two, and three, respectively. The subgroup $\langle\sigma\rangle$ fixes $\zeta$, hence fixes the quadratic field $\mathbb Q(\zeta)$, which must be its full fixed field. The subgroup $\langle\tau\rangle$ fixes $\alpha$, $\langle\sigma\tau\rangle$ fixes $\zeta^2\alpha$, and $\langle\sigma^2\tau\rangle$ fixes $\zeta\alpha$, as follows directly from the displayed actions in step <1>2. Each corresponding cubic field has degree three because its generator is a root of the irreducible polynomial $x^3-7$. Together with $L$ and $\mathbb Q$, these exhaust the intermediate fields.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 establish parts (a), (b), and (c), respectively.
:::

:::

