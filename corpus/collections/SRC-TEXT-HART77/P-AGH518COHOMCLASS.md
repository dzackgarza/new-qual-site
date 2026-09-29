---
schema: qual/card@1
id: P-AGH518COHOMCLASS
kind: problem
title: Cohomology class of a divisor and compatibility with the intersection pairing
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.8, the retained Egbert companion proof, Exercise
    III.7.4 as represented by the cohomology-class card, and the preceding
    algebraic/numerical-equivalence argument. The proof below identifies the
    Serre pairing with restriction to a smooth divisor and degree on that
    divisor, then proves finite generation in characteristic zero by embedding
    Num(X) into a finite-rank integral lattice of intersection numbers; finite
    dimensionality alone would not imply finite generation of an additive
    subgroup.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
For any divisor $D$ on the surface $X$, we define its cohomology class $c(D) \in H^1\left(X, \Omega_X\right)$ by using the isomorphism $\Pic X \cong H^1\left(X, \mathcal{O}_X^*\right)$ of (III, Ex.
4.5) and the sheaf homomorphism $d \log : \mathcal{O}^* \rightarrow \Omega_X$ (III, Ex.
7.4c). Thus we obtain a group homomorphism $c: \Pic X \rightarrow H^1\left(X, \Omega_X\right)$.
On the other hand, $H^1(X, \Omega)$ is dual to itself by Serre duality (III, 7.13), so we have a nondegenerate bilinear map
\[
\langle\quad, \quad\rangle: H^1(X, \Omega) \times H^1(X, \Omega) \rightarrow k .
\]

a. Prove that this is compatible with the intersection pairing, in the following sense: for any two divisors $D, E$ on $X$, we have
\[
\langle c(D), c(E)\rangle=(D . E) \cdot 1
\]
in $k$.

Hint: Reduce to the case where $D$ and $E$ are nonsingular curves meeting transversally.
Then consider the analogous map $c: \Pic D \rightarrow H^1\left(D, \Omega_D\right)$, and the fact (III, Ex.
7.4) that $c(\text{point})$ goes to 1 under the natural isomorphism of $H^1\left(D, \Omega_D\right)$ with $k$.

b. If $\operatorname{char} k=0$, use the fact that $H^1\left(X, \Omega_X\right)$ is a finite-dimensional vector space to show that $\Num X$ is a finitely generated free abelian group.
:::

::: {.solution}
Write
$$
V=H^1(X,\Omega_X).
$$
The Serre-duality pairing on $V$ is the cup product followed by wedge product
and the trace
$$
H^1(X,\Omega_X)\times H^1(X,\Omega_X)
\longrightarrow H^2(X,\omega_X)\xrightarrow{\operatorname{tr}_X}k.
$$

::: pf

