---
schema: qual/card@1
id: P-AGH347PLANECURVEGENUS
kind: problem
title: Čech computation of the cohomology of a plane curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Plane Curves
  - Arithmetic Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the two affine charts, the complex and both requested dimensions with the retained Hartshorne Chapter III section 4 transcription. Made the positive-degree plane-curve convention explicit. Monic division yields free coefficient modules and a Laurent-monomial decomposition of the whole complex without assuming the equation is irreducible or reduced.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be a field and let $X$ be the closed subscheme of $\PP_k^2$ defined by a single homogeneous equation $f(x_0,x_1,x_2)=0$ of degree $d\ge1$.
(Do not assume $f$ is irreducible.)
Assume that $(1,0,0)$ is not on $X$.
Then show that $X$ can be covered by the two open affine subsets $U=X \intersect \theset{x_1 \neq 0}$ and $V=X \intersect \theset{x_2 \neq 0}$.
Now calculate the Čech complex
$$
\Gamma(U, \mco_X) \oplus \Gamma(V, \mco_X) \to \Gamma(U \intersect V, \mco_X)
$$
explicitly, and thus show that
$$
\begin{aligned}
\dim H^0(X, \mco_X)&=1, \\
\dim H^1(X, \mco_X)&=\frac{1}{2}(d-1)(d-2).
\end{aligned}
$$
:::

::: {.solution}
The coefficient of $x_0^d$ in $f$ is $f(1,0,0)$, which is nonzero by hypothesis.
Multiplying $f$ by the inverse of this coefficient does not change $X$, so assume that the coefficient is $1$.

::: pf

::: {.pf-step #s1}

The two indicated affine opens cover $X$ and have coordinate rings
$$
B=k[t,a]/(f(a,1,t)),\qquad C=k[s,b]/(f(b,s,1)),
$$
where $a=x_0/x_1$, $t=x_2/x_1$ on $U$, and $b=x_0/x_2$, $s=x_1/x_2$ on $V$.

::: pf-proof

The only point of $\PP^2$ with $x_1=x_2=0$ is $[1:0:0]$.
Since it does not belong to $X$, the opens $U$ and $V$ cover $X$.
Each is a closed subscheme of a standard affine chart of projective space, with the displayed dehomogenized equation.
Thus both are affine, with precisely these coordinate rings.
Their intersection has coordinate ring
$$
D=B[t^{-1}]=C[s^{-1}],
$$
and the change of coordinates is $s=t^{-1}$ and $b=a/t$.
Homogeneity gives $f(a,1,t)=t^d f(a/t,t^{-1},1)$, so these substitutions identify the two localized quotients.

:::

:::

::: {.pf-step #s2}

As $k$-vector spaces, the Čech complex is the direct sum, for $0\le i<d$, of the complexes
$$
k[t]\oplus t^{-i}k[t^{-1}]\xrightarrow{(u,v)\mapsto v-u}k[t,t^{-1}],
$$
with the $i$th complex multiplied by $a^i$.

::: pf-proof

The polynomial $f(a,1,t)$ is monic of degree $d$ in $a$.
Polynomial division therefore makes $B$ a free $k[t]$-module with basis $1,a,\ldots,a^{d-1}$.
Existence of the remainder follows by division by a monic polynomial, and uniqueness follows because a nonzero multiple of that polynomial cannot have $a$-degree less than $d$.
The same argument makes $C$ free over $k[s]$ with basis $1,b,\ldots,b^{d-1}$.
Localizing gives
$$
D=\bigoplus_{i=0}^{d-1}a^i k[t,t^{-1}].
$$
The maps $B\to D$ and $C\to D$ are injective, since multiplication by $t$ or $s$ on the respective free coefficient module is injective.
Under the coordinate change in step [](#s1){.pf-ref}, their images are
$$
B=\bigoplus_{i=0}^{d-1}a^i k[t],\qquad
C=\bigoplus_{i=0}^{d-1}a^i t^{-i}k[t^{-1}].
$$
Consequently the difference of restrictions decomposes into exactly the displayed coefficientwise maps.
The scheme $X$ is noetherian and separated, and $\OO_X$ is quasi-coherent.
Its cohomology is therefore computed by this two-affine Čech complex [@Har10a, Theorem III.4.5].

:::

:::

::: {.pf-step #s3}

The kernel of the Čech differential consists precisely of the constant functions, so $\boxed{\dim_k H^0(X,\OO_X)=1}$.

::: pf-proof

The kernel is identified with $B\cap C$ in $D$.
In its $a^i$ component, it is the intersection
$$
k[t]\cap t^{-i}k[t^{-1}].
$$
The first space has only exponents at least zero, and the second only exponents at most $-i$.
For $i=0$ their intersection is $k$; for every $i>0$ it is zero.
Uniqueness of Laurent coefficients therefore gives $B\cap C=k$ in the constant $a^0$ component.
The corresponding sections are the same constant on both charts and are exactly the global constant functions.

:::

:::

::: {.pf-step #s4}

The first cohomology has basis
$$
\left\{[a^it^{-j}]:2\le i\le d-1,\ 1\le j\le i-1\right\},
$$
and $\boxed{\dim_k H^1(X,\OO_X)=\frac{(d-1)(d-2)}2}$.

::: pf-proof

The cokernel in component $i$ is
$$
k[t,t^{-1}]/\bigl(k[t]+t^{-i}k[t^{-1}]\bigr).
$$
Its surviving Laurent exponents are the integers strictly between $-i$ and zero.
There are none for $i=0,1$, and for $i\ge2$ they give the basis $t^{-1},\ldots,t^{-(i-1)}$.
The free decomposition of $D$ from step [](#s2){.pf-ref} proves independence between different $a^i$ components as well.
Thus the displayed classes form a basis of the entire cokernel, which is $H^1(X,\OO_X)$.
Their number is
$$
\sum_{i=2}^{d-1}(i-1)=\frac{(d-1)(d-2)}2
$$
for $d\ge2$, and both the basis and the formula give zero for $d=1$.
No step used irreducibility or absence of nilpotents in $B$ or $C$; monicity was the necessary property.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the affine-cover assertion, step [](#s2){.pf-ref} calculates its Čech complex, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} compute the two requested dimensions.

:::

:::

:::

::: {.remark title="Positive degree"}
The condition $d\ge1$ is the plane-curve range of this calculation.
A nonzero constant equation instead defines the empty subscheme, which also avoids $[1:0:0]$ but has zero global-section group.
Thus the stated $H^0$ formula requires the positive-degree hypothesis.
:::
