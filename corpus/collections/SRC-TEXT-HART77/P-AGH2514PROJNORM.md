---
schema: qual/card@1
id: P-AGH2514PROJNORM
kind: problem
title: Projective normality of the $d$-uple embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Normality
  - Normal Schemes
  - Veronese Embedding
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read all four parts of Exercise II.5.14 in the original Hartshorne transcription. Retained the arbitrary base ring in (d), added the necessary integrality condition and the nonempty hypothesis in (a)-(c), and used the nonnegative section ideal as in II.5.10. The erratum gives the disconnected-base and empty-scheme counterexamples. The proof establishes section-ring integrality by a stable finite ideal, not by an unsupported noetherianity assumption on A.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a ring, and let $X$ be a closed subscheme of $\PP^r_A$.
Define the \dfn{homogeneous coordinate ring} $S(X)$ of $X$ for the given embedding to be $A[x_0,\ldots,x_r]/I$, where
$$
I=\bigoplus_{n\ge0}\Gamma(\PP^r_A,\mci_X(n))\subseteq A[x_0,\ldots,x_r]
$$
is the nonnegative section ideal of the ideal sheaf $\mci_X$.
If $A$ is a field and $X$ a variety, this coincides with the definition given in (I, §2).
Recall that a scheme $X$ is normal if its local rings are integrally closed domains.
A closed subscheme $X\subseteq\PP^r_A$ is \dfn{projectively normal} for the given embedding if $S(X)$ is an integrally closed domain (cf. (I, Ex. 3.18)).

Now assume $k$ is an algebraically closed field, and $X$ is a nonempty, connected, normal closed subscheme of $\PP^r_k$.
Show that for some $d>0$ the $d$-uple embedding of $X$ is projectively normal, as follows.

(a) Let $S$ be the homogeneous coordinate ring of $X$, and let $S'=\bigoplus_{n\ge0}\Gamma(X,\OO_X(n))$.
Show that $S$ is a domain, and that $S'$ is its integral closure.

(b) Use (Ex. 5.9) to show that $S_d=S'_d$ for all sufficiently large $d$.

(c) Show that $S^{(d)}$ is integrally closed for sufficiently large $d$, and conclude that the $d$-uple embedding of $X$ is projectively normal.

(d) For an arbitrary ring $A$, show that a closed subscheme $X\subseteq\PP^r_A$ is projectively normal if and only if it is integral and normal and, for every $n\ge0$, the natural map
$$
\Gamma(\PP^r_A,\OO_{\PP^r_A}(n))\longrightarrow\Gamma(X,\OO_X(n))
$$
is surjective.
:::

::: {.hint}
For part (a), first show that $X$ is integral.
Then regard $S'$ as the global sections of the sheaf of rings $\mcs=\bigoplus_{n\ge0}\OO_X(n)$ on $X$, and show that its stalks are integrally closed domains.
:::

::: {.solution}
Write $L=\OO_X(1)$ and $R(X,L)=\bigoplus_{n\ge0}\Gamma(X,L^{\otimes n})$.
Use the [[P-AGH2510SATIDEAL|saturated nonnegative section ideal]] in the definition of $S(X)$, so $X\cong\Proj S(X)$.
The natural map $S(X)\to R(X,L)$ is injective in every degree, since the kernel of restriction from the polynomial ring is precisely that ideal.
The section ring here uses nonnegative degrees, whereas the [[D-MODGRMOD|graded module $\Gamma_*$]] uses all integer degrees.

<1>1. The scheme $X$ in parts (a)--(c) is integral.

::: {.proof}
It is noetherian because it is closed in projective space over $k$.
A [[D-QJ5M9|normal]] scheme is reduced, since all its local rings are domains.
Distinct irreducible components cannot meet: at a point of intersection, their distinct minimal primes would give distinct minimal primes of the local ring, contradicting that it is a domain.
There are only finitely many irreducible components, so each is closed and its complement, a union of the others, is closed as well.
Thus every component is open.
Nonemptiness and connectedness force there to be exactly one component.
Hence $X$ is reduced and irreducible, so integral.
:::

