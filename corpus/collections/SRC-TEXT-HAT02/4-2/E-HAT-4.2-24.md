---
schema: qual/card@1
id: E-HAT-4.2-24
kind: exercise
title: "Moore spaces $M(G,1)$ and $H_2(K(G,1))$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Show there is a Moore space $M(G, 1)$ with $\pi_1\bigl(M(G, 1)\bigr) \approx G$ iff $H_2(K(G, 1); \mathbb{Z}) = 0$.
In particular, there is no $M(\mathbb{Z}^n, 1)$ with fundamental group $\mathbb{Z}^n$, free abelian of rank $n$, if $n \geq 2$.

::: {.solution}
<1>1. A Moore space $M(G, 1)$ is a connected CW complex with $\pi_1 \cong G$ and $\widetilde{H}_i = 0$ for $i \neq 1$.
::: {.proof}
definition of a Moore space of type $(G, 1)$.
:::

<1>2. If $M(G,1)$ exists, then $H_2(K(G,1);\ZZ) = 0$.
<2>1. $M(G,1)$ is a $K(G,1)$.
::: {.proof}
$\pi_1 \cong G$ and $\pi_i = 0$ for $i \ge 2$ (since $\widetilde{H}_i = 0$ for $i \ge 2$ and $\pi_1$ acts trivially, Hurewicz gives $\pi_i = 0$).
:::
<2>2. $H_2(K(G,1);\ZZ) = H_2(M(G,1);\ZZ) = 0$.
::: {.proof}
<2>1 and the Moore-space condition $\widetilde{H}_2 = 0$.
:::

<1>3. Conversely, if $H_2(K(G,1);\ZZ) = 0$, then $M(G,1)$ exists.
<2>1. Attach $3$-cells to $K(G,1)$ to kill $\pi_2$, then $4$-cells to kill $\pi_3$, and so on.
::: {.proof}
standard construction of a Moore space from a $K(G,1)$ by killing higher homotopy groups.
:::
<2>2. This does not change $H_2$ (attaching cells of dimension $\ge 3$ only affects homology in degrees $\ge 2$ via the boundary maps, and $H_2$ remains $0$ since it was already $0$).
::: {.proof}
attaching a $3$-cell can only kill $H_2$ or create $H_3$; since $H_2 = 0$ already, it stays $0$.
:::
<2>3. The result is a $K(G,1)$-based complex with $\pi_1 = G$ and $\widetilde{H}_i = 0$ for $i \neq 1$, i.e. a Moore space $M(G,1)$.
::: {.proof}
<2>1 and <2>2.
:::

<1>4. For $G = \ZZ^n$ with $n \ge 2$, $H_2(K(\ZZ^n,1);\ZZ) = H_2(T^n;\ZZ) = \ZZ^{\binom{n}{2}} \neq 0$.
::: {.proof}
$K(\ZZ^n,1) = T^n$ (the $n$-torus), and $H_2(T^n) \cong \bigwedge^2 \ZZ^n \cong \ZZ^{\binom{n}{2}}$.
:::

<1>5. Hence there is no $M(\ZZ^n, 1)$ for $n \ge 2$.
::: {.proof}
<1>2 (contrapositive) and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>2, <1>3, and <1>5.
:::
:::
