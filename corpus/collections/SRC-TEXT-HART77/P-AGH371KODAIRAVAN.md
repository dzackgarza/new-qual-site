---
schema: qual/card@1
id: P-AGH371KODAIRAVAN
kind: problem
title: Vanishing of global sections of an inverse ample sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Ample Sheaves
  - Vanishing Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the hypotheses and vanishing assertion with the retained Hartshorne III.7.1 transcription. The proof keeps an arbitrary ground field: global functions form a finite field extension, not necessarily k, and a positive-degree hypersurface replaces any assumption of a rational point or a suitable k-hyperplane.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension $\geq 1$ over a field $k$, and let $\mcl$ be an ample invertible sheaf on $X$. Show that
$$
H^0(X, \mcl^{-1}) = 0
.
$$

This is a special case of Kodaira vanishing.
:::

::: {.solution}
Tensor powers of the invertible sheaf $\mcl$ are written $\mcl^a$ for $a\in\ZZ$.

<1>1. The ring $K_0=H^0(X,\OO_X)$ is a finite field extension of $k$.

::: {.proof}
Finiteness of coherent cohomology on a projective scheme makes $K_0$ finite-dimensional over $k$ [@Har10a, Theorem III.5.2].
Restriction to the generic point is injective because $X$ is integral, so $K_0$ is a domain.
Multiplication by any nonzero element is therefore an injective endomorphism of this finite-dimensional vector space, hence is surjective.
In particular that element has an inverse in $K_0$.
Thus $K_0$ is a field, and every nonzero global regular function is a unit at every point of $X$.
:::

<1>2. One has $\boxed{H^0(X,\mcl^{-1})=0}$.

::: {.proof}
Suppose $s$ is a nonzero section of $\mcl^{-1}$.
Choose $m>0$ for which $\mcl^m$ is very ample, using [@Har10a, Theorem II.7.6].
Its immersion $i:X\to\PP_k^N$ is closed because $X$ is proper, and $i^*\OO(1)=\mcl^m$.
Choose a closed point $x\in X$.
Since $X$ has positive dimension, its homogeneous ideal is strictly contained in the homogeneous ideal of the closed subscheme $\{x\}\subseteq\PP^N$.
There is consequently a positive-degree homogeneous polynomial $h$, of some degree $q>0$, vanishing at $x$ but not identically on $X$.
It gives a nonzero section of $\mcl^{mq}$ whose fibre value at $x$ is zero.

The product $h s^{\otimes mq}$ is a global section of $\OO_X$.
Its generic value is nonzero, since both factors have nonzero generic values on the integral scheme.
Its value at $x$ is zero.
This contradicts step <1>1, which makes every nonzero global function a unit at $x$.
Thus no such $s$ exists.
The argument does not assume that $x$ is $k$-rational or that $k$ is infinite.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 establishes the required vanishing under exactly the stated hypotheses.
:::
:::
