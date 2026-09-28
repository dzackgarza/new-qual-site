---
schema: qual/card@1
id: P-AGH291FORMALREG
kind: problem
title: Formal-regular functions along a subvariety of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Completion
  - Conormal Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts and the regular-sequence hint with the retained Hartshorne II.9.1 transcription. Checked the associated graded conormal comparison in Stacks Project section 31.22. The proof uses locally split inclusions before taking symmetric powers, obtains surjectivity on thickening sections from constants rather than H^1 vanishing, and takes the inverse limit of the actual section rings.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, $Y$ a closed subscheme, and $\hat X$ the completion of $X$ along $Y$.
We call the ring $\Gamma(\hat X, \OO_{\hat X})$ the ring of **formal-regular** functions on $X$ along $Y$.
In this exercise we show that if $Y$ is a connected, nonsingular, positive dimensional subvariety of $X = \PP^n_k$ over an algebraically closed field $k$, then $\Gamma(\hat X, \OO_{\hat X}) = k$.

(a) Let $\mci$ be the ideal sheaf of $Y$.
Use (8.13) and (8.17) to show that there is an inclusion of sheaves on $Y$, $\mci/\mci^2 \injects \OO_Y(-1)^{n+1}$.

(b) Show that for any $r \geq 1$, $\Gamma(Y, \mci^r/\mci^{r+1}) = 0$.

(c) Use the exact sequences
$$
0 \to \mci^r/\mci^{r+1} \to \OO_X/\mci^{r+1} \to \OO_X/\mci^r \to 0
$$
and induction on $r$ to show that $\Gamma(Y, \OO_X/\mci^r) = k$ for all $r \geq 1$.

(d) Conclude that $\Gamma(\hat X, \OO_{\hat X}) = k$.
Actually the same result holds without the hypothesis that $Y$ is nonsingular, but the proof is more difficult; see Hartshorne [3, (7.3)] in the book's bibliography.
:::

::: {.hint}
Use Theorem II.8.21A(e) to identify the successive ideal quotients with symmetric powers of the conormal sheaf.
:::

::: {.solution}
For the asserted calculation set $X=\PP_k^n$, let $i:Y\hookrightarrow X$ be the given closed immersion, and put $\mathcal N^*=\mathcal I/\mathcal I^2$.
Regard $\OO_X/\mathcal I^r$ as a sheaf on its underlying closed space $Y$.
All the tensor and symmetric powers on $Y$ are over $\OO_Y$.

<1>1. There is a locally split injection $\mathcal N^*\hookrightarrow\OO_Y(-1)^{\oplus(n+1)}$, proving (a).

::: {.proof}
Since $Y$ and $X$ are nonsingular over $k$, the [[D-MODCONORM|conormal sequence]] is short exact:
$$
0\longrightarrow\mathcal N^*\longrightarrow i^*\Omega_{X/k}
\longrightarrow\Omega_{Y/k}\longrightarrow0
$$
[@Har10a, Theorem II.8.17].
Its quotient is locally free, so the sequence splits locally: lifts of a local basis give a section of its surjection after shrinking.
The [[T-MODEULER|Euler sequence]] on $\PP_k^n$ is
$$
0\to\Omega_{X/k}\to\OO_X(-1)^{\oplus(n+1)}\to\OO_X\to0
$$
[@Har10a, Theorem II.8.13].
This also splits locally, since its quotient is locally free.
Pulling it back to $Y$ therefore preserves exactness and gives a locally split inclusion $i^*\Omega_{X/k}\hookrightarrow\OO_Y(-1)^{\oplus(n+1)}$.
Compose the two inclusions.
On a common open set where both split, the composite of their retractions is a retraction of this inclusion, proving the asserted local splitting.
:::

<1>2. The scheme $Y$ is integral, $\Gamma(Y,\OO_Y)=k$, and $\Gamma(Y,\OO_Y(-r))=0$ for every $r\ge1$.

::: {.proof}
A nonsingular variety over the algebraically closed field is regular and reduced.
Distinct irreducible components cannot meet, because its local rings are domains.
There are finitely many components, so each is open and closed; connectedness forces only one.
Thus $Y$ is integral.
It is projective as a closed subscheme of $\PP^n$.
Every global regular function defines a morphism $Y\to\AA^1\subseteq\PP^1$ with closed irreducible image, by properness, and that image misses infinity.
Hence the image is a point, and reducedness makes the function equal to its constant value.
Since $k$ is algebraically closed, this proves $\Gamma(Y,\OO_Y)=k$.

