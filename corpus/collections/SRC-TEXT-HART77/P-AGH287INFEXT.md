---
schema: qual/card@1
id: P-AGH287INFEXT
kind: problem
title: Infinitesimal extensions of a scheme by a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Deformation Theory
  - Coherent Sheaves
  - Nilpotent Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the extension data, trivial multiplication and affine nonsingular conclusion with the retained Hartshorne II.8.7 transcription. The proof first constructs the trivial scheme on affine charts, then lifts the identity on global sections and localizes the splitting; it does not assume that the given thickening is affine or that its structure sheaf already has an O_X-module structure.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
As an application of the infinitesimal lifting property, consider the following general problem.
Let $k$ be algebraically closed, let $X$ be a scheme of finite type over $k$, and let $\mcf$ be a coherent sheaf on $X$.
We seek to classify schemes $X'$ over $k$ which have a sheaf of ideals $\mci$ such that $\mci^2 = 0$ and $(X', \OO_{X'}/\mci) \cong (X, \OO_X)$, and such that $\mci$ with its resulting structure of $\OO_X\dash$module is isomorphic to the given sheaf $\mcf$.
Such a pair $X', \mci$ is called an **infinitesimal extension of the scheme $X$ by the sheaf $\mcf$**.

One such extension, the trivial one, is obtained as follows.
Take $\OO_{X'} = \OO_X \oplus \mcf$ as sheaves of abelian groups, and define multiplication by
$$
(a \oplus f) \cdot (a' \oplus f') = aa' \oplus (af' + a'f)
.
$$
Then the topological space $X$ with the sheaf of rings $\OO_{X'}$ is an infinitesimal extension of $X$ by $\mcf$.

The general problem of classifying extensions of $X$ by $\mcf$ can be quite complicated.
So for now, just prove the following special case: if $X$ is affine and nonsingular, then any extension of $X$ by a coherent sheaf $\mcf$ is isomorphic to the trivial one.
See (III, Ex. 4.10) for another case.
:::

::: {.solution}
Fix the identification $\OO_{X'}/\mathcal I\cong\OO_X$ and an $\OO_X$-linear identification $\mathcal I\cong\mcf$.
Since $\mathcal I$ is nilpotent, every prime ideal contains it, so the closed immersion $X\hookrightarrow X'$ is a homeomorphism on underlying spaces.
We therefore regard all the sheaves as sheaves on the same topological space $X$.

::: pf

::: {.pf-step #s1}

The ringed space with structure sheaf $\OO_X\oplus\mcf$ and the given multiplication is a scheme and an infinitesimal extension of $X$ by $\mcf$.

::: pf-proof

On an affine open $U=\Spec A\subseteq X$, write $\mcf|_U=\widetilde M$ for a finite $A$-module $M$.
Define the ring $A\oplus M$ with unit $(1,0)$ and multiplication
$$
(a,m)(b,n)=(ab,an+bm).
$$
For $(a,m),(b,n),(c,p)\in A\oplus M$, either parenthesization of their product has module component $abp+acn+bcm$, proving associativity.
The subset $0\oplus M$ is an ideal of square zero, with quotient $A$.
Consequently $\Spec(A\oplus M)$ has underlying space $\Spec A$.
For $a\in A$, localization at $(a,0)$ gives
$$
(A\oplus M)_{(a,0)}\cong A_a\oplus M_a
$$
with the same multiplication; the inverse of $(a,0)$ is $(a^{-1},0)$ in the right-hand ring.
Thus the structure sheaf on this spectrum is exactly $\OO_U\oplus\widetilde M$.
These descriptions agree on open overlaps, since their multiplication is defined by the global $\OO_X$-module structure on $\mcf$.
They prove that the stated ringed space is a scheme, with the required ideal, quotient and module identification.

:::

:::

::: {.pf-step #s2}

If $X=\Spec A$ is affine and nonsingular, the quotient map on global sections admits a $k$-algebra section.

::: pf-proof

The extension gives an exact sequence of sheaves of abelian groups
$$
0\longrightarrow\mcf\longrightarrow\OO_{X'}\xrightarrow{\rho}\OO_X\longrightarrow0.
$$
The group $H^1(X,\mcf)$ vanishes by [[T-COHAFF|affine vanishing]] [@Har10a, Theorem III.3.5].
The long exact sequence therefore gives a surjective ring homomorphism
$$
B'\coloneqq\Gamma(X,\OO_{X'})\twoheadrightarrow A,
$$
whose kernel is $M=\Gamma(X,\mcf)$ and satisfies $M^2=0$.
This step only uses cohomology of abelian sheaves; no $\OO_X$-module structure on $\OO_{X'}$ has been assumed.

Apply [[P-AGH286INFLIFT|infinitesimal lifting]] to the identity map $A\to A$ and the square-zero extension $B'\to A$.
It gives a $k$-algebra map $s:A\to B'$ with $\rho s=\id_A$.
The proof of that lifting result also covers a nonsingular affine scheme with several components: its conormal sequence is exact and its differential module is finite projective, which are the only smoothness properties used there.
Thus the argument does not require $X$ to be irreducible.
For $X=\varnothing$, the underlying space of $X'$ is empty and the conclusion is immediate.

:::

:::

::: {.pf-step #s3}

The section $s$ extends to a splitting $\sigma:\OO_X\to\OO_{X'}$ of sheaves of $k$-algebras.

::: pf-proof

For $a\in A$, the restriction of $s(a)$ to $D(a)$ is a unit in $\OO_{X'}$.
Indeed, at each point its image in the quotient local ring $\OO_X$ is a unit.
A unit lifts across a square-zero ideal: if a local lift of the inverse has product $1+e$ with $e^2=0$, multiplying it by $1-e$ gives an actual inverse.
The resulting local inverses agree wherever both are defined, by uniqueness, and hence glue to an inverse over $D(a)$.

Consequently $s$ determines a ring map
$$
A_a\longrightarrow\Gamma(D(a),\OO_{X'}),\qquad
b/a^q\longmapsto s(b)s(a)^{-q}|_{D(a)}.
$$
The universal property of localization gives well-definedness and compatibility with restrictions to smaller distinguished opens.
Since these opens form a basis and $\OO_X(D(a))=A_a$, the maps glue to a sheaf homomorphism $\sigma$.
Its reduction is the identity on every distinguished open, so $\rho\sigma=\id_{\OO_X}$.

:::

:::

::: {.pf-step #s4}

The map
$$
\Phi:\OO_X\oplus\mcf\longrightarrow\OO_{X'},\qquad
(a,m)\longmapsto\sigma(a)+m
$$
is an isomorphism of sheaves of $k$-algebras inducing the specified identifications on the quotient and ideal.

::: pf-proof

Use the fixed identification of $\mcf$ with $\mathcal I$ in the formula.
Multiplication by $\sigma(a)$ on $\mathcal I$ is exactly multiplication by $a$ in its quotient-module structure, independently of the lift of $a$.
Together with $\mathcal I^2=0$, this proves
$$
\Phi(a,m)\Phi(b,n)=\sigma(ab)+an+bm=\Phi(ab,an+bm).
$$
The map also preserves addition, $k$ and $1$.
Its inverse sends a local section $b$ of $\OO_{X'}$ to
$$
(\rho(b),\ b-\sigma(\rho(b))).
$$
The second component belongs to $\mathcal I$, and these formulas commute with restrictions and are mutual inverses.
Thus $\Phi$ is an isomorphism of sheaves of rings.
On the common topological space it is an isomorphism of locally ringed spaces, hence of schemes, with the trivial extension constructed in step [](#s1){.pf-ref}.
It preserves the quotient $X$ and the identified ideal $\mcf$.
The choice of $s$ need not be unique, so the resulting isomorphism is not asserted to be canonical.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} verifies the trivial extension, and steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} show that every extension in the affine nonsingular case is isomorphic to it.

:::

:::

:::
