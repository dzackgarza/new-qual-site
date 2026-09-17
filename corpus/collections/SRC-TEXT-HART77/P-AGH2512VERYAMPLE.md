---
schema: qual/card@1
id: P-AGH2512VERYAMPLE
kind: problem
title: Tensor products of very ample invertible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Very Ample Sheaves
  - Invertible Sheaves
  - Segre Embedding
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read Exercise II.5.12 and the immersion definition preceding Remark II.5.16.1 in the original Hartshorne transcription. The unrestricted version of (b) is false for that open-in-closed convention. The erratum proves nonexistence of any finite projective embedding in an explicit example, not only failure of the proposed Segre composite. The locally noetherian formulation and the arbitrary-base closed-in-open formulation are proved separately.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
(a) Let $X$ be a scheme over a locally noetherian scheme $Y$, and let $\mcl, \mcm$ be two very ample invertible sheaves on $X$ relative to $Y$.
Show that $\mcl \tensor \mcm$ is also very ample.

(b) Let $f: X \to Y$ and $g: Y \to Z$ be two morphisms of schemes, with $Z$ locally noetherian.
Let $\mcl$ be a very ample invertible sheaf on $X$ relative to $Y$, and let $\mcm$ be a very ample invertible sheaf on $Y$ relative to $Z$.
Show that $\mcl \tensor f^* \mcm$ is a very ample invertible sheaf on $X$ relative to $Z$.
:::

::: {.hint}
Use a Segre embedding.
:::

::: {.solution}
Use [[D-MODAMPLE|very ampleness]] and the [[D-MORIMM|immersion]] convention in which the source is an open subscheme of a closed subscheme of the target.
The locally noetherian hypotheses give a corrected formulation of the source exercise; the erratum treats its unrestricted version.

<1>1. For a scheme $B$ and nonnegative integers $r,s$, the Segre closed immersion
$$
\sigma:\PP_B^r\times_B\PP_B^s\longrightarrow\PP_B^{(r+1)(s+1)-1}
$$
satisfies
$$
\sigma^*\OO(1)\cong q_1^*\OO_{\PP_B^r}(1)\otimes q_2^*\OO_{\PP_B^s}(1),
$$
where $q_1,q_2$ are the projections.

