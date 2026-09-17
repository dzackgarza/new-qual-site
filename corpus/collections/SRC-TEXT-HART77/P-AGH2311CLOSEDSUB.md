---
schema: qual/card@1
id: P-AGH2311CLOSEDSUB
kind: problem
title: Closed subschemes under base change and the scheme-theoretic image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Closed Subschemes
  - Base Change
  - Reduced Induced Structure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.11 statement and the standard scheme-theoretic-image construction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
a. Closed immersions are stable under base extension: if $f: Y \to X$ is a closed immersion and $X' \to X$ is any morphism, then $f': \fiberprod{Y}{X}{X'} \to X'$ is also a closed immersion.

b. If $Y$ is a closed subscheme of an affine scheme $X = \Spec A$, then $Y$ is also affine, and in fact $Y$ is the closed subscheme determined by a suitable ideal $\mfa \subseteq A$ as the image of the closed immersion $\Spec A/\mfa \to \Spec A$.

c. Let $Y$ be a closed subset of a scheme $X$ and give $Y$ the reduced induced subscheme structure.
If $Y'$ is any other closed subscheme of $X$ with the same underlying topological space, show that the closed immersion $Y \to X$ factors through $Y'$.
We express this by saying that **the reduced induced structure is the smallest subscheme structure on a closed subset**.

d. Let $f: Z \to X$ be a morphism.
Then there is a unique closed subscheme $Y$ of $X$ with the following property: the morphism $f$ factors through $Y$, and if $Y'$ is any other closed subscheme of $X$ through which $f$ factors, then $Y \to X$ factors through $Y'$ also.
We call $Y$ the **scheme-theoretic image** of $f$.
If $Z$ is a reduced scheme, then $Y$ is just the reduced induced structure on the closure of the image $f(Z)$.
:::

::: {.remark}
For part (b): first show that $Y$ can be covered by a finite number of open affine subsets of the form $D(f_i) \intersect Y$ with $f_i \in A$.
By adding some more $f_i$ with $D(f_i) \intersect Y = \varnothing$ if necessary, arrange that the $D(f_i)$ cover $X$.
Next show that $f_1, \ldots, f_r$ generate the unit ideal of $A$.
Then use the affineness criterion of II.2.17(b) to show that $Y$ is affine, and II.2.18(d) to show that $Y$ comes from an ideal $\mfa \subseteq A$.
A second proof using sheaves of ideals appears later in Hartshorne V.10.
:::

::: {.solution}
<1>1. Closed immersions are stable under arbitrary base change.
::: {.proof}
Let
\[
i:Y\hookrightarrow X
\]
be a closed immersion and let $X'\to X$ be any morphism.  The assertion is local on $X$ and $X'$.  Thus take
\[
X=\Spec A,
\qquad
Y=\Spec(A/I),
\qquad
X'=\Spec B.
\]
Then
\[
Y\times_XX'
\cong
\Spec\bigl((A/I)\otimes_AB\bigr)
\cong
\Spec(B/IB).
\]
The projection to $X'=\Spec B$ is induced by the quotient map
\[
B\twoheadrightarrow B/IB,
\]
so it is a closed immersion.
:::

<1>2. Let $i:Y\hookrightarrow X=\Spec A$ be a closed subscheme.  The scheme $Y$ has a finite affine cover of the form
\[
Y\cap D(f_1),\ldots,Y\cap D(f_r),
\qquad
f_i\in A.
\]
::: {.proof}
The underlying space of $Y$ is closed in the quasi-compact space $X$, hence is quasi-compact.  Cover $Y$ by affine open subsets of $Y$.

For each $y\in Y$, choose an affine open $W\subseteq Y$ containing $y$.  Write $W=Y\cap O$ for an open $O\subseteq X$.  Choose a distinguished open
\[
y\in D(f)\subseteq O.
\]
Then
\[
Y\cap D(f)=W\cap D(f)
\]
is distinguished inside the affine scheme $W$, hence is affine.  These opens cover $Y$, and quasi-compactness gives a finite subcover.
:::

<1>3. We may enlarge the list in <1>2 so that the distinguished opens $D(f_i)$ cover all of $X$, while every $Y\cap D(f_i)$ remains affine.
::: {.proof}
The opens from <1>2 cover $Y$.  The complement $X\setminus Y$ is covered by distinguished opens $D(g)$ contained in $X\setminus Y$.

Together these form an open cover of the affine scheme $X$, hence a finite subcover.  Add the finitely many selected $g$'s to the list.  For every added one,
\[
Y\cap D(g)=\varnothing,
\]
which is affine.
:::

<1>4. The functions $f_1,\ldots,f_r$ from <1>3 generate the unit ideal of $A$.
::: {.proof}
Since the $D(f_i)$ cover $\Spec A$,
\[
V(f_1,\ldots,f_r)=\varnothing.
\]
Therefore
\[
(f_1,\ldots,f_r)=A.
\]
:::

<1>5. The closed subscheme $Y$ is affine.
::: {.proof}
Let
\[
B=\Gamma(Y,\mathcal O_Y).
\]
The restrictions of the $f_i$ to $Y$ are elements of $B$ and generate the unit ideal there, because the relation
\[
\sum_i a_if_i=1
\]
from <1>4 restricts to $Y$.

Their nonvanishing loci are
\[
Y_{f_i}=Y\cap D(f_i),
\]
which are affine by <1>3.  Hartshorne II.2.17(b) therefore implies that $Y$ is affine.
:::

<1>6. There is an ideal $I\subseteq A$ such that
\[
Y\cong\Spec(A/I)
\]
over $X=\Spec A$.
::: {.proof}
By <1>5, write
\[
Y=\Spec B.
\]
The closed immersion induces a ring homomorphism
\[
\phi:A\longrightarrow B.
\]
By definition, a closed immersion is a homeomorphism onto a closed subset and its map of structure sheaves is surjective.  Hartshorne II.2.18(d) therefore shows that $\phi$ is surjective.

Let
\[
I=\ker\phi.
\]
Then $B\cong A/I$, and the given closed immersion is the standard map
\[
\Spec(A/I)\hookrightarrow\Spec A.
\]
:::

<1>7. Let $Y\subseteq X$ be closed and give it the reduced induced structure.  If $Y'\subseteq X$ is any closed subscheme with the same underlying topological space, then
\[
Y\longrightarrow X
\]
factors uniquely through $Y'$.
::: {.proof}
This is local on $X$.  Take $X=\Spec A$.  By <1>6, write
\[
Y'=\Spec(A/I).
\]
Its underlying closed subset is
\[
V(I).
\]
The reduced induced structure on the same set is
\[
Y=\Spec(A/\sqrt I).
\]
Since
\[
I\subseteq\sqrt I,
\]
there is a quotient homomorphism
\[
A/I\longrightarrow A/\sqrt I,
\]
and therefore a factorization
\[
Y\longrightarrow Y'\longrightarrow X.
\]
It is unique because $Y'\to X$ is a monomorphism, as every immersion is.
:::

<1>8. Let $f:Z\to X$ be any morphism.  Consider all quasi-coherent ideal sheaves
\[
\mathcal I_\lambda\subseteq\mathcal O_X
\]
such that $f$ factors through the corresponding closed subscheme $Y_\lambda\subseteq X$, and put
\[
\mathcal I=\sum_\lambda\mathcal I_\lambda.
\]
Then $\mathcal I$ is a quasi-coherent ideal sheaf.
::: {.proof}
The family is nonempty because $X$ itself is a closed subscheme of $X$, corresponding to the zero ideal sheaf.

On an affine open $U=\Spec A\subseteq X$, each restriction $\mathcal I_\lambda|_U$ corresponds to an ideal $I_\lambda\subseteq A$.  Their sheaf-theoretic sum restricts to the sheaf associated to
\[
\sum_\lambda I_\lambda\subseteq A,
\]
because localization commutes with arbitrary sums of submodules.  Hence $\mathcal I$ is quasi-coherent.
:::

<1>9. Let $Y\subseteq X$ be the closed subscheme defined by $\mathcal I$ from <1>8.  Then $f$ factors through $Y$.
::: {.proof}
Factoring through $Y_\lambda$ means that the pullback of $\mathcal I_\lambda$ to $Z$ maps to zero in $\mathcal O_Z$.  Therefore the pullback of their sum
\[
\mathcal I=\sum_\lambda\mathcal I_\lambda
\]
also maps to zero.

Affine-locally, if $Y\cap U=\Spec(A/I)$, this says that the ring map defining $f$ kills $I$, hence factors through $A/I$.  These local factorizations glue, giving a factorization
\[
Z\longrightarrow Y\longrightarrow X.
\]
:::

<1>10. The closed subscheme $Y$ from <1>9 is contained in every closed subscheme $Y'\subseteq X$ through which $f$ factors.
::: {.proof}
Let $\mathcal I_{Y'}$ be the ideal sheaf of such a $Y'$.  It is one of the summands used to define $\mathcal I$, so
\[
\mathcal I_{Y'}\subseteq\mathcal I.
\]
The inclusion of ideals reverses under $\Spec$ and gives a unique factorization
\[
Y\longrightarrow Y'\longrightarrow X.
\]
:::

<1>11. Hence $Y$ is the unique scheme-theoretic image of $f$.
::: {.proof}
Steps <1>9 and <1>10 show that $Y$ has the defining minimality property.  If two closed subschemes had that property, each would factor through the other over $X$, and the resulting maps would be inverse because closed immersions are monomorphisms.  Thus the scheme-theoretic image is unique.
:::

<1>12. Assume now that $Z$ is reduced, and put
\[
T=\overline{f(Z)}\subseteq X.
\]
Then $f$ factors through the reduced induced subscheme $T_{\mathrm{red}}$.
::: {.proof}
This is local on $X$.  Let $U=\Spec A\subseteq X$ and write
\[
T\cap U=V(J)
\]
with $J$ radical, so
\[
T_{\mathrm{red}}\cap U=\Spec(A/J).
\]

Take $a\in J$.  For every point
\[
z\in f^{-1}(U),
\]
the point $f(z)$ lies in $T\cap U$, so the germ of $f^*a$ at $z$ maps to zero in the residue field $\kappa(z)$.

On an affine open $W=\Spec C\subseteq f^{-1}(U)$, the section $f^*a$ corresponds to an element $c\in C$ lying in every prime ideal of $C$.  Hence $c$ is nilpotent.  Since $Z$ is reduced, $C$ is reduced, so $c=0$.

Thus the ring map $A\to\Gamma(W,\mathcal O_Z)$ kills $J$ on every affine $W$, and $f|_{f^{-1}(U)}$ factors through $\Spec(A/J)$.  These local factorizations glue.
:::

<1>13. The reduced induced subscheme $T_{\mathrm{red}}$ is contained in every closed subscheme $Y'\subseteq X$ through which $f$ factors.
::: {.proof}
If $f$ factors through $Y'$, then
\[
f(Z)\subseteq|Y'|.
\]
Since $|Y'|$ is closed,
\[
T=\overline{f(Z)}\subseteq|Y'|.
\]

Affine-locally, write
\[
Y'\cap U=\Spec(A/I),
\qquad
T\cap U=V(J)
\]
with $J$ radical.  The inclusion $T\subseteq V(I)$ means
\[
I\subseteq J.
\]
Hence
\[
A/I\longrightarrow A/J
\]
induces a factorization
\[
T_{\mathrm{red}}\cap U\longrightarrow Y'\cap U.
\]
These factorizations glue over $X$.
:::

<1>14. If $Z$ is reduced, the scheme-theoretic image of $f$ is exactly
\[
\boxed{\overline{f(Z)}_{\mathrm{red}}.}
\]
::: {.proof}
Step <1>12 shows that $f$ factors through $T_{\mathrm{red}}$, and <1>13 shows that this closed subscheme is contained in every other closed subscheme through which $f$ factors.  By uniqueness in <1>11, it is the scheme-theoretic image.
:::

<1>15. Q.E.D.
::: {.proof}
Step <1>1 proves part (a); steps <1>2--<1>6 prove part (b); <1>7 proves part (c); and steps <1>8--<1>14 prove part (d).
:::
:::
