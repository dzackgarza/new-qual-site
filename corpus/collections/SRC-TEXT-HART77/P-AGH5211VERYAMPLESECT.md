---
schema: qual/card@1
id: P-AGH5211VERYAMPLESECT
kind: problem
title: Base points and very ampleness for sections of a ruled surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.11 and the retained Egbert companion calculation. The
    proof uses the standard restriction sequence along the normalized section
    C_0, with O_X(C_0+b f)|_{C_0}=O_C(b+e), and the fibre restriction
    O_X(C_0+b f)|_f=O_{P^1}(1). For part (b), the retained source's informal
    point/tangent argument is replaced by the equivalent length-two-subscheme
    criterion: the stated nonspeciality hypotheses force H^1 to vanish after
    subtracting every degree-two divisor on the base, so sections restrict
    surjectively to the corresponding doubled or paired fibres.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $X$ be a ruled surface over the curve $C$, defined by a normalized bundle $\mathcal{E}$, and let $\mfe$ be the divisor on $C$ for which $\mathcal{L}(\mfe) \cong \bigwedge^2 \mathcal{E}$ (See 2.8.1). Let $\mfb$ be any divisor on $C$.

a. If $|\mfb|$ and $|\mfb + \mfe|$ have no base points, and if $\mfb$ is nonspecial, then there is a section $D \sim C_0+\mfb f$, and $|D|$ has no base points.

b. If $\mfb$ and $\mfb + \mfe$ are very ample on $C$, and for every point $P \in C$, we have $\mfb-P$ and $\mfb+\mfe-P$ nonspecial, then $C_0+\mfb f$ is very ample.
:::

::: {.solution}
Write
$$
\pi:X=\PP(\mathcal E)\longrightarrow C
$$
for the ruling and put
$$
L=\OO_X(C_0+\mfb f).
$$
For a divisor $A$ on $C$, write $Af=\pi^*A$.

<1>1. If $\mfb-A$ is nonspecial, then
$$
h^0\bigl(X,L(-Af)\bigr)
=
h^0\bigl(C,\OO_C(\mfb-A)\bigr)
+
h^0\bigl(C,\OO_C(\mfb+\mfe-A)\bigr).
$$

::: {.proof}
The normalized section $C_0$ gives the exact sequence
$$
0
\longrightarrow
\OO_X((\mfb-A)f)
\longrightarrow
\OO_X(C_0+(\mfb-A)f)
\longrightarrow
\OO_{C_0}(C_0+(\mfb-A)f)
\longrightarrow0.
$$
Under the identification $C_0\cong C$, the ruled-surface conventions of
(2.8.1) give
$$
\OO_{C_0}(C_0+(\mfb-A)f)
\cong
\OO_C(\mfb+\mfe-A).
$$
Also
$$
\OO_X((\mfb-A)f)=\pi^*\OO_C(\mfb-A),
$$
so
$$
H^i\bigl(X,\OO_X((\mfb-A)f)\bigr)
\cong
H^i\bigl(C,\OO_C(\mfb-A)\bigr),
$$
because $\pi_*\OO_X=\OO_C$ and $R^1\pi_*\OO_X=0$.
The nonspeciality hypothesis says that the $H^1$ group on the left term
vanishes. Taking cohomology therefore gives the displayed sum of dimensions.
:::

<1>2. Under the hypotheses of part (a), for every point $P\in C$,
$$
h^0\bigl(X,L(-Pf)\bigr)=h^0(X,L)-2.
$$

::: {.proof}
Since $|\mfb|$ is base-point free,
$$
h^0(\mfb-P)=h^0(\mfb)-1.
$$
The exact sequence
$$
0\to\OO_C(\mfb-P)\to\OO_C(\mfb)\to k(P)\to0
$$
has surjective evaluation map on global sections. Since $\mfb$ is
nonspecial, its long exact sequence gives
$$
H^1(C,\OO_C(\mfb-P))=0.
$$
Thus step <1>1 applies both to $A=0$ and to $A=P$.

