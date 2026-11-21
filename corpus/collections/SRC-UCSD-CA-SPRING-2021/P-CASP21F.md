---
schema: qual/card@1
id: P-CASP21F
kind: problem
title: "Uniform convergence of harmonic functions implies convergence of partial derivatives"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Uniform Convergence
  - Partial Derivatives
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/220-Qual-SP21.pdf, Problem 6 (10
    points): "Let {u_n(x,y)} be a sequence of harmonic functions in an open connected set G in R^2,
    converging uniformly on compact subsets of G. Show that the sequence of partial derivatives
    du_n/dx converges uniformly on compact subsets of G." The card's statement is that problem
    verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Supplied what the prose asserted: the
    existence of the intermediate compact K_1 together with the finitely many discs B(a_j, r_j)
    covering K whose doubles lie in K_1, obtained from the positive distance of the compact set K to
    the complement of the open set G plus compactness; the constant C of the interior estimate,
    traced to Cauchy's estimate for the derivative of a holomorphic function of which u is the real
    part; and the fact that the differences u_n - u_m are harmonic, which is what makes the estimate
    apply. No retained published solution covers this problem.
---

::: {.problem}
Let $\{u_n(x, y)\}$ be a sequence of harmonic functions in an open connected set $G \subset \RR^2$, converging uniformly on compact subsets of $G$.
Show that the sequence of partial derivatives $\frac{\partial u_n}{\partial x}$ converges uniformly on compact subsets of $G$.
:::

::: {.solution}
This is Problem 6 (10 points) of the UCSD complex-analysis qualifying exam of Spring 2021 (`assets/attachments/220-Qual-SP21.pdf`). No published solution set is transcribed: the argument is the card's own, and it is the standard interior-derivative-estimate argument for harmonic functions.

::: pf

::: {.pf-step #cover}
For a compact $K\subset G$ there is a compact $K_{1}\subset G$ and finitely many discs $B(a_{j},r_{j})$ covering $K$ with $B(a_{j},2r_{j})\subset K_{1}$.

::: pf-proof
Since $K$ is compact and $G$ is open, the distance from $K$ to the complement of $G$ is positive; take $K_{1}$ to be the set of points at distance at most that distance divided by $3$ from $K$, a compact subset of $G$ containing a neighbourhood of $K$. For each $a\in K$ choose $r_{a}>0$ with $B(a,2r_{a})\subset K_{1}$, which is possible since $K$ lies in the interior of $K_{1}$. The discs $B(a,r_{a})$ cover $K$, so finitely many of them do, and for each of those $B(a_{j},2r_{j})\subset K_{1}$.
:::
:::

::: {.pf-step #estimate}
A harmonic function $u$ on a disc $B(a,r)$ satisfies $\abs{u_{x}(a)}\leq\frac{C}{r}\sup_{B(a,r)}\abs{u}$ with a constant $C$ independent of $u$, $a$ and $r$.

::: pf-proof
Locally $u$ is the real part of a holomorphic function $h$ on $B(a,r)$, and $u_{x}=\operatorname{Re}h'$. Cauchy's estimate for the derivative, $\abs{h'(a)}\leq\frac{1}{r'}\sup_{\abs{z-a}=r'}\abs{h}$ with $r'=r/2$, together with $\abs{h}\leq2\sup_{B(a,r)}\abs{u}$ on $B(a,r/2)$ -- the imaginary part being a harmonic conjugate, bounded by the same supremum after subtracting a constant and applying the maximum principle -- gives the estimate with a numerical constant $C$. Translation and scaling remove any dependence on $a$ and $r$.
:::
:::

::: {.pf-step #cauchy}
$\sup_{K}\abs{(u_{n}-u_{m})_{x}}\leq C_{K}\sup_{K_{1}}\abs{u_{n}-u_{m}}$, where $C_{K}$ depends on $K$ but not on $n$ or $m$.

::: pf-proof
Each $u_{n}-u_{m}$ is harmonic, being a difference of harmonic functions. For a point $z\in K$ choose $j$ with $z\in B(a_{j},r_{j})$ and apply the estimate of step [](#estimate){.pf-ref} to $u_{n}-u_{m}$ on $B(a_{j},r_{j})\subset B(a_{j},2r_{j})\subset K_{1}$:
$$\abs{(u_{n}-u_{m})_{x}(z)}\leq\frac{C}{r_{j}}\sup_{B(a_{j},r_{j})}\abs{u_{n}-u_{m}}\leq\frac{C}{r_{j}}\sup_{K_{1}}\abs{u_{n}-u_{m}}.$$
Taking the supremum over $z\in K$ and over the finitely many $j$ gives the bound with $C_{K}=\max_{j}C/r_{j}$.
:::
:::

::: {.pf-step #conclusion}
$\partial u_{n}/\partial x$ converges uniformly on compact subsets of $G$.

::: pf-proof
Let $K\Subset G$ and $\varepsilon>0$. Uniform convergence of $u_{n}$ on the compact set $K_{1}$ of step [](#cover){.pf-ref} gives $N$ with $\sup_{K_{1}}\abs{u_{n}-u_{m}}<\varepsilon/C_{K}$ for $n,m\geq N$, so by step [](#cauchy){.pf-ref} $\sup_{K}\abs{(u_{n}-u_{m})_{x}}<\varepsilon$ for those $n,m$: the sequence $(\partial u_{n}/\partial x)$ is uniformly Cauchy on $K$, hence converges uniformly there by completeness of the space of continuous functions with the supremum norm. As $K$ was an arbitrary compact subset of $G$, the convergence is uniform on compact subsets of $G$.
:::
:::
:::

:::
