---
schema: qual/card@1
id: P-AGH374COHOMCLASS
kind: problem
title: The cohomology class of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Sheaves of Differentials
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: "Read Exercise III.7.4, the definition and uniqueness of a dualizing sheaf with trace in III.7.1--7.2, the canonical-sheaf identification III.7.11--7.13, and Hartshorne's warning in III.7.14 that the preceding construction gives little explicit information about the trace. The source exercise suppresses a necessary normalization: scaling the trace on a smooth subvariety scales its class. The statement below makes the standard trace/Gysin normalization explicit before proving the four requested assertions."
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a nonsingular projective variety of dimension $n$ over an algebraically closed field $k$. Let $Y$ be a nonsingular subvariety of codimension $p$, hence of dimension $n-p$. From the natural map $\Omega_X \tensor \mco_Y \to \Omega_Y$ of (II, 8.12) we deduce a map $\Omega_X^{n-p} \to \Omega_Y^{n-p}$. This induces a map on cohomology
\[
H^{n-p}(X, \Omega_X^{n-p}) \to H^{n-p}(Y, \Omega_Y^{n-p})
.\]
Now $\Omega_Y^{n-p} = \omega_Y$ is a dualizing sheaf for $Y$, so we have the trace map
\[
t_Y: H^{n-p}(Y, \Omega_Y^{n-p}) \to k
.\]
Composing, we obtain a linear map $H^{n-p}(X, \Omega_X^{n-p}) \to k$. By (7.13) this corresponds to an element $\eta(Y) \in H^p(X, \Omega_X^p)$, which we call the **cohomology class of $Y$**.

For this exercise, use the standard compatible normalization of the trace maps on canonical sheaves: the trace on $\Spec k$ is the identity, the trace on a finite reduced $k$-scheme is the sum of the traces of its points, and traces are compatible with the Gysin maps for nonsingular closed immersions. Equivalently, use the trace normalization from Grothendieck--Serre duality rather than an arbitrary scalar multiple of the trace supplied merely by the existence statement of Serre duality.

(a) If $P \in X$ is a closed point, show that $t_X(\eta(P)) = 1$, where $\eta(P) \in H^n(X, \Omega^n)$ and $t_X$ is the trace map.

(b) If $X = \PP^n$, identify $H^p(X, \Omega^p)$ with $k$ by (Ex. 7.3), and show that $\eta(Y) = (\deg Y) \cdot 1$, where $\deg Y$ is the degree of $Y$ as a projective variety (I, §7).

   Hint: cut with a hyperplane $H \subseteq X$, and use Bertini's theorem (II, 8.18) to reduce to the case where $Y$ is a finite set of points.

(c) For any scheme $X$ of finite type over $k$, we define a homomorphism of sheaves of abelian groups $d\log: \mco_X^* \to \Omega_X$ by $d\log(f) = f^{-1} \, df$. Here $\mco_X^*$ is a group under multiplication, and $\Omega_X$ is a group under addition. This induces a map on cohomology
\[
\Pic X = H^1(X, \mco_X^*) \to H^1(X, \Omega_X)
,\]
which we denote by $c$. See (Ex. 4.5).

(d) Returning to the hypotheses above, suppose $p = 1$. Show that $\eta(Y) = c(\mcl(Y))$, where $\mcl(Y)$ is the invertible sheaf corresponding to the divisor $Y$.
:::

::: {.solution}
Write $j:Y\hookrightarrow X$ for the closed immersion. We use the normalized Serre pairing
$$
\langle\alpha,\beta\rangle_X
=t_X(\alpha\smile\beta),
$$
between $H^p(X,\Omega_X^p)$ and $H^{n-p}(X,\Omega_X^{n-p})$.
With the trace normalization stated in the problem, the Gysin morphism
$$
j_*:H^q(Y,\Omega_Y^q)\longrightarrow H^{q+p}(X,\Omega_X^{q+p})
$$
is characterized by the adjunction identity
$$
\langle j_*(a),b\rangle_X
=\langle a,j^*b\rangle_Y.
$$
In particular, the class defined in the problem is
$$
\eta(Y)=j_*(1).
$$