::: {.proof}
The products $X_iY_j$ of the homogeneous coordinate sections generate the displayed tensor product of invertible sheaves and define $\sigma$.
On the target chart with $Z_{ij}\ne0$, its inverse image is $D_+(X_i)\times_B D_+(Y_j)$, and the coordinate map sends
$$
Z_{ab}/Z_{ij}\longmapsto (X_a/X_i)(Y_b/Y_j).
$$
The coordinates with $b=j$ and $a=i$ recover all affine coordinates of the two factors, so the map is surjective on coordinate rings.
Thus $\sigma$ is a closed immersion.
The construction by generating sections identifies its pullback of $\OO(1)$ with their invertible sheaf; equivalently, the chart frames are $X_iY_j$, with transition functions $(X_a/X_i)(Y_b/Y_j)$.
This construction commutes with base change, so the calculation over affine opens proves the assertion over every $B$; see the [Segre embedding](https://stacks.math.columbia.edu/tag/01WD) and [[P-AGH2511CARTPROD]].
:::

<1>2. A [[D-MORIMM|locally closed immersion]] into a locally noetherian scheme is an [[D-MORIMM|immersion]] in the source convention.

::: {.proof}
Let $h:V\to W$ be closed in an open subscheme $W'\subseteq W$.
For every affine open $T\subseteq W$, the open subset $T\cap W'$ of the noetherian space $T$ is quasi-compact.
Its closed subscheme $h^{-1}(T)$ is therefore quasi-compact.
Thus $h$ is quasi-compact.
The [factorization for quasi-compact immersions](https://stacks.math.columbia.edu/tag/01QV) writes $h$ as an open immersion followed by a closed immersion.
Concretely, its closed factor is defined by the quasi-coherent ideal $\ker(\OO_W\to h_*\OO_V)$; its restriction to $W'$ is the ideal defining $V$, so $V$ is open in that closed factor.
:::

<1>3. The assertion of part (a) holds.

::: {.proof}
Choose $Y$-immersions
$$
i:X\longrightarrow\PP_Y^r,\qquad j:X\longrightarrow\PP_Y^s
$$
with $i^*\OO(1)\cong\mcl$ and $j^*\OO(1)\cong\mcm$.
The graph $\Gamma_j:X\to X\times_Y\PP_Y^s$ is a closed immersion because $\PP_Y^s\to Y$ is separated.
The map $i\times\operatorname{id}:X\times_Y\PP_Y^s\to\PP_Y^r\times_Y\PP_Y^s$ is a base change of $i$.
Their composite is $(i,j)$, which is a locally closed immersion since closed and open immersions are stable under base change and locally closed immersions are stable under composition.
Consequently
$$
h=\sigma\circ(i,j):X\longrightarrow\PP_Y^{(r+1)(s+1)-1}
$$
is a locally closed immersion.
The target is locally noetherian, so step <1>2 makes $h$ an immersion in the source convention.
Step <1>1 gives
$$
h^*\OO(1)\cong i^*\OO(1)\otimes j^*\OO(1)\cong\mcl\otimes\mcm.
$$
This realizes the required very ample sheaf.
:::

<1>4. The assertion of part (b) holds.

::: {.proof}
Choose immersions over the indicated bases
$$
i:X\longrightarrow\PP_Y^r,\qquad j:Y\longrightarrow\PP_Z^s
$$
with $i^*\OO_{\PP_Y^r}(1)\cong\mcl$ and $j^*\OO_{\PP_Z^s}(1)\cong\mcm$.
Write $\pi:\PP_Y^r\to Y$ for the projection and $a:\PP_Y^r\to\PP_Z^r$ for the base-change map, so $\pi\circ i=f$.
The identification $\PP_Y^r\cong\PP_Z^r\times_Z Y$ gives the base change
$$
k=(a,j\circ\pi):\PP_Y^r\longrightarrow\PP_Z^r\times_Z\PP_Z^s
$$
of $j$.
The composite
$$
h=\sigma\circ k\circ i:X\longrightarrow\PP_Z^{(r+1)(s+1)-1}
$$
is a locally closed immersion.
Its target is locally noetherian, so step <1>2 gives the required open-in-closed factorization.
The twisting sheaf on relative projective space commutes with base change, giving $a^*\OO_{\PP_Z^r}(1)\cong\OO_{\PP_Y^r}(1)$ [@Har10a, Chapter II, §5].
Therefore step <1>1 gives
$$
\begin{aligned}
h^*\OO(1)
&\cong i^*a^*\OO_{\PP_Z^r}(1)\otimes (j\circ f)^*\OO_{\PP_Z^s}(1)\\
&\cong\mcl\otimes f^*\mcm.
\end{aligned}
$$
Thus this sheaf is very ample relative to $Z$.
:::

<1>5. With the closed-in-open immersion convention, the same two assertions hold over arbitrary base schemes.

::: {.proof}
The constructions in steps <1>3 and <1>4 already give locally closed immersions and the asserted pullbacks over arbitrary bases.
Only the conversion in step <1>2 used local noetherianity.
Omitting that conversion proves the arbitrary-base formulation when very ampleness is witnessed by a closed immersion into an open subscheme of a finite-dimensional relative projective space.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 prove the corrected assertions in the source convention, and step <1>5 proves their arbitrary-base closed-in-open formulation.
:::
:::

::: {.remark title="Erratum to the unrestricted source convention"}
Exercise II.5.12 does not state the locally noetherian hypotheses added here.
The definition preceding Remark II.5.16.1 uses open-in-closed immersions, not closed-in-open immersions [@Har10a, Chapter II, §5 and Exercise II.5.12].
With that definition, unrestricted part (b) is false.
The locally noetherian hypotheses are sufficient conditions for both assertions, not a claim of necessity in part (a).

Let $k$ be a field, put $A=k[x_1,x_2,\ldots]$, and let
$$
V=\Spec A,\qquad U=\bigcup_{n\ge1}D(x_n).
$$
On $D(x_n)$ take the ideal
$$
I_n=(x_1^n,\ldots,x_{n-1}^n,x_n-1,x_{n+1},x_{n+2},\ldots)A_{x_n}.
$$
For $m\ne n$, localizing $I_n$ at $x_m$ gives the unit ideal, so these ideals glue to a quasi-coherent ideal on $U$.
Its closed subscheme is
$$
W=\coprod_{n\ge1}W_n,\qquad
W_n=\Spec R_n,\qquad
R_n=k[x_1,\ldots,x_{n-1}]/(x_1^n,\ldots,x_{n-1}^n).
$$
In the structural map $A\to R_n$, the variable $x_n$ maps to $1$ and every $x_i$ with $i>n$ maps to $0$.
Each $W_n$ has one point, denoted $w_n$.
This is the [nonfactorizable immersion example](https://stacks.math.columbia.edu/tag/01QW).
The following argument strengthens its conclusion: $W$ has no open immersion over $A$ into any finite-type $A$-scheme.

Suppose such an open immersion existed.
A finite affine cover of the finite-type target would contain an affine member whose intersection with $W$ contains $W_n$ for an infinite set $E\subseteq\NN_{>0}$.
Since $W_n$ has only one point, its nonempty intersection with that member is all of $W_n$.
We would obtain an open immersion
$$
W_E=\coprod_{n\in E}W_n\longrightarrow\Spec B
$$
with $B$ a finite-type $A$-algebra.
Quotient $B$ by the kernel of $B\to\Gamma(W_E,\OO_{W_E})=\prod_{n\in E}R_n$.
Every element of that kernel restricts to zero on $W_E$, so this quotient preserves the open subscheme $W_E$.
Thus we may assume $B\subseteq\prod_{n\in E}R_n$.

The map $A\to B$ is injective.
Indeed, a nonzero polynomial in finitely many $x_i$ survives in $R_n$ whenever $n\in E$ exceeds every variable index and every exponent appearing in it.
Choose a presentation $B=A[t_1,\ldots,t_q]/J$ and put $K=\operatorname{Frac}A$.
The ideal $J_K\subset K[t_1,\ldots,t_q]$ is proper and has finitely many generators.
Choose $m$ so that the coefficients of these generators all belong to $K_m=k(x_1,\ldots,x_m)$, and put $A_m=k[x_1,\ldots,x_m]$.
Let $J^0\subset K_m[t_1,\ldots,t_q]$ be their generated ideal and set
$$
J_m=J^0\cap A_m[t_1,\ldots,t_q].
$$
Then
$$
J_K\cap A[t_1,\ldots,t_q]=J_m A[t_1,\ldots,t_q].
$$
To verify this equality, first pass from $A_m$ to $K_m$ and expand polynomials coefficientwise in the remaining $x_i$.
The module
$$
\bigl(K_m[t_1,\ldots,t_q]/J^0\bigr)[x_{m+1},x_{m+2},\ldots]
$$
is free over $K_m[x_{m+1},x_{m+2},\ldots]$, by choosing a $K_m$-basis of the coefficient algebra.
Consequently localization of that polynomial base to $K$ is injective, and contraction is computed coefficientwise as claimed.

The noetherian ring $A_m[t_1,\ldots,t_q]$ makes $J_m$ finitely generated, say by $F_1,\ldots,F_a$.
For each $F_j\in J_K$, choose a nonzero $d_j\in A$ such that $d_jF_j\in J$.
Choose $n\in E$ larger than $m$, than every variable index in the finitely many $d_j$, and than their total degrees.
Each $d_j$ has nonzero image in $R_n$.
Since $d_jF_j=0$ in $R_n$, the image of $F_j$ cannot be a unit in this local ring.
It therefore has zero residue at $w_n$.

It follows that $w_n$ lies in the closed subscheme
$$
H=\Spec\bigl(A[t_1,\ldots,t_q]/J_m A[t_1,\ldots,t_q]\bigr)
\subseteq\Spec B.
$$
Its coordinate ring is
$$
\bigl(A_m[t_1,\ldots,t_q]/J_m\bigr)[x_{m+1},x_{m+2},\ldots].
$$
Because $n>m$, multiplication by the monic polynomial $x_n-1$ is injective on this ring and remains injective in its nonzero local ring at $w_n$.
Thus $x_n-1$ is nonzero in $\OO_{H,w_n}$.
But $W_E$ is open in $\Spec B$, so $\OO_{\Spec B,w_n}=R_n$, in which $x_n-1=0$.
Its image in the quotient local ring $\OO_{H,w_n}$ must also be zero, a contradiction.
This proves the nonembedding assertion.

Now take $f:W\hookrightarrow U$ to be the closed immersion and $g:U\hookrightarrow V$ the open immersion, with $\mcl=\OO_W$ and $\mcm=\OO_U$.
Both sheaves are very ample over their respective bases using $\PP^0$ and the source immersion convention.
Their proposed tensor product is $\OO_W$.
If it were very ample over $V$, there would be an immersion of $W$ as an open subscheme of a closed subscheme of some $\PP_V^N$.
That closed subscheme is of finite type over $A$, contradicting the nonembedding assertion.
Hence the unrestricted conclusion of part (b) fails; failure of a particular Segre map is not the only obstruction.
:::
