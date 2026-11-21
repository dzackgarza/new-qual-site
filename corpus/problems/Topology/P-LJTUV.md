---
schema: qual/card@1
id: P-LJTUV
kind: problem
title: $\pi_i(T^n)=0$ for $i\geq 2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Covering Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Two of the three steps asserted their claim with no justification; each now carries a pf-proof. The
    product of universal covers is identified as the product of the exponential maps, with $\RR^n$
    contractible through the straight-line homotopy, which is what makes $p$ the universal cover; and the
    closing step now cites both the covering and the covering-isomorphism step instead of restating the
    answer. The argument is the card's own: the card stands alone, so no collection provenance and no
    retained published solution stands behind it. The statement is unchanged.
---

::: {.problem}
Compute the higher homotopy groups $\pi_i(T^n)$ of the $n$-torus $T^n = (S^1)^n$ for all $i \ge 2$.
:::

::: {.solution}

::: pf

::: {.pf-step #torus-cover}

The product of the universal covering maps $\RR\to S^1$ gives a universal covering map
$$
p:\RR^n\longrightarrow T^n=(S^1)^n.
$$
The total space $\RR^n$ is contractible.


::: pf-proof
The map $p$ is the product of $n$ copies of the exponential map $\exp \colon \RR \to S^1$, $p(t_1, \dots, t_n) = (e^{2\pi i t_1}, \dots, e^{2\pi i t_n})$, and a product of covering maps is a covering map. Its total space $\RR^n$ is simply connected and is contractible through $(t, s) \mapsto (1-s)t$, so $p$ is the universal covering of $T^n$.
:::

:::

::: {.pf-step #covering-isomorphism}

A covering map induces an isomorphism on homotopy groups in every degree $i\ge2$.

::: pf-proof

For $i\ge2$, every based map $S^i\to T^n$ lifts uniquely after choosing the lift of the basepoint, since $S^i$ is simply connected. The same lifting statement for homotopies shows that this correspondence induces a bijection on based homotopy classes, hence an isomorphism on $\pi_i$.

:::

:::

::: pf-step

Therefore, for every $i\ge2$,
$$
\boxed{\pi_i(T^n)\cong\pi_i(\RR^n)=0.}
$$


::: pf-proof
By step [](#torus-cover){.pf-ref} the map $p \colon \RR^n \to T^n$ is a covering map and $\RR^n$ is contractible, so $\pi_i(\RR^n) = 0$ for every $i \ge 1$; by step [](#covering-isomorphism){.pf-ref} a covering map induces an isomorphism on $\pi_i$ for $i \ge 2$. Composing the two gives $\pi_i(T^n) \cong \pi_i(\RR^n) = 0$ for all $i \ge 2$.
:::

:::

:::

:::
