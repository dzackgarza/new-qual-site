---
schema: qual/card@1
id: P-GMWKE
kind: problem
title: Cohomology of $S^2 \vee S^2 \vee S^4$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Three of the four steps asserted their claim with no justification and each now carries one: the
    wedge's reduced cohomology as the direct sum over summands, with $\tilde H^k(S^2)$ and
    $\tilde H^k(S^4)$ giving $\ZZ^2$ in degree $2$ and $\ZZ$ in degree $4$; the existence of the three
    classes, which needs the collapse maps to split the inclusions; and the ring presentation, which is
    the additive computation together with the vanishing of all products of positive-degree classes.
    Checked while writing: $\alpha^2$ lies in $H^4(S^2_a) = 0$ and $\alpha\beta$ restricts to zero on
    each summand, so the relations are forced, and the quotient has the ranks the first step computes.
    The statement is unchanged. The card stands alone, with no collection provenance and no retained
    published solution, so the argument is the card's own.
---

::: {.problem}
Compute the cohomology groups and cohomology ring $H^*(S^2 \vee S^2 \vee S^4; \ZZ)$ of the wedge sum $X = S^2 \vee S^2 \vee S^4$.
:::

::: {.solution}
Let
$$
X=S^2_a\vee S^2_b\vee S^4.
$$

::: pf

::: {.pf-step #additive}

The reduced cohomology of a finite wedge is the direct sum of the reduced cohomologies of the summands. Hence
$$
H^k(X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,4,\\
\ZZ^2,&k=2,\\
0,&\text{otherwise}.
\end{cases}
$$


::: pf-proof
$X$ is the quotient of the disjoint union of the three spheres by identifying one point of each, and for a wedge of finitely many pointed spaces the reduced cohomology is the direct sum of the reduced cohomologies of the summands: the collapse maps $X \to S^2_a$, $X \to S^2_b$, $X \to S^4$ make the inclusions retracts, so the sum map $\bigoplus_i \tilde H^*(X_i) \to \tilde H^*(X)$ is an isomorphism. Since $\tilde H^k(S^2)$ is $\ZZ$ for $k = 2$ and zero otherwise, and $\tilde H^k(S^4)$ is $\ZZ$ for $k = 4$ and zero otherwise, the reduced group is $\ZZ$ in degrees $2$, $2$ and $4$; with $X$ path connected, adding the degree-zero group $\ZZ$ gives the table displayed.
:::

:::

::: {.pf-step #classes}

Let $\alpha,\beta\in H^2(X;\ZZ)$ be the classes coming from the two $2$-sphere summands, and let $\gamma\in H^4(X;\ZZ)$ be the class coming from the $4$-sphere summand.


::: pf-proof
Each inclusion of a summand is split injective on cohomology, being a section of the corresponding collapse map, so the generator of $H^2(S^2_a)$ has an image $\alpha$ in $H^2(X;\ZZ)$, and likewise $\beta$ from $S^2_b$ and $\gamma$ from $S^4$. By the additive computation of step [](#additive){.pf-ref} these three classes span the positive-degree reduced cohomology, and they are independent because their restrictions to their own summands are generators.
:::

:::

::: {.pf-step #products}

Every product of two positive-degree classes is zero.

::: pf-proof

For each wedge summand, the square of its positive-degree generator vanishes for dimensional reasons. Products of classes supported on distinct wedge summands vanish because the reduced diagonal of a wedge has no mixed component between distinct summands. Thus
$$
\alpha^2=\beta^2=\alpha\beta=0,
$$
and every product involving $\gamma$ also vanishes by degree.

:::

:::

::: {.pf-step #ring}

Therefore, as a graded ring,
$$
\boxed{H^*(X;\ZZ)
\cong
\ZZ[\alpha,\beta,\gamma]/
(\alpha^2,\beta^2,\alpha\beta,\alpha\gamma,\beta\gamma,\gamma^2),}
$$
with $\abs{\alpha}=\abs{\beta}=2$ and $\abs{\gamma}=4$.


::: pf-proof
Step [](#additive){.pf-ref} gives the additive groups and step [](#products){.pf-ref} says every product of two positive-degree classes vanishes, so the multiplication is determined up to nothing: the ring is the free abelian group on the three classes with all products zero. Presenting that as a quotient of the polynomial ring gives exactly the display, since the listed relations are precisely the vanishing of the products of pairs of positive-degree generators, and the degree-$2$ part is spanned by $\alpha$ and $\beta$ while the degree-$4$ part is spanned by $\gamma$.
:::

:::

:::

:::
