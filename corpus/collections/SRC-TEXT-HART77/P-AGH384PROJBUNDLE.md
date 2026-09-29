---
schema: qual/card@1
id: P-AGH384PROJBUNDLE
kind: problem
title: Cohomology of a projective bundle and geometrically ruled surfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Higher Direct Images
  - Projective Bundles
  - Relative Canonical Sheaf
  - Ruled Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.8.4, Theorem III.5.1 on projective-space cohomology over a noetherian ring, Proposition III.8.1, and the projective-bundle and differential inputs II.7.11 and II.8.13. The source states p_a and p_g in part (d) while assuming only a noetherian base; the statement below makes explicit the nonsingular projective-variety hypotheses under which those invariants are defined at this point in Hartshorne.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a noetherian scheme, and let $\mce$ be a locally free $\mco_Y\dash$module of rank $n+1$, with $n \geq 1$.
Let $X = \PP(\mce)$ (II, §7), with the invertible sheaf $\mco_X(1)$ and the projection morphism $\pi: X \to Y$.

a. Show that:

   - $\pi_*(\mco(l)) \cong \operatorname{Sym}^l(\mce)$ for $l \geq 0$, and $\pi_*(\mco(l)) = 0$ for $l < 0$ (II, 7.11);

   - $R^i \pi_*(\mco(l)) = 0$ for $0 < i < n$ and all $l \in \ZZ$; and

   - $R^n \pi_*(\mco(l)) = 0$ for $l > -n-1$.

b. Show there is a natural exact sequence
\[
0 \to \Omega_{X/Y} \to (\pi^* \mce)(-1) \to \mco \to 0
,\]
cf. (II, 8.13), and conclude that the **relative canonical sheaf** $\omega_{X/Y} = \wedge^n \Omega_{X/Y}$ is isomorphic to $(\pi^* \wedge^{n+1} \mce)(-n-1)$. Show furthermore that there is a natural isomorphism $R^n \pi_*(\omega_{X/Y}) \cong \mco_Y$ (cf. (7.1.1)).

(c) Now show, for any $l \in \ZZ$, that \[ R^n \pi_*(\mco(l)) \cong \pi_*\dualof{(\mco(-l-n-1))} \tensor \dualof{(\wedge^{n+1} \mce)}
.\]

(d) Assume additionally that $Y$ is a nonsingular projective variety over an algebraically closed field $k$.
    Show that $p_a(X) = (-1)^n p_a(Y)$ (use (Ex.
    8.1)) and $p_g(X) = 0$ (use (II, 8.11)).

(e) In particular, if $Y$ is a nonsingular projective curve of genus $g$, and $\mce$ a locally free sheaf of rank $2$, then $X$ is a projective surface with $p_a = -g$, $p_g = 0$, and irregularity $g$ (7.12.3). This kind of surface is called a **geometrically ruled surface** (V, §2).
:::

::: {.solution}
Write
$$
D=\det\mce=\bigwedge^{n+1}\mce.
$$
All statements in parts (a)--(c) are local on $Y$, so we repeatedly use affine open subsets $U=\Spec A$ on which $\mce|_U\cong\OO_U^{n+1}$; then
$$
\pi^{-1}(U)\cong\PP_A^n.
$$

::: pf

