---
title: Curves in projective space
order: 7
topics:
- Space Curves
- Projection
- Quadric Surface
---

# Curves in projective space

A very ample divisor $D$ on a smooth projective curve $C$ gives a closed immersion $\varphi_{\abs{D}}\colon C\to\PP^{\ell(D)-1}$ with $\deg\varphi_{\abs{D}}(C)=\deg D$.

[[PR-CRVDEGBD]]

If $\deg D\ge2g$, then $D$ and $D-p$ are nonspecial for every point $p$, and Riemann--Roch gives $\ell(D-p)=\ell(D)-1$.
If $\deg D\ge2g+1$, then $D-p-q$ is nonspecial as well, and $\ell(D-p-q)=\ell(D)-2$ for all points $p,q$.
Neither degree bound is necessary: on a smooth plane quartic, $g=3$ and $K\sim\OO_C(1)$ is very ample of degree $4<2g+1$.

[[T-CRVEMBP3]]

For $C\subseteq\PP^N$ with $N\ge4$, the secant variety has dimension at most $3$ and the tangent variety at most $2$, so some point $O$ lies on neither, and projection from $O$ embeds $C$ in $\PP^{N-1}$.
Iterating gives an embedding in $\PP^3$.
In $\PP^3$ the secant variety is all of $\PP^3$, and projection from a general point is birational onto a plane curve whose singularities are nodes.

[[D-CRVPLSING]]

Projection from $O\in\PP^3\setminus C$ produces a triple point when $O$ lies on a trisecant line, a cusp when $O$ lies on a tangent line, and a tacnode when $O$ lies on a secant line whose two tangent lines at the points of $C$ are coplanar.

## Curves on a quadric

[[FE-CRVQUAD]]

A curve of type $(g+1,2)$ on a smooth quadric has degree $g+3$ and genus $g$, so every genus occurs for curves on a quadric.
The twisted cubic has type $(1,2)$, the elliptic quartic type $(2,2)$, and the canonical curve of genus $4$ on a smooth quadric type $(3,3)$.

## Castelnuovo's bound

[[T-CRVCAST]]

The bound is attained by curves of type $(a,a)$, with $d=2a$ and $g=(a-1)^2$, and of type $(a,a+1)$, with $d=2a+1$ and $g=a^2-a$, on a smooth quadric.
A smooth plane curve of degree $d\ge3$ has genus $\binom{d-1}{2}$, which exceeds Castelnuovo's bound.

[[FE-CRVDEGS]]

A nondegenerate curve $C\subseteq\PP^3$ of degree $d$ whose hyperplane section is nonspecial has $4\le h^0(\OO_C(1))=d+1-g$, so $g\le d-3$.

## Dual curves

[[D-CRVDUAL]]
