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
---

::: {.problem}
Determine whether the following statements are true or false.
Justify your answer.

(a) Let $G = \{z \in \mathbb{C} : |z| < 2 \text{ and } |z-1| > 1\}$.
Then the set of polynomials is dense in the space $H(G)$ of analytic functions on $G$.

(b) Let $u_1, u_2$ be harmonic functions on $\mathbb{D}$.
Then $u := \max\{u_1, u_2\}$ is also harmonic on $\mathbb{D}$.
:::

::: {.solution}
(a) **True.** By Runge's theorem, polynomials are dense in $H(G)$ exactly
when the complement of $G$ in the Riemann sphere is connected. Here
\[
G=\{|z|<2\}\cap\{|z-1|>1\}.
\]
Its complement is the union of
\[
\{|z|\ge2\}\cup\{\infty\}
\]
and
\[
\{|z-1|\le1\}.
\]
These two closed sets meet at $z=2$, so the complement is connected. Hence
polynomials are dense in $H(G)$.

(b) **False.** Take
\[
u_1(x+iy)=x,
\qquad
u_2(x+iy)=-x.
\]
Both are harmonic, but
\[
\max\{u_1,u_2\}=|x|
\]
is not even differentiable on the imaginary axis and therefore is not
harmonic.
:::