::: {.pf-step #s1}

If $j:D\hookrightarrow X$ is a nonsingular curve, then for every
$\alpha\in V$,
$$
\langle c(D),\alpha\rangle
=
\operatorname{tr}_D(j^*\alpha).
$$

::: pf-proof

Exercise III.7.4 identifies the logarithmic class $c(D)$ of the divisor with
its normalized codimension-one cohomology class; this identification is proved
on [[P-AGH374COHOMCLASS]], part (d). For that Gysin class, compatibility of
Serre duality with the closed immersion $j$ gives
$$
\langle c(D),\alpha\rangle_X
=
\langle 1,j^*\alpha\rangle_D
=
\operatorname{tr}_D(j^*\alpha).
$$
This is the claimed identity.

:::

:::

::: {.pf-step #s2}

If $D,E$ are nonsingular curves meeting transversally, then
$$
\boxed{\langle c(D),c(E)\rangle=(D\cdot E)\cdot1}.
$$

::: pf-proof

Naturality of $d\log$ under restriction gives
$$
j^*c(E)=c\qty(\OO_X(E)|_D).
$$
Because $D$ and $E$ meet transversally,
$$
\OO_X(E)|_D
\cong
\OO_D\!\left(\sum_{P\in D\cap E}P\right),
$$
and the number of points in the sum is $D\cdot E$.

On a nonsingular projective curve, Exercise III.7.4 identifies
$H^1(D,\Omega_D)$ with $k$ by the trace and sends the logarithmic class of a
point to $1$. Since $c$ is a group homomorphism,
$$
\operatorname{tr}_D\qty(j^*c(E))
=
(D\cdot E)\cdot1.
$$
Step [](#s1){.pf-ref} now gives the displayed equality.

:::

:::

::: {.pf-step #s3}

Every divisor class on $X$ is a difference of classes of nonsingular
very ample curves, and two such representatives can be chosen to meet
transversally.

::: pf-proof

Fix a very ample divisor $H$. For an arbitrary divisor $A$, ampleness implies
that for $n\gg0$ the sheaf
$$
\OO_X(A+(n-1)H)
$$
is globally generated. By [[P-AGH275AMPLEPROPS]], part (d),
$$
\OO_X(A+nH)
=
\OO_X(H)\tensor\OO_X(A+(n-1)H)
$$
is then very ample. Thus
$$
A\sim A_1-A_2
$$
with $A_1$ and $A_2$ very ample.

Choose general members of the two very ample linear systems. Bertini's theorem
makes them nonsingular. Given finitely many such curves, choosing them
successively and generally also makes every pair needed below meet
transversally. Replacing a divisor by a linearly equivalent one changes
neither its logarithmic class nor its intersection numbers.

:::

:::

::: {.pf-step #s4}

For arbitrary divisors $D,E$ on $X$,
$$
\boxed{\langle c(D),c(E)\rangle=(D\cdot E)\cdot1}.
$$

::: pf-proof

By step [](#s3){.pf-ref}, write, up to linear equivalence,
$$
D=D_1-D_2,
\qquad
E=E_1-E_2,
$$
where the four curves are nonsingular and the required pairs meet
transversally. Both $c$ and the intersection pairing are additive in each
divisor. Bilinearity of the Serre pairing and step [](#s2){.pf-ref} therefore give
$$
\begin{aligned}
\langle c(D),c(E)\rangle
&=\sum_{i,j=1}^2(-1)^{i+j}
\langle c(D_i),c(E_j)\rangle\\
&=\sum_{i,j=1}^2(-1)^{i+j}(D_i\cdot E_j)\cdot1\\
&=(D\cdot E)\cdot1.
\end{aligned}
$$
This proves part (a).

:::

:::

::: {.pf-step #s5}

Assume $\operatorname{char}k=0$. There exist divisors
$E_1,\ldots,E_r$ such that
$$
c(E_1),\ldots,c(E_r)
$$
form a $k$-basis of the vector subspace of $V$ spanned by $c(\Pic X)$.

::: pf-proof

The vector space $V$ is finite-dimensional. Hence the subspace
$$
W=\operatorname{span}_k c(\Pic X)\subseteq V
$$
has finite dimension, say $r$. Since $W$ is spanned by elements of the image
of $c$, a basis can be extracted from that spanning set. Choose divisors
$E_1,\ldots,E_r$ representing the corresponding line bundles.

:::

:::

::: {.pf-step #s6}

The homomorphism
$$
\Phi:\Num X\longrightarrow\ZZ^r,
\qquad
[D]\longmapsto
\bigl(D\cdot E_1,\ldots,D\cdot E_r\bigr)
$$
is injective.

::: pf-proof

Intersection numbers depend only on numerical equivalence, so $\Phi$ is
well-defined and additive.

Suppose $\Phi([D])=0$. Step [](#s4){.pf-ref} gives
$$
\langle c(D),c(E_i)\rangle=0
\qquad(1\le i\le r).
$$
By step [](#s5){.pf-ref}, the classes $c(E_i)$ span every class $c(E)$ with
$E\in\Div X$. Hence
$$
\langle c(D),c(E)\rangle=0
$$
for every divisor $E$. Applying step [](#s4){.pf-ref} again yields
$$
(D\cdot E)\cdot1=0\in k
$$
for every $E$. Since $\operatorname{char}k=0$, the canonical map
$\ZZ\to k$ is injective, so
$$
D\cdot E=0
$$
as an integer for every divisor $E$. Thus $D$ is numerically equivalent to
zero, and $[D]=0$ in $\Num X$. Therefore $\Phi$ is injective.

:::

:::

::: {.pf-step #s7}

The group $\Num X$ is finitely generated and free abelian.

::: pf-proof

By step [](#s6){.pf-ref}, $\Num X$ is isomorphic to a subgroup of the finitely generated
free abelian group $\ZZ^r$. Every subgroup of a finitely generated free
abelian group is itself finitely generated free abelian. Hence
$$
\boxed{\Num X\text{ is a finitely generated free abelian group}.}
$$
This proves part (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a), and steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (b).

:::

:::

:::
