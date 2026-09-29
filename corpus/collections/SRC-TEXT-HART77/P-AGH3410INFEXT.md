---
schema: qual/card@1
id: P-AGH3410INFEXT
kind: problem
title: Infinitesimal extensions classified by $H^1$ of the twisted tangent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Infinitesimal Extensions
  - Tangent Sheaf
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the classification and both hints with the retained Hartshorne Chapter III section 4 transcription. Read the affine splitting and square-zero derivation proofs. The solution specifies isomorphisms of extensions over the fixed quotient and kernel, constructs their transition cocycles and inverse gluing, and identifies derivations with F tensor the tangent sheaf.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a nonsingular variety over an algebraically closed field $k$, and let $\mcf$ be a coherent sheaf on $X$.
Show that there is a one-to-one correspondence between the set of infinitesimal extensions of $X$ by $\mcf$ (II, Ex. 8.7) up to isomorphism of extensions, and the group $H^1(X,\mcf\tensor\mct)$, where $\mct$ is the tangent sheaf of $X$, see (II, §8).
An extension here includes its identification of the quotient with $X$ and its square-zero ideal with $\mcf$; an isomorphism of extensions induces the identity on both $X$ and the identified sheaf $\mcf$.
:::

::: {.hint}
Use (II, Ex. 8.6) and Theorem III.4.5.
:::

::: {.solution}
Write $\mathcal T=\sheafhom_{\OO_X}(\Omega_{X/k},\OO_X)$ and
$$
\mathcal D=\sheafhom_{\OO_X}(\Omega_{X/k},\mcf).
$$
Regard an extension as a sheaf of $k$-algebras $\mathcal A$ on the underlying space of $X$, with an exact sequence
$$
0\longrightarrow\mcf\xrightarrow{\iota}\mathcal A\xrightarrow{\rho}\OO_X\longrightarrow0,
$$
where $\iota(\mcf)$ is an ideal of square zero and its induced quotient-module structure is the given one on $\mcf$.
This is legitimate because a nilpotent closed immersion is a homeomorphism on the underlying spaces.
The ringed space $(X,\mathcal A)$ is required to be a scheme, as in [[P-AGH287INFEXT]].

::: pf

