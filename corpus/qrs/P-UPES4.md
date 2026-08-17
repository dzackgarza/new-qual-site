---
schema: qual/card@1
id: P-UPES4
kind: problem
title: $ce^z$ has a unique fixed point in $\{\operatorname{Re} z<1\}$ when $|c|<\frac13$
classification:
  areas:
  - complex-analysis
  topics:
  - fixed-points
  - rouche
  - zeros
relations: []
review: draft
solved: true
---

::: problem
Let $c\in \CC$ with $\abs{c} < {1\over 3}$.
Show that on the open set $\theset{z\in \CC \suchthat \Re(z) < 1}$, the function $f(z) \definedas ce^z$ has exactly one fixed point.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $\abs{c} < \frac13$, show $f(z) = ce^z$ has exactly one fixed point in $\theset{\Re z < 1}$.

<1>1. Fixed points of $f$ are zeros of $g(z) \definedas z - ce^z$.
Proof: $f(z) = z \iff ce^z = z \iff z - ce^z = 0$.

<1>2. On the line $\Re z = 1$, $\abs{ce^z} < \abs{z}$.
Proof: $\abs{ce^z} = \abs c e^{\Re z} = \abs c e < \frac{e}{3} < 1$, while $\abs z \geq \abs{\Re z} = 1$ on that line; hence $\abs{ce^z} < 1 \leq \abs z$ (and at $z = 1$ the inequality is strict: $\abs{ce} < 1 = \abs 1$).

<1>3. On the semicircle $\abs z = R$, $\Re z \leq 1$, with $R > 1$: $\abs{ce^z} < \abs{z}$.
Proof: For $\Re z \leq 1$, $\abs{ce^z} = \abs c e^{\Re z} \leq \abs c e < \frac e3 < 1 < R = \abs z$.

<1>4. In the half-disk $D_R \definedas \theset{\abs z < R, \Re z < 1}$, $g$ has exactly one zero, namely $z = 0$.
Proof: Apply Rouch\'e's theorem on the boundary of $D_R$ (the segment $\Re z = 1$, $\abs{\Im z} \leq R$ plus the semicircle $\abs z = R$, $\Re z \leq 1$) with $h(z) = z$ and $k(z) = -ce^z$: by <1>2 and <1>3, $\abs{k(z)} < \abs{h(z)}$ on the whole boundary, so $g = h + k$ and $h$ have the same number of zeros in $D_R$.
The function $h(z) = z$ has exactly one zero (at $0$, simple), and $0 \in D_R$; hence $g$ has exactly one zero in $D_R$.

<1>5. $g$ has exactly one zero in the half-plane $\theset{\Re z < 1}$.
Proof: The zeros of $g$ are isolated.
Every zero of $g$ with $\Re z < 1$ lies in $D_R$ for all sufficiently large $R$ (since $\abs z < R$ eventually).
By <1>4, $D_R$ contains exactly one zero for every $R > 1$, and these zeros agree as $R$ varies (a zero in $D_R$ persists in $D_{R'}$ for $R' > R$), so the half-plane contains exactly one zero.

<1>6. Q.E.D. Proof: <1>1 and <1>5 show $f(z) = ce^z$ has exactly one fixed point in $\theset{\Re z < 1}$.
:::
