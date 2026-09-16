---
title: The standard spaces
order: 8
topics:
- Cell Complexes
- Surfaces
- Projective Spaces
- Spheres
- Suspension
- Suspensions
- Simply Connected
- Graphs

---

# The standard spaces

Fundamental groups and integral homology of spheres, tori, projective spaces, closed surfaces, and wedges of spheres.

| $X$ | $\pi_1$ | $H_*$ | Notes |
| --- | --- | --- | --- |
| $S^n$, $n\geq 2$ | $1$ | $\ZZ$ in degrees $0, n$ | simply connected, its own universal cover |
| $S^1$ | $\ZZ$ | $\ZZ, \ZZ$ | universal cover $\RR$ |
| $T^n$ | $\ZZ^n$ | $\ZZ^{\binom nk}$ in degree $k$ | universal cover $\RR^n$; product of circles |
| $\RP^n$, $n\geq 2$ | $\ZZ/2$ | $\ZZ, \ZZ/2, 0, \ZZ/2, \dots$ | universal cover $S^n$; $H_n = \ZZ$ iff $n$ odd |
| $\CP^n$ | $1$ | $\ZZ$ in every even degree $\leq 2n$ | no odd cells, so all boundary maps vanish |
| Klein bottle $K$ | $\gens{a,b \st abab\inv}$ | $\ZZ, \ZZ\oplus\ZZ/2, 0$ | non-orientable, so $H_2 = 0$ |
| $\Sigma_g$, genus $g$ | $\gens{a_i,b_i \st \prod[a_i,b_i]}$ | $\ZZ, \ZZ^{2g}, \ZZ$ | closed orientable |
| $N_k$, $k$ crosscaps | $\gens{a_i \st \prod a_i^2}$ | $\ZZ, \ZZ^{k-1}\oplus\ZZ/2, 0$ | closed non-orientable |
| $\bigvee_n S^1$ | free on $n$ | $\ZZ, \ZZ^n$ | $\pi_1$ free, homology free |
| $\bigvee_n S^2$ | $1$ | $\ZZ, 0, \ZZ^n$ |  |
| Möbius band | $\ZZ$ | $\ZZ, \ZZ$ | deformation retracts to its core circle |
| $S^1\times S^2$ | $\ZZ$ | $\ZZ, \ZZ, \ZZ, \ZZ$ |  |

## Constructions

::: {.fact}
\envlist

- **Wedges.** For good pointed spaces, $\tilde H_*(X\vee Y) \cong \tilde H_*(X)\oplus\tilde H_*(Y)$, and if $X$ and $Y$ are CW complexes wedged at $0$-cells, $\pi_1(X\vee Y)\cong\pi_1(X)*\pi_1(Y)$ by van Kampen's theorem.

- **Products.** $\pi_1(X\times Y)\cong\pi_1(X)\times\pi_1(Y)$, and by the Künneth theorem for CW complexes
$$
H_n(X\times Y)\cong \bigoplus_{i+j=n} H_i(X)\tensor H_j(Y)\ \oplus \bigoplus_{i+j=n-1}\Tor(H_i(X),H_j(Y)).
$$

- **Deleting a point.** If a closed $n$-manifold $M$ has a CW structure with a single $n$-cell, then $M$ minus a point in that cell deformation retracts onto the $(n-1)$-skeleton; a closed surface minus a point deformation retracts onto a wedge of circles.

- **Connected sums.** For closed $n$-manifolds with $n\geq 2$, the homology of $M\# N$ is computed by the Mayer--Vietoris sequence for the decomposition along the separating $S^{n-1}$; $\Sigma_g\#\Sigma_h\cong\Sigma_{g+h}$.

:::

## Spaces distinguished by one invariant

::: {.example title="$T^2$ and the Klein bottle"}
$H_1(T^2)\cong\ZZ^2$ and $H_1(K)\cong\ZZ\oplus\ZZ/2$, and $H_2(T^2)\cong\ZZ$ while $H_2(K)=0$.

:::

::: {.example title="$\RP^2$ and $S^2$"}
$\pi_1(\RP^2)\cong\ZZ/2$ and $\pi_1(S^2)=1$.

:::

::: {.example title="$\RP^3$ and $S^1\times S^2$"}
$\pi_1(\RP^3)\cong\ZZ/2$ and $\pi_1(S^1\times S^2)\cong\ZZ$; also $H_1(\RP^3)\cong\ZZ/2$ and $H_1(S^1\times S^2)\cong\ZZ$.

:::

::: {.example title="$S^1\vee S^1\vee S^2$ and $T^2$"}
Both have homology $\ZZ,\ZZ^2,\ZZ$, and $\pi_1(S^1\vee S^1\vee S^2)$ is free of rank $2$ while $\pi_1(T^2)\cong\ZZ^2$ is abelian, so they are not homotopy equivalent.

:::