::: {.pf-step #s1}

For every $l\in\ZZ$,
$$
\pi_*\OO_X(l)\cong
\begin{cases}
\operatorname{Sym}^l\mce,&l\ge0,\\
0,&l<0,
\end{cases}
$$
and
$$
R^i\pi_*\OO_X(l)=0
$$
for $0<i<n$ and every $l$, and for $i=n$ whenever $l>-n-1$.

::: pf-proof

The formula for $\pi_*\OO_X(l)$ is Hartshorne II.7.11 with the convention
$$
X=\PP(\mce)=\underline{\operatorname{Proj}}_Y(\operatorname{Sym}\mce).
$$

For the higher direct images, Proposition III.8.1 says that $R^i\pi_*\OO_X(l)$ is associated to the presheaf
$$
U\longmapsto H^i(\pi^{-1}(U),\OO_X(l)|_{\pi^{-1}(U)}).
$$
On an affine trivializing open $U=\Spec A$, this is
$$
H^i(\PP_A^n,\OO_{\PP_A^n}(l)).
$$
Theorem III.5.1 gives
$$
H^i(\PP_A^n,\OO(l))=0
$$
for $0<i<n$ and all $l$, and also for $i=n$ when $l>-n-1$.
Since such trivializing affine opens form a basis of $Y$, the corresponding higher-direct-image sheaves vanish.
This proves part (a).

:::

:::

::: {.pf-step #s2}

There is a natural relative Euler sequence
$$
\boxed{
0\longrightarrow\Omega_{X/Y}
\longrightarrow(\pi^*\mce)(-1)
\longrightarrow\OO_X
\longrightarrow0}.
$$

::: pf-proof

Hartshorne II.7.11 gives the universal quotient
$$
\pi^*\mce\twoheadrightarrow\OO_X(1).
$$
Tensoring by $\OO_X(-1)$ gives a surjection
$$
(\pi^*\mce)(-1)\twoheadrightarrow\OO_X.
$$
Let its kernel be $\mck$.
On every affine trivializing open $U\subseteq Y$, the restriction to
$$
\pi^{-1}(U)\cong\PP_U^n
$$
is the usual Euler sequence for relative projective space from II.8.13, whose kernel is $\Omega_{\PP_U^n/U}$.
These local identifications are natural under change of trivialization and therefore glue, giving
$$
\mck\cong\Omega_{X/Y}.
$$

:::

:::

::: {.pf-step #s3}

The relative canonical sheaf is
$$
\boxed{
\omega_{X/Y}=\bigwedge^n\Omega_{X/Y}
\cong(\pi^*D)(-n-1)}.
$$

::: pf-proof

In step [](#s2){.pf-ref}, the middle term has rank $n+1$ and the quotient has rank one.
Taking determinants in the short exact sequence gives
$$
\det\Omega_{X/Y}
\cong
\det\bigl((\pi^*\mce)(-1)\bigr).
$$
For a rank-$(n+1)$ bundle,
$$
\det\bigl((\pi^*\mce)(-1)\bigr)
\cong
\pi^*(\det\mce)\otimes\OO_X(-1)^{\otimes(n+1)}.
$$
Thus
$$
\omega_{X/Y}\cong(\pi^*D)(-n-1).
$$

:::

:::

::: {.pf-step #s4}

There is a natural trace isomorphism
$$
\boxed{R^n\pi_*\omega_{X/Y}\cong\OO_Y}.
$$

::: pf-proof

On a trivializing affine open $U=\Spec A$, step [](#s3){.pf-ref} identifies
$$
\omega_{X/Y}|_{\pi^{-1}(U)}
\cong
\OO_{\PP_A^n}(-n-1)\otimes_A D(U).
$$
Theorem III.5.1 gives the canonical top-cohomology trace
$$
H^n(\PP_A^n,\OO(-n-1))\cong A,
$$
represented in the standard Čech cover by the class of
$$
(x_0x_1\cdots x_n)^{-1}.
$$
If the frame of $\mce$ changes by a matrix $M\in\operatorname{GL}_{n+1}(A)$, the projective coordinates change by $M$, and this top Čech class changes by $(\det M)^{-1}$.
The local generator of $D=\det\mce$ changes by $\det M$.
Hence the two factors cancel.
The local identifications
$$
R^n\pi_*\omega_{X/Y}|_U\cong\OO_U
$$
therefore agree on overlaps and glue to a natural global isomorphism.
This proves the last assertion of part (b).

:::

:::

::: {.pf-step #s5}

Put $m=-l-n-1$.
Multiplication of twists and the trace of step [](#s4){.pf-ref} give a natural pairing
$$
\pi_*\OO_X(m)\otimes R^n\pi_*\OO_X(l)
\longrightarrow D^\vee.
$$

::: pf-proof

Multiplication of sections gives
$$
\OO_X(m)\otimes\OO_X(l)\longrightarrow\OO_X(-n-1).
$$
Step [](#s3){.pf-ref} and the projection formula [[P-AGH383PROJFORMULA|from Exercise III.8.3]] yield
$$
R^n\pi_*\omega_{X/Y}
\cong
R^n\pi_*\OO_X(-n-1)\otimes D.
$$
Combining with step [](#s4){.pf-ref} gives
$$
R^n\pi_*\OO_X(-n-1)\cong D^\vee.
$$
Pushing forward the multiplication map and then using this identification produces the displayed pairing.

:::

:::

::: {.pf-step #s6}

The pairing of step [](#s5){.pf-ref} is perfect, and therefore for every $l\in\ZZ$,
$$
\boxed{
R^n\pi_*\OO_X(l)
\cong
\bigl(\pi_*\OO_X(-l-n-1)\bigr)^\vee\otimes D^\vee}.
$$

::: pf-proof

The assertion is local on $Y$.
Over a trivializing affine open $U=\Spec A$, it becomes the standard pairing
$$
H^0(\PP_A^n,\OO(m))
\otimes_A
H^n(\PP_A^n,\OO(-m-n-1))
\longrightarrow
H^n(\PP_A^n,\OO(-n-1))\cong A.
$$
Theorem III.5.1 describes these modules by monomials and shows that this pairing is perfect: a degree-$m$ monomial is paired with the unique complementary negative monomial whose product is $(x_0\cdots x_n)^{-1}$.

If $m<0$, the left $H^0$ vanishes and step [](#s1){.pf-ref} gives the corresponding top-cohomology vanishing, so the statement remains valid.
The perfect local pairings are exactly the restrictions of the global pairing in step [](#s5){.pf-ref}, hence glue to the asserted sheaf isomorphism.
This proves part (c).

:::

:::

::: {.pf-step #s7}

Under the hypotheses of part (d),
$$
\boxed{p_a(X)=(-1)^n p_a(Y)}.
$$

::: pf-proof

Step [](#s1){.pf-ref} with $l=0$ gives
$$
\pi_*\OO_X=\OO_Y,
\qquad
R^i\pi_*\OO_X=0\quad(i>0).
$$
Indeed the intermediate groups vanish by step [](#s1){.pf-ref}, and the top group vanishes because $0>-n-1$.
Exercise III.8.1 therefore gives natural isomorphisms
$$
H^i(X,\OO_X)\cong H^i(Y,\OO_Y)
$$
for every $i$.
Hence
$$
\chi(\OO_X)=\chi(\OO_Y).
$$

Let $m=\dim Y$, so $\dim X=m+n$.
For a projective variety $V$,
$$
p_a(V)=(-1)^{\dim V}\bigl(\chi(\OO_V)-1\bigr).
$$
Therefore
$$
\begin{aligned}
p_a(X)
&=(-1)^{m+n}(\chi(\OO_X)-1)\\
&=(-1)^n(-1)^m(\chi(\OO_Y)-1)\\
&=(-1)^n p_a(Y).
\end{aligned}
$$

:::

:::

::: {.pf-step #s8}

Under the hypotheses of part (d),
$$
\boxed{p_g(X)=0}.
$$

::: pf-proof

Since $Y$ is nonsingular and $\pi$ is a projective-space bundle, $X$ is nonsingular.
The exact sequence of differentials for the smooth morphism $\pi$ is
$$
0\longrightarrow\pi^*\Omega_Y
\longrightarrow\Omega_X
\longrightarrow\Omega_{X/Y}
\longrightarrow0.
$$
Taking determinants gives
$$
\omega_X\cong\pi^*\omega_Y\otimes\omega_{X/Y}.
$$
By step [](#s3){.pf-ref},
$$
\omega_X
\cong
\pi^*(\omega_Y\otimes D)\otimes\OO_X(-n-1).
$$
The ordinary projection formula and step [](#s1){.pf-ref} give
$$
\pi_*\omega_X
\cong
(\omega_Y\otimes D)\otimes\pi_*\OO_X(-n-1)
=0.
$$
Thus
$$
H^0(X,\omega_X)
=H^0(Y,\pi_*\omega_X)=0,
$$
so $p_g(X)=0$.

:::

:::

::: {.pf-step #s9}

If $Y$ is a nonsingular projective curve of genus $g$ and $\operatorname{rk}\mce=2$, then $X$ is a geometrically ruled surface with
$$
\boxed{p_a(X)=-g,\qquad p_g(X)=0,\qquad q(X)=g}.
$$

::: pf-proof

Here $n=1$, so $\dim X=2$.
The morphism $\pi:X\to Y$ is projective, and $Y$ is projective over $k$, hence $X$ is projective.
It is nonsingular because it is locally $\PP^1$ over the nonsingular curve $Y$.

For a nonsingular projective curve,
$$
p_a(Y)=g.
$$
Step [](#s7){.pf-ref} therefore gives
$$
p_a(X)=-g,
$$
while step [](#s8){.pf-ref} gives $p_g(X)=0$.
For a nonsingular projective surface, Remark III.7.12.3 gives
$$
q=p_g-p_a.
$$
Hence
$$
q(X)=0-(-g)=g.
$$
This is the asserted geometrically ruled surface.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (b), steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (c), steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (d), and step [](#s9){.pf-ref} proves part (e).

:::

:::

:::

::: {.remark title="Scope of the genus assertions"}
The source states part (d) after assuming only that $Y$ is noetherian, but at this point in Hartshorne the invariants $p_a$ and $p_g$ used there are invariants of projective varieties, and the formula for $p_g$ uses nonsingularity.
The additional hypothesis stated in part (d) is therefore necessary for the literal assertions made there; parts (a)--(c) retain the source's original noetherian-base generality.
:::
