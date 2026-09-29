---
schema: qual/card@1
id: P-AGXVARPROJMORPHISMS
kind: problem
title: "Morphisms of complex projective varieties: properness, images, and birationality"
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Properness
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the corresponding clauses of Zaidenberg Exercises 8.5 in the recorded
    source. They concern properness and closedness of morphisms of projective
    varieties, projectivity of the image, surjectivity of dominant and
    birational morphisms, constancy of global regular functions, computation
    of C(X) from a dense affine open, the function-field criterion for
    birationality, and projectivity of X x Y via the Segre embedding.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Restored the source hypotheses that U is a Zariski-open dense affine
    subset and that C(X)=Frac O(U). Replaced the incorrect sheaf-level map
    O_Y -> O_X in the birationality clause by the source's pullback
    C(Y) -> C(X) on function fields, and separated constancy of global regular
    functions from the surjectivity clause.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Factored f through its graph to prove projectivity and properness, used
    closedness and irreducibility for the image and surjectivity statements,
    identified function fields on dense affine opens, proved the converse
    birational criterion by clearing denominators on affine charts, and used
    the Segre closed immersion for the product.
---

::: {.problem}
Let
$$
f:X\longrightarrow Y
$$
be a morphism of projective varieties over $\CC$.

(a) Show that $f$ is proper and closed.

(b) Show that $f(X)$ is a projective subvariety of $Y$.

(c) Show that every dominant, and hence every birational, morphism $X\to Y$ is surjective.

(d) Show that every global regular function on $X$ is constant.

(e) If $U\subseteq X$ is a Zariski-open dense affine subset, show that
$$
\CC(X)=\Frac\mco(U).
$$

(f) If $f$ is dominant, show that $f$ is birational if and only if
$$
f^*:\CC(Y)\xrightarrow{\sim}\CC(X)
$$
is an isomorphism.

(g) Show that $X\cross Y$ is projective, using the Segre embedding.
:::

::: {.solution}
Choose projective embeddings
$$
X\subseteq\PP^n_\CC,
\qquad
Y\subseteq\PP^m_\CC.
$$

::: pf

