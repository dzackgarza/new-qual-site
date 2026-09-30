---
schema: qual/card@1
id: P-AGH4422FAMILYOVERAFFINELINE
kind: problem
title: A family of elliptic curves over $\AA^1_\CC$ with a section is trivial
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.22 together with the preceding torsion and etale-cover
    exercises. Cross-checked that multiplication by 2 is finite etale in
    characteristic zero and that full 2-torsion gives Legendre form. The
    proof also closes the residual quadratic-twist issue after lambda is
    shown constant.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $X \to \AA_{\CC}^1$ is a family of elliptic curves having a section, show that the family is trivial.

Hints: Use the section to fix the group structure on the fibres.
Show that the points of order 2 on the fibres form an étale cover of $\AA_{\CC}^1$, which must be trivial, since $\AA_{\CC}^1$ is simply connected.
This implies that $\lambda$ can be defined on the family, so it gives a map $\AA_{\CC}^1 \to \AA_{\CC}^1-\theset{0,1}$.
Any such map is constant, so $\lambda$ is constant, so the family is trivial.
:::

::: {.solution}
Put
$$
S=\AA^1_{\CC}=\Spec\CC[t],
$$
write
$$
\pi:E\longrightarrow S
$$
for the family, and let
$$
O:S\longrightarrow E
$$
be the given section.

::: pf

