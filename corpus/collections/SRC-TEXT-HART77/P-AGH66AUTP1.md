---
schema: qual/card@1
id: P-AGH66AUTP1
kind: problem
title: $\Aut \PP^1$ is the group of fractional linear transformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Function Fields
  - Projective Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.6 and Corollary I.6.12 in the Hartshorne source. The proof identifies curve automorphisms with function-field automorphisms through the category equivalence and reduces an automorphism fixing infinity to an automorphism of k[x], hence to an affine linear map.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Milne, Fields and Galois Theory, Example 3.1(b) printed p. 35 and
    Lemma 9.24 printed p. 119: [F(X):F(a_i)] = deg(a_i) for a_i in lowest
    terms, so a k-automorphism of k(x) with x -> a/b forces max(deg a, deg
    b) = [k(x):k(a/b)] = 1 and a, b linear. That is the implication
    Borcherds, Egbert and Cutrone-Marshburn assert. Rechecked the card's own
    route: an automorphism of P^1 carrying phi(infty) back to infty
    restricts to an automorphism of A^1, whose coordinate-ring automorphism
    has x -> ax+b because degrees multiply under composition.
    The page given above for Lemma 9.24 is wrong: the lemma is on printed
    p. 118, and Example 9.25, which states the conclusion in the form used
    here, is on printed p. 119. Both were re-read at those folios in the
    PDF, `tmp/sources/milne-fields-and-galois-theory.pdf`.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Part (c) is now Milne's proof rather than the card's own. Steps
    degree-of-a-rational-function (Lemma 9.24, printed p. 118) and
    field-automorphism-fractional-linear (Example 9.25, printed p. 119) give
    it over an arbitrary base field, and step pgl1-isomorphism deduces
    PGL(1) = Aut P^1 from parts (a) and (b). The two steps that proved
    "every automorphism of P^1 is fractional linear" by reducing to an
    automorphism of k[x] were removed; the remark records that route as the
    card's earlier one. Read against the book: Exercise I.6.6 on printed
    p. 46 asks (c) for k(x), which is what the transcribed argument proves.
    The base field is not arbitrary in the exercise: Chapter I fixes k
    algebraically closed (text version
    tmp/sources/hartshorne-1977-algebraic-geometry.md, line 350, "We work
    over a fixed algebraically closed field k"), and part (b) appeals to
    Corollary I.6.12, which is stated there for such a k. Nothing in the
    argument for (c) uses more than that k is a field: Lemma 9.24 and
    Example 9.25 are stated over an arbitrary field F, so the proof is
    stronger than the exercise asks for.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Reader's report on issue #121, two repairs. First, the note above said
    the exercise asks (c) over an arbitrary field k, which is false:
    Hartshorne fixes k algebraically closed for Chapter I, and part (b)
    needs Corollary I.6.12 in that setting. The note is corrected rather than
    the statement, since the card's problem block already prints the exercise
    with the chapter's k. Second, the notation of step
    field-automorphism-fractional-linear used a, b for the coprime numerator
    and denominator and then for the scalars of the fractional linear form,
    and wrote the form in the homogeneous coordinate X; the polynomials are
    now p and q and the form is in the affine coordinate x. Re-read at the
    folios given: Milne, Lemma 9.24 with its proof on printed p. 118 and
    Example 9.25 on printed p. 119, text version
    tmp/sources/milne-fields-and-galois-theory.md, and Example 3.1(b) on
    printed p. 35. Not checked in this pass: the mathematical content of the
    steps, which the reader accepted.
---

::: {.problem}
Think of $\PP^1$ as $\AA^1 \union \theset{\infty}$.
Define a *fractional linear transformation* of $\PP^1$ by sending
$$
x \mapsto \frac{ax + b}{cx + d}, \qquad a,b,c,d \in k, \quad ad - bc \neq 0.
$$

(a) Show that a fractional linear transformation induces an automorphism of $\PP^1$, that is, an isomorphism of $\PP^1$ with itself.
   Denote the group of all these fractional linear transformations by $\PGL(1)$.

(b) Let $\Aut \PP^1$ denote the group of all automorphisms of $\PP^1$.
   Show that $\Aut \PP^1 \cong \Aut k(x)$, the group of $k$-automorphisms of the field $k(x)$.

(c) Show that every automorphism of $k(x)$ is a fractional linear transformation, and deduce that $\PGL(1) \to \Aut \PP^1$ is an isomorphism.

Note: a similar result holds for $\PP^n$ (II, 7.1.1): every automorphism is given by a linear transformation of the homogeneous coordinates.
:::

::: {.solution}
Use homogeneous coordinates $[X:Z]$ on $\PP^1$, with affine coordinate $x=X/Z$ on $Z\ne0$ and $\infty=[1:0]$.

::: pf

::: {.pf-step #matrix-gives-automorphism}
Every matrix
$$
M=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in\operatorname{GL}_2(k)
$$
defines an automorphism
$$
T_M([X:Z])=[aX+bZ:cX+dZ]
$$
of $\PP^1$.

::: pf-proof
The two homogeneous linear forms $aX+bZ$ and $cX+dZ$ have no common nonzero zero because $M$ is invertible.
Hence they define a morphism $T_M:\PP^1\to\PP^1$.
The inverse matrix $M^{-1}$ gives a morphism $T_{M^{-1}}$ satisfying
$$
T_{M^{-1}}T_M=T_MT_{M^{-1}}=\operatorname{id}_{\PP^1}.
$$
Thus $T_M$ is an automorphism.
On the affine chart it sends
$$
x\longmapsto\frac{ax+b}{cx+d},
$$
with the usual value $\infty$ when the denominator vanishes.

Multiplying $M$ by a nonzero scalar does not change $T_M$, and two matrices inducing the same projective transformation differ by such a scalar.
Thus these transformations form the projective linear group $\operatorname{PGL}_2(k)$, denoted $\PGL(1)$ in the source.
This proves part (a).
:::

:::

::: {.pf-step #aut-p1-iso-aut-kx}
Pullback of rational functions gives an isomorphism
$$
\Aut(\PP^1)\xrightarrow{\cong}\Aut_k k(x).
$$

::: pf-proof
An automorphism $\phi:\PP^1\to\PP^1$ induces the $k$-automorphism
$$
\phi^*:K(\PP^1)=k(x)\longrightarrow k(x),
\qquad h\longmapsto h\circ\phi.
$$
Composition of maps reverses under pullback, so if one uses ordinary composition on both groups the assignment $\phi\mapsto(\phi^{-1})^*$ is a group homomorphism.

Corollary I.6.12 identifies nonsingular projective curves with their function fields contravariantly: every $k$-homomorphism of function fields is induced by a unique dominant morphism of the corresponding nonsingular projective curves.
Apply this with both fields equal to $k(x)$.
An automorphism of $k(x)$ therefore induces a unique dominant morphism $\psi:\PP^1\to\PP^1$, and its inverse field automorphism induces a morphism inverse to $\psi$ by uniqueness in the category equivalence.
Hence $\psi$ is an automorphism.

Thus the pullback construction is bijective, and after the harmless inverse convention just noted it is an isomorphism of groups.
This proves part (b).
:::

:::

::: {.pf-step #degree-of-a-rational-function}
For $u=a/b\in k(x)\setminus k$ with $a,b$ coprime polynomials, define
$$
\deg(u)=\max(\deg a,\deg b).
$$
Then $x$ is algebraic over $k(u)$ with
$$
[k(x):k(u)]=\deg(u),
$$
so $k(u)=k(x)$ forces $\deg(u)=1$.

::: pf-proof
This is J. S. Milne, *Fields and Galois Theory*, Lemma 9.24, printed p. 118, whose proof is repeated here.

The polynomial
$$
a(T)-b(T)u\in k(u)[T]
$$
has $x$ as a root, so $x$ is algebraic over $k(u)$; hence $u$ is transcendental over $k$, since otherwise $x$ would be algebraic over $k$.

The polynomial $a(T)-b(T)Z\in k[Z,T]$ is irreducible: it is linear in $Z$, so a factorization into two nonconstant factors would have one factor $f\in k[T]$, which would then divide the constant term $a(T)$ and the coefficient $-b(T)$ of $Z$, hence divide the greatest common divisor of $a$ and $b$, forcing $f$ to be constant.
Since $u$ is transcendental over $k$, substitution $Z\mapsto u$ identifies $k[Z,T]$ with $k[u,T]$, so $a(T)-b(T)u$ is irreducible in $k[u,T]$ and hence, by Gauss's lemma, in $k(u)[T]$.
It has $x$ as a root, so up to a constant it is the minimal polynomial of $x$ over $k(u)$, and its degree is $\max(\deg a,\deg b)=\deg(u)$.

Consequently $k(u)=k(x)$ gives $1=[k(x):k(u)]=\deg(u)$.
:::

:::

::: {.pf-step #field-automorphism-fractional-linear}
Every $k$-automorphism of $k(x)$ is a fractional linear transformation.

::: pf-proof
Let $\sigma$ be a $k$-automorphism of $k(x)$ and put $u=\sigma(x)$.
Then $\sigma$ is determined by $u$, because $\sigma(h(x))=h(u)$ for every $h\in k(x)$; and $k(u)=\sigma(k(x))=k(x)$.

Write $u=p/q$ in lowest terms, with $p,q\in k[x]$ coprime. By step [](#degree-of-a-rational-function){.pf-ref}, $\deg(u)=1$, so $p$ and $q$ are linear; after multiplying numerator and denominator by a nonzero constant,
$$
u=\frac{ax+b}{cx+d}
$$
with $a,b,c,d\in k$ and $ad-bc\ne0$. Coprimality of $p$ and $q$ forbids the two linear polynomials $ax+b$ and $cx+d$ from having a common factor, and a common factor of two linear polynomials is a common root, which exists exactly when $ad-bc=0$; so $ad-bc\ne0$ is the coprimality just used.

This is J. S. Milne, *Fields and Galois Theory*, Example 9.25, printed p. 119, text version `tmp/sources/milne-fields-and-galois-theory.md`, which states the conclusion in the form "$F(X)=F(u)$ if and only if $u=\frac{aX+b}{cX+d}$ with $ad-bc\ne0$", for an arbitrary base field $F$; his $X$ is the affine coordinate $x$ of this card.
:::

:::

::: {.pf-step #pgl1-isomorphism}
The map $\PGL(1)\to\Aut\PP^1$ is an isomorphism, and
$$
\boxed{\PGL(1)\cong\Aut(\PP^1)\cong\Aut_k k(x)}.
$$

::: pf-proof
Step [](#matrix-gives-automorphism){.pf-ref} produces a map $\PGL(1)\to\Aut\PP^1$, which is a homomorphism because composition of fractional linear transformations corresponds to multiplication of the matrices.
It is injective: a matrix inducing the identity transformation is a scalar matrix, since it fixes every point of $\PP^1$.

For surjectivity, let $\phi\in\Aut(\PP^1)$. By step [](#aut-p1-iso-aut-kx){.pf-ref} the pullback $\phi^*$ is a $k$-automorphism of $k(x)$, so by step [](#field-automorphism-fractional-linear){.pf-ref} there are scalars $a,b,c,d$ with $ad-bc\ne0$ and $\phi^*(x)=(ax+b)/(cx+d)$ as a rational function of the affine coordinate $x$.
Then $\phi^*(h)=h\bigl((ax+b)/(cx+d)\bigr)$ for every $h\in k(x)$, so $\phi^*$ is the pullback along the fractional linear transformation $T$ of step [](#matrix-gives-automorphism){.pf-ref}, and $\phi=T$ because pullback is injective on morphisms of $\PP^1$.

Composing with the isomorphism of step [](#aut-p1-iso-aut-kx){.pf-ref} gives the second isomorphism.
This proves part (c) together with the two asserted isomorphisms.
:::

:::

::: pf-qed
Step [](#matrix-gives-automorphism){.pf-ref} proves part (a), step [](#aut-p1-iso-aut-kx){.pf-ref} proves part (b), and steps [](#degree-of-a-rational-function){.pf-ref}, [](#field-automorphism-fractional-linear){.pf-ref} and [](#pgl1-isomorphism){.pf-ref} prove part (c) and both isomorphisms.
:::

:::
:::

::: {.remark title="Published solution"}
Part (c) is transcribed from J. S. Milne, *Fields and Galois Theory*, Lemma 9.24 on printed p. 118 and Example 9.25 on printed p. 119, text version `tmp/sources/milne-fields-and-galois-theory.md`, read in the PDF at those folios. Lemma 9.24 is proved there in full: for $u=a/b$ in lowest terms, $a(T)-b(T)u$ is the minimal polynomial of $X$ over $F(u)$, so $[F(X):F(u)]=\deg(u)$, the larger of the two degrees. Example 9.25 draws the conclusion used here, $F(X)=F(u)$ if and only if $u=\frac{aX+b}{cX+d}$ with $ad-bc\ne0$, for an arbitrary field $F$. Applied to a $k$-automorphism $\sigma$ of $k(x)$ with $\sigma(x)=u$, $k(u)=k(x)$ gives $\deg(u)=1$, hence $u$ and with it $\sigma$ are fractional linear. That is exactly the implication the retained sets assert and none proves. Example 3.1(b) on printed p. 35 states the same conclusion over $\CC$ and refers forward to Lemma 9.24; the general statement is 9.25. Milne's two results need only a field, so the argument for (c) adds no hypothesis; the exercise itself is stated where Chapter I is in force, with $k$ algebraically closed (text version `tmp/sources/hartshorne-1977-algebraic-geometry.md`, line 350), and part (b) uses Corollary I.6.12 in that setting. The card's own earlier route, through part (b) and the affine-line reduction of an automorphism of $\PP^1$ fixing $\infty$ to a $k$-algebra automorphism of $k[x]$ with $\deg x=\deg(q\circ p)$, is not used in the proof now: it proves the same thing by another route.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, Exercise 6.6, PDF p. 8: (a) the inverse of $x\mapsto(ax+b)/(cx+d)$ is $x\mapsto(dx-b)/(a-cx)$ when $ad-bc\ne0$; (b) "follows from corollary 6.12 (i) and (iii)"; (c) "any automorphism of $k(x)$ maps $x$ to $f(x)/g(x)$ for coprime polynomials $f$ and $g$ ... therefore $f(x)/g(x)$ is not equal to $f(y)/g(y)$ if $x\ne y$. But if $f$ or $g$ have degree greater than $1$ then $g(y)a=f(y)$ will usually have more than one solution for $y$. Hence $f$ and $g$ have degrees at most $1$." The middle sentence is not an argument; the equation printed there mixes the two coprime polynomials.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), text version `tmp/sources/hartshorne-solutions-troiani.md`, stops at §I.5 and gives no solution to 6.6.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise I.6.6, PDF pp. 54--55: (a) invertibility of the matrix; (b) "$(\phi\in\operatorname{Aut}\PP^1$ gives $f\mapsto f\circ\phi\in\operatorname{Aut}k(x)$; if $\varphi\in\operatorname{Aut}k(x)$, $\varphi$ induces an auto-birational map of $\PP^1$, a nonsingular curve" — the parenthetical question in the original is his; (c) "$\phi$ maps $x\mapsto f(x)/g(x)$ for coprime $f,g$; injectivity of $\varphi$ implies $f,g$ are linear", the implication being asserted.
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, text version `tmp/sources/hartshorne-solutions-cutrone-marshburn.md`, Exercise I.6.6, PDF p. 25: (a) the inverse formula; (b) an automorphism of $k(x)$ induces a birational map of $\PP^1$, and a birational map of nonsingular projective curves is an isomorphism; (c) "if $\deg g,\deg f>1$, the map won't be injective, so both $f$ and $g$ are linear", the same assertion.
Parts (a) and (b) agree across the three sets. Every set asserts that a nonconstant rational function of degree greater than one is not injective and none proves it; part (c) of all three therefore rests on an unproved step, and none of them is a complete published solution. Steps [](#degree-of-a-rational-function){.pf-ref} and [](#field-automorphism-fractional-linear){.pf-ref} are Milne's proof of that step, carried out for an arbitrary base field, and step [](#pgl1-isomorphism){.pf-ref} adds the deduction of the isomorphism that the exercise asks for.
:::
