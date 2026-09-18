---
schema: qual/card@1
id: P-AGH394FLATLOCUS
kind: problem
title: The flat locus is open
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Openness of Flatness
  - Noetherian Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.9.4 and checked the cited EGA IV_3, 11.1.1 openness theorem against the modern finite-presentation flat-locus formulation. The proof reduces the scheme statement exactly to the affine commutative-algebra theorem; no regularity, Cohen--Macaulay, or fibre-dimension hypothesis is inserted.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be a morphism of finite type of noetherian schemes.
Show that
\[
\ts{ x \in X \st f \text{ is flat at } x }
\]
is an open subset of $X$, possibly empty.

See Grothendieck, EGA $\mathrm{IV}_3$, 11.1.1.
:::

::: {.solution}
Let
$$
F=\{x\in X:f\text{ is flat at }x\}.
$$
The commutative-algebra input is the openness-of-flatness theorem cited in the problem: if
$$
R\longrightarrow S
$$
is a ring homomorphism of finite presentation, then
$$
\{\mathfrak q\in\Spec S:S_{\mathfrak q}
\text{ is flat over }R_{\mathfrak q\cap R}\}
$$
is open in $\Spec S$.
This is EGA $\mathrm{IV}_3$, 11.1.1; equivalently it is the affine finite-presentation flat-locus theorem.

<1>1. The assertion is local on both $X$ and $Y$.

::: {.proof}
Whether $f$ is flat at a point $x\in X$ depends only on the local homomorphism
$$
\OO_{Y,f(x)}\longrightarrow\OO_{X,x}.
$$
Thus replacing $X$ by an open neighborhood of $x$, or $Y$ by an open neighborhood of $f(x)$ containing the image of that neighborhood, does not change flatness at $x$.

To prove that $F$ is open, it is therefore enough to show that every $x\in F$ has an open neighborhood contained in $F$.
Choose affine opens
$$
f(x)\in V=\Spec R\subseteq Y
$$
first.
The inverse image $f^{-1}(V)$ is an open neighborhood of $x$, so choose an affine open
$$
x\in U=\Spec S\subseteq f^{-1}(V).
$$
Then the restricted morphism is induced by a ring map
$$
R\longrightarrow S.
$$
:::

<1>2. The affine ring map $R\to S$ in step <1>1 is of finite presentation.

::: {.proof}
The restricted morphism $U\to V$ is of finite type because $f$ is of finite type.
Hence $S$ is a finitely generated $R$-algebra, say
$$
S\cong R[t_1,\ldots,t_m]/I.
$$
The scheme $Y$ is noetherian, so the affine ring $R$ is noetherian.
Therefore the polynomial ring
$$
R[t_1,\ldots,t_m]
$$
is noetherian, and its ideal $I$ is finitely generated.
Thus $S$ is finitely presented as an $R$-algebra.
:::

<1>3. On the affine open $U=\Spec S$, the flat locus of $f$ is open.

::: {.proof}
Let $\mathfrak q\in\Spec S$ correspond to a point of $U$, and put
$$
\mathfrak p=\mathfrak q\cap R.
$$
The local homomorphism of the morphism $U\to V$ at $\mathfrak q$ is
$$
R_{\mathfrak p}\longrightarrow S_{\mathfrak q}.
$$
Thus $f$ is flat at the point $\mathfrak q$ exactly when $S_{\mathfrak q}$ is flat over $R_{\mathfrak p}$.

By step <1>2, $R\to S$ is of finite presentation.
The affine openness-of-flatness theorem quoted above therefore says that
$$
F\cap U
=
\{\mathfrak q\in\Spec S:S_{\mathfrak q}
\text{ is flat over }R_{\mathfrak q\cap R}\}
$$
is open in $U$.
In particular, if $x\in F\cap U$, there is an open neighborhood of $x$ in $U$, hence in $X$, on which $f$ is flat at every point.
:::

<1>4. The flat locus $F$ is open in $X$.

::: {.proof}
For every $x\in F$, step <1>1 supplies an affine neighborhood $U$ to which step <1>3 applies.
Thus $F\cap U$ is an open neighborhood of $x$ contained in $F$.
Therefore
$$
F=\bigcup_{x\in F}(F\cap U_x)
$$
is a union of open subsets of $X$ and hence is open.
The union may be empty, exactly as allowed in the statement.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves that the set of points where $f$ is flat is open.
:::
:::
