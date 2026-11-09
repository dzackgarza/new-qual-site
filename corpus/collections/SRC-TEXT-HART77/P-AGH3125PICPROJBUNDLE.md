---
schema: qual/card@1
id: P-AGH3125PICPROJBUNDLE
kind: problem
title: The Picard group of a projective bundle
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Picard Group
  - Projective Bundles
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.5 together with II.7.9. The printed III.12.5 statement
    drops the rank-at-least-two hypothesis: for rank one, P(E) is Y and the
    asserted extra Z summand is false. The proof below treats the corrected
    rank-at-least-two statement, using III.12.4 after fixing the fibre degree.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-09
  note: 'Read III.12.5 against Hartshorne p. 291 and Dongryul Kim, Solutions to Hartshorne, p. 216, whose solution opens by saying that E must have rank at least 2. The statement is now kept as printed, without the rank hypothesis, and the solution names the rank-one counterexample P(E) = Y and proves the corrected statement for rank at least 2.'
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne III.12.5 omits the rank hypothesis, and for rank one P(E) = Y.
---

::: {.problem}
Let $Y$ be an integral scheme of finite type over an algebraically closed field $k$.
Let $\mce$ be a locally free sheaf on $Y$, and let $X = \PP(\mce)$; see (II, §7).

Show that $\Pic X \cong (\Pic Y) \times \ZZ$.
This strengthens (II, Ex.
7.9).
:::

::: {.solution}
As printed the statement needs the hypothesis $\operatorname{rank}\mce\ge2$. For an
invertible $\mce$ the projective bundle is $\PP(\mce)=Y$ itself, since
$\Sym\mce$ is generated in degree one by $\mce$ and $\Proj\Sym\mce=Y$; then the
printed formula would read $\Pic Y\cong\Pic Y\times\ZZ$, which is false for every
$Y$ because $\ZZ$ is infinite. So the counterexample is the case
$\operatorname{rank}\mce=1$, and the statement proved below is the corrected one,
with $\operatorname{rank}\mce\ge2$. The printed formula is correct in that range,
and the proof also shows where it breaks: with $r-1=0$ the fibre
$\PP^{r-1}_{\kappa(y)}$ is a point, its Picard group is not $\ZZ[\OO(1)]$, and
step s1 fails.

Let
$$
p:X=\PP(\mce)\longrightarrow Y
$$
be the projection of the corrected statement, let
$$
r=\operatorname{rank}\mce\ge2,
$$
and write $\mco_X(1)$ for the tautological twisting sheaf.

::: pf

