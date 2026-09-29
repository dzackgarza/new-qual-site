---
schema: qual/card@1
id: P-AGH2714PROJVERYAMPLE
kind: problem
title: Very ampleness on a relative Proj
classification:
  areas:
  - algebraic-geometry
  topics:
  - Relative Proj
  - Very Ample Sheaves
  - Ample Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts and the hint with the retained Hartshorne II.7.14 transcription. Expanded the relative-Proj condition from the indexed source convention preceding Lemma II.7.9. Checked the affine-basis, section-localization and quasi-compact-immersion lemmas against Stacks Project Tags 01Q3, 01PW and 01QV; the proof does not assume that Y is affine or noetherian.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
(a) Give an example of a noetherian scheme $X$ and a locally free coherent sheaf $\mce$ such that the invertible sheaf $\OO(1)$ on $\PP(\mce)$ is not very ample relative to $X$.

(b) Let $X$ be noetherian, let $f:X\to Y$ be a morphism of finite type, and let $\mcl$ be an ample invertible sheaf on $X$.
Let $\mcs=\bigoplus_{d\ge0}\mcs_d$ satisfy the relative-Proj condition (†): it is a quasi-coherent graded $\OO_X$-algebra with $\mcs_0=\OO_X$, its degree-one sheaf $\mcs_1$ is coherent, and the multiplication map $\operatorname{Sym}^{\bullet}\mcs_1\to\mcs$ is surjective.
Let $P = \Proj \mcs$, let $\pi: P \to X$ be the projection, and let $\OO_P(1)$ be the associated invertible sheaf.
Show that for all $n \gg 0$, the sheaf $\OO_P(1) \tensor \pi^* \mcl^n$ is very ample on $P$ relative to $Y$.
:::

::: {.hint}
Use Proposition II.7.10 and Exercise II.5.12.
:::

::: {.solution}
Very ampleness over a scheme $B$ means an immersion into $\PP_B^N$ for some finite $N$, pulling back $\OO(1)$ to the given sheaf, as in [[D-MODAMPLE]].
We use the source's open-in-closed immersion convention, as in [[P-AGH2512VERYAMPLE]].
Tensor powers are indicated by superscripts, and all sheaf tensor products on $X$ are over $\OO_X$.

::: pf

