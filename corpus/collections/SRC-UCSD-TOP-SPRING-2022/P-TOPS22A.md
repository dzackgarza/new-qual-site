---
schema: qual/card@1
id: P-TOPS22A
kind: problem
title: 'Wedge and product of $\RP^3$ and $S^1\vee S^1$: $\pi_1$, homology, cohomology rings, maps, and double cover'
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Cohomology
  - Cup Product
  - Wedge Product
  - Covering Spaces
  - Euler Characteristic
  - Projective Spaces
  - Homotopy
relations: []
review: draft
---

::: problem
Let $X = \mathbb{RP}^3$ and $Y = S^1 \vee S^1$.

(a) Let $A = X \vee Y$ be their wedge sum (one-point union).
Provide a presentation of the group $\pi_1(A)$.

(b) Let $B = X \times Y$ be their product.
Provide a presentation of the group $\pi_1(B)$.

(c) Compute $H_*(A; \mathbb{Z})$.

(d) Compute $H_*(B; \mathbb{Z})$.

(e) Compute $H^*(B; \mathbb{Z})$ as groups.

(f) Compute $H^*(A; \mathbb{Z}/2)$ as a ring.

(g) Compute $H^*(B; \mathbb{Z}/2)$ as a ring.

(h) Are all maps $f : X \to Y$ null-homotopic?
Explain your reason.

(i) Are all maps $g : Y \to X$ null-homotopic?
Explain your reason.

(j) Let $C$ be a double cover ($2$-sheeted covering space) of $B$.
Compute the Euler characteristic of $C$.
:::

::: {.solution}
<1>1. For $A=\mathbb{RP}^3\vee(S^1\vee S^1)$,
$$\boxed{\pi_1(A)\cong\langle r,a,b\mid r^2=1\rangle\cong(\mathbb Z/2)*F_2.}$$
::: {.proof}
Van Kampen gives the free product of $\pi_1(\mathbb{RP}^3)=\mathbb Z/2$ and $\pi_1(S^1\vee S^1)=F_2$.
:::

<1>2. For $B=\mathbb{RP}^3\times(S^1\vee S^1)$,
$$\boxed{\pi_1(B)\cong(\mathbb Z/2)\times F_2
\cong\langle r,a,b\mid r^2,[r,a],[r,b]\rangle.}$$
::: {.proof}
Fundamental groups commute with products, and the direct-product relations force $r$ to commute with the two free generators.
:::

<1>3. The integral homology of $A$ is
$$\boxed{H_i(A;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z^2\oplus\mathbb Z/2,&i=1,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
Reduced homology of a wedge is the direct sum of the reduced homologies. Use $H_1(\mathbb{RP}^3)=\mathbb Z/2$, $H_3(\mathbb{RP}^3)=\mathbb Z$, and $H_1(S^1\vee S^1)=\mathbb Z^2$.
:::

<1>4. The integral homology of $B$ is
$$\boxed{H_i(B;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,3,\\
\mathbb Z^2\oplus\mathbb Z/2,&i=1,\\
(\mathbb Z/2)^2,&i=2,\\
\mathbb Z^2,&i=4,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
The graph $Y=S^1\vee S^1$ has free homology only in degrees $0,1$, so the integral Künneth theorem has no Tor terms. Tensor $H_*(\mathbb{RP}^3)$ with $H_0(Y)=\mathbb Z$ and $H_1(Y)=\mathbb Z^2$.
:::

<1>5. The integral cohomology groups of $B$ are
$$\boxed{H^i(B;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^2,&i=1,4,\\
\mathbb Z/2,&i=2,\\
\mathbb Z\oplus(\mathbb Z/2)^2,&i=3,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
Apply the universal coefficient theorem for cohomology to <1>4. Free summands contribute through Hom and each $\mathbb Z/2$ summand contributes an Ext group one degree later.
:::

<1>6. With $\mathbb F_2$ coefficients,
$$\boxed{H^*(A;\mathbb F_2)\cong
\mathbb F_2[x,a,b]/(x^4,a^2,b^2,ab,ax,bx),}$$
with $|x|=|a|=|b|=1$.
::: {.proof}
$H^*(\mathbb{RP}^3;\mathbb F_2)=\mathbb F_2[x]/(x^4)$. The graph has degree-$1$ generators $a,b$ with all positive-degree products zero. In a wedge, all products between positive-degree classes from different summands vanish.
:::

<1>7. For the product,
$$\boxed{H^*(B;\mathbb F_2)\cong
\mathbb F_2[x,a,b]/(x^4,a^2,b^2,ab),}$$
again with all generators in degree $1$.
::: {.proof}
The field-coefficient Künneth theorem is multiplicative, so the ring is the tensor product of $\mathbb F_2[x]/(x^4)$ with the cohomology ring of the figure-eight. Cross-products such as $xa$ and $xb$ are now generally nonzero.
:::

<1>8. Every map $f:\mathbb{RP}^3\to S^1\vee S^1$ is null-homotopic.
::: {.proof}
Its induced homomorphism on fundamental groups is a map $\mathbb Z/2\to F_2$, necessarily trivial because a free group is torsion-free. The target graph is a $K(F_2,1)$, so a map inducing the trivial fundamental-group homomorphism is null-homotopic.
:::

<1>9. Not every map $g:S^1\vee S^1\to\mathbb{RP}^3$ is null-homotopic.
::: {.proof}
Map one circle to a loop representing the nontrivial element of $\pi_1(\mathbb{RP}^3)=\mathbb Z/2$ and the other circle to the basepoint. The induced map on $\pi_1$ is nontrivial, so the map cannot be null-homotopic.
:::

<1>10. Every double cover $C\to B$ has
$$\boxed{\chi(C)=0.}$$
::: {.proof}
$\chi(\mathbb{RP}^3)=0$, so $\chi(B)=\chi(\mathbb{RP}^3)\chi(S^1\vee S^1)=0$. Euler characteristic multiplies by the number of sheets of a finite cover.
:::
:::
