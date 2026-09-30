---
schema: qual/card@1
id: P-AGXGATHSTALKSUBVAR
kind: problem
title: The stalk along an irreducible subvariety as a localization of the coordinate ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stalks
  - Localization
  - Coordinate Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Gathmann 3.23 and the preceding definition of the stalk at a
    subspace in the retained native source at revision 7eafedfc0. The current
    card matches that source, which gives no worked solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the localization construction. Checked the equivalence between
    D(g) meeting Y and g lying outside I(Y), well-definedness on localized
    fractions, surjectivity from local fraction representatives, and
    injectivity via vanishing on a principal neighborhood meeting Y.
---

::: {.problem}
Let $Y\subset X$ be a nonempty and irreducible subspace of a topological space $X$ carrying a sheaf $\mcf$.
The stalk of $\mcf$ at $Y$ is defined by the pairs $(U, \phi)$ such that $U\subset X$ is open, $U\intersect Y$ is nonempty, and $\phi \in \mcf(U)$, where $(U, \phi) \sim (U',\phi')$ iff there is a small enough open set on which the restrictions agree.

Let $Y\subset X$ be a nonempty and irreducible subvariety of an affine variety $X$, and show that the stalk $\OO_{X, Y}$ of $\OO_X$ at $Y$ is a $k\dash$algebra isomorphic to the localization $A(X)_{I(Y)}$.
:::

::: {.solution}
Put
$$
A=A(X),
\qquad
\mfp=I(Y)\normal A.
$$
Since $Y$ is irreducible, $\mfp$ is prime.

::: pf

::: {.pf-step #s1}

For $g\in A$,
$$
D(g)\cap Y\ne\emptyset
\quad\Longleftrightarrow\quad
g\notin\mfp.
$$

::: pf-proof

By definition,
$$
g\in I(Y)
$$
exactly when $g$ vanishes at every point of $Y$. This is equivalent to
$$
Y\cap\{x\in X:g(x)\ne0\}=\emptyset.
$$
The set in braces is $D(g)$, proving the equivalence.

:::

:::

::: {.pf-step #s2}

There is a canonical $k$-algebra homomorphism
$$
\Phi:A_{\mfp}\longrightarrow\OO_{X,Y}
$$
given by
$$
\Phi\left(\frac fg\right)
=
\left[D(g),\frac fg\right]_Y
$$
for $g\notin\mfp$.

::: pf-proof

If $g\notin\mfp$, step [](#s1){.pf-ref} shows that $D(g)$ meets $Y$, so the regular
function $f/g\in\OO_X(D(g))=A_g$ represents a germ along $Y$.

Suppose
$$
\frac fg=\frac{f'}{g'}
$$
in $A_{\mfp}$. By the definition of localization, there is
$$
h\notin\mfp
$$
such that
$$
h(g'f-gf')=0
$$
in $A$. Since $\mfp$ is prime,
$$
gg'h\notin\mfp,
$$
so $D(gg'h)$ meets $Y$ by step [](#s1){.pf-ref}. On this open set, $g,g'$, and $h$
are invertible, and the displayed equality implies
$$
\frac fg=\frac{f'}{g'}.
$$
Thus the two representatives define the same germ along $Y$, so $\Phi$ is
well defined. Addition, multiplication, and scalar multiplication are all
computed by the same fraction operations on a common principal open, so
$\Phi$ is a $k$-algebra homomorphism.

:::

:::

::: {.pf-step #s3}

The homomorphism $\Phi$ is surjective.

::: pf-proof

Let a germ in $\OO_{X,Y}$ be represented by
$$
(U,\phi),
\qquad
U\cap Y\ne\emptyset.
$$
Choose
$$
y\in U\cap Y.
$$
Because $\phi$ is regular at $y$, after shrinking to a principal open
neighborhood
$$
y\in D(g)\subseteq U
$$
there are $f,g\in A$ such that
$$
\restrictionof{\phi}{D(g)}=\frac fg.
$$
Since $y\in D(g)\cap Y$, step [](#s1){.pf-ref} gives $g\notin\mfp$. Hence
$$
\frac fg\in A_{\mfp},
$$
and its image under $\Phi$ is the original germ.

:::

:::

::: {.pf-step #s4}

The homomorphism $\Phi$ is injective.

::: pf-proof

Suppose
$$
\Phi\left(\frac fg\right)=0,
\qquad
g\notin\mfp.
$$
Then the regular function $f/g$ vanishes on some open subset
$$
W\subseteq D(g)
$$
with
$$
W\cap Y\ne\emptyset.
$$
Choose $y\in W\cap Y$ and then a principal open neighborhood
$$
y\in D(h)\subseteq W.
$$
By step [](#s1){.pf-ref}, $h\notin\mfp$. The restriction of $f/g$ to $D(h)$ is zero.
Since $D(h)\subseteq D(g)$, the element $g$ is invertible in $A_h$, so
the image of $f$ in $A_h$ is zero. Therefore
$$
h^Nf=0
$$
in $A$ for some $N\ge0$.

Because $h\notin\mfp$, the element $h$ is a unit in $A_{\mfp}$. Hence
$f/1=0$ in $A_{\mfp}$, and therefore
$$
\frac fg=0.
$$
Thus $\ker\Phi=0$.

:::

:::

::: {.pf-step #s5}

Consequently,
$$
\boxed{\OO_{X,Y}\cong A(X)_{I(Y)}}
$$
as $k$-algebras.

::: pf-proof

Step [](#s2){.pf-ref} constructs the canonical $k$-algebra homomorphism, and steps
[](#s3){.pf-ref} and [](#s4){.pf-ref} prove that it is bijective.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required localization description of the stalk along
$Y$.

:::

:::

:::
