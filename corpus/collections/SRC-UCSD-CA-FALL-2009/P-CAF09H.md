---
schema: qual/card@1
id: P-CAF09H
kind: problem
title: "Interpolation by entire functions with prescribed values and multiplicities"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked the algebra: the
    genus-one Weierstrass product with simple zeros at the alpha_j, the expansions of P
    and P^2 at a zero, the choice A_j = beta_j/p_1j^2 and B_j = -2p_2j beta_j/p_1j^3
    killing both the constant and the linear term of P^2 h, removable singularity with
    f(alpha_j) = beta_j and f'(alpha_j) = 0, and the bonus coefficient
    c_j + p_1j^2 g(alpha_j). The bonus's interpolation of an arbitrary entire g is now
    proved (Mittag-Leffler for the simple poles with residues w_j/P'(alpha_j), then
    multiply by P) rather than asserted. The collection's provenance is the examination
    paper only, so no retained solution set covers the exercise and the argument is the
    card's own.
---

::: {.problem}
We are given two sequences of complex numbers, $\{\alpha_j\}_{j \geq 1}$ and $\{\beta_j\}_{j \geq 1}$, where the $\alpha_j$ are all distinct and $\abs{\alpha_j} \to \infty$ as $j \to \infty$.
Use a combination of the Mittag-Leffler Theorem and the Weierstrass Product Theorem, or any other method, to show that there exists an entire function $f(z)$ such that for each $j$, $f(z)$ takes the value $\beta_j$ at $\alpha_j$ with multiplicity at least 2.

(Bonus: show that $f(z)$ can be chosen so that for all $j$, $f(z)$ takes the value $\beta_j$ at $z = \alpha_j$ with multiplicity exactly 2.)
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #product}
There is an entire function $P$ whose zeros are exactly the points $\alpha_j$, each of them simple.

::: pf-proof
The hypothesis $\abs{\alpha_j}\to\infty$ makes $\{\alpha_j\}$ a closed discrete subset of $\CC$. For a genus-one Weierstrass product take the elementary factors $E_1(u)=(1-u)e^{u}$ and set $P(z)\coloneqq\prod_jE_1(z/\alpha_j)$; the product converges locally uniformly because $\sum_j\abs{\alpha_j}^{-2}<\infty$ for a discrete set whose points tend to infinity, and each factor $E_1(z/\alpha_j)$ vanishes exactly at $z=\alpha_j$ and has there the simple zero of $1-z/\alpha_j$. Hence $P$ is entire with precisely the simple zeros $\alpha_j$.
:::

:::

