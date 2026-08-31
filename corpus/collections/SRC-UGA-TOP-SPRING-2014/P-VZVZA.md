---
schema: qual/card@1
id: P-VZVZA
kind: problem
title: Surfaces covered by a closed surface of genus $2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Find *all* surfaces, orientable and non-orientable, which can be covered by a closed surface (i.e. compact with empty boundary) of genus 2. Prove that your answer is correct.
:::

::: {.solution}
**Goal.** Classify all closed surfaces covered by the closed orientable surface $\Sigma_2$ of genus $2$.

<1>1. A surface covered by $\Sigma_2$ is closed.
::: {.proof}
a covering map is a local homeomorphism; the image of a compact space is compact, and boundary is a local property preserved by covering, so the covered surface has empty boundary.
:::

<1>2. If $p: \Sigma_2 \to S$ is a covering of degree $d$, then $\chi(\Sigma_2) = d \cdot \chi(S)$.
::: {.proof}
the Euler characteristic is multiplicative under finite coverings (lift a triangulation of $S$).
:::

<1>3. $\chi(\Sigma_2) = -2$.
::: {.proof}
$\chi(\Sigma_g) = 2 - 2g = 2 - 4 = -2$.
:::

<1>4. Hence $d \cdot \chi(S) = -2$, so $d \in \theset{1, 2}$ and $\chi(S) \in \theset{-2, -1}$.
::: {.proof}
$d$ is a positive integer dividing $-2$, so $d = 1$ or $d = 2$; thus $\chi(S) = -2$ or $-1$.
:::

<1>5. Closed surfaces with $\chi = -2$ or $-1$.
<2>1. Orientable: $\chi(\Sigma_g) = 2 - 2g$ is even, so $\chi = -1$ is impossible; $\chi = -2$ gives $g = 2$, i.e. $\Sigma_2$.
::: {.proof}
$2 - 2g = -2$ forces $g = 2$.
:::
<2>2. Non-orientable: $\chi(N_k) = 2 - k$, so $\chi = -2$ gives $k = 4$ (i.e. $N_4$), and $\chi = -1$ gives $k = 3$ (i.e. $N_3$).
::: {.proof}
$2 - k = -2$ forces $k = 4$; $2 - k = -1$ forces $k = 3$.
:::

<1>6. Eliminate $N_4$: it is not covered by $\Sigma_2$.
<2>1. A covering $\Sigma_2 \to N_4$ would have degree $d$ with $-2 = d \cdot \chi(N_4) = d \cdot (-2)$, so $d = 1$.
::: {.proof}
by <1>2 and $\chi(N_4) = -2$.
:::
<2>2. A degree-$1$ covering is a homeomorphism, but $\Sigma_2$ is orientable and $N_4$ is not.
::: {.proof}
orientability is a homeomorphism invariant, contradiction.
:::

<1>7. The remaining candidates are covered by $\Sigma_2$.
<2>1. $\Sigma_2$ covers itself (degree $1$).
::: {.proof}
the identity map.
:::
<2>2. $N_3$ is covered by $\Sigma_2$ (degree $2$).
::: {.proof}
the orientable double cover of $N_k$ is $\Sigma_{k-1}$, so the orientable double cover of $N_3$ is $\Sigma_2$.
:::

<1>8. Q.E.D.
::: {.proof}
the surfaces covered by $\Sigma_2$ are exactly $\Sigma_2$ and $N_3$.
:::
:::
