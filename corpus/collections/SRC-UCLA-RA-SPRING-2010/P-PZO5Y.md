---
schema: qual/card@1
id: P-PZO5Y
kind: problem
title: Newtonian and Cauchy potentials of a compactly supported measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\mu$ be a finite, positive, regular Borel measure supported on a compact subset of $\mathbb{C}$ and define the Newtonian potential $$U_\mu(z) = \int_\mathbb{C} \left|\frac{1}{z-w}\right| d\mu(w).$$

a. Prove that $U_\mu$ exists at Lebesgue almost all $z\in\mathbb{C}$ and that $$\iint_K U_\mu(z)\,dx\,dy < \infty$$ for every compact $K\subseteq\mathbb{C}$.

b. Prove that for almost every horizontal or vertical line $L\subseteq\mathbb{C}$, $\mu(L)=0$ and $\int_K U_\mu(z)\,ds < \infty$ for every compact subset $K\subseteq L$, where $ds$ denotes Lebesgue linear measure on $L$.

c. Define the Cauchy potential of $\mu$ to be $$S_\mu(z) = \int_\mathbb{C} \frac{1}{z-w}\,d\mu(w).$$ Let $R$ be a rectangle in $\mathbb{C}$ whose four sides are contained in lines $L$ having the conclusions of (b). Prove that $$\frac{1}{2\pi i}\int_{\partial R} S_\mu(z)\,dz = \mu(R).$$
:::

:::: {.solution}
<1>1. (a) $U_\mu(z) < \infty$ for Lebesgue-a.e. $z$, and $\iint_K U_\mu < \infty$ for every compact $K$.
Proof: fix a compact $K \subseteq \mathbb{C}$.
Since $\mu$ is supported on a compact set, $\mathrm{supp}\,\mu$ is bounded, say contained in a disk $B(0,R)$; likewise $K \subseteq B(0,R)$.
By Tonelli, \[\iint_K U_\mu(z)\,dx\,dy = \int_{\mathbb{C}}\left(\iint_K \frac{dx\,dy}{|z-w|}\right)d\mu(w).\] For $w \in \mathrm{supp}\,\mu$, the inner integral is uniformly bounded: $\iint_K \frac{dx\,dy}{|z-w|} \le \iint_{|z-w|\le 2R}\frac{dx\,dy}{|z-w|} = 2\pi\cdot 2R < \infty$.
Hence $\iint_K U_\mu \le 4\pi R\,\mu(\mathbb{C}) < \infty$, so $U_\mu < \infty$ a.e. on $K$.
Exhausting $\mathbb{C}$ by compact $K_m \nearrow \mathbb{C}$ gives $U_\mu < \infty$ a.e. on $\mathbb{C}$.
<1>2. (b) For a.e. horizontal line $L$, $\mu(L) = 0$; and $\int_{K\cap L}U_\mu\,ds < \infty$ for every compact $K$.
Proof: first, $\mu(L) = 0$ for all but countably many horizontal lines: for each $n$, at most $n\,\mu(\mathbb{C})$ horizontal lines can carry mass $> 1/n$ (disjoint lines and finite additivity), so the union over $n$ of the lines with positive mass is countable.
Second, from <1>1, $\iint_K U_\mu < \infty$; by Fubini (integrating over the $y$-coordinate of the line), \[\iint_K U_\mu\,dx\,dy = \int_{\mathbb{R}}\left(\int_{K\cap L_y} U_\mu\,ds\right)dy < \infty,\] so the inner integral is finite for a.e. horizontal line $L_y$.
Intersecting the two full-measure sets of lines gives the claim.
The argument for vertical lines is identical.
<1>3. (c) $\frac{1}{2\pi i}\int_{\partial R}S_\mu(z)\,dz = \mu(R)$.
Proof: the sides of $R$ lie in lines with the conclusions of (b), so $\mu(\partial R) = 0$ and, since $|S_\mu| \le U_\mu$, $\int_{\partial R}|S_\mu|\,ds < \infty$ (each side is compact).
Fubini therefore applies: \[\int_{\partial R}S_\mu(z)\,dz = \int_{\mathbb{C}}\left(\int_{\partial R}\frac{dz}{z-w}\right)d\mu(w) = \int_{\mathbb{C}} 2\pi i\,\mathbf 1_{w \in R^\circ}\,d\mu(w) = 2\pi i\,\mu(R^\circ),\] where the middle equality is Cauchy's integral formula (the winding number of $\partial R$ about $w$ is $1$ for $w \in R^\circ$, $0$ for $w \notin R$). Since $\mu(\partial R) = 0$, $\mu(R^\circ) = \mu(R)$, and dividing by $2\pi i$ gives the claim.
<1>4. Q.E.D.
:::
