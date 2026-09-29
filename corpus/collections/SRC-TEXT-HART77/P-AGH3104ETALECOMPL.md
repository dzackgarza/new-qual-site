---
schema: qual/card@1
id: P-AGH3104ETALECOMPL
kind: problem
title: Etale morphisms via completed local rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Etale Morphisms
  - Complete Local Rings
  - Separable Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.4 together with III.10.3 and the coefficient-field
    theorem for complete equicharacteristic local rings. The proof compares
    the full associated graded rings under an étale local map and uses faithful
    flatness of noetherian completion for the converse.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that a morphism $f: X \to Y$ of schemes of finite type over $k$ is étale if and only if the following condition is satisfied.
For each $x \in X$, let $y = f(x)$.
Let $\hat{\mco}_x$ and $\hat{\mco}_y$ be the completions of the local rings at $x$ and $y$.
Choose fields of representatives (II, 8.25A) $k(x) \subseteq \hat{\mco}_x$ and $k(y) \subseteq \hat{\mco}_y$ so that $k(y) \subseteq k(x)$ via the natural map $\hat{\mco}_y \to \hat{\mco}_x$.

The condition is that for every $x \in X$, the field $k(x)$ is a separable algebraic extension of $k(y)$, and the natural map
\[
\hat{\mco}_y \tensor_{k(y)} k(x) \to \hat{\mco}_x
\]
is an isomorphism.
:::

::: {.solution}
Fix $x\in X$, put $y=f(x)$, and write
$$
A=\OO_{Y,y},
\qquad
B=\OO_{X,x},
\qquad
k_y=\kappa(y),
\qquad
k_x=\kappa(x).
$$
Let $\mathfrak n$ and $\mathfrak m$ be the maximal ideals of $A$ and $B$,
respectively. Write $\widehat A$ and $\widehat B$ for their completions.

Choose compatible coefficient fields
$$
k_y\subseteq\widehat A,
\qquad
k_x\subseteq\widehat B,
$$
as in the statement. They give the natural continuous homomorphism
$$
\Phi:\widehat A\tensor_{k_y}k_x\longrightarrow\widehat B,
\qquad
a\tensor c\longmapsto f^\sharp(a)c.
$$

::: pf

