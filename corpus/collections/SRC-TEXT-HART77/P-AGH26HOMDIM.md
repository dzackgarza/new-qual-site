---
schema: qual/card@1
id: P-AGH26HOMDIM
kind: problem
title: The homogeneous coordinate ring satisfies $\dim S(Y) = \dim Y + 1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Coordinate Rings
  - Transcendence Degree
relations: []
review: draft
---

::: {.problem}
Let $Y$ be a projective variety with homogeneous coordinate ring $S(Y)$.
Show that $\dim S(Y) = \dim Y + 1$.

Here $U_i \da \PP^n \sm H_i$, where $H_i = Z(x_i)$ is a coordinate hyperplane, and $\phi_i : U_i \to \AA^n$ is the homeomorphism
\[
\tv{a_0 : \cdots : a_n} \mapsto \qty{ \frac{a_0}{a_i}, \ldots, \widehat{\frac{a_i}{a_i}}, \ldots, \frac{a_n}{a_i} } .
\]
Conclude also that $\dim Y = \dim Y_i$ whenever $Y_i \da \phi_i(Y \intersect U_i)$ is nonempty.
:::

::: {.solution}
Cover $Y$ by the affine charts $Y_i$.
Then $\dim Y = \sup_i \dim Y_i$, and since there are only finitely many charts the supremum is attained; after relabelling, assume it is attained at $Y_0$.

**The chart ring is the degree-zero part of a localization.** Define maps between $A(Y_0)$ and the degree-zero piece $\qty{S(Y)_{x_0}}_0$ by
\[
\alpha(f) \da f\qty{1, \frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}},
\qquad
\beta(g) \da x_0^{\deg g} \cdot g(x_0, x_1, \ldots, x_n) .
\]
These are mutually inverse ring maps: on the one hand
\[
\alpha(\beta(g)) = x_0^{\deg g} \, g\qty{1, \frac{x_1}{x_0}, \ldots, \frac{x_n}{x_0}} = g(x_0, x_1, \ldots, x_n),
\]
and on the other hand $\beta(\alpha(f)) = f$ by the same computation read backwards.
Hence $A(Y_0) \cong \qty{S(Y)_{x_0}}_0$.

**Identifying the localization.** We have $S(Y) \cong A(Y_0)[x_0]$ and $S(Y)_{x_0} \cong S(Y)[x_0\inv]$, so
\[
S(Y)_{x_0} \cong A(Y_0)[x_0, x_0\inv] .
\]

**Counting transcendence degree.** Adjoining $x_0\inv$ adds nothing transcendental, since $x_0$ and $x_0\inv$ satisfy the relation $uv - 1 = 0$.
So the transcendence degree of $A(Y_0)[x_0, x_0\inv]$ over $A(Y_0)$ equals that of $A(Y_0)[x_0]$ over $A(Y_0)$, namely $1$, and therefore
\[
\trdeg_k A(Y_0)[x_0, x_0\inv] = \trdeg_k A(Y_0) + 1 .
\]
Using the isomorphism above, $\trdeg_k S(Y)_{x_0} = \trdeg_k A(Y_0) + 1$.

**Conclusion.** Since $\dim Y_0 = \trdeg_k A(Y_0)$ and $\dim S(Y)_{x_0} = \trdeg_k S(Y)_{x_0}$, this reads
\[
\dim S(Y)_{x_0} = \dim Y_0 + 1 = \dim Y + 1 .
\]
It remains to see $\dim S(Y)_{x_0} = \dim S(Y)$, and this holds because $x_0 \in S(Y)$ already, so that $S(Y)_{x_0} \cong S(Y)[x_0\inv]$ adds only the element $x_0\inv$, which is algebraically dependent on $x_0$ via $uv - 1$.
:::