::: {.pf-step #s1}

The abelian sheaf $\mathcal D$ is the sheaf of $k$-derivations $\OO_X\to\mcf$, and there is a natural isomorphism $\mathcal D\cong\mcf\otimes\mathcal T$.

::: pf-proof

The universal property of [[D-4GCH6|Kähler differentials]] identifies a sheaf morphism $\Omega_{X/k}\to\mcf$ with its composite with the universal derivation.
This works on every open subset and commutes with restriction, giving the first assertion.
Since $X$ is nonsingular over the algebraically closed field, $\Omega_{X/k}$ is locally free of finite rank [@Har10a, Theorem II.8.15].
For a finite locally free sheaf $E$, the evaluation map $\mcf\otimes E^\vee\to\sheafhom(E,\mcf)$ is an isomorphism, as is checked in a local basis.
Apply this with $E=\Omega_{X/k}$ to obtain the stated isomorphism.
In particular $\mathcal D$ is coherent.

:::

:::

::: {.pf-step #s2}

The automorphisms of the split extension $\OO_X\oplus\mcf$ that fix the quotient and kernel are exactly
$$
u_D(a,v)=(a,v+D(a)),\qquad D\in\mathcal D(X),
$$
and the same description holds over every open subset.

::: pf-proof

The split multiplication is $(a,v)(b,w)=(ab,aw+bv)$.
An additive map inducing the identity on both the quotient and the kernel must have the displayed form for a unique additive map $D:\OO_X\to\mcf$.
Being a $k$-algebra homomorphism requires $D$ to annihilate $k$ and satisfy
$$
D(ab)=aD(b)+bD(a).
$$
Conversely, these conditions make the displayed map multiplicative and unital, by expanding the two products and using the square-zero ideal, as in [[P-AGH286INFLIFT]], part (a).
It has inverse $u_{-D}$.
Composition satisfies $u_Du_E=u_{D+E}$, proving the identification with the additive derivation sheaf.
All formulas commute with restriction.

:::

:::

::: {.pf-step #s3}

Each extension determines a well-defined class in $H^1(X,\mathcal D)$.

::: pf-proof

Choose a finite affine open cover $\mathfrak U=(U_i)$ of $X$.
The affine splitting theorem [[P-AGH287INFEXT]], proved from infinitesimal lifting in [[P-AGH286INFLIFT]], gives isomorphisms of identified extensions
$$
\theta_i:(\OO_X\oplus\mcf)|_{U_i}\xrightarrow{\cong}\mathcal A|_{U_i}.
$$
On each overlap, step [](#s2){.pf-ref} writes the transition uniquely as
$$
\theta_i^{-1}\theta_j=u_{D_{ij}},\qquad D_{ij}\in\mathcal D(U_i\cap U_j).
$$
The identity $\theta_i^{-1}\theta_j\theta_j^{-1}\theta_h=\theta_i^{-1}\theta_h$ gives $D_{ij}+D_{jh}=D_{ih}$, so these sections form a Čech one-cocycle.

Replacing $\theta_i$ by $\theta_i u_{b_i}$ changes this cocycle to $D_{ij}+b_j-b_i$.
It therefore changes it by a Čech coboundary.
An isomorphism of extensions, composed with all the $\theta_i$, gives the same cocycle for the other extension.
Thus its Čech class depends only on the extension isomorphism class.
The scheme $X$ is noetherian and separated, and $\mathcal D$ is quasi-coherent, so the affine-cover comparison identifies this class with an element of $H^1(X,\mathcal D)$ [@Har10a, Theorem III.4.5].
Refining the cover restricts the cocycle, and the comparison commutes with refinement by [[P-AGH344REFINEMENTH1]], part (b).
Hence the cohomology class is also independent of the cover.

:::

:::

::: {.pf-step #s4}

Every class in $H^1(X,\mathcal D)$ is obtained by gluing split extensions, and the glued object is a scheme.

::: pf-proof

Use the same finite affine cover.
By the affine-cover comparison, represent the class by a Čech cocycle $(D_{ij})$.
Glue the sheaves of $k$-algebras $(\OO_X\oplus\mcf)|_{U_i}$ using the maps $u_{D_{ij}}$ from the $j$th chart to the $i$th chart.
Their composition rule in step [](#s2){.pf-ref} and the cocycle identity give the required gluing identities.
Explicitly, the resulting sheaf consists of local tuples whose components satisfy $s_i=u_{D_{ij}}(s_j)$ on overlaps.
It restricts on each $U_i$ to that split extension.

On an affine $U_i=\Spec A_i$ with $\mcf|_{U_i}=\widetilde{M_i}$, the split ringed space is $\Spec(A_i\oplus M_i)$ with the square-zero multiplication.
This was proved by localization in [[P-AGH287INFEXT]], step [](#s1){.pf-ref}.
Thus the glued ringed space is locally a scheme and is a scheme.
Every transition fixes the quotient and the kernel, so the quotient maps glue to $\rho$ and the kernel inclusions glue to the specified identification with $\mcf$.
Its kernel is square-zero and has the required module structure, as can be checked on each chart.
It is an extension of the desired kind, and its class from step [](#s3){.pf-ref} is the original class.

:::

:::

::: {.pf-step #s5}

Two extensions determine the same cohomology class exactly when they are isomorphic as identified extensions.

::: pf-proof

Both extensions split on every member of the fixed affine cover by the same affine splitting theorem.
If their cohomology classes agree, the affine-cover comparison is injective, so their cocycles differ by a coboundary on that cover.
Write $D'_{ij}=D_{ij}+b_j-b_i$.
The local maps $u_{-b_i}$ identify the corresponding gluings: on an overlap they satisfy
$$
u_{-b_i}u_{D_{ij}}=u_{D'_{ij}}u_{-b_j}.
$$
They therefore glue to an isomorphism of sheaves of $k$-algebras fixing the quotient and kernel, hence to an isomorphism of extensions.
Conversely, such an isomorphism preserves the class by step [](#s3){.pf-ref}.
This proves injectivity of the classification, while step [](#s4){.pf-ref} proves surjectivity.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} give a bijection between extension isomorphism classes and $H^1(X,\mathcal D)$.
Step [](#s1){.pf-ref} identifies the latter with $H^1(X,\mcf\otimes\mathcal T)$, proving the stated correspondence.
The zero cocycle glues the split extension by identity maps and therefore corresponds to the trivial extension.

:::

:::

:::

::: {.remark title="Forgetting the kernel identification changes the classification"}
For an automorphism $v$ of $\mcf$, the map $(a,m)\mapsto(a,v(m))$ conjugates $u_D$ to $u_{v\circ D}$.
Thus forgetting the identification of the kernel with $\mcf$, while fixing $X$, identifies classes under the induced action of $\Aut_{\OO_X}(\mcf)$.
For example, on $X=\PP_k^1$ with $\mcf=\OO(-4)$, one has $\mathcal T\cong\OO(2)$ and $H^1(X,\mcf\otimes\mathcal T)\cong H^1(\PP_k^1,\OO(-2))\cong k$ [@Har10a, Example II.8.20.1 and Theorem III.5.1].
Scalar automorphisms of $\mcf$ identify distinct nonzero scalar multiples of a class when the kernel identification is forgotten.
The correspondence proved here retains that identification, as required for isomorphisms of extensions.
:::
