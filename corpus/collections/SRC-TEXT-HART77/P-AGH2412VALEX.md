---
schema: qual/card@1
id: P-AGH2412VALEX
kind: problem
title: Valuation rings of function fields of dimension one and two
classification:
  areas:
  - algebraic-geometry
  topics:
  - Valuation Rings
  - Function Fields
  - Blowing Up
relations: []
review: draft
---

::: problem
Let $k$ be an algebraically closed field.

a. If $K$ is a function field of dimension $1$ over $k$, then every valuation ring of $K/k$ except $K$ itself is discrete.
   Thus the set of all of them is just the abstract nonsingular curve $C_K$ of (I, §6).

b. If $K/k$ is a function field of dimension two, there are several different kinds of valuations.
   Suppose that $X$ is a complete nonsingular surface with function field $K$.

    - If $Y$ is an irreducible curve on $X$ with generic point $x_1$, then the local ring $R = \OO_{x_1, X}$ is a discrete valuation ring of $K/k$ with center at the nonclosed point $x_1$ on $X$.
    - If $f: X' \to X$ is a birational morphism, and if $Y'$ is an irreducible curve in $X'$ whose image in $X$ is a single closed point $x_0$, then the local ring $R$ of the generic point of $Y'$ on $X'$ is a discrete valuation ring of $K/k$ with center at the closed point $x_0$ on $X$.
    - Let $x_0 \in X$ be a closed point. Let $f: X_1 \to X$ be the blowing-up of $x_0$ (I, §4) and let $E_1 = f\inv(x_0)$ be the exceptional curve. Choose a closed point $x_1 \in E_1$, let $f_2: X_2 \to X_1$ be the blowing-up of $x_1$, and let $E_2 = f_2\inv(x_1)$ be the exceptional curve. Repeat.

      In this way we obtain a sequence of varieties $X_i$ with closed points $x_i$ chosen on them, and for each $i$ the local ring $\OO_{x_{i+1}, X_{i+1}}$ dominates $\OO_{x_i, X_i}$.
      Let $R_0 = \Union_{i \geq 0} \OO_{x_i, X_i}$.
      Then $R_0$ is a local ring, so it is dominated by some valuation ring $R$ of $K/k$ by (I, 6.1A).

      Show that $R$ is a valuation ring of $K/k$, and that it has center $x_0$ on $X$.
      When is $R$ a discrete valuation ring?

Note: we will see later (V, Ex. 5.6) that in fact the $R_0$ of the third kind is already a valuation ring itself, so $R_0 = R$.
Furthermore, every valuation ring of $K/k$ except $K$ itself is one of the three kinds just described.
:::