<1>2. For an integral closed subscheme $X\subseteq\PP_A^r$ over any ring $A$, both $S=S(X)$ and $R=R(X,L)$ are domains, with
$$
S\subseteq R\subseteq\operatorname{Frac}S.
$$

::: {.proof}
Let $\eta$ be the generic point of $X$ and put $K=\OO_{X,\eta}$.
Choose a nonzero element $\tau\in L_\eta$ and an indeterminate $t$ over $K$.
Restriction to $\eta$ embeds each $\Gamma(X,L^{\otimes n})$ into the one-dimensional space $L_\eta^{\otimes n}$.
Indeed, a section with zero generic germ is zero on every trivializing affine open of the integral scheme.
Sending $a\tau^{\otimes n}$ to $at^n$ therefore embeds $R$ as a graded subring of $K[t]$.
Thus $R$, and its subring $S$, are domains.

Let $\ell$ be a nonzero coordinate section in $S_1$; one exists because the coordinates generate $L$ and $X$ is nonempty.
The chart $D_+(\ell)$ has coordinate ring $S_{(\ell)}=(S_\ell)_0$, with fraction field $K$.
The grading and the invertible degree-one element $\ell$ give
$$
S_\ell\cong S_{(\ell)}[\ell,\ell^{-1}].
$$
Taking $\tau=\ell_\eta$ in the preceding construction identifies $\ell$ with $t$, so $\operatorname{Frac}S=K(t)$.
A section of $L^{\otimes n}$ restricts on $D_+(\ell)$ to an element of $(S_\ell)_n$.
Its generic value therefore lies in $\operatorname{Frac}S$ under this same identification, proving the stated inclusions.
Changing $\tau$ rescales $t$ by an element of $K^\times$ and does not change the inclusion of $S$ in its section ring.
:::

<1>3. Under the hypotheses of step <1>2, the extension $S\subseteq R$ is integral, with no noetherian hypothesis on $A$.

::: {.proof}
Fix a homogeneous $u\in R_e$, with $e\ge0$.
Let $\ell_0,\ldots,\ell_r\in S_1$ be the coordinate sections.
For each nonzero $\ell_i$, the restriction of $u$ to $D_+(\ell_i)$ belongs to $(S_{\ell_i})_e$.
Consequently there is an integer $N\ge1$, chosen to work for all $i$, such that $\ell_i^N u\in S$.
For a zero coordinate this equality holds with value zero.

Put $q=(r+1)(N-1)+1$ and $J=S_+^q=S_{\ge q}$.
Every degree-$q$ monomial in the $r+1$ coordinates is divisible by some $\ell_i^N$.
Those monomials generate $J$, so $uJ\subseteq S$.
Since $e\ge0$, the products still have degree at least $q$, and hence $uJ\subseteq J$.
The ideal $J$ is finitely generated by these monomials and is nonzero because a nonzero coordinate has nonzero $q$th power in the domain $S$.

Choose generators $z_1,\ldots,z_a$ of $J$ and coefficients $c_{ij}\in S$ with $uz_j=\sum_i c_{ij}z_i$.
Multiplying the resulting matrix equation by the adjugate of $u\operatorname{id}-(c_{ij})$ shows that
$$
\det\bigl(u\operatorname{id}-(c_{ij})\bigr)z_j=0
$$
for every $j$.
Some $z_j$ is nonzero in the field $\operatorname{Frac}S$, so the determinant is zero.
This is a monic polynomial equation for $u$ over $S$.

Every element of $R$ is a finite sum of homogeneous elements.
The ring generated over $S$ by finitely many integral elements is a finite $S$-module, since their monic equations bound the powers needed to generate it.
The same determinant argument for multiplication on that finite module makes every element of it integral.
Thus every element of $R$ is integral over $S$.
:::

