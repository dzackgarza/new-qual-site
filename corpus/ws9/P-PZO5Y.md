---
schema: qual/card@1
id: P-PZO5Y
kind: problem
title: Let $\mu$ be a finite, positive, regular Borel measure supported on a…
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
  - fubini-tonelli
relations: []
review: draft
---

:::{.problem title="?"}
Let $\mu$ be a finite, positive, regular Borel measure supported on a compact subset of $\mathbb{C}$ and define the Newtonian potential
$$U_\mu(z) = \int_\mathbb{C} \left|\frac{1}{z-w}\right| d\mu(w).$$

a. Prove that $U_\mu$ exists at Lebesgue almost all $z\in\mathbb{C}$ and that
$$\iint_K U_\mu(z)\,dx\,dy < \infty$$
for every compact $K\subseteq\mathbb{C}$.

b. Prove that for almost every horizontal or vertical line $L\subseteq\mathbb{C}$, $\mu(L)=0$ and $\int_K U_\mu(z)\,ds < \infty$ for every compact subset $K\subseteq L$, where $ds$ denotes Lebesgue linear measure on $L$.

c. Define the Cauchy potential of $\mu$ to be
$$S_\mu(z) = \int_\mathbb{C} \frac{1}{z-w}\,d\mu(w).$$
Let $R$ be a rectangle in $\mathbb{C}$ whose four sides are contained in lines $L$ having the conclusions of (b). Prove that
$$\frac{1}{2\pi i}\int_{\partial R} S_\mu(z)\,dz = \mu(R).$$
:::