::: {.pf-step #expansion}
Near $\alpha_j$, with $t\coloneqq z-\alpha_j$,
$$
P(z)=p_{1,j}t+p_{2,j}t^2+O(t^3),\qquad p_{1,j}=P'(\alpha_j)\ne0,
\qquad\text{and}\qquad
P(z)^2=p_{1,j}^2t^2+2p_{1,j}p_{2,j}t^3+O(t^4).
$$

::: pf-proof
$P$ is analytic at $\alpha_j$, so its Taylor expansion there reads $P(z)=P(\alpha_j)+P'(\alpha_j)t+\frac{P''(\alpha_j)}{2}t^2+O(t^3)$ with $P(\alpha_j)=0$; put $p_{1,j}\coloneqq P'(\alpha_j)$ and $p_{2,j}\coloneqq P''(\alpha_j)/2$. The zero is simple, so $p_{1,j}\ne0$. Squaring the expansion gives the displayed expansion of $P^2$.
:::

:::

::: {.pf-step #principal-parts}
For $A_j\coloneqq\frac{\beta_j}{p_{1,j}^2}$ and $B_j\coloneqq-\frac{2p_{2,j}\beta_j}{p_{1,j}^3}$ the function $h$ with principal part $\frac{A_j}{t^2}+\frac{B_j}{t}$ at $\alpha_j$ satisfies
$$
P(z)^2h(z)=\beta_j+O(t^2)\qquad(t=z-\alpha_j).
$$

::: pf-proof
Write the principal part as $h(z)=\frac{A_j}{t^2}+\frac{B_j}{t}+O(1)$, which is what a pole of order at most $2$ means. Multiplying by the expansion of step [](#expansion){.pf-ref},
$$
P^2h=\left(p_{1,j}^2t^2+2p_{1,j}p_{2,j}t^3+O(t^4)\right)\left(\frac{A_j}{t^2}+\frac{B_j}{t}+O(1)\right)
=p_{1,j}^2A_j+\left(p_{1,j}^2B_j+2p_{1,j}p_{2,j}A_j\right)t+O(t^2),
$$
and $p_{1,j}^2A_j=\beta_j$ while $p_{1,j}^2B_j+2p_{1,j}p_{2,j}A_j=-2p_{2,j}\beta_j+2p_{2,j}\beta_j=0$ by the choice of $A_j$ and $B_j$.
:::

:::

::: {.pf-step #mittag-leffler}
There is a meromorphic $h$ on $\CC$ whose only poles are the points $\alpha_j$, with the principal part $\frac{A_j}{t^2}+\frac{B_j}{t}$ at $\alpha_j$.

::: pf-proof
The set $\{\alpha_j\}$ is closed and discrete, and the prescribed principal parts are finite sums of terms $\frac{c}{(z-\alpha)^k}$ with $1\le k\le2$. Mittag--Leffler's theorem produces a meromorphic function with exactly these principal parts, the sum being made locally uniformly convergent by subtracting from each term its Taylor polynomial of sufficiently high order at $0$.
:::

:::

::: {.pf-step #entire}
$f\coloneqq P^2h$ extends to an entire function satisfying $f(\alpha_j)=\beta_j$ and $f'(\alpha_j)=0$ for every $j$.

::: pf-proof
Away from the points $\alpha_j$ the function $h$ is analytic, so $f$ is analytic there. At $\alpha_j$ step [](#principal-parts){.pf-ref} shows that $f(z)-\beta_j=O(t^2)$ with $t=z-\alpha_j$, so the singularity of $P^2h$ at $\alpha_j$ is removable, the extended value is $\beta_j$, and the derivative there vanishes. Hence $f-\beta_j$ has a zero of multiplicity at least $2$ at $\alpha_j$.
:::

:::

::: {.pf-step}
(Bonus) Such an $f$ can be chosen so that $f-\beta_j$ has a zero of multiplicity exactly $2$ at every $\alpha_j$.

::: pf-proof

::: {.pf-step #preserved}
For every entire $g$ the function $f\coloneqq f_0+P^2g$ is entire and satisfies $f(\alpha_j)=\beta_j$ and $f'(\alpha_j)=0$ for all $j$.

::: pf-proof
$P^2g$ is entire. Since $P$ has a zero of order $2$ at each $\alpha_j$, the summand $P^2g$ vanishes to order at least $2$ at $\alpha_j$, so it changes neither the value nor the first derivative of $f_0$ at $\alpha_j$.
:::

:::

::: {.pf-step #quadratic-coefficient}
At $\alpha_j$, the coefficient of $t^2$ in $f(z)-\beta_j$ equals $c_j+p_{1,j}^2g(\alpha_j)$, where $c_j$ is the coefficient of $t^2$ in $f_0(z)-\beta_j$; it vanishes for exactly one value of $g(\alpha_j)$.

::: pf-proof
By the expansion of step [](#expansion){.pf-ref}, $P(z)^2g(z)=p_{1,j}^2t^2g(\alpha_j)+O(t^3)$, since $g$ is analytic at $\alpha_j$ and $g(z)=g(\alpha_j)+O(t)$. Adding this to the expansion of $f_0-\beta_j$, whose constant and linear terms vanish by step [](#preserved){.pf-ref}, gives the coefficient $c_j+p_{1,j}^2g(\alpha_j)$. As $p_{1,j}\ne0$ by step [](#expansion){.pf-ref}, this vanishes exactly when $g(\alpha_j)=-c_j/p_{1,j}^2$.
:::

:::

::: {.pf-step #interpolation}
For any prescribed complex numbers $w_j$ there is an entire $g$ with $g(\alpha_j)=w_j$ for every $j$.

::: pf-proof
Let $P$ be the product of step [](#product){.pf-ref} and put $r_j\coloneqq w_j/P'(\alpha_j)$. Mittag--Leffler's theorem, as in step [](#mittag-leffler){.pf-ref} with simple poles, gives a meromorphic $\varphi$ with simple poles exactly at the $\alpha_j$ and residue $r_j$ there. Then $g\coloneqq P\varphi$ is analytic away from the $\alpha_j$, and at $\alpha_j$ the computation $P(z)\varphi(z)=\bigl(P'(\alpha_j)t+O(t^2)\bigr)\bigl(r_j/t+O(1)\bigr)=w_j+O(t)$ shows a removable singularity with value $w_j$; so $g$ is entire with the prescribed values.
:::

:::

::: {.pf-step}
There is an entire $f$ taking the value $\beta_j$ at $\alpha_j$ with multiplicity exactly $2$ for every $j$.

::: pf-proof
For each $j$ choose $w_j\ne-c_j/p_{1,j}^2$, possible because $\CC$ is infinite, and let $g$ be the entire function of step [](#interpolation){.pf-ref} with $g(\alpha_j)=w_j$. Then $f\coloneqq f_0+P^2g$ is entire with $f(z)-\beta_j$ vanishing to order at least $2$ at each $\alpha_j$ by step [](#preserved){.pf-ref}, and with nonvanishing $t^2$ coefficient by step [](#quadratic-coefficient){.pf-ref}; hence the order is exactly $2$.
:::

:::

:::

:::
:::
:::