Because $|\mfb+\mfe|$ is also base-point free,
$$
h^0(\mfb+\mfe-P)=h^0(\mfb+\mfe)-1.
$$
Subtracting the two formulas from step <1>1 therefore gives
$$
h^0(X,L)-h^0\bigl(X,L(-Pf)\bigr)=2.
$$
:::

<1>3. The complete linear system $|L|$ restricts to the complete system
$|\OO_{\PP^1}(1)|$ on every fibre of $\pi$. In particular, $|L|$ has no
base points.

::: {.proof}
For the fibre
$$
F_P=\pi^{-1}(P)\cong\PP^1,
$$
one has
$$
L|_{F_P}\cong\OO_{\PP^1}(1).
$$
The exact sequence
$$
0\to L(-Pf)\to L\to L|_{F_P}\to0
$$
shows that the kernel of the restriction map on global sections is
$H^0(X,L(-Pf))$. By step <1>2 the image has dimension $2$, which equals
$$
h^0(\PP^1,\OO(1)).
$$
Hence
$$
H^0(X,L)\twoheadrightarrow H^0(F_P,\OO_{F_P}(1))
$$
for every $P$.

The system $|\OO_{F_P}(1)|$ has no base point. Since every point of $X$ lies
on some fibre, $|L|$ has no base points on $X$.
:::

<1>4. Under the hypotheses of part (a), there is a member
$$
D\in|C_0+\mfb f|
$$
which is a section of $\pi$.

::: {.proof}
Put
$$
V=H^0(X,L).
$$
By step <1>3, for each $P\in C$ the kernel of
$$
V\longrightarrow H^0(F_P,\OO_{F_P}(1))
$$
has codimension $2$. Consider the incidence set
$$
I={(P,[s])\in C\times\PP(V):s|_{F_P}=0\}.
$$
Its fibre over $P$ is the projectivization of that codimension-two kernel,
so
$$
\dim I\le\dim\PP(V)-1.
$$
The projection $I\to\PP(V)$ has closed image because $C$ is projective.
Thus a section $s\in V$ can be chosen whose divisor $D=(s=0)$ contains no
fibre.

Since
$$
D\cdot f=(C_0+\mfb f)\cdot f=1,
$$
and $D$ contains no fibre, every irreducible component of $D$ dominates
$C$.  An effective Cartier divisor on the nonsingular surface $X$ is pure of
dimension one, and the sum of the generic degrees of its horizontal
components, counted with multiplicity, is $D\cdot f=1$.  Thus $D$ has one
horizontal component, with multiplicity one; in particular $D$ is integral.
The proper morphism
$$
\pi|_D:D\longrightarrow C
$$
is therefore finite of degree one and birational. Since $C$ is nonsingular,
hence normal, a finite birational map to $C$ is an isomorphism. Thus $D$ is
a section of the ruling. Together with step <1>3 this proves part (a).
:::

<1>5. Assume the hypotheses of part (b). Then $\mfb$ is nonspecial, and
part (a) applies; in particular $L$ is base-point free and restricts
surjectively to $\OO_{\PP^1}(1)$ on every fibre.

::: {.proof}
Fix any point $P\in C$. By hypothesis
$$
H^1(C,\OO_C(\mfb-P))=0.
$$
The long exact sequence of
$$
0\to\OO_C(\mfb-P)\to\OO_C(\mfb)\to k(P)\to0
$$
then gives
$$
H^1(C,\OO_C(\mfb))=0.
$$
Thus $\mfb$ is nonspecial. The divisors $\mfb$ and $\mfb+\mfe$ are very
ample, hence base-point free, so all hypotheses of part (a) hold. Steps
<1>2--<1>4 therefore apply.
:::

<1>6. Let $A$ be any effective divisor of degree $2$ on $C$, including a
double point $2P$. Then both
$$
\mfb-A
\qquad\text{and}\qquad
\mfb+\mfe-A
$$
are nonspecial.

::: {.proof}
Choose a point $P$ contained in $A$, and write
$$
A=P+Q,
$$
allowing $Q=P$.

