---
schema: qual/card@1
id: PR-DJZLY
kind: proposition
title: Isomorphism theorems for modules
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Modules
  - Homomorphisms
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a ring and $M$ an $R$-module.

(a) For an $R$-module homomorphism $\phi\colon M \to M'$, there is an isomorphism $M/\ker\phi \cong \im\phi$.

(b) For submodules $A, B \subseteq M$,
$$
\frac{A+B}{B} \cong \frac{A}{A \intersect B}.
$$

(c) For submodules $A \subseteq B \subseteq M$,
$$
\frac{M/A}{B/A} \cong \frac{M}{B}.
$$

(d) For a submodule $N \subseteq M$, there is an inclusion-preserving bijection
$$
\begin{aligned}
\correspond{\text{Submodules of } M \\ \text{containing } N}
&\mapstofrom
\correspond{\text{Submodules of } M/N} \\
A &\mapstofrom A/N.
\end{aligned}
$$
:::

::: {.remark}
The bijection in (d) preserves sums and intersections: for submodules $A, A' \subseteq M$ containing $N$, $(A+A')/N = A/N + A'/N$ and $(A \intersect A')/N = A/N \intersect A'/N$.
:::
