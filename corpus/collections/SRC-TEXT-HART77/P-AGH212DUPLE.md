---
schema: qual/card@1
id: P-AGH212DUPLE
kind: problem
title: The $d$-uple embedding of $\PP^n$ in $\PP^N$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Veronese Embedding
  - Homogeneous Ideals
  - Twisted Cubic
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all four parts and the image-calculation hint with the retained Hartshorne I.2.12 transcription. Explicit binomial relations cover the target by pure-power charts and recover every source coordinate, proving equality of the image and zero set in every characteristic.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed.
For given $n, d > 0$, let $M_0, M_1, \ldots, M_N$ be all the monomials of degree $d$ in the $n+1$ variables $x_0,\ldots,x_n$, where $N = \binom{n+d}{n} - 1$.
Define $\rho_d : \PP^n \to \PP^N$ by
$$
\rho_d\qty{ \tv{a_0 : \cdots : a_n} } = \tv{ M_0(a) : \cdots : M_N(a) } .
$$
This is the **$d$-uple embedding** of $\PP^n$ in $\PP^N$.
For example, when $n = 1$ and $d = 2$ we have $N = 2$, and the image of the $2$-uple embedding of $\PP^1$ in $\PP^2$ is a conic.

(a) Let $\theta: k[y_0,\ldots,y_N] \to k[x_0,\ldots,x_n]$ be the homomorphism sending $y_i \mapsto M_i$, and let $\mfa = \ker \theta$.
Show that $\mfa$ is a homogeneous prime ideal, so that $Z(\mfa)$ is a projective variety in $\PP^N$.

(b) Show that the image of $\rho_d$ is exactly $Z(\mfa)$.

(c) Show that $\rho_d$ is a homeomorphism of $\PP^n$ onto the projective variety $Z(\mfa)$.

(d) Show that the twisted cubic curve in $\PP^3$ is the $3$-uple embedding of $\PP^1$ in $\PP^3$, for a suitable choice of coordinates.
:::

::: {.hint}
For (b), one inclusion follows from the definition of $\ker\theta$; the other can be checked by recovering the source coordinates on affine charts.
:::

::: {.solution}
Index the degree-$d$ monomials by tuples $\alpha=(\alpha_0,\ldots,\alpha_n)$ of nonnegative integers with $\sum_j\alpha_j=d$.
Write $x^\alpha=\prod_jx_j^{\alpha_j}$ and denote its target coordinate by $y_\alpha$.
Let $e_i$ be the $i$th coordinate vector in $\ZZ^{n+1}$, and put $T=k[y_\alpha]$, $S=k[x_0,\ldots,x_n]$ and $V=Z(\mfa)$.

<1>1. The map $\rho_d$ is well-defined, and $\mfa=\ker\theta$ is a homogeneous prime ideal with nonempty projective zero set.

::: {.proof}
For a nonzero source vector $a$, some $a_i\ne0$, so the monomial $a_i^d$ is nonzero and the list of target coordinates is not zero.
Scaling $a$ by $\lambda\in k^\times$ scales every degree-$d$ monomial by $\lambda^d$.
Thus the projective image is independent of the representative.

If $F=\sum_qF_q\in T$ is its homogeneous decomposition, then $\theta(F_q)$ is homogeneous of degree $dq$ in $S$.
These degrees are distinct for distinct $q$, so $\theta(F)=0$ implies $\theta(F_q)=0$ for each $q$.
Hence $\mfa$ is homogeneous.
It is prime because $T/\mfa$ is isomorphic to the subring $\im\theta$ of the domain $S$.
Every point $\rho_d(a)$ satisfies its equations, since $F\in\mfa$ means $F((x^\alpha)_\alpha)=0$ as a polynomial.
In particular $V$ is nonempty, and [[P-AGH24CORRESPONDENCE]] makes it an irreducible projective algebraic set.
This proves (a).
:::

<1>2. The opens $V_i=V\cap D_+(y_{de_i})$ cover $V$.

