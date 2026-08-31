---
schema: qual/card@1
id: E-HAT-3.3-6
kind: exercise
title: "Connected sums of manifolds"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Given two disjoint connected $n$-manifolds $M_1$ and $M_2$, a connected $n$-manifold $M_1 \sharp M_2$, their connected sum, can be constructed by deleting the interiors of closed $n$-balls $B_1 \subset M_1$ and $B_2 \subset M_2$ and identifying the resulting boundary spheres $\partial B_1$ and $\partial B_2$ via some homeomorphism between them.
(Assume that each $B_i$ embeds nicely in a larger ball in $M_i$.)

(a) Show that if $M_1$ and $M_2$ are closed then there are isomorphisms $H_i(M_1 \sharp M_2; \mathbb{Z}) \approx H_i(M_1; \mathbb{Z}) \oplus H_i(M_2; \mathbb{Z})$ for $0 < i < n$, with one exception: If both $M_1$ and $M_2$ are nonorientable, then $H_{n-1}(M_1 \sharp M_2; \mathbb{Z})$ is obtained from $H_{n-1}(M_1; \mathbb{Z}) \oplus H_{n-1}(M_2; \mathbb{Z})$ by replacing one of the two $\mathbb{Z}_2$ summands by a $\mathbb{Z}$ summand.

(b) Show that $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$ if $M_1$ and $M_2$ are closed.

::: {.solution}
**Goal.** (a) Compute $H_i(M_1 \sharp M_2)$ for $0 < i < n$. (b) Prove the Euler characteristic formula.

<1>1. (a) $H_i(M_1 \sharp M_2) \cong H_i(M_1) \oplus H_i(M_2)$ for $0 < i < n$ (with one exception).
<2>1. $M_1 \sharp M_2 = (M_1 \sm \operatorname{int} B_1) \cup (M_2 \sm \operatorname{int} B_2)$ glued along $S^{n-1}$.
::: {.proof}
definition of connected sum.
:::
<2>2. Apply Mayer–Vietoris to the two punctured manifolds with intersection $S^{n-1}$.
::: {.proof}
the two pieces are $M_1 \sm \operatorname{int} B_1$ and $M_2 \sm \operatorname{int} B_2$, intersecting in $S^{n-1}$.
:::
<2>3. For $0 < i < n-1$: $H_i(M_j \sm \operatorname{int} B_j) \cong H_i(M_j)$ and $H_i(S^{n-1}) = 0$, so $H_i(M_1 \sharp M_2) \cong H_i(M_1) \oplus H_i(M_2)$.
::: {.proof}
removing a ball does not change $H_i$ for $i < n-1$, and $H_i(S^{n-1}) = 0$ for $0 < i < n-1$.
:::
<2>4. For $i = n-1$: the Mayer–Vietoris sequence gives $0 \to H_{n-1}(S^{n-1}) \to H_{n-1}(M_1 \sm B_1) \oplus H_{n-1}(M_2 \sm B_2) \to H_{n-1}(M_1 \sharp M_2) \to 0$.
::: {.proof}
the relevant part of the Mayer–Vietoris sequence (with $H_{n-2}(S^{n-1}) = 0$ for $n > 2$).
:::
<2>5. $H_{n-1}(M_j \sm \operatorname{int} B_j) \cong H_{n-1}(M_j)$.
::: {.proof}
removing a ball does not change $H_{n-1}$.
:::
<2>6. Hence $H_{n-1}(M_1 \sharp M_2) \cong \qty(H_{n-1}(M_1) \oplus H_{n-1}(M_2)) / \im(\ZZ \to \cdots)$.
::: {.proof}
the map $H_{n-1}(S^{n-1}) = \ZZ \to H_{n-1}(M_1) \oplus H_{n-1}(M_2)$ sends the generator to the boundary sphere class in each summand.
:::
<2>7. If at least one of $M_1, M_2$ is orientable, the boundary sphere class is $0$ in that summand, so the quotient is the direct sum $H_{n-1}(M_1) \oplus H_{n-1}(M_2)$.
::: {.proof}
in an orientable manifold, the boundary sphere of a ball is null-homologous.
:::
<2>8. If both are nonorientable, the boundary sphere class is the $\ZZ_2$ generator in each $H_{n-1}(M_j)$, so the quotient replaces one $\ZZ_2$ summand by $\ZZ$.
::: {.proof}
the map $\ZZ \to \ZZ_2 \oplus \ZZ_2$ sends $1 \mapsto (1, 1)$, and the quotient $(\ZZ_2 \oplus \ZZ_2)/\langle(1,1)\rangle \cong \ZZ_2 \oplus \ZZ$ (one $\ZZ_2$ survives, and the diagonal gives a $\ZZ$).
:::

<1>2. (b) $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - \chi(S^n)$.
<2>1. $\chi(M_1 \sharp M_2) = \chi(M_1 \sm \operatorname{int} B_1) + \chi(M_2 \sm \operatorname{int} B_2) - \chi(S^{n-1})$.
::: {.proof}
additivity of Euler characteristic for a union along a common subspace (inclusion-exclusion).
:::
<2>2. $\chi(M_j \sm \operatorname{int} B_j) = \chi(M_j) - \chi(\operatorname{int} B_j) = \chi(M_j) - (-1)^n$.
::: {.proof}
removing the interior of an $n$-ball removes a cell of dimension $n$, contributing $(-1)^n$ to $\chi$.
:::
<2>3. $\chi(S^{n-1}) = 1 + (-1)^{n-1}$.
::: {.proof}
$S^{n-1}$ has one cell in dimensions $0$ and $n-1$.
:::
<2>4. Hence $\chi(M_1 \sharp M_2) = \chi(M_1) + \chi(M_2) - 2(-1)^n - (1 + (-1)^{n-1})$.
::: {.proof}
substitute <1>2.2 and <1>2.3 into <1>2.1.
:::
<2>5. $= \chi(M_1) + \chi(M_2) - (1 + (-1)^n) = \chi(M_1) + \chi(M_2) - \chi(S^n)$.
::: {.proof}
$\chi(S^n) = 1 + (-1)^n$, and $-2(-1)^n - (1 + (-1)^{n-1}) = -2(-1)^n - 1 + (-1)^n = -1 - (-1)^n = -(1 + (-1)^n)$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves (a); <1>2 proves (b).
:::
:::