::: {.pf-step #s1}

The section $O$ makes $E/S$ an elliptic scheme, and its $2$-torsion
$$
E[2]=\ker[2]
$$
is a finite etale cover of $S$ of degree $4$.

::: pf-proof

The section chooses an origin on every fibre, so the fibrewise elliptic-curve
group laws assemble to the group law on the elliptic scheme $E/S$.

Multiplication by $2$ on an elliptic scheme is finite locally free of degree
$4$.  Since $2$ is invertible on $S$, its differential on the relative
tangent line is multiplication by $2$, hence an isomorphism.  Thus
$$
[2]:E\longrightarrow E
$$
is etale.  Base-changing along the zero section gives
$$
E[2]\longrightarrow S,
$$
which is therefore finite etale of degree $4$.

:::

:::

::: {.pf-step #s2}

There are four pairwise disjoint sections
$$
O,T_0,T_1,T_\lambda:S\longrightarrow E
$$
whose images are exactly $E[2]$.

::: pf-proof

The affine line over $\CC$ has no nontrivial connected finite etale covers.
Hence every finite etale cover of $S$ is a disjoint union of copies of $S$.
Applying this to the degree-$4$ cover in step [](#s1){.pf-ref} gives four sections.
One is the zero section $O$; label the other three
$$
T_0,T_1,T_\lambda.
$$
Because $E[2]\to S$ is etale, these components are disjoint.

:::

:::

::: {.pf-step #s3}

The complete linear system
$$
\abs{2O}
$$
defines a finite flat double cover
$$
q:E\longrightarrow\PP^1_S
$$
whose branch sections are exactly the images of
$$
O,T_0,T_1,T_\lambda.
$$
After an automorphism of $\PP^1_S$, the first three branch sections are
$$
\infty,\qquad 0,\qquad 1.
$$

::: pf-proof

On every elliptic fibre $E_s$, the line bundle
$$
\OO_{E_s}(2O_s)
$$
has degree $2$ and two independent sections.  Its complete linear system is
the quotient map by the involution
$$
[-1]:E_s\longrightarrow E_s.
$$
By cohomology and base change, the rank-$2$ bundle
$$
\pi_*\OO_E(2O)
$$
and its fibrewise linear systems give the relative quotient
$$
q:E\longrightarrow\PP\bigl(\pi_*\OO_E(2O)\bigr),
$$
whose restriction to every fibre has degree $2$.  This morphism is proper
and fibrewise finite, hence finite.  The fibrewise flatness criterion then
shows that it is flat.  Thus it is finite flat of degree $2$.

Every vector bundle on
$$
S=\Spec\CC[t]
$$
is free, so the target is isomorphic to $\PP^1_S$.  The fixed points of
$[-1]$ are precisely the points killed by $2$; hence the ramification
sections of $q$ are the four sections in step [](#s2){.pf-ref}, and their images are the
four branch sections.

It remains to normalize three branch sections globally.  Since
$\Pic(S)=0$, each section of $\PP^1_S$ can be represented by a unimodular
column vector in $\CC[t]^2$.  Choose vectors $v_\infty,v_0$ representing
the images of $O,T_0$.  Their sections are disjoint, so
$$
\det(v_\infty,v_0)
$$
vanishes nowhere on $S$ and hence is a unit of $\CC[t]$.  Thus the matrix
with columns $v_\infty,v_0$ lies in $\GL_2(\CC[t])$.  Its inverse gives
an automorphism of $\PP^1_S$ carrying these two sections to
$$
\infty=[1:0],
\qquad
0=[0:1].
$$

Write the image of $T_1$ in these coordinates as $[a:b]$.  Disjointness
from $\infty$ and $0$ says respectively that $b$ and $a$ vanish nowhere,
so
$$
a,b\in\CC[t]^*=\CC^*.
$$
A diagonal automorphism preserving $\infty$ and $0$ now carries $[a:b]$
to
$$
1=[1:1].
$$
This gives the required global normalization.

:::

:::

::: {.pf-step #s4}

The fourth branch section defines a morphism
$$
\boxed{
\lambda:S\longrightarrow\AA^1_{\CC}\setminus\{0,1\}.
}
$$

::: pf-proof

In the coordinate fixed in step [](#s3){.pf-ref}, write the fourth branch section as
$$
x=\lambda.
$$
It is disjoint from the section at infinity, so it takes values in the
affine chart $\AA^1_S$.  It is also disjoint from the branch sections
$x=0$ and $x=1$.  Therefore its coordinate is a regular function
$$
\lambda\in\Gamma(S,\OO_S)=\CC[t]
$$
such that neither $\lambda$ nor $\lambda-1$ vanishes anywhere on $S$.
Equivalently, it is the displayed morphism.

:::

:::

::: {.pf-step #s5}

The function $\lambda$ is constant.

::: pf-proof

Since the map in step [](#s4){.pf-ref} avoids $0$ and $1$, both
$$
\lambda
\qquad\text{and}\qquad
\lambda-1
$$
are units of $\CC[t]$.  But
$$
\CC[t]^*=\CC^*.
$$
Hence $\lambda\in\CC\setminus\{0,1\}$ is constant.

:::

:::

::: {.pf-step #s6}

The double cover $q$ is the product over $S$ of the Legendre double
cover
$$
E_\lambda:
y^2=x(x-1)(x-\lambda)
\longrightarrow
\PP^1_{\CC}.
$$

::: pf-proof

By step [](#s5){.pf-ref} the branch divisor on $\PP^1_S$ is the constant divisor
$$
B
=
\{0\}+\{1\}+\{\lambda\}+\{\infty\}.
$$
Because $2$ is invertible, the finite flat double cover has the trace
decomposition
$$
q_*\OO_E
\cong
\OO_{\PP^1_S}\oplus\mcl^{-1},
$$
where multiplication on the trace-zero summand is specified by a section
$$
s\in H^0(\PP^1_S,\mcl^{\tensor2})
$$
whose zero divisor is $B$.

The branch divisor has relative degree $4$, so
$$
\mcl^{\tensor2}\cong\OO_{\PP^1_S}(4).
$$
Moreover
$$
\Pic(S)=0
$$
and
$$
\Pic(\PP^1_S)\cong\ZZ,
$$
generated by $\OO(1)$.  Hence
$$
\mcl\cong\OO_{\PP^1_S}(2).
$$

In homogeneous coordinates $[X:Z]$, the standard section
$$
s_0=XZ(X-Z)(X-\lambda Z)
$$
of $\OO(4)$ has zero divisor $B$.  The sections $s$ and $s_0$ have the same
zero divisor, so their quotient is a global unit on $\PP^1_S$.  Such a unit
comes from
$$
\CC[t]^*=\CC^*.
$$
Thus
$$
s=c\,s_0
$$
for some $c\in\CC^*$.  Since $\CC$ is algebraically closed, write
$$
c=u^2.
$$
Rescaling the trace-zero generator by $u$ identifies the two double-cover
algebras.  Therefore
$$
E\cong E_\lambda\times_{\Spec\CC}S
$$
over $S$, with the given zero section corresponding to the point at
infinity.

:::

:::

::: {.pf-step #s7}

The family $E\to\AA^1_{\CC}$ is trivial.

::: pf-proof

Step [](#s6){.pf-ref} gives an isomorphism of elliptic schemes
$$
\boxed{
E\cong E_\lambda\times\AA^1_{\CC}
}
$$
over the base.  This is precisely the required trivialization.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} trivialize the relative $2$-torsion, steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}
produce Hartshorne's Legendre parameter and show it is constant, and steps
[](#s6){.pf-ref} and [](#s7){.pf-ref} show that no residual quadratic twist remains.

:::

:::

:::