<1>4. If the integral scheme in step <1>2 is also [[D-QJ5M9|normal]], then $R$ is integrally closed in $\operatorname{Frac}S$.
Consequently $R$ is the integral closure of $S$, proving part (a).

::: {.proof}
Let $\mathscr R=\bigoplus_{n\ge0}L^{\otimes n}$ be the sheaf of graded algebras on $X$.
At a point $x$, a local frame of $L$ identifies
$$
\mathscr R_x\cong\OO_{X,x}[T].
$$
The local ring $\OO_{X,x}$ is a normal domain, so its polynomial ring is a normal domain by the [polynomial normality lemma](https://stacks.math.columbia.edu/tag/030A).
All these stalks embed in the field $K(t)=\operatorname{Frac}S$ from step <1>2 and have this fraction field.

Inside $K(t)$,
$$
R=\Gamma(X,\mathscr R)=\bigcap_{x\in X}\mathscr R_x.
$$
For the first equality, a section of a direct-sum sheaf has only finitely many nonzero degrees locally, and quasi-compactness of $X$ makes that set finite globally.
For the second, an element belonging to every stalk has a section representative on a neighborhood of each point.
Their generic values agree in $K(t)$, so they agree on overlaps and glue.
An element of $K(t)$ integral over $R$ is integral over each $\mathscr R_x$ and thus lies in each of them.
The intersection formula gives that it lies in $R$.

By step <1>3, $R$ is integral over $S$.
Conversely, an element of $\operatorname{Frac}S$ integral over $S$ is also integral over $R$, hence belongs to $R$ by the preceding argument.
Thus $R$ is exactly the integral closure of $S$.
For parts (a)--(c), step <1>1 supplies the integral scheme and $R=S'$.
:::

<1>5. There is an integer $n_0$ such that $S_n=S'_n$ for every $n\ge n_0$, proving part (b).

::: {.proof}
Here $S$ is a finitely generated graded $k$-algebra generated in degree one.
Apply [[P-AGH259GAMMASTAR]], part (b), with graded module $M=S$.
Its canonical comparison map is the inclusion
$$
S_n\longrightarrow\Gamma(X,\OO_X(n))=S'_n.
$$
That result makes this map an isomorphism for all sufficiently large $n$, proving equality under the given inclusions.
:::

<1>6. For every sufficiently large $d>0$, the ring $S^{(d)}$ is normal and is the homogeneous coordinate ring of the $d$-uple embedding, proving part (c).

::: {.proof}
The ring $\Gamma(X,\OO_X)$ is a finite-dimensional $k$-vector space by [[T-COHFIN|finiteness of coherent cohomology]] [@Har10a, Theorem III.5.2].
It is a domain by step <1>2, so multiplication by a nonzero element is an injective endomorphism of a finite-dimensional vector space, hence surjective.
Thus it is a field finite over the algebraically closed field $k$, and equals $k$.
Therefore $S_0=S'_0=k$.
For $d\ge\max(1,n_0)$, step <1>5 now gives
$$
S^{(d)}=(S')^{(d)}.
$$

To verify that a Veronese subring of a normal graded domain is normal, let $B$ be such a domain and let $z\in\operatorname{Frac}B^{(d)}$ be integral over $B^{(d)}$.
It is integral over $B$ and lies in $\operatorname{Frac}B$, so $z\in B$.
Write $z=a/b$ with $a,b\in B^{(d)}$ and $b\ne0$.
Decompose $B$ into its degree classes modulo $d$.
Multiplication by $b$ preserves those classes, and $bz=a$ has only class zero.
Since $B$ is a domain, the components of $z$ in all other classes must be zero.
Thus $z\in B^{(d)}$.
Applying this to $B=S'$ proves normality of $S^{(d)}$.

By [[P-AGH2513VERONESE]], the degree-$d$ monomials give the $d$-uple embedding of $X$, with graded image algebra $S^{(d)}$.
The kernel of its polynomial presentation is a homogeneous prime, since $S^{(d)}$ is a domain.
Some degree-one coordinate has nonzero image.
If a homogeneous polynomial belongs to the saturation of the kernel, a power of that coordinate times the polynomial belongs to the kernel; primality forces the polynomial itself into the kernel.
Hence the kernel is saturated, so its quotient $S^{(d)}$ is the homogeneous coordinate ring in the stated definition.
It is normal, proving projective normality.
:::

<1>7. The corrected criterion in part (d) holds over every ring $A$.

<2>1. Projective normality implies the integral and normal assertions and the surjectivity of every restriction map.

::: {.proof}
Suppose $S=S(X)$ is a normal domain.
The scheme $X$ is nonempty, since the section ideal of the empty subscheme is the entire polynomial ring and its coordinate ring is zero.
The homogeneous prime $(0)$ is a generic point of $\Proj S$, and all its nonempty standard affine charts are domains.
Thus $X$ is integral.

For a nonzero coordinate $\ell\in S_1$, the ring $S_\ell$ is normal by [localization of normal domains](https://stacks.math.columbia.edu/tag/00GY).
Put $C=(S_\ell)_0$.
If $z\in\operatorname{Frac}C$ is integral over $C$, it is integral over $S_\ell$ and hence lies in $S_\ell$.
Writing $bz=a$ with $a,b\in C$ and $b\ne0$, the graded decomposition shows that $z$ has only degree zero, since multiplication by $b$ preserves degree and is injective.
Thus $z\in C$.
Each such chart is normal, and its localizations are normal as well, so $X$ is [[D-QJ5M9|normal]].

Step <1>3 makes the section ring $R(X,L)$ integral over $S$ inside $\operatorname{Frac}S$.
Normality of $S$ forces $R(X,L)=S$.
For every $n\ge0$, the canonical map
$$
A[x_0,\ldots,x_r]_n\xrightarrow{\cong}\Gamma(\PP_A^r,\OO(n))
$$
is the isomorphism established in [[P-AGH2510SATIDEAL]], including $r=0$.
The restriction map has image $S_n=R(X,L)_n$, so it is surjective.
:::

<2>2. Conversely, integrality and normality of $X$, together with these surjections, imply projective normality.

::: {.proof}
The surjections identify every graded component of $S(X)$ with that of $R(X,L)$, since the kernels are the components of the defining section ideal.
They respect multiplication, giving $S(X)\cong R(X,L)$ as graded rings.
Steps <1>2 and <1>4 make the latter an integrally closed domain for every normal integral $X\subseteq\PP_A^r$.
Therefore $S(X)$ is an integrally closed domain.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 establish both implications without restricting the base ring.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove part (a), step <1>5 proves part (b), step <1>6 proves part (c), and step <1>7 proves part (d).
:::
:::

::: {.remark title="Errata and the degree-zero exception"}
The source part (d) states only normality and the restriction-map surjections, over an arbitrary ring $A$ [@Har10a, Exercise II.5.14(d)].
For a field $k$, take $A=k\times k$ and $X=\PP_A^1$.
Then $X$ is the disjoint union of two normal projective lines, and every restriction map is the identity.
Its homogeneous coordinate ring $A[x_0,x_1]$ is not a domain: the nonzero elements $(1,0)$ and $(0,1)$ have product zero.
The added integrality condition excludes this counterexample and is necessary by step <1>7.

The nonempty hypothesis in parts (a)--(c) excludes $X=\varnothing$, which is connected and normal under the usual definitions but has zero homogeneous coordinate ring.

The nonnegative section ideal in the definition agrees with the source's $\Gamma_*(\mci_X)$ for $r\ge1$.
For $r=0$, the all-integer-degree convention for $\Gamma_*$ can give negative components and hence not an ideal of $A[x_0]$; [[P-AGH2510SATIDEAL]] gives the explicit example and the nonnegative-degree formulation.
:::