::: {.pf-step #s1}

For any invertible sheaf $\mcl$ on $X$, there is a unique integer
$n$ such that
$$
\mcl_y\cong\mco_{\PP^{r-1}_{\kappa(y)}}(n)
$$
for every $y\in Y$.

::: pf-proof

For each $y$, the fibre is
$$
X_y\cong\PP^{r-1}_{\kappa(y)}.
$$
Since $r-1\ge1$,
$$
\Pic X_y\cong\ZZ
$$
with generator $\mco_{X_y}(1)$. Thus there is a unique integer $n(y)$
such that
$$
\mcl_y\cong\mco_{X_y}(n(y)).
$$

The sheaf $\mcl$ is flat over $Y$: locally it is $\mco_X$, and
$p$ is flat. Hence [[T-COHBC|constancy of Euler characteristic]] says
that for every integer $m$, the function
$$
y\longmapsto
\chi\bigl(X_y,\mcl_y(m)\bigr)
$$
is locally constant. The base $Y$ is integral, hence connected, so this
integer is independent of $y$.

On the fibre,
$$
\chi\bigl(X_y,\mcl_y(m)\bigr)
=
\chi\bigl(\PP^{r-1}_{\kappa(y)},\mco(m+n(y))\bigr)
=
\binom{m+n(y)+r-1}{r-1}
$$
as a polynomial in $m$. Therefore the Hilbert polynomial
$$
m\longmapsto\chi\bigl(X_y,\mcl_y(m)\bigr)
$$
is independent of $y$. Distinct integers $a\ne b$ give distinct
translated polynomials
$$
\binom{m+a+r-1}{r-1}
\ne
\binom{m+b+r-1}{r-1};
$$
for example, their coefficients of $m^{r-2}$ differ when $r>2$, and
for $r=2$ they are the distinct linear polynomials $m+a+1$ and
$m+b+1$. Thus $n(y)$ is independent of $y$. Denote its common value
by $n$.

:::

:::

::: {.pf-step #s2}

Every invertible sheaf $\mcl$ on $X$ has the form
$$
\mcl\cong p^*\mcn\tensor\mco_X(n)
$$
for some $\mcn\in\Pic Y$ and $n\in\ZZ$.

::: pf-proof

Let $n$ be the integer from step [](#s1){.pf-ref} and put
$$
\mcl_0=\mcl\tensor\mco_X(-n).
$$
Then for every $y\in Y$,
$$
(\mcl_0)_y\cong\mco_{X_y}.
$$

The morphism
$$
p:X\longrightarrow Y
$$
is flat and projective, and all of its fibres are projective spaces, hence
integral. Apply
[[P-AGH3124FIBREWISEISO|Exercise III.12.4]]
to the two invertible sheaves $\mcl_0$ and $\mco_X$. There exists an
invertible sheaf $\mcn$ on $Y$ such that
$$
\mcl_0\cong p^*\mcn.
$$
Tensoring by $\mco_X(n)$ gives
$$
\mcl\cong p^*\mcn\tensor\mco_X(n).
$$

:::

:::

::: {.pf-step #s3}

Define
$$
\Phi:\Pic Y\times\ZZ\longrightarrow\Pic X
$$
by
$$
\Phi([\mcn],n)
=
[p^*\mcn\tensor\mco_X(n)].
$$
Then $\Phi$ is a surjective group homomorphism.

::: pf-proof

Pullback and tensor product give
$$
p^*(\mcn_1\tensor\mcn_2)
\cong
p^*\mcn_1\tensor p^*\mcn_2,
$$
and
$$
\mco_X(n_1)\tensor\mco_X(n_2)
\cong
\mco_X(n_1+n_2).
$$
Hence $\Phi$ is a homomorphism. Its surjectivity is exactly step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The homomorphism $\Phi$ is injective.

::: pf-proof

Suppose
$$
p^*\mcn\tensor\mco_X(n)\cong\mco_X.
$$
Restricting to any fibre gives
$$
\mco_{\PP^{r-1}_{\kappa(y)}}(n)\cong
\mco_{\PP^{r-1}_{\kappa(y)}}.
$$
Since $r-1\ge1$ and
$$
\Pic\PP^{r-1}_{\kappa(y)}\cong\ZZ[\mco(1)],
$$
we obtain $n=0$. Thus
$$
p^*\mcn\cong\mco_X.
$$

For a projective bundle,
$$
p_*\mco_X\cong\mco_Y.
$$
By the projection formula,
$$
p_*p^*\mcn
\cong
\mcn\tensor p_*\mco_X
\cong
\mcn.
$$
Pushing forward $p^*\mcn\cong\mco_X$ therefore gives
$$
\mcn\cong\mco_Y.
$$
Hence the kernel of $\Phi$ is trivial.

:::

:::

::: {.pf-step #s5}

Consequently
$$
\boxed{\Pic\PP(\mce)\cong\Pic Y\times\ZZ}
$$
when $\operatorname{rank}\mce\ge2$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that $\Phi$ is a bijective group homomorphism.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the asserted formula.

:::

:::

:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter III §12, Exercise 12.5, PDF p. 216, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he opens by writing "(Obviously, E is supposed to be of rank at least 2)", fixes the fibre degree by comparing the closed sets $\{\deg\scr L_y\ge d\}$ and $\{\deg\scr L_y\le -d\}$ on connected $Y$, applies Corollary 12.9, and reduces to $\scr L$ with $f_*\scr L=\OO_Y$ exactly as in Exercise 12.4. The corrected statement he proves is the one proved above: the printed formula needs $\operatorname{rank}\mce\ge2$, and for $\operatorname{rank}\mce=1$ one has $\PP(\mce)=Y$. Step s1 replaces his degree argument by the constancy of the Euler characteristic, which gives the same conclusion.
:::
