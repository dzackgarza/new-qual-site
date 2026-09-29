---
schema: qual/card@1
id: P-AGH551RESOLVERATFN
kind: problem
title: Resolving a rational function to a morphism to $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Birational Geometry
  - Blowups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.5.1 as transcribed here, the retained Andrew Egbert
    companion sketch, embedded resolution V.3.9, and the point-blowup divisor
    formulas used in V.3.2. The companion has the intended first step but
    merely asserts that further blowups separate zero and pole curves. The
    proof below supplies the missing termination argument: at a transverse
    zero/pole crossing with orders a,b, a blowup replaces the pair by
    (a-b,b) or (a,b-a), so a positive-integer measure decreases exactly as
    in the Euclidean algorithm. Once the positive and negative parts of the
    divisor are disjoint, the sections f and 1 of O(P) form a base-point-free
    pencil and hence give the required morphism to P^1.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the V.3.9 embedded-resolution input
    and the local point-blowup formulas. Checked that a transverse
    zero/pole crossing of orders a,b produces exceptional coefficient a-b,
    that the global sum of crossing-order pairs strictly decreases under
    every further blowup, and that no untouched crossing changes. After
    termination, verified directly from div(f)=Z'-P' that f and 1 are
    sections of O(P') with disjoint zero divisors, hence a base-point-free
    pencil whose coordinate ratio is the original function f.
---

::: {.problem}
Let $f$ be a rational function on the surface $X$.
Show that it is possible to "resolve the singularities of $f$" in the following sense: there is a birational morphism $g: X^{\prime} \rightarrow X$ so that $f$ induces a morphism of $X^{\prime}$ to $\PP^1$.

Hints: Write the divisor of $f$ as $(f)=\sum n_i C_i$.
Then apply embedded resolution (3.9) to the curve $Y=\bigcup C_i$.
Then blow up further as necessary whenever a curve of zeros meets a curve of poles until the zeros and poles of $f$ are disjoint.
:::

::: {.solution}
If $f$ is constant, it already defines a constant morphism
$$
X\longrightarrow\PP^1,
$$
so take $g=\operatorname{id}_X$. Assume from now on that
$$
f\in K(X)^\times
$$
is nonconstant.

Write its principal divisor as
$$
(f)=\sum_i n_iC_i=Z-P,
$$
where
$$
Z=\sum_{n_i>0}n_iC_i,
\qquad
P=\sum_{n_i<0}(-n_i)C_i
$$
are effective divisors with no common irreducible component.

::: pf

::: {.pf-step #snc-resolution}
After a birational morphism
$$
g_1:X_1\longrightarrow X
$$
which is a finite composition of point blowups, the support of the divisor
of $f$ on $X_1$ is a simple normal-crossing divisor.

::: pf-proof
Let
$$
Y=\operatorname{Supp}(Z)\cup\operatorname{Supp}(P).
$$
Apply embedded resolution V.3.9 to the reduced curve $Y$ on the nonsingular
surface $X$. This gives a finite composition of point blowups
$$
g_1:X_1\longrightarrow X
$$
such that the reduced total transform of $Y$ is simple normal crossings.

The birational map identifies the function fields,
$$
K(X_1)=K(X),
$$
so we regard the same rational function $f$ on $X_1$. Its divisor is the
pullback of $(f)$: its components are the strict transforms of the $C_i$ and
some exceptional curves, with integer coefficients. Hence its support is a
union of components of the resolved total transform of $Y$. A union of
components of a simple normal-crossing divisor is again simple normal
crossings.

On any subsequent surface write
$$
(f)=Z'-P'
$$
for the positive and negative parts.
:::

:::

::: {.pf-step #blowup-crossing-coefficient}
Suppose a zero component of multiplicity $a>0$ and a pole component
of multiplicity $b>0$ meet at a point $Q$. After blowing up $Q$, their
strict transforms are disjoint and the exceptional curve $E$ occurs in
$(f)$ with coefficient
$$
\boxed{a-b.}
$$

::: pf-proof
Because the support is simple normal crossings, there are regular parameters
$$
x,y\in\OO_{X,Q}
$$
such that the zero component is $x=0$, the pole component is $y=0$, and no
other component of $(f)$ passes through $Q$. Thus locally
$$
f=u\,x^a y^{-b}
$$
for a unit $u$.

Let
$$
\pi:\widetilde X\longrightarrow X
$$
be the blowup at $Q$. The total transforms of the two local curves are
$$
\pi^*(x=0)=C_x'+E,
\qquad
\pi^*(y=0)=C_y'+E.
$$
Therefore
$$
\operatorname{div}_{\widetilde X}(f)
=
aC_x'-bC_y'+(a-b)E
$$
near the exceptional fibre.

The strict transforms $C_x'$ and $C_y'$ meet $E$ at the two distinct points
corresponding to the tangent directions $x=0$ and $y=0$, so they no longer
meet one another.
:::

:::

::: {.pf-step #euclidean-algorithm-step}
The effect of step [](#blowup-crossing-coefficient){.pf-ref} on zero--pole crossings is the Euclidean
algorithm:
$$
\boxed{
(a,b)\longmapsto
\begin{cases}
(a-b,b),&a>b,\\
\text{no crossing},&a=b,\\
(a,b-a),&b>a.
\end{cases}}
$$

::: pf-proof
If $a=b$, step [](#blowup-crossing-coefficient){.pf-ref} gives coefficient zero on $E$. Since the two strict
transforms are disjoint, no zero component meets a pole component over $Q$.

If $a>b$, then $E$ is a zero component of multiplicity $a-b$. It meets the
strict transform of the pole component, of multiplicity $b$, at one point.
Its other intersection is with the strict transform of the original zero
component, so that intersection is zero--zero and is irrelevant. Thus the
only new zero--pole pair over $Q$ has orders
$$
(a-b,b).
$$

The case $b>a$ is symmetric: $E$ is a pole component of multiplicity
$b-a$ and the unique new zero--pole crossing has orders
$$
(a,b-a).
$$
:::

:::

::: {.pf-step #zero-pole-disjoint}
A finite sequence of further point blowups makes
$$
\boxed{\operatorname{Supp}(Z')\cap\operatorname{Supp}(P')=\varnothing.}
$$

::: pf-proof
At every stage the support of $(f)$ remains simple normal crossings: blowing
up a transverse crossing of two components replaces it by an exceptional
curve meeting the two strict transforms transversely at distinct points.

Consequently every zero--pole intersection point $Q$ has exactly one zero
component and one pole component through it. Let their positive
multiplicities be $a_Q,b_Q$, and define the positive integer
$$
M
=
\sum_{Q\in\operatorname{Supp}(Z')\cap\operatorname{Supp}(P')}
(a_Q+b_Q).
$$
There are only finitely many terms because the two effective divisors have
finitely many components, and two distinct irreducible curves on the
noetherian surface have zero-dimensional, hence finite, intersection unless
they share a component. The positive and negative parts share none.

Blow up one zero--pole crossing of orders $(a,b)$. By step [](#euclidean-algorithm-step){.pf-ref}:

- if $a=b$, its contribution $a+b$ disappears;
- if $a>b$, it is replaced by a contribution
  $$(a-b)+b=a<a+b;$$
- if $b>a$, it is replaced by a contribution
  $$a+(b-a)=b<a+b.$$

No other zero--pole crossing is changed, since the blowup is an isomorphism
away from its centre. Hence $M$ strictly decreases after every such blowup.
Because $M$ is a nonnegative integer, the process terminates after finitely
many steps. At termination $M=0$, which is exactly the displayed
disjointness.

Let
$$
g:X'\longrightarrow X
$$
be the composite of the embedded resolution in step [](#snc-resolution){.pf-ref} and all the
additional blowups in step [](#zero-pole-disjoint){.pf-ref}. On $X'$ write
$$
(f)=Z'-P',
\qquad
\operatorname{Supp}(Z')\cap\operatorname{Supp}(P')=\varnothing.
$$
:::

:::

::: {.pf-step #sections-and-zero-divisors}
The rational functions
$$
1,\qquad f
$$
are global sections of the line bundle
$$
\OO_{X'}(P'),
$$
and their zero divisors as sections are respectively
$$
P',
\qquad
Z'.
$$

::: pf-proof
For a divisor $D$ on a nonsingular variety,
$$
H^0(X',\OO_{X'}(D))
=
\{\,h\in K(X'):\operatorname{div}(h)+D\ge0\,\}\cup\{0\}.
$$
For $h=1$,
$$
\operatorname{div}(1)+P'=P'\ge0.
$$
For $h=f$,
$$
\operatorname{div}(f)+P'
=
(Z'-P')+P'
=
Z'\ge0.
$$
Thus both are global sections. Under this description the zero divisor of a
section $h$ of $\OO(P')$ is
$$
\operatorname{div}(h)+P',
$$
which gives $P'$ for $1$ and $Z'$ for $f$.
:::

:::

::: {.pf-step #pencil-base-point-free}
The two-dimensional subspace
$$
V=\langle f,1\rangle
\subseteq
H^0(X',\OO_{X'}(P'))
$$
is base-point free.

::: pf-proof
Since $f$ is nonconstant, the sections $f$ and $1$ are linearly independent.
By step [](#sections-and-zero-divisors){.pf-ref}, their common zero locus is
$$
\operatorname{Supp}(Z')\cap\operatorname{Supp}(P').
$$
Step [](#zero-pole-disjoint){.pf-ref} makes this intersection empty. Hence at every point of $X'$ at
least one of the two sections is nonzero, which is precisely base-point
freeness of $V$.
:::

:::

::: {.pf-step #morphism-to-p1}
The base-point-free pencil $V$ defines a morphism
$$
\boxed{\varphi_f:X'\longrightarrow\PP^1}
$$
whose induced rational function is $f$.

::: pf-proof
The standard construction of a morphism from a base-point-free linear
system [[T-DIVMAPPN]] applied to the ordered basis $(f,1)$ gives
regular local coordinate pairs which are never simultaneously zero.
On the open set
$$
X'\setminus\operatorname{Supp}(P'),
$$
the section $1$ is nonvanishing and therefore trivializes
$\OO_{X'}(P')$; in this trivialization the two sections are represented by
$f$ and $1$. Hence on this open set
$$
\varphi_f(x)=[f(x):1]
$$
and the ratio of the two homogeneous coordinates is $f$.

Therefore in the common function field the rational function induced by
$\varphi_f$ is
$$
\frac{f}{1}=f.
$$
Therefore the morphism $\varphi_f$ represents the pullback of the original
rational map defined by $f$.
:::

:::

::: {.pf-step #g-birational-resolves-f}
The morphism $g:X'\to X$ is birational and resolves the rational
function $f$ in the required sense.

::: pf-proof
Every morphism used to construct $g$ is the blowup of a point on a
nonsingular surface. Each is birational, and a finite composition of
birational morphisms is birational. Hence $g$ is a birational morphism.

Step [](#morphism-to-p1){.pf-ref} gives a genuine morphism
$$
\varphi_f:X'\to\PP^1
$$
which agrees in the common function field with the rational function $f$.
This is exactly the required resolution.
:::

:::

::: pf-qed
Step [](#snc-resolution){.pf-ref} makes the divisor of $f$ simple normal crossings. Steps
[](#blowup-crossing-coefficient){.pf-ref}, [](#euclidean-algorithm-step){.pf-ref} and [](#zero-pole-disjoint){.pf-ref} separate its zero and pole divisors by finitely many additional
blowups. Steps [](#sections-and-zero-divisors){.pf-ref}, [](#pencil-base-point-free){.pf-ref} and [](#morphism-to-p1){.pf-ref} turn the resulting disjoint positive and negative
parts into a base-point-free pencil and hence a morphism to $\PP^1$.
Step [](#g-birational-resolves-f){.pf-ref} verifies that the composite modification is birational.
:::

:::
:::