::: {.pf-step #s1}

If $f$ is étale, then
$$
\mathfrak m=\mathfrak nB
$$
and $k_x/k_y$ is finite separable.

::: pf-proof

By [[P-AGH3103ETALECHAR|Exercise III.10.3]], an étale morphism is flat and
unramified. Hartshorne's definition of unramifiedness gives
$$
\mathfrak nB=\mathfrak m
$$
and says that $k_x/k_y$ is separable algebraic.
Because $B$ is essentially of finite type over $A$, the residue-field
extension is finitely generated. A finitely generated algebraic field
extension is finite. Thus $k_x/k_y$ is finite separable.

:::

:::

::: {.pf-step #s2}

If $f$ is étale, then for every $r\ge0$ there is a natural isomorphism
$$
\mathfrak m^r/\mathfrak m^{r+1}
\cong
(\mathfrak n^r/\mathfrak n^{r+1})\tensor_{k_y}k_x.
$$

::: pf-proof

The local map $A\to B$ is flat by step [](#s1){.pf-ref}. Tensor the exact sequence
$$
0\longrightarrow\mathfrak n^{r+1}
\longrightarrow\mathfrak n^r
\longrightarrow\mathfrak n^r/\mathfrak n^{r+1}
\longrightarrow0
$$
with $B$. Flatness preserves exactness, so
$$
(\mathfrak n^r/\mathfrak n^{r+1})\tensor_A B
\cong
\mathfrak n^rB/\mathfrak n^{r+1}B.
$$
By step [](#s1){.pf-ref},
$$
\mathfrak n^rB=\mathfrak m^r.
$$
Moreover $\mathfrak n$ annihilates
$\mathfrak n^r/\mathfrak n^{r+1}$, so tensoring with $B$ factors through
$$
B/\mathfrak nB=B/\mathfrak m=k_x.
$$
Hence
$$
(\mathfrak n^r/\mathfrak n^{r+1})\tensor_A B
\cong
(\mathfrak n^r/\mathfrak n^{r+1})\tensor_{k_y}k_x,
$$
which proves the assertion.

:::

:::

::: {.pf-step #s3}

If $f$ is étale, the map
$$
\Phi:\widehat A\tensor_{k_y}k_x\longrightarrow\widehat B
$$
is an isomorphism.

::: pf-proof

Because $k_x/k_y$ is finite, the source is a finite free $\widehat A$-module.
It is therefore complete and separated for the
$\mathfrak n\widehat A$-adic filtration.

Completion does not change the associated graded pieces of a noetherian local
ring:
$$
(\mathfrak n\widehat A)^r/(\mathfrak n\widehat A)^{r+1}
\cong
\mathfrak n^r/\mathfrak n^{r+1},
$$
and similarly for $B$.
Thus the map induced by $\Phi$ on the $r$th associated graded piece is exactly
the isomorphism of step [](#s2){.pf-ref}.

It follows inductively that for every $N\ge1$, $\Phi$ induces an isomorphism
$$
(\widehat A\tensor_{k_y}k_x)/(\mathfrak n\widehat A)^N
\xrightarrow{\sim}
\widehat B/(\mathfrak m\widehat B)^N.
$$
Indeed, pass from $N$ to $N+1$ using the short exact sequences whose kernels
are the $N$th associated graded pieces.
Taking inverse limits and using completeness and separatedness gives
$$
\boxed{
\widehat A\tensor_{k_y}k_x\xrightarrow{\sim}\widehat B.
}
$$
This proves the required completed-local-ring condition in the forward
direction.

:::

:::

::: {.pf-step #s4}

Conversely, assume that $k_x/k_y$ is separable algebraic and that $\Phi$ is an isomorphism. Then
$$
\mathfrak m\widehat B=\mathfrak n\widehat B.
$$

::: pf-proof

Again $k_x/k_y$ is finite because it is algebraic and finitely generated.
Modulo $\mathfrak n\widehat A$, the source of $\Phi$ is
$$
(\widehat A/\mathfrak n\widehat A)\tensor_{k_y}k_x
\cong
k_y\tensor_{k_y}k_x
\cong k_x,
$$
a field.
Therefore
$$
\mathfrak n(\widehat A\tensor_{k_y}k_x)
$$
is the maximal ideal of the source. Under the local-ring isomorphism $\Phi$ it
maps to the maximal ideal $\mathfrak m\widehat B$ of $\widehat B$. Hence
$$
\boxed{\mathfrak n\widehat B=\mathfrak m\widehat B}.
$$

:::

:::

::: {.pf-step #s5}

Under the hypotheses of step [](#s4){.pf-ref}, the local map $A\to B$ is flat and satisfies
$$
\mathfrak nB=\mathfrak m.
$$

::: pf-proof

The completion $\widehat A$ is flat over the noetherian local ring $A$.
Since $k_x$ is a vector space over $k_y$,
$$
\widehat A\tensor_{k_y}k_x
$$
is also flat as an $A$-module. By the assumed isomorphism $\Phi$,
$\widehat B$ is therefore flat over $A$.

The completion map
$$
B\longrightarrow\widehat B
$$
is faithfully flat. To test flatness of $B$ over $A$, tensor an exact sequence
of $A$-modules first with $B$ and then with the faithfully flat $B$-module
$\widehat B$. The result is exact because $\widehat B$ is $A$-flat; faithful
flatness then shows that the sequence after tensoring with $B$ was already
exact. Thus $B$ is flat over $A$.

Now step [](#s4){.pf-ref} gives
$$
(\mathfrak m/\mathfrak nB)\tensor_B\widehat B=0.
$$
Faithful flatness of $B\to\widehat B$ implies
$$
\mathfrak m/\mathfrak nB=0.
$$
Hence
$$
\boxed{\mathfrak nB=\mathfrak m}.
$$

:::

:::

::: {.pf-step #s6}

The completed-local-ring condition implies that $f$ is étale at $x$.

::: pf-proof

Step [](#s5){.pf-ref} proves that $A\to B$ is flat and that
$$
\mathfrak m_y\OO_{X,x}=\mathfrak m_x.
$$
By hypothesis $k_x/k_y$ is separable algebraic. Thus $f$ is unramified at
$x$ in Hartshorne's sense.
Exercise [[P-AGH3103ETALECHAR|III.10.3]] says that flat plus unramified is
equivalent to étale. Therefore $f$ is étale at $x$.

:::

:::

::: {.pf-step #s7}

The two conditions are equivalent globally.

::: pf-proof

If $f$ is étale, steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} establish the stated completed-local-ring
condition for every $x\in X$.
Conversely, if that condition holds for every $x$, steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} show that
$f$ is étale at every point of $X$. Hence $f$ is étale.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove the forward implication by comparing associated graded
rings, and steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} recover flatness and unramifiedness from the
completed isomorphism and descend them to the original local rings.

:::

:::

:::