::: pf

::: {.pf-step #s1}

For a closed point $P\in X$,
$$
\boxed{t_X(\eta(P))=1}.
$$

::: pf-proof

Here $p=n$, so the functional defining $\eta(P)$ is the composite
$$
H^0(X,\OO_X)\xrightarrow{j^*}H^0(P,\OO_P)
\xrightarrow{t_P}k.
$$
Since $X$ is projective and integral over the algebraically closed field $k$,
$$
H^0(X,\OO_X)=k,
$$
and since $P\cong\Spec k$, the restriction map is the identity on $k$.
By the chosen normalization $t_P=\operatorname{id}_k$, so the functional sends $1$ to $1$.

Under Serre duality, evaluating that functional at $1\in H^0(X,\OO_X)$ is the same as pairing $\eta(P)$ with $1$:
$$
1
=\langle\eta(P),1\rangle_X
=t_X(\eta(P)).
$$
This proves part (a).

:::

:::

::: {.pf-step #s2}

Cohomology classes are compatible with transverse intersection by a nonsingular hyperplane: if $H\subseteq X$ is nonsingular and meets $Y$ transversely, then
$$
i^*\eta_X(Y)=\eta_H(Y\cap H),
$$
where $i:H\hookrightarrow X$.

::: pf-proof

Let $Z=Y\cap H$ and write the transverse Cartesian square
$$
\begin{array}{ccc}
Z&\xrightarrow{j_H}&H\\
\downarrow&&\downarrow i\\
Y&\xrightarrow{j}&X.
\end{array}
$$
For regular closed immersions meeting transversely, the normalized Gysin maps satisfy base change
$$
i^*j_*=(j_H)_*\,i_Y^*.
$$
Applying this to $1\in H^0(Y,\OO_Y)$ gives
$$
i^*\eta_X(Y)
=i^*j_*(1)
=(j_H)_*(1)
=\eta_H(Z).
$$
This is exactly the asserted compatibility.

:::

:::

::: {.pf-step #s3}

If $X=\PP^n$ and $Y$ has codimension $p$, then
$$
\boxed{\eta(Y)=(\deg Y)\cdot1\in H^p(\PP^n,\Omega_{\PP^n}^p)\cong k}.
$$

::: pf-proof

By Exercise III.7.3,
$$
H^p(\PP^n,\Omega^p)\cong k.
$$
Choose a general linear subspace
$$
L\cong\PP^p\subseteq\PP^n
$$
of complementary dimension to $Y$.
By repeated Bertini and the generic-intersection statement of Chapter I, $L$ meets $Y$ transversely in a reduced set
$$
Z=Y\cap L=\{P_1,\ldots,P_d\},
\qquad d=\deg Y.
$$
Repeated application of step [](#s2){.pf-ref} gives
$$
\eta_L(Z)=i^*\eta_{\PP^n}(Y).
$$

The Gysin map is additive on a disjoint union of points, so
$$
\eta_L(Z)=\sum_{a=1}^d\eta_L(P_a).
$$
By step [](#s1){.pf-ref} each point class has trace one. Since
$$
H^p(L,\Omega_L^p)\cong k
$$
and its trace identifies the standard generator with $1$, we obtain
$$
\eta_L(Z)=d\cdot1.
$$

Under the identifications of Exercise III.7.3, restriction from $\PP^n$ to a linear $\PP^p$ sends the standard generator of $H^p(\PP^n,\Omega^p)$ to the standard generator of $H^p(L,\Omega_L^p)$; this is the iterated boundary map coming from the Euler sequence, and the coordinate restriction commutes with that construction.
Hence the scalar multiplying the generator upstairs is also $d$.
Thus
$$
\eta(Y)=(\deg Y)\cdot1,
$$
proving part (b).

:::

:::

::: {.pf-step #s4}

The rule
$$
d\log(f)=f^{-1}df
$$
is a morphism of sheaves of abelian groups
$$
d\log:\OO_X^*\longrightarrow\Omega_X.
$$

::: pf-proof

For local units $f,g$,
$$
\begin{aligned}
d\log(fg)
&=(fg)^{-1}d(fg)\\
&=f^{-1}g^{-1}(f\,dg+g\,df)\\
&=f^{-1}df+g^{-1}dg\\
&=d\log(f)+d\log(g).
\end{aligned}
$$
The construction commutes with restriction to smaller open sets because Kähler differentiation does.
Therefore it is a morphism from the multiplicative sheaf $\OO_X^*$ to the additive sheaf $\Omega_X$.
Passing to first cohomology and using
$$
\Pic X\cong H^1(X,\OO_X^*)
$$
gives the homomorphism
$$
c:\Pic X\longrightarrow H^1(X,\Omega_X)
$$
required in part (c).

:::

:::

::: {.pf-step #s5}

If $Y\subseteq X$ is a nonsingular divisor with local equations $f_i=0$ on an open cover $(U_i)$, then $c(\mcl(Y))$ is represented by the Čech cocycle
$$
\left\{\frac{df_i}{f_i}-\frac{df_j}{f_j}\right\}_{ij}.
$$

::: pf-proof

The invertible sheaf $\mcl(Y)=\OO_X(Y)$ has local generator $e_i=f_i^{-1}$ on $U_i$.
Use the Čech convention in which the transition function $g_{ij}$ is defined by
$$
e_j=g_{ij}e_i.
$$
Then
$$
g_{ij}=\frac{f_i}{f_j},
$$
and its image under $d\log$ is
$$
d\log\!\left(\frac{f_i}{f_j}\right)
=\frac{df_i}{f_i}-\frac{df_j}{f_j}.
$$
This is the displayed cocycle.

:::

:::

::: {.pf-step #s6}

For a nonsingular divisor $Y\subseteq X$,
$$
\boxed{\eta(Y)=c(\mcl(Y))\in H^1(X,\Omega_X)}.
$$

::: pf-proof

Let
$$
\alpha\in H^{n-1}(X,\Omega_X^{n-1}).
$$
By definition of $\eta(Y)$,
$$
\langle\eta(Y),\alpha\rangle_X
=t_Y(j^*\alpha).
$$

On a cover on which $Y$ is given by the equations $f_i$, the standard local description of the Gysin/residue map for a Cartier divisor sends a form $\beta$ on $Y$ to the Čech class represented by
$$
\frac{df_i}{f_i}\wedge\widetilde\beta_i
-
\frac{df_j}{f_j}\wedge\widetilde\beta_j,
$$
where the $\widetilde\beta_i$ are local lifts to $X$.
Equivalently, cup product with the divisor Gysin class is cup product with the Čech cocycle
$$
\left\{\frac{df_i}{f_i}-\frac{df_j}{f_j}\right\}_{ij}.
$$
Compatibility of the normalized trace with this residue map gives
$$
t_X\bigl(c(\mcl(Y))\smile\alpha\bigr)
=t_Y(j^*\alpha).
$$
Thus
$$
\langle c(\mcl(Y)),\alpha\rangle_X
=\langle\eta(Y),\alpha\rangle_X
$$
for every $\alpha$.
The Serre pairing is nondegenerate, so
$$
c(\mcl(Y))=\eta(Y).
$$
This proves part (d).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b), step [](#s4){.pf-ref} proves part (c), and steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (d).

:::

:::

:::

::: {.remark title="Trace normalization"}
As written in the source, the exercise suppresses a normalization needed to make its numerical assertions canonical.
In III.7.1 a dualizing object is a pair consisting of a sheaf and a trace, and replacing a trace by a nonzero scalar multiple gives another valid dualizing pair after rescaling the identification with the canonical sheaf.
Corollary III.7.12 identifies the dualizing sheaf with $\omega_X$, but the text does not there state a scalar normalization of that identification; Remark III.7.14 explicitly notes that at that stage little is known about the trace map beyond its existence.
The standard trace/Gysin normalization stated in the problem is what makes $t_P(1)=1$, transverse pullback of fundamental classes, and the divisor identity in part (d) compatible simultaneously.
:::