For $r>0$, suppose a nonzero section $s$ of $\OO_Y(-r)$ existed.
Positive dimension gives two distinct closed points of $Y$.
Choose a homogeneous linear form $h$ vanishing at the first but not at the second; its restriction is a nonzero section of $\OO_Y(1)$.
The product $h^r s$ is a nonzero section of $\OO_Y$, because both factors have nonzero generic values on the integral scheme $Y$.
It vanishes at the first point, contradicting that every nonzero global function is a nonzero constant.
This proves the negative-twist vanishing without any complete-intersection assumption on $Y$.
:::

<1>3. For every $r\ge1$ there is an injection
$$
\mathcal I^r/\mathcal I^{r+1}
\hookrightarrow\OO_Y(-r)^{\oplus\binom{n+r}{r}},
$$
and consequently its global sections vanish, proving (b).

::: {.proof}
The closed immersion of the two regular schemes $Y$ and $X$ is a regular immersion, so its ideal is locally generated by a regular sequence.
The multiplication map gives canonical isomorphisms
$$
\operatorname{Sym}^r(\mathcal I/\mathcal I^2)
\xrightarrow{\cong}\mathcal I^r/\mathcal I^{r+1}
$$
[@Har10a, Theorem II.8.21A(e)].
This is the associated graded description of a [regular immersion](https://stacks.math.columbia.edu/tag/0638).
These are local regular-sequence isomorphisms whose maps are defined globally by multiplication, so they agree on overlaps.

Apply $\operatorname{Sym}^r$ to the injection in step <1>1.
Its local retraction remains a retraction after applying this functor, so the induced symmetric-power map is injective.
Furthermore
$$
\operatorname{Sym}^r(\OO_Y(-1)^{\oplus(n+1)})
\cong\OO_Y(-r)\otimes\operatorname{Sym}^r(\OO_Y^{\oplus(n+1)})
\cong\OO_Y(-r)^{\oplus\binom{n+r}{r}},
$$
as is seen on the degree-$r$ monomial basis [@Har10a, Exercise II.5.16].
The stated injection follows.
Taking global sections is left exact, and step <1>2 makes the target section group zero.
Hence $\Gamma(Y,\mathcal I^r/\mathcal I^{r+1})=0$.
The use of a locally split inclusion avoids assuming that symmetric powers preserve arbitrary injections.
:::

<1>4. The constants give compatible isomorphisms
$$
k\xrightarrow{\cong}\Gamma(Y,\OO_X/\mathcal I^r)
\qquad(r\ge1),
$$
proving (c).

::: {.proof}
For $r=1$, the sheaf is $\OO_Y$ and the assertion is step <1>2.
For the induction step, the exact sequence in (c) and the vanishing in step <1>3 give an injection
$$
\Gamma(Y,\OO_X/\mathcal I^{r+1})
\longrightarrow\Gamma(Y,\OO_X/\mathcal I^r).
$$
By induction the target is $k$ under the constants map.
Every such constant already has its constant lift to $\Gamma(Y,\OO_X/\mathcal I^{r+1})$.
Thus this injection is also surjective, and the constants map to its source is an isomorphism.
The transition homomorphisms preserve constants, so under these isomorphisms every transition is the identity of $k$.
No vanishing of $H^1(Y,\mathcal I^r/\mathcal I^{r+1})$ is needed or asserted.
:::

<1>5. The formal-regular function ring is $\boxed{\Gamma(\hat X,\OO_{\hat X})=k}$.

::: {.proof}
By the [[D-SCHFORMAL|definition of formal completion]], the underlying space of $\hat X$ is $Y$ and its structure sheaf is
$$
\OO_{\hat X}=\varprojlim_{r\ge1}\OO_X/\mathcal I^r.
$$
Limits of sheaves of rings are computed on sections: compatible tuples of local sections have unique glued tuples by the sheaf axiom at every index.
Therefore
$$
\Gamma(\hat X,\OO_{\hat X})
\cong\varprojlim_{r\ge1}\Gamma(Y,\OO_X/\mathcal I^r)
\cong\varprojlim(k\xleftarrow{\id}k\xleftarrow{\id}\cdots)
\cong k,
$$
where step <1>4 identifies both the rings and their transition maps.
The isomorphism is the original map from constant functions, so it is an equality of the stated constant subring with the whole ring.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves (a), step <1>3 proves (b), step <1>4 proves (c), and step <1>5 proves (d).
:::
:::
