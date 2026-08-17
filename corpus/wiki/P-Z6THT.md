---
schema: qual/card@1
id: P-Z6THT
kind: problem
title: Homotopy groups of the total space of $S^3\to E\to S^5$
classification:
  areas:
  - topology
  topics:
  - homotopy
  - homology
relations: []
review: draft
solved: false
---

::: problem
Facts used:

- Homotopy LES

- Hurewicz

- $0\to A\to B \to 0$ exact iff $A\cong B$

From the LES in homotopy we have
$$
\begin{align}
4\qquad \pi_4(S^3) \to \pi_4(E) \to \pi_4(S^5) \\
3\qquad \pi_3(S^3) \to \pi_3(E) \to \pi_3(S^5) \\
2\qquad \pi_2(S^3) \to \pi_2(E) \to \pi_2(S^5) \\
1\qquad \pi_1(S^3) \to \pi_1(E) \to \pi_1(S^5) \\
0\qquad \pi_0(S^3) \to \pi_0(E) \to \pi_0(S^5) \\
\end{align}
$$

and plugging in known information yields
$$
\begin{align}
4\qquad &\pi_4(S^3) \to &\pi_4(E) \quad \to 0 \\
3\qquad &\ZZ \to &\pi_3(E) \quad\to 0 \\
2\qquad &0 \to &\pi_2(E) \quad\to 0 \\
1\qquad &0 \to &\pi_1(E) \quad\to 0 \\
0\qquad &\ZZ \to &\pi_0(E) \quad\to \ZZ \\
\end{align}
$$

where rows 3 and 4 force $\pi_3(E) \cong \ZZ$, rows 0 and 1 force $\pi_0(E) = \ZZ$, and the remaining rows force $\pi_1(E) = \pi_2(E) = 0$.

By Hurewicz, we thus have $H_3(E) = \pi_3(E) = \ZZ$.
$\qed$
:::