::: {.proof}
For every index $\alpha$, the binomial
$$
y_\alpha^d-\prod_{i=0}^n y_{de_i}^{\alpha_i}
$$
belongs to $\mfa$, since its two monomials have the same image $x^{d\alpha}$ under $\theta$.
If all the pure-power coordinates $y_{de_i}$ vanished at a point of $V$, these relations would give $y_\alpha^d=0$ for every $\alpha$.
Over a field that forces every $y_\alpha=0$, which is not a projective point.
Thus at least one pure-power coordinate is nonzero.
:::

<1>3. On $V_i$, the inverse coordinates are
$$
a_i=1,\qquad
a_j=\frac{y_{(d-1)e_i+e_j}}{y_{de_i}}\quad(j\ne i),
$$
and they prove $\rho_d(\PP^n)=V$.

::: {.proof}
Fix $b\in V_i$ and use the displayed ratios evaluated at $b$ to define $a$; with $a_i=1$ the vector is nonzero.
For every $\alpha$, the binomial relation
$$
y_\alpha y_{de_i}^{d-1}
-\prod_{j=0}^n y_{(d-1)e_i+e_j}^{\alpha_j}\in\mfa
$$
follows by applying $\theta$: both terms become $x^\alpha x_i^{d(d-1)}$.
Divide this relation at $b$ by $y_{de_i}^d$.
Since $y_{(d-1)e_i+e_i}=y_{de_i}$, it gives
$$
\frac{y_\alpha(b)}{y_{de_i}(b)}=\prod_{j=0}^n a_j^{\alpha_j}=a^\alpha.
$$
These are all the normalized coordinates of $b$, so $\rho_d([a])=b$.
Step <1>2 covers every point of $V$ by such a chart, proving the reverse inclusion in (b); the forward inclusion was proved in step <1>1.

Conversely, on the source chart $x_i\ne0$ the displayed ratio pulls back to
$$
\frac{x_i^{d-1}x_j}{x_i^d}=\frac{x_j}{x_i}.
$$
It therefore recovers the source point uniquely.
This proves injectivity as well as surjectivity, and uses no choice of a $d$th root.
:::

<1>4. The bijection $\rho_d:\PP^n\to V$ and its inverse are continuous.

::: {.proof}
For a homogeneous polynomial $F\in T$ of degree $q$, the polynomial $\theta(F)$ is homogeneous of degree $dq$, or zero.
Thus the inverse image of its projective zero set is $Z(\theta(F))$, a closed subset of $\PP^n$.
Intersecting such zero sets proves continuity of $\rho_d$.

On $V_i$, the inverse from step <1>3 maps to the affine source chart $x_i\ne0$ and has coordinate functions $y_{(d-1)e_i+e_j}/y_{de_i}$.
These are regular functions on that affine target chart.
A polynomial equation in the source affine coordinates pulls back to a polynomial in these coordinate ratios, so its zero set is closed in $V_i$.
The inverse is therefore continuous on each $V_i$.
The $V_i$ form an open cover, and their inverses agree because step <1>3 proves uniqueness of the preimage.
They give a continuous global inverse, proving (c).
The same formulas also show that both directions are morphisms of varieties.
:::

<1>5. The projective twisted cubic is the image of
$$
\boxed{\rho_3:\PP^1\longrightarrow\PP^3,\qquad
[u:v]\longmapsto[u^3:u^2v:uv^2:v^3].}
$$

::: {.proof}
The four displayed coordinates are precisely the degree-three monomials in $u,v$.
On $u\ne0$, put $t=v/u$.
The image is $[1:t:t^2:t^3]$, the affine twisted cubic of [[P-AGH29PROJCLOSURE]] in the chart where the first coordinate is nonzero.
By steps <1>1--<1>4, the whole image is closed and is homeomorphic to the irreducible projective line.
The open subset $u\ne0$ is dense in that line, so its image is dense in the whole image.
Consequently the whole image is exactly the projective closure of the affine twisted cubic, as required in (d).
The remaining point $[0:1]$ maps to $[0:0:0:1]$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves (a), steps <1>2--<1>3 prove (b), step <1>4 proves (c), and step <1>5 proves (d).
:::
:::
