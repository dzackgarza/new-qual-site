---
schema: qual/card@1
id: P-AGH281DIFFNONCLOSED
kind: problem
title: Differentials at nonclosed points and regularity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves of Differentials
  - Regular Local Rings
  - Separable Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts and the coefficient-field hint with the retained Hartshorne II.8.1 transcription. Checked the quotient differential sequence and localization against Stacks Project section 10.131 and the local dimension formula against Tag 00P1. Constructed a coefficient field modulo the square of the maximal ideal and retained irreducible schemes that need not be reduced in part (c).
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Here we strengthen the results of the text to include information about the sheaf of differentials at a not necessarily closed point of a scheme $X$.

(a) Generalize (8.7) as follows. Let $B$ be a local ring containing a field $k$, and assume that the residue field $k(B) = B/\mfm$ of $B$ is a separably generated extension of $k$.
Then the exact sequence of (8.4A),
$$
0 \to \mfm/\mfm^2 \mapsvia{\delta} \Omega_{B/k} \tensor k(B) \to \Omega_{k(B)/k} \to 0
$$
is exact on the left also.

(b) Generalize (8.8) as follows. With $B, k$ as above, assume furthermore that $k$ is perfect and that $B$ is a localization of an algebra of finite type over $k$.
Show that $B$ is a regular local ring if and only if $\Omega_{B/k}$ is free of rank $\dim B + \trdeg k(B)/k$.

(c) Strengthen (8.15) as follows. Let $X$ be an irreducible scheme of finite type over a perfect field $k$, and let $\dim X = n$.
For any point $x \in X$, not necessarily closed, show that the local ring $\OO_{x, X}$ is a regular local ring if and only if the stalk $(\Omega_{X/k})_x$ is free of rank $n$.

(d) Strengthen (8.16) as follows. If $X$ is a variety over an algebraically closed field $k$, then $U = \theset{x \in X \st \OO_x \text{ is a regular local ring}}$ is an open dense subset of $X$.
:::

::: {.hint}
For (a), in copying the proof of Proposition II.8.7, first pass to $B/\mfm^2$, which is a complete local ring, and then use Theorem II.8.25A to choose a field of representatives containing $k$.
:::

::: {.solution}
For the local statements put $\mathfrak m=\mfm$ and $K=B/\mathfrak m$.
Tensor products with $K$ are over $B$ unless indicated otherwise.
Use the [[D-4GCH6|universal derivation]] $d:B\to\Omega_{B/k}$.

::: pf

