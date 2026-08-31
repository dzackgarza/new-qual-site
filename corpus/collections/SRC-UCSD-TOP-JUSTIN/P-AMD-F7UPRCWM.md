---
schema: qual/card@1
id: P-AMD-F7UPRCWM
kind: problem
title: $S^2$ is not homeomorphic to $S^3$
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that $S^2 \not\cong S^3$.
:::

::: {.solution}
**Goal:** Prove that the 2-sphere $S^2$ is not homeomorphic to the 3-sphere $S^3$ ($S^2 \not\cong S^3$).

<1>1. Compute the homology groups of $S^2$ and $S^3$.
<2>1. For the 2-sphere $S^2$, the singular homology groups are:

- $H_0(S^2; \mathbb{Z}) \cong \mathbb{Z}$,

- $H_2(S^2; \mathbb{Z}) \cong \mathbb{Z}$,

- $H_k(S^2; \mathbb{Z}) = 0$ for all $k \neq 0, 2$ (in particular, $H_3(S^2; \mathbb{Z}) = 0$). <2>2. For the 3-sphere $S^3$, the singular homology groups are:

- $H_0(S^3; \mathbb{Z}) \cong \mathbb{Z}$,

- $H_3(S^3; \mathbb{Z}) \cong \mathbb{Z}$,

- $H_k(S^3; \mathbb{Z}) = 0$ for all $k \neq 0, 3$ (in particular, $H_2(S^3; \mathbb{Z}) = 0$).
::: {.proof}
<2>3. The sphere $S^n$ has a CW structure with one 0-cell and one $n$-cell, so its cellular chain complex has $H_0 \cong \mathbb{Z}$, $H_n \cong \mathbb{Z}$, and all other homology groups zero.
:::

<1>2. Apply topological invariance of homology.
<2>1. If two topological spaces $X$ and $Y$ are homeomorphic ($X \cong Y$), then their homology groups are isomorphic in every dimension: $H_k(X; \mathbb{Z}) \cong H_k(Y; \mathbb{Z})$ for all $k \ge 0$.
<2>2. Comparing at dimension $k = 2$: $$H_2(S^2; \mathbb{Z}) \cong \mathbb{Z} \not\cong 0 \cong H_2(S^3; \mathbb{Z}).$$ <2>3. Comparing at dimension $k = 3$: $$H_3(S^2; \mathbb{Z}) \cong 0 \not\cong \mathbb{Z} \cong H_3(S^3; \mathbb{Z}).$$ <2>4. Therefore, $S^2$ cannot be homeomorphic to $S^3$.
::: {.proof}
<2>5. A homeomorphism would induce isomorphisms on all homology groups, but $H_2(S^2) \cong \mathbb{Z} \not\cong 0 \cong H_2(S^3)$; this contradiction shows $S^2 \not\cong S^3$.
:::

<1>3. Alternative proof via point deletion and local homology / dimension invariance.
<2>1. For any point $p \in S^n$, $H_k(S^n, S^n \setminus \{p\}) \cong \widetilde{H}_{k-1}(S^{n-1}) \cong \begin{cases} \mathbb{Z} & k = n, \\ 0 & k \neq n. \end{cases}$ <2>2. A homeomorphism $S^2 \cong S^3$ would induce an isomorphism on local homology groups $H_2(S^2, S^2 \setminus \{p\}) \cong H_2(S^3, S^3 \setminus \{f(p)\})$, meaning $\mathbb{Z} \cong 0$, a contradiction.
::: {.proof}
<2>3. Excision identifies $H_k(S^n, S^n \setminus \{p\})$ with $H_k(D^n, \partial D^n)$, and the long exact sequence of the pair gives $\widetilde{H}_{k-1}(S^{n-1})$; this is $\mathbb{Z}$ only when $k = n$, so a homeomorphism $S^2 \cong S^3$ would force $\mathbb{Z} \cong 0$.
:::

<1>4. Q.E.D.
::: {.proof}
<2>1. Both <1>2 and <1>3 show $S^2 \not\cong S^3$.
:::
:::
