---
schema: qual/card@1
id: P-S7WVQ
kind: problem
title: $S^2\times\RP^4$ is not homotopy equivalent to $S^4\times\RP^2$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homotopy
  - Product Topology
relations: []
review: draft
---

::: {.problem}
Show that $S^2 \cross \RP^4 \not\homotopic S^4 \cross \RP^2$.
:::

::: {.solution}
Let $X_1 = S^2 \times \RP^4$ and $X_2 = S^4 \times \RP^2$, and take cohomology with coefficients in $\FF_2$.

::: pf

::: {.pf-step #rings}
There are graded ring isomorphisms
$$
\begin{aligned}
H^*(X_1; \FF_2) &\cong \FF_2[x]/(x^2) \otimes_{\FF_2} \FF_2[y]/(y^5), & \deg x &= 2,\ \deg y = 1,\\
H^*(X_2; \FF_2) &\cong \FF_2[w]/(w^2) \otimes_{\FF_2} \FF_2[z]/(z^3), & \deg w &= 4,\ \deg z = 1.
\end{aligned}
$$

::: pf-proof
We have $H^*(S^n; \FF_2) \cong \FF_2[x]/(x^2)$ with $\deg x = n$ and $H^*(\RP^n; \FF_2) \cong \FF_2[y]/(y^{n+1})$ with $\deg y = 1$.
Over a field the Künneth formula is a ring isomorphism $H^*(A \times B) \cong H^*(A) \otimes H^*(B)$ for finite CW complexes $A, B$.
:::

:::

::: pf-step
$X_1 \not\simeq X_2$.

::: pf-proof
By step [](#rings){.pf-ref}, $H^1(X_1; \FF_2) = \FF_2 \cdot y$ and $H^1(X_2; \FF_2) = \FF_2 \cdot z$.
A homotopy equivalence $X_1 \to X_2$ would induce a graded ring isomorphism $\varphi\colon H^*(X_2; \FF_2) \to H^*(X_1; \FF_2)$ with $\varphi(z) = y$, the only nonzero element of $H^1(X_1;\FF_2)$.
Then $y^3 = \varphi(z)^3 = \varphi(z^3) = 0$, but $y^3 \neq 0$ in $H^3(X_1; \FF_2)$ by step [](#rings){.pf-ref}.
:::

:::

:::

:::
