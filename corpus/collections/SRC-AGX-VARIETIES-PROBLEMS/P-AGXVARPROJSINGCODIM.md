---
schema: qual/card@1
id: P-AGXVARPROJSINGCODIM
kind: problem
title: The singular locus of a normal projective variety has codimension at least two
classification:
  areas:
  - algebraic-geometry
  topics:
  - Singular Locus
  - Normality
  - Codimension
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Proposition 8.3 together with Definitions 8.2 in the
    recorded source. It states that the singular locus of a projective variety
    is proper Zariski closed, and that for a normal projective variety every
    irreducible component of the singular locus has codimension at least 2.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Replaced the unused symbol d' by the actual codimension statement and made
    the source's standing algebraically closed characteristic-zero field
    explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Applied the affine regular-locus theorem chartwise to prove the singular
    locus proper closed, then used the one-dimensional normal-local-domain DVR
    criterion at codimension-one generic points to exclude codimension-one
    singular components.
---

::: {.problem}
Let $X$ be a projective variety over an algebraically closed field $k$ of
characteristic zero. Show that
$$
\operatorname{Sing}(X)
$$
is a proper Zariski-closed subset of $X$. If $X$ is normal, show that every
irreducible component $Z$ of $\operatorname{Sing}(X)$ satisfies
$$
\codim(Z,X)\geq2.
$$
:::

::: {.solution}
Choose an embedding
$$
X\subseteq\PP^n_k
$$
and let
$$
U_i=\{x_i\ne0\}\subseteq\PP^n_k,
\qquad
X_i=X\intersect U_i.
$$
The nonempty $X_i$ are affine varieties and cover $X$.

<1>1. For every $i$,
$$
\operatorname{Sing}(X)\intersect X_i
=
\operatorname{Sing}(X_i).
$$

::: {.proof}
Smoothness and regularity are local properties. The open immersion
$$
X_i\hookrightarrow X
$$
identifies the local ring of $X_i$ at any point $p\in X_i$ with the local
ring of $X$ at $p$. Hence $p$ is smooth in $X_i$ exactly when it is smooth
in $X$, giving the displayed identity.
:::

<1>2. For every nonempty affine chart $X_i$, the subset
$$
\operatorname{Sing}(X_i)
$$
is a proper Zariski-closed subset of $X_i$.

::: {.proof}
For an affine variety over an algebraically closed field, the regular locus
is a nonempty Zariski-open subset; equivalently the singular locus is proper
and closed. This is the standard regular-locus theorem
[@Har10a, Theorem I.5.3], and it is computed by the Jacobian criterion
recorded in [[PR-MORJAC]].

Applying that theorem to the affine variety $X_i$ gives the assertion.
:::

<1>3. The singular locus
$$
\operatorname{Sing}(X)
$$
is Zariski closed in $X$.

::: {.proof}
By step <1>1 and step <1>2, for every chart $X_i$ the intersection
$$
\operatorname{Sing}(X)\intersect X_i
$$
is closed in $X_i$. Therefore its complement has open intersection with
every member of the open cover $\{X_i\}$. Hence
$$
X\sm\operatorname{Sing}(X)
$$
is open in $X$, so $\operatorname{Sing}(X)$ is closed.
:::

<1>4. The singular locus is a proper subset of $X$.

::: {.proof}
Since $X$ is nonempty, at least one chart $X_i$ is nonempty. By step <1>2,
that chart contains a smooth point. Step <1>1 says that this point is smooth
in $X$ as well. Hence
$$
\operatorname{Sing}(X)\ne X.
$$
Together with step <1>3, this proves that the singular locus is proper
Zariski closed.
:::

<1>5. Assume now that $X$ is normal. Every codimension-one point of $X$ is
smooth.

::: {.proof}
Let $\eta$ be the generic point of an irreducible closed subset of
codimension one. Then
$$
\dim\mco_{X,\eta}=1.
$$
Normality of $X$ makes $\mco_{X,\eta}$ a normal domain. Since $X$ is a
variety, this local ring is Noetherian.

A one-dimensional Noetherian normal local domain is a discrete valuation
ring by [[D-QJ5M9]]. Hence $\mco_{X,\eta}$ is regular. The field $k$ is
perfect because it is algebraically closed, so regularity is equivalent to
smoothness for varieties over $k$ by [[T-MORSMREG]]. Therefore $\eta$ is a
smooth point of $X$.
:::

<1>6. If $X$ is normal, every irreducible component $Z$ of
$\operatorname{Sing}(X)$ has
$$
\boxed{\codim(Z,X)\geq2.}
$$

::: {.proof}
By step <1>4, the singular locus is a proper closed subset, so every
irreducible component has positive codimension.

Suppose some component $Z$ had codimension one, and let $\eta_Z$ be its
generic point. Since $Z\subseteq\operatorname{Sing}(X)$ and the singular
locus is closed,
$$
\eta_Z\in\operatorname{Sing}(X).
$$
But step <1>5 says every codimension-one point is smooth, a contradiction.
Thus codimension one cannot occur, and every component has codimension at
least two.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove that the singular locus is proper Zariski closed.
Steps <1>5--<1>6 prove the codimension bound under normality.
:::
:::
