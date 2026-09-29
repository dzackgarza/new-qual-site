---
schema: qual/card@1
id: P-AGH53MULTIPLICITY
kind: problem
title: Multiplicity $\mu_P(Y)$ of a point on a plane curve and its tangent directions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Singularities
  - Plane Curves
  - Multiplicity
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both requests with the retained Hartshorne I.5.3 transcription. The multiplicity calculation includes the two additional singular points of the third quartic that occur in characteristics 7 and 13, as established on the preceding exercise card.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $Y \subseteq \AA^2$ be a curve defined by the equation $f(x,y) = 0$, and let $P = (a,b)$ be a point of $\AA^2$.
Make a linear change of coordinates so that $P$ becomes the point $(0,0)$.
Write $f$ as a sum $f = f_0 + f_1 + \cdots + f_d$, where $f_i$ is homogeneous of degree $i$ in $x$ and $y$.
Define the *multiplicity* of $P$ on $Y$, denoted $\mu_P(Y)$, to be the least $r$ with $f_r \neq 0$.
Note that $P \in Y$ if and only if $\mu_P(Y) > 0$.
The linear factors of $f_r$ are called the *tangent directions* at $P$.

1. Show that $\mu_P(Y) = 1$ if and only if $P$ is a nonsingular point of $Y$.

2. Find the multiplicity of each of the singular points of the four quartics $x^2 = x^4 + y^4$, $xy = x^6 + y^6$, $x^3 = y^2 + x^4 + y^4$, and $x^2 y + x y^2 = x^4 + y^4$.
:::

::: {.solution}
Translate coordinates so that the point under consideration is the origin, as in the statement.
Then $P\in Y$ means $f_0=0$.

::: pf

::: {.pf-step #linear-part-formula}
The linear homogeneous part of the translated equation is
$$
f_1=f_x(P)x+f_y(P)y.
$$

::: pf-proof
Write the original coordinates as $X=a+x$ and $Y=b+y$.
For a monomial $X^iY^j$, the terms of total degree one after substitution are
$$
i a^{i-1}b^j x+j a^i b^{j-1}y.
$$
Summing over the monomials of $f$ gives exactly the displayed expression.
This computation is polynomial and is valid in every characteristic.
:::

:::

::: {.pf-step #multiplicity-one-criterion}
One has
$$
\boxed{\mu_P(Y)=1\quad\Longleftrightarrow\quad P\text{ is nonsingular on }Y.}
$$

::: pf-proof
Because $P\in Y$, the multiplicity is one exactly when $f_1\ne0$.
By step [](#linear-part-formula){.pf-ref} this is equivalent to
$$
(f_x(P),f_y(P))\ne(0,0).
$$
For a plane hypersurface, the Jacobian criterion says precisely that $P$ is nonsingular when at least one first partial derivative is nonzero [@Har10a, Chapter I, §5].
This proves part (1).
:::

:::

::: {.pf-step #origin-multiplicities}
At the origin, the multiplicities of the four curves from Exercise I.5.1 are
$$
\boxed{2,\quad2,\quad2,\quad3}
$$
in the order listed.

::: pf-proof
The defining polynomials, grouped by degree, begin as
$$
\begin{aligned}
f_1&=x^2-(x^4+y^4),\\
f_2&=xy-(x^6+y^6),\\
f_3&=-y^2+x^3-(x^4+y^4),\\
f_4&=(x^2y+xy^2)-(x^4+y^4).
\end{aligned}
$$
Their first nonzero homogeneous pieces have degrees $2,2,2,3$, respectively.
By the definition in the statement, these degrees are exactly the four multiplicities.
The corresponding tangent cones are
$$
x^2,\qquad xy,\qquad -y^2,\qquad xy(x+y),
$$
agreeing with the tacnode, node, cusp, and ordinary triple point identified in [[P-AGH51PLANECURVESING]].
:::

:::

::: {.pf-step #char-7-13-multiplicity}
In characteristics $7$ and $13$, the two additional singular points of the third curve also have multiplicity $2$.

::: pf-proof
By [[P-AGH51PLANECURVESING]], these points are
$$
P_\pm=\left(\frac34,\ \pm\sqrt{-\frac12}\right).
$$
Their first-order terms vanish because they are singular.
For
$$
f_3=x^3-y^2-x^4-y^4,
$$
the second partial derivatives are
$$
(f_3)_{xx}=6x-12x^2,\qquad
(f_3)_{xy}=0,\qquad
(f_3)_{yy}=-2-12y^2.
$$
At either $P_\pm$ they become
$$
(f_3)_{xx}=-\frac94,\qquad (f_3)_{yy}=4.
$$
These values are nonzero in characteristics $7$ and $13$.
Hence the translated equation has a nonzero quadratic part and no nonzero term of lower degree, so its multiplicity is $2$.
:::

:::

::: pf-qed
Steps [](#linear-part-formula){.pf-ref} and [](#multiplicity-one-criterion){.pf-ref} prove the nonsingularity criterion, while steps [](#origin-multiplicities){.pf-ref} and [](#char-7-13-multiplicity){.pf-ref} give the multiplicity of every singular point occurring under the characteristic hypothesis of Exercise I.5.1.
:::

:::

:::
