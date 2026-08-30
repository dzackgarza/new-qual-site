---
title: The standard spaces
order: 8
problems:
  topics:
  - Cell Complexes
  - Surfaces
  - Projective Spaces
  - Projective Space
  - Spheres
  - Suspension
  - Suspensions
  - Simply Connected
  - Graphs
---

# The standard spaces

The table the exam is written from.
Nearly every problem is one of these spaces, a wedge or product of them, or one of them with something removed, so knowing the rows saves the computation entirely.

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
| $\bigvee_n S^2$ | $1$ | $\ZZ, 0, \ZZ^n$ | |
| Möbius band | $\ZZ$ | $\ZZ, \ZZ$ | retracts to its core circle |
| $S^1\times S^2$ | $\ZZ$ | $\ZZ, \ZZ, \ZZ, \ZZ$ | |

## How to use it

- **Wedges** add reduced homology: $\tilde H_*(X\vee Y) = \tilde H_*(X)\oplus\tilde H_*(Y)$, and $\pi_1$ takes the free product.
- **Products** multiply $\pi_1$ and, by Künneth, tensor homology.
- **Deleting a point** from an $n\dash$manifold leaves something homotopy equivalent to a lower complex; deleting a point from a closed surface leaves a wedge of circles.
- **Connected sums** are handled by Mayer--Vietoris along the separating sphere; for surfaces the genus adds.

## The pairs to keep straight

- $T^2$ against $K$: same $H_1$ rank, different torsion, and $H_2$ separates them.
- $\RP^2$ against $S^2$: same $H_0$, and $\pi_1$ separates them at once.
- $\RP^3$ against $S^1\times S^2$: both have $\pi_1$ abelian of order dividing 2 or infinite, and homology separates them.
- $S^2\vee S^1$ against $T^2$: same $H_1$, different $H_2$.
