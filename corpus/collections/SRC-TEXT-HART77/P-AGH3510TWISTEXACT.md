---
schema: qual/card@1
id: P-AGH3510TWISTEXACT
kind: problem
title: Exactness of global sections of a complex after a large twist
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Vanishing
  - Coherent Sheaves
  - Projective Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the finite exact sequence and uniform eventual bound with the retained Hartshorne III.5.10 transcription. The proof applies Serre vanishing to the finitely many coherent kernels and verifies exactness at each displayed interior term, with endpoint injectivity or surjectivity preserved when the corresponding zero is part of the given sequence.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a projective scheme over a noetherian ring $A$, and let $\mcf^1 \to \mcf^2 \to \cdots \to \mcf^r$ be an exact sequence of coherent sheaves on $X$.
Use the twists from a fixed projective embedding of $X$ over $A$.
Show that there is an integer $n_0$, such that for all $n \geq n_0$, the sequence of global sections
$$
\Gamma(X, \mcf^1(n)) \to \Gamma(X, \mcf^2(n)) \to \cdots \to \Gamma(X, \mcf^r(n))
$$
is exact.
:::

::: {.solution}
Write $d_i:\mcf^i\to\mcf^{i+1}$ for $1\le i<r$ and $K_i=\ker d_i$.
Exactness of a displayed sequence without terminal zeros is asserted at its interior terms.
The argument also treats any endpoint at which an initial or final zero is part of the given sequence.

<1>1. All the $K_i$ and all the image sheaves are coherent, and for $2\le i<r$ there are short exact sequences
$$
0\longrightarrow K_{i-1}\longrightarrow\mcf^{i-1}\longrightarrow K_i\longrightarrow0.
$$

::: {.proof}
The scheme $X$ is noetherian because it is projective over a noetherian ring.
Kernels, images and cokernels of maps of coherent sheaves on a noetherian scheme are coherent [@Har10a, Proposition II.5.7].
At an interior term, the assumed exactness is $\im d_{i-1}=\ker d_i=K_i$.
Factoring $d_{i-1}$ through that image gives the displayed short exact sequence, with kernel $K_{i-1}$ by definition.
:::

<1>2. There is one integer $n_0$ such that, for every $n\ge n_0$, every map $\Gamma(X,\mcf^{i-1}(n))\to\Gamma(X,K_i(n))$ in step <1>1 is surjective.

::: {.proof}
By [[T-COHSVAN|Serre vanishing]], for each coherent $K_j$ there is a bound beyond which $H^1(X,K_j(n))=0$ [@Har10a, Theorem III.5.2].
There are only finitely many $K_j$, so take $n_0$ to be the maximum of these finitely many bounds.
If the index set is empty, take $n_0=0$.

Twisting a short exact sequence from step <1>1 is exact because $\OO_X(n)$ is invertible.
Its cohomology sequence has the segment
$$
\Gamma(X,\mcf^{i-1}(n))\longrightarrow\Gamma(X,K_i(n))
\longrightarrow H^1(X,K_{i-1}(n)).
$$
The last group is zero for every $n\ge n_0$, giving the asserted surjectivity simultaneously for all the interior indices.
:::

<1>3. The sequence of global sections is exact at every required term for all $n\ge n_0$.

::: {.proof}
By left exactness of global sections,
$$
\ker\bigl(\Gamma(X,\mcf^i(n))\to\Gamma(X,\mcf^{i+1}(n))\bigr)
=\Gamma(X,K_i(n)).
$$
Step <1>2 identifies this subgroup with the image of $\Gamma(X,\mcf^{i-1}(n))$, because the map induced by $d_{i-1}$ factors through $K_i(n)$ and is surjective on its sections.
This proves exactness at each interior term.

If an initial zero is included, its injectivity remains true after twisting and taking sections by left exactness.
If a terminal zero is included, $d_{r-1}$ is surjective, so
$$
0\to K_{r-1}(n)\to\mcf^{r-1}(n)\to\mcf^r(n)\to0
$$
and $H^1(X,K_{r-1}(n))=0$ give surjectivity on sections for the same bound.
For a sequence with no interior term, the interior assertion is empty and these endpoint arguments still apply whenever required.
Thus the one bound works for the full given exact sequence.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 supplies coherent kernels, step <1>2 chooses one eventual vanishing bound, and step <1>3 proves exactness for every twist beyond that bound.
:::
:::
