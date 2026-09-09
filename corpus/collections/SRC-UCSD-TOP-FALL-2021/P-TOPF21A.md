---
schema: qual/card@1
id: P-TOPF21A
kind: problem
title: 'Connected sum and wedge of $\RP^2$ and $T^2$: $\pi_1$, homology, cohomology, orientability, and covers'
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Cohomology
  - Cup Product
  - Connected Sum
  - Wedge Product
  - Covering Spaces
  - Euler Characteristic
  - Surfaces
  - Projective Spaces
relations: []
review: draft
---

::: problem
Let $\mathbb{RP}^2$ be the real projective plane.
Let $T = S^1 \times S^1$ be the torus.

(a) Let $A$ be their connected sum.
Provide a presentation of the group $\pi_1(A)$.

(b) Let $B = \mathbb{RP}^2 \vee T$ be their wedge sum (one-point union).
Provide a presentation of the group $\pi_1(B)$.

(c) Compute $H_*(A; \mathbb{Z})$.

(d) Compute $H_*(B; \mathbb{Z})$.

(e) Compute $H^*(A; \mathbb{Z}/2)$ as a ring.

(f) Compute $H^*(B; \mathbb{Z}/2)$ as a ring.

(g) Is $A$ orientable?
Explain your reason.

(h) Is $B$ homotopy equivalent to a manifold?
Explain your reason.

(i) Let $C$ be a double cover ($2$-sheeted covering space) of $B$.
Compute the Euler characteristic of $C$.
:::

::: {.solution}
<1>1. The connected sum $A=\mathbb{RP}^2\#T^2$ is the closed nonorientable surface $N_3$ of nonorientable genus $3$, and
$$\boxed{\pi_1(A)\cong\langle x,y,z\mid x^2y^2z^2=1\rangle.}$$
::: {.proof}
A torus is the connected sum of two projective planes, so $\mathbb{RP}^2\#T^2\cong\#^3\mathbb{RP}^2$. The displayed presentation is the standard polygon presentation of $N_3$.
:::

<1>2. For $B=\mathbb{RP}^2\vee T^2$,
$$\boxed{\pi_1(B)\cong\langle r,a,b\mid r^2=1,\ [a,b]=1\rangle\cong(\mathbb Z/2)*\mathbb Z^2.}$$
::: {.proof}
Van Kampen gives the free product of the fundamental groups of the wedge summands.
:::

<1>3. The integral homology of $A$ is
$$\boxed{H_i(A;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^2\oplus\mathbb Z/2,&i=1,\\
0,&i\ge2.
\end{cases}}$$
::: {.proof}
For the closed nonorientable surface $N_g$, one has $H_1(N_g;\mathbb Z)\cong\mathbb Z^{g-1}\oplus\mathbb Z/2$ and $H_2(N_g;\mathbb Z)=0$. Take $g=3$.
:::

<1>4. The integral homology of $B$ is
$$\boxed{H_i(B;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z^2\oplus\mathbb Z/2,&i=1,\\
0,&i\ge3.
\end{cases}}$$
::: {.proof}
Reduced homology of a wedge is the direct sum of the reduced homologies of the summands. Use $H_1(\mathbb{RP}^2)=\mathbb Z/2$, $H_2(\mathbb{RP}^2)=0$, and $H_1(T^2)=\mathbb Z^2$, $H_2(T^2)=\mathbb Z$.
:::

<1>5. With $\mathbb F_2$ coefficients,
$$\boxed{H^*(A;\mathbb F_2)\cong
\mathbb F_2[x,y,z,u]/(xy,xz,yz,\ x^2-u,y^2-u,z^2-u,\text{terms of degree}>2),}$$
where $|x|=|y|=|z|=1$ and $|u|=2$.
::: {.proof}
For $N_3$, choose the standard three one-sided simple closed curves representing a basis of $H_1(-;\mathbb F_2)$. Their mod-$2$ intersection pairing is diagonal with each self-intersection equal to $1$. Under Poincaré duality this means $x_i x_j=0$ for $i\ne j$ and $x_i^2=u$, the mod-$2$ fundamental cohomology class.
:::

<1>6. For $B$, choose $x\in H^1(\mathbb{RP}^2;\mathbb F_2)$ and the standard torus classes $a,b\in H^1(T^2;\mathbb F_2)$. Then
$$\boxed{x^2=u\ne0,\qquad ab=v\ne0,}$$
with $a^2=b^2=0$ and every product involving positive-degree classes from different wedge summands equal to $0$; $u,v$ form a basis of $H^2(B;\mathbb F_2)$.
::: {.proof}
The cohomology ring of a wedge in positive degrees is the product of the rings of its summands with all cross-products zero. For $\mathbb{RP}^2$, $H^*=\mathbb F_2[x]/(x^3)$; for $T^2$, $H^*=\Lambda_{\mathbb F_2}(a,b)$ with $ab$ the top class.
:::

<1>7. The surface $A$ is nonorientable.
::: {.proof}
It is $N_3$, equivalently it contains a projective-plane crosscap. Also $H_2(A;\mathbb Z)=0$, whereas a closed connected orientable surface has top homology $\mathbb Z$.
:::

<1>8. Under the standard intended meaning “closed manifold,” $B$ is not homotopy equivalent to a manifold.
::: {.proof}
Since $H_2(B;\mathbb Z)\cong\mathbb Z$ and all higher homology vanishes, any closed connected manifold homotopy equivalent to $B$ would have dimension $2$ and be orientable. But the first homology of a closed orientable surface is torsion-free, whereas $H_1(B;\mathbb Z)$ contains $\mathbb Z/2$. If manifolds with boundary or noncompact manifolds are allowed, the literal statement needs qualification: finite $2$-complexes can be thickened in sufficiently high dimension to manifolds with boundary having the same homotopy type.
:::

<1>9. Every double cover $C\to B$ satisfies
$$\boxed{\chi(C)=2\chi(B)=0.}$$
::: {.proof}
Euler characteristic is additive on wedges up to subtracting the wedge point:
$$\chi(B)=\chi(\mathbb{RP}^2)+\chi(T^2)-1=1+0-1=0.$$
Euler characteristic multiplies by the number of sheets of a finite cover.
:::
:::
