---
schema: qual/card@1
id: P-ZPH3J
kind: problem
title: Integer-matrix maps of the torus, the induced map on $H_1$, and homotopy to
  the identity or to a fixed-point-free map
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
  - Fixed Points
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked all four parts against problem VIII of the official UGA Spring 2009 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Identified the induced map on H_1 from the coordinate loops. For the
    fixed-point-free criterion, used the Lefschetz number on T^2 for necessity
    and explicit affine translations for sufficiency.
---

::: problem
View the torus $T$ as the quotient space $\RR^2 /\ZZ^2$.

Let $A$ be a $2 \times 2$ matrix with $\ZZ$ coefficients.

Show that the linear map $A : \RR^2 \to \RR^2$ descends to a continuous map $\mca : T \to T$.

Show that, with respect to a suitable basis for $H_1 (T ; \ZZ)$, the matrix $A$ represents the map induced on $H_1$ by $\mca$.

Find a necessary and sufficient condition on $A$ for $\mca$ to be homotopic to the identity.

Assume additionally that $\mca$ is a homeomorphism, that $\det A = 1$, and that all entries of $A$ are nonnegative.
Find a necessary and sufficient condition on $A$ for $\mca$ to be homotopic to a map with no fixed points.
:::

::: {.solution}
Write
\[
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}.
\]

<1>1. The linear map $A:\RR^2\to\RR^2$ induces a well-defined continuous map
\[
\mca:T=\RR^2/\ZZ^2\longrightarrow T,
\qquad
\mca([x])=[Ax].
\]
::: {.proof}
If $x,x'\in\RR^2$ represent the same point of $T$, then $x'=x+z$ for some $z\in\ZZ^2$.
Since $A$ has integer entries,
\[
Az\in\ZZ^2,
\]
so
\[
A x'=A x+A z
\]
represents the same point of $T$ as $Ax$.
Thus $[x]\mapsto[Ax]$ is well defined.

Let $q:\RR^2\to T$ be the quotient map.
Then
\[
\mca\circ q=q\circ A.
\]
The right-hand side is continuous, and $q$ is a quotient map, so $\mca$ is continuous.
:::

<1>2. With respect to the basis of $H_1(T;\ZZ)$ given by the two coordinate circles, the matrix of $\mca_*$ is exactly $A$.
::: {.proof}
Let
\[
\alpha(t)=[(t,0)],
\qquad
\beta(t)=[(0,t)]
\qquad (0\le t\le1).
\]
Their homology classes $[\alpha],[\beta]$ form the standard basis of
\[
H_1(T;\ZZ)\cong\ZZ^2.
\]
Since
\[
\mca\circ\alpha(t)=[(at,ct)],
\]
the first basis vector is sent to
\[
a[\alpha]+c[\beta].
\]
Similarly,
\[
\mca\circ\beta(t)=[(bt,dt)]
\]
represents
\[
b[\alpha]+d[\beta].
\]
Hence the two columns of the matrix of $\mca_*$ in the ordered basis $([\alpha],[\beta])$ are
\[
\binom ac,
\qquad
\binom bd,
\]
so that matrix is $A$.
:::

<1>3. The map $\mca$ is homotopic to the identity if and only if
\[
\boxed{A=I_2}.
\]
::: {.proof}
If $A=I_2$, then $\mca$ is the identity map itself.

Conversely, suppose $\mca\simeq\id_T$.
Homotopic maps induce the same map on singular homology, hence
\[
\mca_*=(\id_T)_*=I_2
\]
on $H_1(T;\ZZ)$.
By <1>2, the matrix of $\mca_*$ is $A$.
Therefore $A=I_2$.
:::

<1>4. Under the additional assumptions in the last part, if $\mca$ is homotopic to a fixed-point-free map, then
\[
\operatorname{tr}(A)=2.
\]
::: {.proof}
Let $f:T\to T$ be fixed-point-free and homotopic to $\mca$.
The torus is a finite CW complex, so the Lefschetz fixed-point theorem applies.
Its contrapositive says that a fixed-point-free self-map has Lefschetz number zero.

Homotopic maps induce the same maps on homology, so $L(f)=L(\mca)$.
For the torus,
\[
H_0(T;\ZZ)\cong\ZZ,
\qquad
H_1(T;\ZZ)\cong\ZZ^2,
\qquad
H_2(T;\ZZ)\cong\ZZ.
\]
The induced map on $H_0$ is the identity, the trace on $H_1$ is $\operatorname{tr}(A)$ by <1>2, and the induced map on $H_2$ is multiplication by the degree $\det A$.
Therefore
\[
L(\mca)
 =1-\operatorname{tr}(A)+\det A.
\]
Since $\det A=1$, this becomes
\[
L(\mca)=2-\operatorname{tr}(A).
\]
The equality $L(f)=0$ now forces $\operatorname{tr}(A)=2$.
:::

<1>5. With integer nonnegative entries and $\det A=1$, the condition $\operatorname{tr}(A)=2$ is equivalent to
\[
A=\begin{pmatrix}1&m\\0&1\end{pmatrix}
\quad\text{or}\quad
A=\begin{pmatrix}1&0\\m&1\end{pmatrix}
\qquad
\text{for some }m\in\ZZ_{\ge0}.
\]
::: {.proof}
The trace condition gives
\[
a+d=2.
\]
Because $a,d$ are nonnegative integers, the only possibilities are
\[
(a,d)=(0,2),(1,1),(2,0).
\]
The determinant equation
\[
ad-bc=1
\]
with $b,c\ge0$ rules out $(a,d)=(0,2)$ and $(2,0)$, since either would give $-bc=1$.
Thus $a=d=1$.
Then
\[
1-bc=1,
\]
so $bc=0$.
Hence either $c=0$ or $b=0$, giving exactly the two displayed forms.
Conversely, every displayed matrix has trace $2$, determinant $1$, and nonnegative integer entries.
:::

<1>6. Every matrix in <1>5 yields a map $\mca$ homotopic to a fixed-point-free map.
::: {.proof}
First suppose
\[
A=\begin{pmatrix}1&m\\0&1\end{pmatrix}.
\]
In quotient coordinates on $T=\RR^2/\ZZ^2$,
\[
\mca([x,y])=[x+my,y].
\]
Define
\[
g([x,y])=[x+my,y+\tfrac12].
\]
This is well defined, and the homotopy
\[
H_s([x,y])=[x+my,y+\tfrac{s}{2}]
\qquad(0\le s\le1)
\]
runs from $\mca$ to $g$.
If $g([x,y])=[x,y]$, then the second coordinate would give
\[
y+\tfrac12\equiv y\pmod{\ZZ},
\]
which is impossible.
Thus $g$ has no fixed points.

Now suppose
\[
A=\begin{pmatrix}1&0\\m&1\end{pmatrix}.
\]
Then
\[
\mca([x,y])=[x,mx+y].
\]
Define
\[
h([x,y])=[x+\tfrac12,mx+y].
\]
The homotopy
\[
K_s([x,y])=[x+\tfrac{s}{2},mx+y]
\]
runs from $\mca$ to $h$, and a fixed point of $h$ would force
\[
x+\tfrac12\equiv x\pmod{\ZZ},
\]
again impossible.
Therefore $h$ is fixed-point-free.
:::

<1>7. Hence, under the hypotheses of the final part, the necessary and sufficient condition is
\[
\boxed{\operatorname{tr}(A)=2}.
\]
Equivalently, $A$ has one of the two unipotent forms listed in <1>5.
::: {.proof}
Necessity is <1>4, and sufficiency follows from <1>5 and <1>6.
:::
:::
