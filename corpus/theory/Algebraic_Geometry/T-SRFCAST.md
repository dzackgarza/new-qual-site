---
schema: qual/card@1
id: T-SRFCAST
kind: definition
title: Castelnuovo's contractibility criterion
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Minimal Models
  - Surfaces
relations:
- kind: uses
  target: FE-SRFBLOW
review: draft
prompts:
- State Castelnuovo's contractibility criterion.
- What is a $(-1)$-curve?
- What is a minimal surface?
- What is the minimal model program for surfaces?
---

A proper integral curve on a smooth surface is the exceptional curve of a blowup of a smooth surface at a point exactly when it is $\PP^1$ with self-intersection $-1$.
Being the whole exceptional locus belongs to the hypothesis: a curve that some composite contraction merely sends to a smooth point need not be a $(-1)$-curve.

::: {.definition}
Let $X$ be a smooth projective surface over a field.
A \dfn{$(-1)$-curve} on $X$ is a smooth integral curve $E\subseteq X$ with
$$
E\cong\PP^1
\qquad\text{and}\qquad
E^2=-1.
$$
A \dfn{minimal surface} is a smooth projective surface containing no $(-1)$-curves.
:::

::: {.theorem}
Let $X$ be a smooth surface, separated and of finite type over an algebraically closed field $k$, and let $E \subseteq X$ be an integral curve that is proper over $k$.
There exist a smooth surface $Y$ over $k$, a point $p \in Y$ and a morphism $\sigma \colon X \to Y$ that is the blowup of $Y$ at $p$ with exceptional curve $E$ if and only if $E \cong \PP^1$ and $E^2 = -1$.
Such a curve is also called an exceptional curve of the first kind.
Hartshorne prints the criterion for a nonsingular projective surface $X$ and a curve $E\subseteq X$ on it, in the direction that $E\cong\PP^1$ with $E^2=-1$ makes $X$ the monoidal transformation of a nonsingular projective surface at a point, with $E$ the exceptional curve [@Har77, Theorem V.5.7], the converse being [@Har77, §V.3, (3.1)].
Projectivity is needed in neither direction, and the hypotheses above are the Stacks Project's, by numbered statement; this paragraph is read in `tmp/sources/stacks-tags/0C2I.md`, which carries §54.16 in full at stacks-project commit a04446e57ec1fbc252a871afcec7752fb2807b14.
An integral curve $E\cong\PP^1$ with $E^2=-1$ on a smooth surface is an exceptional curve of the first kind in the sense of Stacks Project, §54.16 (tag 0C2I): its ideal is a height-one prime in the regular local ring of $X$, which is a UFD, so $E$ is an effective Cartier divisor; its normal sheaf is $\OO_E(E)$; and $E^2=-1$ is exactly the statement that this sheaf pulls back to $\OO_{\PP^1}(-1)$.
Such an $X$ is quasi-projective over $k$ without being assumed projective, $k$ being Noetherian and $X$ separated, of finite type and regular of dimension two over it: that is Stacks Project, Lemma 54.16.10 (tag 0C5N).
The base $\Spec k$ is a single point, so $E$ lies in a fibre of $X\to\Spec k$ automatically, and Stacks Project, Lemma 54.16.9(2) (tag 0C2N) gives a contraction $\sigma\colon X\to Y$ of $E$ with $Y$ quasi-projective over $k$; a contraction is by definition the blowup of a closed point $p\in Y$ with $\OO_{Y,p}$ regular of dimension two and $E$ its exceptional curve (Stacks Project, §54.16, tag 0C2I), and $Y$ is regular away from $p$ because $\sigma$ is an isomorphism there and $X$ is regular, so $Y$ is a smooth surface over the algebraically closed $k$, nonsingular in the sense of [@Har77, §I.5].
In the other direction the exceptional curve of the blowup of a regular point of dimension two is an exceptional curve of the first kind, hence is $\PP^1$ with normal sheaf $\OO_{\PP^1}(-1)$, so has $E^2=-1$ (Stacks Project, §54.16, tag 0C2I, whose claim rests on Lemma 54.3.1, tag 0AGQ).
If $X$ is projective over $k$, then so is $Y$: Stacks Project, Lemma 54.16.9(1) (tag 0C2N), which is Hartshorne's projective case [@Har77, Theorem V.5.7] with projectivity assumed on both sides.
:::

::: {.remark}
For smooth projective surfaces, Castelnuovo's criterion identifies nonminimality with the existence of a birational contraction to another smooth surface: repeatedly contracting $(-1)$-curves produces a minimal surface.
Since each contraction raises $K^2$ by one and $\rho$ drops by one, the process terminates.

By adjunction, $E \cong \PP^1$ with $E^2 = -1$ is equivalent to $E^2 = -1$ and $K \cdot E = -1$, which is the form the criterion is usually applied in.

A surface can have infinitely many $(-1)$-curves: the blowup of $\PP^2$ at $9$ points in general position, in the sense that no three of the points are collinear after any finite sequence of quadratic transformations centred at three of them, has infinitely many ([[P-AGH5415GENPOSITION]], part (e)), while for $r = 7$ and $r = 8$ points in general position there are exactly $56$ and $240$ (part (d)). The minimal model is not unique in general: a rational surface can contract to $\PP^2$ and also to a Hirzebruch surface.
:::
