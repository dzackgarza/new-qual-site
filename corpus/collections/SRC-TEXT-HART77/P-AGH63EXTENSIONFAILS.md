---
schema: qual/card@1
id: P-AGH63EXTENSIONFAILS
kind: problem
title: Failures of extension for rational maps
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingular Curves
  - Rational Maps
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.3 and the rational-map extension theorem I.6.8 in the Hartshorne source. The solution gives independent counterexamples for the source-dimension and target-projectivity hypotheses. The title was corrected because the dimension-two counterexample has indeterminacy at a codimension-two point, not a codimension-one locus.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Exercise I.6.3 as printed, whose text is exactly the two
    alternatives. Both counterexamples on the card are correct. In (a) the
    rational map A^2 dash P^1, (x,y) to (x:y), cannot extend: on the punctured
    x-axis and the punctured y-axis an extension would take the constant values
    [1:0] and [0:1], and separatedness of P^1 spreads each value to the origin,
    which is impossible. In (b) the affine source A^1 with t to 1/t has no
    extension to 0, since an extension would be a polynomial p with t p(t) = 1,
    while the same function extends to P^1. Repaired the published-solution
    remark: it claimed that the (b) answers of Borcherds and Egbert are the
    identity on an affine source and so do not exhibit a failure of extension,
    and that no retained set states a counterexample for (b) whose map fails to
    extend. Both claims are false as the answers are meant. The source P^1 is
    the curve and P^1 minus infinity names the open subset carrying the
    rational map, so the map is the identity of A^1 viewed on P^1; it does not
    extend, because a morphism P^1 to A^1 is constant as k[P^1] = k, or
    equivalently because an extension agreeing with the identity on the dense
    open A^1 would equal the identity by separatedness and could not land in
    A^1, which is the argument Cutrone-Marshburn give. The remark now states
    this, keeps the note that their printed domain P^1 minus A^1 is wrong, and
    presents the card's own affine example as the same failure with the pole at
    the origin as the obstruction. The quotations were checked in the text
    versions, and the Borcherds and Egbert page numbers in the PDFs.
---

::: {.problem}
The following statement holds: if $X$ is a nonsingular curve and $Y$ is a projective variety, then every rational map $\varphi: X \dashrightarrow Y$ extends to a morphism on all of $X$.

Show by example that this result is false if either

(a) $\dim X \geq 2$, or

(b) $Y$ is not projective.
:::

::: {.solution}
::: pf

::: {.pf-step #dimension-two-counterexample}
The extension theorem fails in dimension two even when the target is projective.

::: pf-proof
Take
$$
X=\AA_k^2=\Spec k[x,y],\qquad Y=\PP_k^1,
$$
and define on $X\setminus\{(0,0)\}$ the morphism
$$
\varphi(x,y)=[x:y].
$$
This represents a rational map $X\dashrightarrow\PP^1$.

Suppose it extended to a morphism
$$
\overline\varphi:\AA^2\longrightarrow\PP^1.
$$
On the punctured $x$-axis, $\varphi(t,0)=[1:0]$.
The restriction of $\overline\varphi$ to the whole $x$-axis is a morphism $\AA^1\to\PP^1$ which agrees with the constant map $[1:0]$ on the dense open subset $\AA^1\setminus\{0\}$.
Since $\PP^1$ is separated, two morphisms agreeing on a dense open subset of the integral scheme $\AA^1$ agree everywhere.
Hence
$$
\overline\varphi(0,0)=[1:0].
$$

Applying the same argument to the $y$-axis, where
$$
\varphi(0,t)=[0:1]\qquad(t\ne0),
$$
gives
$$
\overline\varphi(0,0)=[0:1],
$$
a contradiction.
Thus the rational map does not extend across the origin.
This disproves the dimension-$\ge2$ analogue while retaining a projective target.
:::

:::

::: {.pf-step #nonprojective-target-counterexample}
The extension theorem fails for a nonprojective target even when the source is a nonsingular curve.

::: pf-proof
Take
$$
X=\AA_k^1=\Spec k[t],\qquad Y=\AA_k^1,
$$
and define on $D(t)=\AA^1\setminus\{0\}$ the morphism
$$
\psi(t)=t^{-1}.
$$
This is a rational map $X\dashrightarrow Y$.

If it extended to a morphism $\overline\psi:\AA^1\to\AA^1$, then $\overline\psi$ would correspond to a polynomial $p(t)\in k[t]$.
On the dense open set $D(t)$ we would have
$$
p(t)=t^{-1},
$$
so $tp(t)=1$ in the function field $k(t)$.
Since both sides lie in $k[t]$, this would be a polynomial identity, impossible because $t$ is not a unit in $k[t]$.
Thus $t^{-1}$ has no extension over $0$ with values in $\AA^1$.

The same rational function does extend to $\PP^1$ by sending $0$ to $\infty$, which isolates precisely the missing projectivity of the target in this example.
:::

:::

::: pf-qed
Step [](#dimension-two-counterexample){.pf-ref} proves failure when the source has dimension at least two, and step [](#nonprojective-target-counterexample){.pf-ref} proves failure when the target is not projective.
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 6.3, PDF p. 8, text version `tmp/sources/hartshorne-solutions-borcherds.md`: (a) "map $\AA^2\setminus(0,0)$ to $\PP^1$ by $(x,y)\mapsto(x:y)$"; (b) "map $\PP^1\setminus\infty$ to $\AA^1$ in the obvious way", that is, the identity of $\AA^1$. Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.6.3, PDF p. 54, text version `tmp/sources/hartshorne-solutions-egbert.md`, gives the same two answers, the second with the formula $(x:y)\mapsto x/y$. Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.6.3, PDF p. 24, text version `tmp/sources/hartshorne-solutions-cutrone-marshburn.md`: (a) the same map, with the observation that it is not regular at the origin; (b) "let $Y=\AA^1$, then $\varphi:\PP^1\setminus\AA^1$ defined by $(x:y)\mapsto x/y$; if $\varphi$ had an extension, then the identity map and $\varphi$ would agree on some dense open set, and thus be equal, which is a contradiction". The domain printed there is wrong, since $\PP^1\setminus\AA^1$ is the single point at infinity, but the argument is the one for the identity of $\AA^1$: if $h:\PP^1\to\AA^1$ extended it, then $h$ and the identity of $\PP^1$ would agree on the dense open $\AA^1$, hence be equal because $\PP^1$ is separated, and the image of $h$ would not lie in $\AA^1$.

Read this way, (b) is settled in all three sets by the identity of $\AA^1$ viewed as a rational map on $\PP^1$, and the obstruction is that $\PP^1$ admits no nonconstant morphism to the affine line, since its only global functions are the constants. Read instead with source $\AA^1$, the identity is everywhere defined and would not be a counterexample; the phrase $\PP^1\setminus\infty$ names the open subset of $\PP^1$ carrying the rational map, which is the reading under which the answers work. Step [](#dimension-two-counterexample){.pf-ref} follows (a) in all three sets and closes the separatedness argument they leave at "this map is not regular at the origin". Step [](#nonprojective-target-counterexample){.pf-ref} gives the affine form of the same failure: $\AA^1\dashrightarrow\AA^1$, $t\mapsto t^{-1}$, has no extension to $t=0$ because an extension would be a polynomial $p$ with $tp(t)=1$, and the same rational function does extend to $\PP^1$.
:::
