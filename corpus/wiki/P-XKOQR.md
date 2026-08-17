---
schema: qual/card@1
id: P-XKOQR
kind: problem
title: A holomorphic map is a local bijection iff $f'\neq 0$
classification:
  areas:
  - complex-analysis
  topics:
  - biholomorphisms
  - open-mapping-theorem
  - argument-principle
  - rouche
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
A holomorphic mapping $f: U \rightarrow V$ is a local bijection on $U$ if for every $z \in U$ there exists an open disc $D \subset U$ centered at $z$ so that $f: D \rightarrow f(D)$ is a bijection. Prove that a holomorphic map $f: U \rightarrow V$ is a local bijection if and only if $f^{\prime}(z) \neq 0$ for all $z \in U$.
:::

:::{.concept}
\envlist

- Inverse function theorem: if $F\in C^1(\RR^n\to \RR^n)$ and $D_f$ is invertible at $p$, the $F$ is invertible in a neighborhood of $p$, and $F\inv$ is $C^1$.

:::

:::{.solution}
$\impliedby$:
Let $z\in U$ be fixed.
Since $f$ is holomorphic at $z$ and $f'(z)\neq 0$, consider $f(x, y)$ and its Jacobian as a real-valued function:
\[
D_f = \matt{u_x}{u_y}{v_x}{v_y}
\implies
\det(D_f) = u_x v_y - v_x u_y = u_x^2 + v_x^2 = \abs{f'}^2 > 0
,\]
so the derivative matrix is invertible at $z$.
Applying the inverse function theorem yields that $f$ is a smooth diffeomorphism on some neighborhood $N\ni p$, and in particular is bijective  on $N$.

$\not\impliedby$:
If $f'(z) = 0$ for some $z$, then we claim that $f$ can not be injective.
Equivalently, injectivity of $f$ implies $f'\neq 0$.
Suppose $f$ is holomorphic at $z_0$ but $f'(z_0)=0$.
Write $h(z) \da f(z) - f(z_0)$, which has a zero $z_0$ of some order $k\geq 2$.
For a disc $D$ small enough about $z_0$ avoiding the other (isolated) zeros of $h$ and $f'$, for any $p$ in a neighborhood of $z_0$ and contained in $D$,
\[
\int_{\bd D} {f'(\xi) \over f(\xi) - p} \dxi
= \size Z(f(z) - p) 
,\]
using the argument principle and that $(f(\xi) - p)' = f'(\xi)$.
But for $D$ small enough, $\size Z(f(z) - p) = \size Z(f(z) - f(z_0)) = k$ by Rouché, so there are $k$ solutions to $f(z) = p$.
Since $(f(z) - p)' \neq 0$ in $D$, none of these can be repeated roots, so these $k$ solutions are distinct, forcing $f$ to be $k$-to-one and fail injectivity.

Expanding on the Rouché argument: set $c \da \inf_{z\in D} \abs{f(z) - w_0}$, then for $D'$ of radius $c$, set

- $F(z) \da (f(z) - z_0) - (f(z) - p) = z-p$
- $G(z) = f(z) - z_0$
- $(F+G)(z) = f(z) - p$

Then $F>G$ on $\bd D'$ will imply $F, F+G$ have the same number of zeros within $D'$, and this bound follows from
\[
\abs{F(z)} = \abs{z-p} < c \leq \abs{f(z) - p }
,\]
where the first inequality is from making the disc small and the second from choosing $c$ as an inf.

:::