::: {.pf-step #s1}

The quotient map $C=B/\mathfrak m^2\to K$ has a $k$-algebra section $j:K\to C$.

::: pf-proof

Put $N=\mathfrak m/\mathfrak m^2$, the maximal ideal of $C$; then $N^2=0$.
Choose a separating transcendence basis $(t_i)$ for $K/k$, so that $K$ is separable algebraic over $F=k(t_i)$.
Lift the $t_i$ to elements of $C$.
Every nonzero polynomial in the lifts has nonzero residue, by algebraic independence, and is therefore a unit of the local ring $C$.
The lifts consequently define a copy of the field $F$ in $C$, with the required residue map.

Consider embeddings into $C$ of intermediate fields $F\subseteq E\subseteq K$ that extend this copy of $F$ and are sections of the residue map on $E$.
An increasing chain has its union as an upper bound, so Zorn's lemma gives a maximal such embedded field $E$.
If $\alpha\in K\setminus E$, its minimal polynomial $p(T)\in E[T]$ is separable.
Choose a lift $a\in C$ of $\alpha$ and view the coefficients of $p$ in $C$.
Then $p(a)\in N$ and $p'(a)$ is a unit because its residue is $p'(\alpha)\ne0$.
The element
$$
a'=a-\frac{p(a)}{p'(a)}
$$
satisfies $p(a')=0$: expanding the polynomial, the linear correction cancels $p(a)$ and all higher correction terms lie in $N^2=0$.
Thus $E[T]/(p)$ embeds in $C$, since a unital map from this field is injective, and its residue map identifies it with $E(\alpha)\subseteq K$.
This contradicts maximality.
Hence $E=K$, giving $j$.
This proves the coefficient-field assertion needed from the hint without a noetherian assumption on $B$.

:::

:::

::: {.pf-step #s2}

The map $\delta:N\to\Omega_{B/k}\otimes_B K$ is injective, proving (a).

::: pf-proof

Let $\rho:C\to K$ be the residue map and use the section from step [](#s1){.pf-ref}.
Define
$$
D:C\longrightarrow N,\qquad c\longmapsto c-j(\rho(c)).
$$
It is additive and annihilates $k$.
Writing $c=j(\bar c)+a$ and $c'=j(\bar c')+a'$ with $a,a'\in N$ gives
$$
D(cc')=\bar c\,D(c')+\bar c'\,D(c),
$$
since $aa'=0$.
Thus $D$ is a $k$-derivation into the $C$-module $N$, on which $C$ acts through $K$.
Its composite with $B\to C$ is also a $k$-derivation and induces a $K$-linear map
$$
r:\Omega_{B/k}\otimes_B K\longrightarrow N.
$$
For $b\in\mathfrak m$, one has $r(db\otimes1)=b\bmod\mathfrak m^2$.
Therefore $r\circ\delta=\id_N$, proving injectivity.
The middle and right exactness are the quotient differential sequence [@Har10a, Proposition II.8.4A], whose first map is $b\bmod\mathfrak m^2\mapsto db\otimes1$.
This proves the entire short exact sequence; the chosen splitting is not asserted to be canonical.

:::

:::

::: {.pf-step #s3}

For the ring in (b), put $t=\operatorname{trdeg}_kK$ and $e=\dim_K(\mathfrak m/\mathfrak m^2)$.
Then
$$
\dim_K(\Omega_{B/k}\otimes_B K)=e+t.
$$

::: pf-proof

The ring $B$ is noetherian because it is a localization of a finite-type $k$-algebra.
Its differential module is generated by the differentials of finitely many algebra generators before localization: differentiation of a polynomial uses these generators, and $d(s^{-1})=-s^{-2}ds$ adds none after localization.
Thus $\Omega_{B/k}$ is a finite $B$-module.
The residue field is finitely generated over $k$.
Since $k$ is perfect, every finitely generated extension of $k$ is separably generated [@Har10a, Theorem I.4.8A].
The field-differential formula gives $\dim_K\Omega_{K/k}=t$ [@Har10a, Theorem II.8.6A].
Taking dimensions in the short exact sequence of step [](#s2){.pf-ref} proves the equality.

:::

:::

::: {.pf-step #s4}

The local ring $B$ is regular if and only if $\Omega_{B/k}$ is free of rank $\dim B+t$.

::: pf-proof

If $\Omega_{B/k}$ is free of that rank, step [](#s3){.pf-ref} gives $e+t=\dim B+t$, so $e=\dim B$.
This is the definition of regularity for the noetherian local ring $B$.

Conversely, suppose $B$ is regular and put $r=\dim B+t$.
Step [](#s3){.pf-ref} says its differential module has an $r$-dimensional residue space.
Lift a basis and apply Nakayama's lemma to obtain a surjection
$$
B^{\oplus r}\twoheadrightarrow\Omega_{B/k}.
$$
A regular local ring is a domain [@Har10a, Remark II.6.11.1A]; write $L=\operatorname{Frac}B$.
There is a finite-type $k$-domain $A$ and a prime $\mathfrak p$ with $B=A_{\mathfrak p}$: start with a finite-type presentation for $B$ and quotient by the kernel of its map to this domain.
The [dimension formula for finite-type algebras](https://stacks.math.columbia.edu/tag/00P1), together with $\dim A=\operatorname{trdeg}_k L$, gives
$$
\operatorname{trdeg}_k L=\dim B+\operatorname{trdeg}_kK=r.
$$
Again $L/k$ is separably generated, so $\dim_L\Omega_{L/k}=r$.
Localizing differentials identifies $\Omega_{B/k}\otimes_B L$ with $\Omega_{L/k}$.
Our surjection consequently becomes an isomorphism after tensoring with $L$.
Its kernel is therefore a torsion submodule of the free module $B^{\oplus r}$ and must be zero, since $B$ is a domain.
Thus the original surjection is an isomorphism, proving (b).

:::

:::

::: {.pf-step #s5}

For the irreducible finite-type scheme in (c), the rank in step [](#s4){.pf-ref} is $n$ at every point.

::: pf-proof

Choose an affine neighborhood $\Spec A$ of $x$ and let $\mathfrak p$ correspond to $x$.
The reduced ring $A_{\mathrm{red}}$ is a domain because $X$ is irreducible.
It has dimension $n$: its fraction field is the function field of $X_{\mathrm{red}}$, and the dimension of every nonempty affine open in this integral finite-type scheme is its transcendence degree over $k$.
Reduction does not change dimensions or residue fields.
The same dimension formula used in step [](#s4){.pf-ref} therefore gives
$$
\dim\OO_{X,x}+\operatorname{trdeg}_k\kappa(x)=n.
$$
Localization in the construction of the differential sheaf gives
$$
(\Omega_{X/k})_x\cong\Omega_{\OO_{X,x}/k}.
$$
Applying step [](#s4){.pf-ref} proves (c), without assuming that $x$ is closed or that $X$ is reduced.

:::

:::

::: {.pf-step #s6}

The locus in (d) is open and dense.

::: pf-proof

The sheaf $\Omega_{X/k}$ is coherent, since $X$ is of finite type over the field $k$.
The locus where its stalk is free of rank $n=\dim X$ is open.
Indeed, a basis at a stalk extends to a morphism $\OO^{\oplus n}\to\Omega_{X/k}$ on a neighborhood; its coherent kernel and cokernel vanish at that point, and hence vanish after shrinking the neighborhood.
Step [](#s5){.pf-ref} identifies this open locus with the regular locus.

The variety $X$ is integral, so the local ring at its generic point is a field and is regular.
Thus the regular locus contains the generic point and is dense.
This proves (d).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a), steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (b), step [](#s5){.pf-ref} proves (c), and step [](#s6){.pf-ref} proves (d).

:::

:::

:::