::: {.pf-step #s1}

An example for (a) is
$$
\boxed{X=\PP_k^1,\qquad\mce=\OO_X(-1).}
$$

::: pf-proof

The scheme $X$ is noetherian, and $\mce$ is locally free and coherent of rank one.
In the quotient convention, the projection $\PP(\mce)\to X$ is an isomorphism: on every framed open its symmetric algebra is the polynomial algebra in one degree-one variable, whose Proj is that open.
The tautological quotient then identifies $\OO_{\PP(\mce)}(1)$ with $\mce$ [@Har10a, Proposition II.7.12], as constructed in [[P-AGH278SECTIONSPE]].

If this sheaf were very ample relative to $X$, the coordinate sections from a witnessing immersion into some $\PP_X^N$ would pull back to finitely many global sections generating $\OO_X(-1)$.
But $\Gamma(\PP_k^1,\OO(-1))=0$ [@Har10a, Proposition II.5.13].
This contradicts generation of a nonzero invertible sheaf and proves (a).

:::

:::

::: {.pf-step #s2}

Under the hypotheses in (b), some positive power $\mcl^h$ is very ample relative to $Y$.

::: pf-proof

For $X=\varnothing$, its empty immersion supplies the assertion, so assume $X$ is nonempty.
The [affine-basis criterion for ampleness](https://stacks.math.columbia.edu/tag/01Q3) says that the affine opens $X_s$, with $s$ a global section of a positive power of $\mcl$, form a basis of $X$.
Here $X_s$ is the open set on which $s$ is a frame.
Choose finitely many such opens $W_i=X_{s_i}$ covering $X$, with $s_i\in\Gamma(X,\mcl^{d_i})$, $d_i>0$, and each $W_i$ mapped into an affine open $V_i=\Spec A_i$ of $Y$.
Finiteness of this cover follows from quasi-compactness of $X$.

Write $W_i=\Spec B_i$.
The restriction $W_i\to V_i$ is of finite type, so choose finitely many $A_i$-algebra generators $b_{ij}$ of $B_i$.
The [localization formula for sections](https://stacks.math.columbia.edu/tag/01PW) on the quasi-compact, quasi-separated scheme $X$ gives sections
$$
t_{ij}\in\Gamma(X,\mcl^{d_iq_{ij}}),\qquad
t_{ij}|_{W_i}=b_{ij}s_i^{q_{ij}}
$$
for some integers $q_{ij}\ge0$.
Choose a positive common multiple $h$ of the $d_i$ large enough that $h/d_i\ge q_{ij}$ for every pair.
The global sections
$$
a_i=s_i^{h/d_i},\qquad
c_{ij}=t_{ij}s_i^{h/d_i-q_{ij}}
$$
of $\mcl^h$ have ratios $c_{ij}/a_i=b_{ij}$ on $W_i$.
The $a_i$ have no common zero, so this finite list generates $\mcl^h$ and defines a $Y$-morphism $i:X\to\PP_Y^N$ with $i^*\OO(1)\cong\mcl^h$ [@Har10a, Theorem II.7.1].

The inverse image of the target affine chart over $V_i$ where the coordinate for $a_i$ is nonzero is exactly $W_i$.
Its coordinate-ring map onto $B_i$ is surjective, because its coordinate ratios include every $b_{ij}$.
Thus $i$ is a closed immersion over each of these target opens.
Their union contains the image, so $i$ is a locally closed immersion.
It is quasi-compact because every open subset of the noetherian space $X$ is quasi-compact.
The [factorization of a quasi-compact immersion](https://stacks.math.columbia.edu/tag/01QV) makes it an open immersion into a closed subscheme of $\PP_Y^N$.
This proves very ampleness in the stated convention, with no noetherian or affine hypothesis on $Y$.

:::

:::

::: {.pf-step #s3}

For each integer $a$, twisting the graded pieces gives
$$
\mcs^{[a]}=\bigoplus_{d\ge0}\mcs_d\otimes\mcl^{ad},
\qquad\operatorname{Proj}_X\mcs^{[a]}\cong P,
$$
and its twisting sheaf corresponds to
$$
N_a\coloneqq\OO_P(1)\otimes\pi^*\mcl^a.
$$

::: pf-proof

On an open set with a frame $e$ for $\mcl$, identify the degree-$d$ piece with $\mcs_d$ by writing a section as $s\otimes e^{ad}$.
These identifications respect products and give local graded-algebra isomorphisms.
Replacing $e$ by $ue$ changes degree $d$ by the factor $u^{ad}$.
The factors cancel in every degree-zero homogeneous fraction, so the induced Proj isomorphisms agree on overlaps.

For the twisting sheaf, a homogeneous local fraction has numerator degree one greater than its denominator degree.
Its change of frame retains the factor $u^a$, exactly the transition factor of $\pi^*\mcl^a$.
Thus the twisting sheaves glue with the displayed extra tensor factor.
This proves both assertions, which are the graded twist of [@Har10a, Lemma II.7.9].

:::

:::

::: {.pf-step #s4}

There is an integer $a_0\ge0$ such that, for every $a\ge a_0$, $N_a$ is the pullback of $\OO(1)$ under a closed immersion $j_a:P\to\PP_X^{r_a}$ for some finite $r_a$.

::: pf-proof

The sheaf $\mcs_1$ is coherent, so ampleness of $\mcl$ makes $\mcs_1\otimes\mcl^a$ globally generated for every sufficiently large $a$.
A globally generated coherent sheaf on a quasi-compact scheme is generated by finitely many global sections: at each point finitely many generate the stalk, continue to generate on a neighborhood by coherence, and choose a finite subcover.
Consequently, for every $a\ge a_0$ there is a surjection
$$
\OO_X^{\oplus(r_a+1)}\twoheadrightarrow\mcs_1\otimes\mcl^a.
$$
A redundant zero generator may be added to make $r_a\ge0$.
Since the algebra is generated in degree one, this induces a graded surjection
$$
\OO_X[T_0,\ldots,T_{r_a}]\twoheadrightarrow\mcs^{[a]}.
$$
On every affine open of $X$ it gives a closed immersion of Proj schemes; these closed immersions and their coordinate sections glue.
The result is $j_a$ with twisting sheaf $N_a$ by step [](#s3){.pf-ref}.
This is the construction underlying [@Har10a, Proposition II.7.10].

:::

:::

::: {.pf-step #s5}

The conclusion in (b) holds for every $n\ge a_0+h$.

::: pf-proof

Fix the immersion $i:X\to\PP_Y^N$ from step [](#s2){.pf-ref}.
For $n\ge a_0+h$, put $a=n-h$ and take the closed immersion $j_a$ from step [](#s4){.pf-ref}.
Base-changing $i$ and then applying the Segre closed immersion gives the composite
$$
P\xrightarrow{j_a}\PP_X^{r_a}
\longrightarrow\PP_Y^{r_a}\times_Y\PP_Y^N
\longrightarrow\PP_Y^{(r_a+1)(N+1)-1}.
$$
It is a locally closed immersion, and the Segre twisting formula from [[P-AGH2512VERYAMPLE]], step [](#s1){.pf-ref}, shows that its pullback of $\OO(1)$ is
$$
N_a\otimes\pi^*i^*\OO(1)
\cong\OO_P(1)\otimes\pi^*\mcl^{a+h}
=\OO_P(1)\otimes\pi^*\mcl^n.
$$
The scheme $P$ is noetherian: over a finite affine cover of $X$, it is a closed subscheme of a finite-dimensional projective space, since $\mcs_1$ is coherent and generates the algebra.
The composite is therefore quasi-compact, so the same immersion factorization used in step [](#s2){.pf-ref} supplies the source's open-in-closed convention.
It witnesses the required relative very ampleness for every stated $n$, not just a subsequence of exponents.
If $P$ or $X$ is empty, the empty immersion gives the assertion directly.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a); steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} construct the required immersions over $Y$ for all sufficiently large powers, proving (b).

:::

:::

:::
