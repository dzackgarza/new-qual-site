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
---

::: {.problem}
The following statement holds: if $X$ is a nonsingular curve and $Y$ is a projective variety, then every rational map $\varphi: X \dashrightarrow Y$ extends to a morphism on all of $X$.

Show by example that this result is false if either

(a) $\dim X \geq 2$, or

(b) $Y$ is not projective.
:::

::: {.solution}
<1>1. The extension theorem fails in dimension two even when the target is projective.

::: {.proof}
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

<1>2. The extension theorem fails for a nonprojective target even when the source is a nonsingular curve.

::: {.proof}
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

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves failure when the source has dimension at least two, and step <1>2 proves failure when the target is not projective.
:::
:::
