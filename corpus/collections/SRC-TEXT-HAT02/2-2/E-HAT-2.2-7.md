---
schema: qual/card@1
id: E-HAT-2.2-7
kind: problem
title: Induced map on local homology of invertible linear transformation is $\pm 1$ according to sign of determinant
classification:
  areas:
  - topology
  topics:
  - Degree
  - Local Homology
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 7; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete degree/cellular proof checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the three steps: a path in $GL_n(\RR)$ is a homotopy of pairs $(\RR^n,\RR^n-\{0\})$
    because every $f_t$ is injective; $GL_n(\RR)$ has two components, distinguished by the
    determinant, containing $I$ and $r=\mathrm{diag}(-1,1,\dots,1)$; and under the boundary
    isomorphism $r$ induces the reflection of $S^{n-1}$, of degree $-1$.
---

::: {.problem}
For an invertible linear transformation $f: \RR^n \to \RR^n$ show that the induced map on $H_n(\RR^n, \RR^n - \{0\}) \approx \tilde{H}_{n-1}(\RR^n - \{0\}) \approx \ZZ$ is $\id$ or $-\id$ according to whether the determinant of $f$ is positive or negative.
[Use Gaussian elimination to show that the matrix of $f$ can be joined by a path of invertible matrices to a diagonal matrix with $\pm 1$'s on the diagonal.]
:::

::: {.solution}
Let $f:\RR^n\to\RR^n$ be invertible. Since $n$ is fixed throughout, write $11$ for the identity map of $\RR^n$.

::: pf

::: {.pf-step #s1}

The induced map on $H_n(\RR^n,\RR^n-\{0\})$ depends only on the path component of $f$ in $GL_n(\RR)$.

::: pf-proof

If $f_t$, $t\in[0,1]$, is a path in $GL_n(\RR)$, then $f_t$ maps $\RR^n-\{0\}$ to itself, so $H(x,t)=f_t(x)$ is a homotopy of pairs $(\RR^n,\RR^n-\{0\})\to(\RR^n,\RR^n-\{0\})$ through maps of pairs, and maps homotopic through maps of pairs induce the same homomorphism $H_n(\RR^n,\RR^n-\{0\})\to H_n(\RR^n,\RR^n-\{0\})$ by Proposition 2.19 (Hatcher p. 118).

:::

:::

::: {.pf-step #s2}

Every matrix of positive determinant is path connected in $GL_n(\RR)$ to the identity, and every matrix of negative determinant is path connected to $r=\operatorname{diag}(-1,1,\dots,1)$.

::: pf-proof

Gaussian elimination, as the hint directs, writes $A\in GL_n(\RR)$ as a product of elementary matrices: shears $I+\lambda E_{ij}$ with $i\neq j$, dilations by nonzero scalars, and transpositions of two coordinates, each of which stays invertible throughout the path below.
A shear is joined to $I$ by $I+t\lambda E_{ij}$, a dilation by $c>0$ by the path of dilations by $c^t$, and a dilation by $c<0$ is a transposition composed with a dilation by $|c|$.
On a two coordinate block, the transposition equals $R\,r_{0}$ where $r_{0}=\operatorname{diag}(-1,1)$ and $R$ is rotation by $-\pi/2$ of that plane; replacing $R$ by the rotation through $-t\pi/2$ gives a path from the transposition to $r_{0}$ with determinant $-1$ throughout, and the block extends by the identity on the other coordinates.
The product of these paths joins $A$ to a diagonal matrix with entries $\pm1$. An even number of entries $-1$ is removed by rotating each pair of such coordinates through angle $\pi t$ in its plane, a path of determinant $+1$ from $\operatorname{diag}(1,1)$ to $\operatorname{diag}(-1,-1)$; an odd number is reduced to the single entry $-1$ in the first coordinate. Since $\det$ is continuous and nonzero on $GL_n(\RR)$, these paths cannot meet a singular matrix, and they end at $11$ when $\det A>0$ and at $r$ when $\det A<0$.

:::

:::

::: {.pf-step #s3}

The identity $11$ induces $+11$ on $H_n(\RR^n,\RR^n-\{0\})$ and $r$ induces $-11$.

::: pf-proof

The inclusion of pairs $(\RR^n-\{0\},\emptyset)\to(\RR^n,\RR^n-\{0\})$ sits in the long exact sequence of the pair (Theorem 2.13, Hatcher p. 114), whose boundary map $\partial:H_n(\RR^n,\RR^n-\{0\})\to\widetilde H_{n-1}(\RR^n-\{0\})$ is an isomorphism because $\RR^n$ is contractible; the target is $\widetilde H_{n-1}(S^{n-1})\approx\ZZ$ by Theorem 2.10 (p. 111) applied to the homotopy equivalence $x\mapsto x/\norm x$ together with Corollary 2.14 (p. 114). The maps induced by $11$ and by $r$ commute with $\partial$, so it suffices to know their effect on $\widetilde H_{n-1}$ of $\RR^n-\{0\}$, where $r$ acts as the restriction of $r$ to $S^{n-1}$, the reflection fixing the subsphere $x_1=0$ and interchanging the two hemispheres, of degree $-1$ by property (e) of degree (Hatcher p. 134). Hence $r$ acts as $-11$ and $11$ acts as $+11$.

:::

:::

::: {.pf-step #s4}
Combining steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref},
$$
\boxed{
f_*=
\begin{cases}
+11,&\det f>0,\\
-11,&\det f<0.
\end{cases}}
$$

::: pf-proof
Step [](#s1){.pf-ref} makes the induced map depend only on the path component of $f$ in $GL_n(\RR)$, step [](#s2){.pf-ref} separates the two components by the sign of $\det f$, and step [](#s3){.pf-ref} gives the value $+11$ on the component of $11$ and $-11$ on the component of $r$.
:::

:::

:::

Thus the induced map is $11$ or $-11$ according as $\det f$ is positive or negative.
:::