::: {.pf-step #f-is-projective}
The morphism $f:X\to Y$ is projective.

::: pf-proof
Because the projective variety $Y$ is separated over $\CC$, the graph
$$
\Gamma_f
\subseteq
X\cross Y
$$
is closed.
The graph map identifies $X$ with $\Gamma_f$.

The closed immersion
$$
X\hookrightarrow\PP^n_\CC
$$
base-changes to a closed immersion
$$
X\cross Y
\hookrightarrow
\PP^n_\CC\cross Y
=
\PP^n_Y.
$$
Composing the graph embedding with this closed immersion gives
$$
X
\cong
\Gamma_f
\hookrightarrow
\PP^n_Y.
$$
The projection
$$
\PP^n_Y\longrightarrow Y
$$
restricted to the graph is exactly $f$.
Hence $f$ has the factorization required by [[D-MORPROJ|the definition of a projective morphism]].
:::

:::

::: {.pf-step #f-proper-closed}
The morphism $f$ is proper and closed.

::: pf-proof
By step [](#f-is-projective){.pf-ref}, $f$ is projective.
Projective morphisms over a Noetherian base are proper by [[D-MORPROJ]]. A proper morphism is universally closed by definition ([[D-8XX95]]), hence in particular is a closed map.
This proves (a).
:::

:::

::: {.pf-step #image-projective-subvariety}
The image $f(X)$ is a projective subvariety of $Y$.

::: pf-proof
By step [](#f-proper-closed){.pf-ref}, $f$ is closed, so
$$
f(X)\subseteq Y
$$
is Zariski closed.
Since $Y$ is a closed subvariety of $\PP^m_\CC$, the image $f(X)$ is also Zariski closed in $\PP^m_\CC$.

The variety $X$ is irreducible, and a continuous image of an irreducible space is irreducible.
Therefore $f(X)$ is irreducible.
It is nonempty because $X$ is nonempty.
Thus $f(X)$ is a projective variety, proving (b).
:::

:::

::: {.pf-step #dominant-implies-surjective}
Every dominant morphism $f:X\to Y$ is surjective; in particular every birational morphism is surjective.

::: pf-proof
If $f$ is dominant, then
$$
\overline{f(X)}=Y.
$$
Step [](#f-proper-closed){.pf-ref} makes $f(X)$ closed, so
$$
f(X)=\overline{f(X)}=Y.
$$
Thus $f$ is surjective.

A birational morphism is dominant because it restricts to an isomorphism between dense open subsets.
Hence the same conclusion applies to every birational morphism.
This proves (c).
:::

:::

::: {.pf-step #global-functions-constant}
Every global regular function on $X$ is constant.

::: pf-proof
The projective variety $X$ is irreducible, hence connected.
The proposition [[PR-EFW6B|regular functions on a projective variety are constant]] gives
$$
\mco_X(X)=\CC.
$$
Thus every global regular function on $X$ is constant, proving (d).
:::

:::

::: {.pf-step #function-field-formula}
If $U\subseteq X$ is a Zariski-open dense affine subset, then
$$
\boxed{\CC(X)=\Frac\mco(U).}
$$

::: pf-proof
Since $X$ is irreducible and $U$ is a nonempty open subset, $U$ is irreducible.
Write
$$
U=\mspec A,
\qquad
A=\mco(U).
$$
Then $A$ is a domain and the function field of the affine variety $U$ is
$$
\CC(U)=\Frac A.
$$

Rational functions are unchanged after restricting an irreducible variety to a dense open subset: a rational function is represented on some nonempty open subset, and intersecting that domain with $U$ gives the same rational function on $U$; conversely every rational function on $U$ is defined on a nonempty open subset of $X$ and therefore defines a rational function on $X$.
Hence
$$
\CC(X)=\CC(U)=\Frac\mco(U).
$$
This proves (e).
:::

:::

::: {.pf-step #birational-implies-field-iso}
If $f$ is birational, then
$$
f^*:\CC(Y)\longrightarrow\CC(X)
$$
is an isomorphism.

::: pf-proof
Birationality gives dense open subsets
$$
U\subseteq X,
\qquad
V\subseteq Y
$$
such that
$$
f|_U:U\xrightarrow{\sim}V.
$$
Restricting rational functions to these dense opens identifies
$$
\CC(X)=\CC(U),
\qquad
\CC(Y)=\CC(V).
$$
The isomorphism $U\cong V$ induces an isomorphism of these fields, and this is exactly the pullback $f^*$.
:::

:::

::: {.pf-step #field-iso-implies-birational}
Conversely, let $f$ be dominant and suppose
$$
f^*:\CC(Y)\xrightarrow{\sim}\CC(X)
$$
is an isomorphism.
Then $f$ is birational.

::: pf-proof
Choose a nonempty affine open
$$
V=\mspec A\subseteq Y.
$$
Since $f$ is dominant, $f^{-1}(V)$ is nonempty.
Choose a nonempty affine open
$$
U=\mspec B\subseteq f^{-1}(V).
$$
The restriction $U\to V$ is a morphism of varieties, so $B$ is a finitely generated $A$-algebra.
By step [](#function-field-formula){.pf-ref},
$$
\Frac A=\CC(Y),
\qquad
\Frac B=\CC(X).
$$
Under the assumed isomorphism, regard these as the same field
$$
K.
$$
The ring map
$$
A\longrightarrow B
$$
is then injective.

Choose algebra generators
$$
B=A[b_1,\ldots,b_r].
$$
Since every $b_i$ lies in
$$
K=\Frac A,
$$
write
$$
b_i=\frac{a_i}{s_i},
\qquad
a_i,s_i\in A,
\quad
s_i\ne0.
$$
Set
$$
s=s_1\cdots s_r.
$$
After localizing,
$$
b_i\in A_s
$$
for every $i$.
Hence
$$
B_s\subseteq A_s.
$$
The original inclusion $A\subseteq B$ gives the reverse inclusion, so
$$
B_s=A_s.
$$
Therefore the restriction of $f$ is an isomorphism
$$
D_U(s)\xrightarrow{\sim}D_V(s).
$$
Because $s\ne0$ in the domains $A$ and $B$, these distinguished opens are nonempty and hence dense.
Thus $f$ is birational.
:::

:::

::: {.pf-step #birational-criterion}
For a dominant morphism $f:X\to Y$,
$$
\boxed{
f\text{ is birational}
\quad\Longleftrightarrow\quad
f^*:\CC(Y)\xrightarrow{\sim}\CC(X).
}
$$

::: pf-proof
Step [](#birational-implies-field-iso){.pf-ref} proves the forward implication and step [](#field-iso-implies-birational){.pf-ref} proves the converse.
This proves (f).
:::

:::

::: {.pf-step #product-projective}
The product $X\cross Y$ is a projective variety.

::: pf-proof
The product projections show
$$
X\cross Y
=
\pi_1^{-1}(X)
\intersect
\pi_2^{-1}(Y),
$$
so $X\cross Y$ is closed in
$$
\PP^n_\CC\cross\PP^m_\CC.
$$
The product of varieties is again a variety, glued from affine product charts [[P-AGH2323VARPRODUCT]].

Let
$$
\sigma:
\PP^n_\CC\cross\PP^m_\CC
\longrightarrow
\PP^N_\CC,
\qquad
N=(n+1)(m+1)-1,
$$
be the Segre embedding.
By [[P-AGH214SEGRE]], $\sigma$ is an isomorphism onto a closed projective subvariety of $\PP^N_\CC$.

Since $X\cross Y$ is closed in the source of this embedding,
$$
\sigma(X\cross Y)
$$
is closed in the Segre image and therefore closed in $\PP^N_\CC$.
It is irreducible because $X\cross Y$ is a variety.
Hence $\sigma(X\cross Y)$ is a projective variety isomorphic to $X\cross Y$.
This proves (g).
:::

:::

::: pf-qed
Steps [](#f-is-projective){.pf-ref} and [](#f-proper-closed){.pf-ref} prove (a), step [](#image-projective-subvariety){.pf-ref} proves (b), step [](#dominant-implies-surjective){.pf-ref} proves (c), step [](#global-functions-constant){.pf-ref} proves (d), step [](#function-field-formula){.pf-ref} proves (e), steps [](#birational-implies-field-iso){.pf-ref}, [](#field-iso-implies-birational){.pf-ref} and [](#birational-criterion){.pf-ref} prove (f), and step [](#product-projective){.pf-ref} proves (g).
:::

:::

:::
