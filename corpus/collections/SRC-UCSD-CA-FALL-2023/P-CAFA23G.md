---
schema: qual/card@1
id: P-CAFA23G
kind: problem
title: "True/false on polynomial density and maximum of harmonic functions"
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
    Lamport structure for both parts. In (a) the connectedness of the complement is now argued: the two closed pieces meet at z = 2, which is the one point that makes the union connected, and the card names the corollary of Runge's theorem it applies (polynomials dense in H(G) iff the complement in the sphere is connected) rather than "Runge's theorem" alone. In (b) the failure is now witnessed at a specific point: at z_0 = i/2 the difference quotient of |Re z| tends to +1 along one side and -1 along the other, so the partial derivative does not exist and the function is not differentiable, hence not harmonic. Both answers (true, false) are unchanged. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own.
---

::: {.problem}
Determine whether the following statements are true or false.
Justify your answer.

(a) Let $G = \{z \in \CC : \abs{z} < 2 \text{ and } \abs{z-1} > 1\}$.
Then the set of polynomials is dense in the space $H(G)$ of analytic functions on $G$.

(b) Let $u_1, u_2$ be harmonic functions on $\DD$.
Then $u := \max\{u_1, u_2\}$ is also harmonic on $\DD$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #domain}
$G=\{z:\abs{z}<2\}\cap\{z:\abs{z-1}>1\}$ is a domain, and its complement in the Riemann sphere is connected.

::: pf-proof
$G$ is the intersection of the open disk $\abs{z}<2$ with the open set $\abs{z-1}>1$, hence open. The complement of $G$ in the sphere is
$$
K=\{\abs{z}\ge2\}\cup\{\infty\}\cup\{\abs{z-1}\le1\}.
$$
The set $\{\abs{z}\ge2\}\cup\{\infty\}$ is the image of the closed disk under $z\mapsto1/z$ followed by compactification, hence closed and connected, and $\{\abs{z-1}\le1\}$ is a closed disk, also connected. They meet at $z=2$, where $\abs{2}=2$ and $\abs{2-1}=1$. A union of two connected sets with a common point is connected, and $K$ is closed, so $K$ is connected.
:::

:::

::: {.pf-step #runge}
The polynomials are dense in $H(G)$.

::: pf-proof
The corollary of Runge's theorem used here: for a domain $G$ in $\CC$, the polynomials are dense in $H(G)$ if and only if the complement of $G$ in the Riemann sphere is connected. By step [](#domain){.pf-ref} that complement is connected, so the polynomials are dense in $H(G)$. Statement (a) is therefore true.
:::

:::

::: {.pf-step #falseb}
Statement (b) is false.

::: pf-proof
Define $u_1(z)=\operatorname{Re}z$ and $u_2(z)=-\operatorname{Re}z$ on $\DD$. Both are harmonic: they are the real parts of the holomorphic functions $z$ and $-z$. Their maximum is $u(z)=\abs{\operatorname{Re}z}$.
Suppose $u$ were harmonic on $\DD$. A harmonic function is real analytic, in particular differentiable. But at $z_0=i/2\in\DD$ and for real $t\ne0$ small,
$$
\frac{u(z_0+t)-u(z_0)}{t}=\frac{\abs{t}}{t}=\pm1,
$$
so the limit as $t\to0$ does not exist and the partial derivative $u_x(i/2)$ does not exist. So $u$ is not harmonic, and (b) is false.
:::

:::

:::
:::
