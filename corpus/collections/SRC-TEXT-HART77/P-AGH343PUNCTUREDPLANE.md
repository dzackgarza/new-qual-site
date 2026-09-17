---
schema: qual/card@1
id: P-AGH343PUNCTUREDPLANE
kind: problem
title: Cohomology of the punctured affine plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Affine Space
  - Non-Affine Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the cover computation, infinite-dimensionality and nonaffineness assertion with the retained Hartshorne Chapter III section 4 transcription. The proof computes the actual Laurent-polynomial quotient and proves independence of all surviving monomials, rather than only producing nonzero classes.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X=\AA_k^2=\Spec k[x, y]$, and let $U=X-\ts{(0,0)}$.
Using a suitable cover of $U$ by open affine subsets, show that $H^1(U, \mco_U)$ is isomorphic to the $k$-vector space spanned by $\ts{x^i y^j \st i, j<0}$.
In particular, it is infinite-dimensional.

Using (3.5), this provides another proof that $U$ is not affine — cf. (I, Ex. 3.6).
:::

::: {.solution}
Put $A=k[x,y]$, $U_x=D(x)$ and $U_y=D(y)$, viewed as open subsets of $X=\Spec A$.
Their union is $U$, since $V(x,y)$ consists of the origin.

<1>1. The affine cover $(U_x,U_y)$ identifies the requested group with
$$
H^1(U,\OO_U)\cong A_{xy}/(A_x+A_y).
$$

::: {.proof}
The two opens and their intersection are affine, with rings
$$
A_x=k[x,x^{-1},y],\qquad A_y=k[x,y,y^{-1}],\qquad
A_{xy}=k[x,x^{-1},y,y^{-1}].
$$
The scheme $U$ is noetherian and separated, and $\OO_U$ is quasi-coherent.
The affine-cover Čech comparison therefore computes sheaf cohomology by the complex
$$
A_x\oplus A_y\xrightarrow{(a,b)\mapsto b-a}A_{xy}
$$
in degrees zero and one [@Har10a, Theorem III.4.5].
There is no term in degree two for this two-member cover.
The image of the differential is the additive subgroup $A_x+A_y$, giving the displayed quotient.
All these maps are $k$-linear.
:::

<1>2. The classes of the Laurent monomials with both exponents negative form a basis, giving
$$
\boxed{H^1(U,\OO_U)\cong\bigoplus_{i<0,\ j<0}k\,x^iy^j.}
$$

::: {.proof}
The Laurent polynomial ring $A_{xy}$ has $k$-basis the monomials $x^iy^j$ for $(i,j)\in\ZZ^2$.
The subspace $A_x$ is spanned by those with $j\ge0$, while $A_y$ is spanned by those with $i\ge0$.
Thus $A_x+A_y$ is spanned by exactly the monomials for which at least one exponent is nonnegative.
The remaining monomials have $i,j<0$.
Uniqueness of Laurent polynomial coefficients gives a direct-sum decomposition into these two spans.
Projection onto the negative-negative span has kernel $A_x+A_y$ and is surjective onto that span.
It therefore induces the stated isomorphism on the quotient in step <1>1.
In particular, each element is a finite linear combination of the displayed basis monomials, with no additional linear relations.
:::

<1>3. The group is infinite-dimensional over $k$, and $U$ is not affine.

::: {.proof}
For $m\ge1$, the classes $x^{-m}y^{-1}$ are distinct members of the basis in step <1>2 and are linearly independent.
Hence the cohomology group is infinite-dimensional and nonzero.
If $U$ were affine, the higher cohomology of its quasi-coherent structure sheaf would vanish by [[T-COHAFF]] [@Har10a, Theorem III.3.5].
The nonzero group in degree one contradicts that vanishing, proving nonaffineness.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 give the requested cohomology computation and basis, and step <1>3 proves both consequences.
:::
:::