Since $\mfb$ is very ample, every length-two divisor imposes two independent
conditions, so
$$
h^0(\mfb-A)=h^0(\mfb)-2.
$$
Also $\mfb$ is base-point free, hence
$$
h^0(\mfb-P)=h^0(\mfb)-1.
$$
By hypothesis $\mfb-P$ is nonspecial. In the exact sequence
$$
0\to\OO_C(\mfb-A)
\to\OO_C(\mfb-P)
\to\OO_Q(\mfb-P)
\to0,
$$
the global-section dimensions show that the last evaluation map is
surjective. The resulting long exact sequence therefore gives
$$
H^1(C,\OO_C(\mfb-A))=0.
$$

The identical argument, using the very ampleness of $\mfb+\mfe$ and the
assumed nonspeciality of $\mfb+\mfe-P$, gives
$$
H^1(C,\OO_C(\mfb+\mfe-A))=0.
$$
:::

<1>7. For every effective degree-two divisor $A$ on $C$, restriction is
surjective:
$$
H^0(X,L)
\twoheadrightarrow
H^0\bigl(\pi^{-1}(A),L|_{\pi^{-1}(A)}\bigr).
$$

::: {.proof}
Apply the normalized-section exact sequence from step <1>1 to
$$
L(-Af)=\OO_X(C_0+(\mfb-A)f).
$$
Step <1>6 makes the $H^1$ groups of both the left term
$$
\OO_X((\mfb-A)f)
$$
and the quotient on $C_0$
$$
\OO_C(\mfb+\mfe-A)
$$
vanish. Hence
$$
H^1(X,L(-Af))=0.
$$

Now use
$$
0\to L(-Af)
\to L
\to L|_{\pi^{-1}(A)}
\to0.
$$
The vanishing just proved makes the restriction map on $H^0$ surjective.
:::

<1>8. The line bundle $L$ separates every zero-dimensional subscheme of
$X$ of length $2$.

::: {.proof}
Let $Z\subset X$ have length $2$.

If $Z$ is contained in one fibre $F_P$, step <1>5 gives a surjection
$$
H^0(X,L)\twoheadrightarrow H^0(F_P,\OO_{F_P}(1)).
$$
Since $\OO_{\PP^1}(1)$ separates every length-two subscheme of $\PP^1$,
the composite map onto $H^0(Z,L|_Z)$ is surjective.

Suppose $Z$ is not contained in a fibre. Its scheme-theoretic image on the
nonsingular curve $C$ is then a degree-two effective divisor $A$; this is
either the sum of the two base points of two distinct fibres or the double
point $2P$ when $Z$ is a tangent direction transverse to the fibre. Moreover
the definition of scheme-theoretic image makes
$$
\OO_A\longrightarrow (\pi|_Z)_*\OO_Z
$$
injective. Both sides have length $2$, so this map is an isomorphism and
$Z\cong A$.

Step <1>7 gives
$$
H^0(X,L)\twoheadrightarrow
H^0\bigl(\pi^{-1}(A),L|_{\pi^{-1}(A)}\bigr).
$$
Over the Artinian scheme $A$, the surface $\pi^{-1}(A)$ is the projective
bundle $\PP(\mathcal E|_A)$ and $L$ is its relative $\OO(1)$ tensored by a
line bundle from $A$. The subscheme $Z\cong A$ is a section, hence corresponds
to a quotient of the rank-two bundle on $A$ by an invertible sheaf. Since
$A$ is affine, taking global sections of that quotient is surjective. Thus
the restriction map from $H^0(\pi^{-1}(A),L)$ to $H^0(Z,L|_Z)$ is
surjective, and so is the composite from $H^0(X,L)$.
:::

<1>9. Under the hypotheses of part (b),
$$
\boxed{C_0+\mfb f\text{ is very ample}.}
$$

::: {.proof}
A line bundle on a projective scheme is very ample exactly when its complete
linear system separates every zero-dimensional subscheme of length $2$;
equivalently, it separates distinct points and tangent vectors, as in
[[T-DIVMAPPN]]. Step <1>8 proves this criterion for $L$. Hence $L$ is very
ample, proving part (b).
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove part (a), and steps <1>5--<1>9 prove part (b).
:::
:::
