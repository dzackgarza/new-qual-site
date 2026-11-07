---
schema: qual/card@1
id: E-HAT-3.3-11
kind: problem
title: Degree 1 maps between surfaces
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 11; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both directions: a degree 1 map makes $f^*$ injective on $H^1$ because the pairing on
    $M_h$ is nondegenerate and $f^*\mu_h=\mu_g\ne0$, giving $2h\le2g$; conversely the pinch map
    collapsing one connected-summand of $M_g=M_h\#M_{g-h}$ has degree 1.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The card stated "iff", but p.258 prints "degree 1 maps $M_g\to M_h$ exist if $g\ge h$"; the
    card's own note had called the stored statement a match. The printed sentence is restored, and
    the converse is kept and labelled as an addition, since Exercises 12 and 13 need the
    impossibility for $j<k$ and the print does not ask for it. Both arguments rechecked: $f^*\mu_h
    =\mu_g$ from $\deg f=1$ by evaluation on the fundamental class, nondegeneracy of the cup product
    pairing on $H^1$ of a closed orientable surface, and the pinch map on $M_h\#M_{g-h}$ which is a
    local orientation-preserving homeomorphism off the collapsed point.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    The existence direction now follows Guanyu Li, Hatcher.pdf, Exercise 3.3.6 (Hatcher 3.3 #11),
    printed pp.57-58. The standard one-vertex, one-two-cell structure on M_g has attaching word the
    product of the g commutators; quotienting by X, the union of the last g-h handles a_i and b_i,
    leaves exactly the attaching word of M_h and maps the positive two-cell once onto the target's
    positive two-cell. Hence degree one. The earlier connected-sum construction is retained in the
    git history but this quotient construction is the published one shown at the top of p.58. Li's
    necessity direction uses Ex.10 and H_1 rank; the checked cup-product necessity on this card is
    retained and the printed if-statement is not widened.

---

::: {.problem}
If $M_g$ denotes the closed orientable surface of genus $g$, show that degree 1 maps $M_g \to M_h$ exist if $g \geq h$.
:::

::: {.solution}
Step [](#s1){.pf-ref} proves the converse, used by Exercises 12 and 13, although the printed sentence asks only for the direction $g\ge h$. Step [](#s2){.pf-ref} is the existence construction in Guanyu Li, Exercise 3.3.6 (Hatcher §3.3 #11), pp. 57--58.

::: pf

::: {.pf-step #s1}

Converse, proved here although the print does not ask for it, and used by Exercises 12 and 13 ($f: M_g \to M_h$ of degree $1 \implies g \ge h$):

::: pf-proof

::: pf-step

Let $f: M_g \to M_h$ be a continuous map of degree 1.
Then the induced map on top cohomology sends the fundamental class to the fundamental class:
$$
f^*(\mu_h) = \mu_g, \quad \text{where } \mu_g \in H^2(M_g; \RR) \cong \RR \text{ and } \mu_h \in H^2(M_h; \RR) \cong \RR.
$$

::: pf-proof

definition of degree via cohomology.

:::

:::

::: pf-step

We claim $f^*: H^1(M_h; \RR) \to H^1(M_g; \RR)$ is injective:
Let $\alpha \in H^1(M_h; \RR) \setminus \{0\}$.
By Poincaré Duality on $M_h$, the cup product pairing $H^1(M_h; \RR) \times H^1(M_h; \RR) \to H^2(M_h; \RR)$ is non-degenerate (skew-symmetric and non-singular).
Thus there exists $\beta \in H^1(M_h; \RR)$ such that $\alpha \smile \beta = \mu_h$.

::: pf-proof

Poincaré duality pairing on closed orientable surfaces.

:::

:::

::: pf-step

Applying $f^*$ and the ring homomorphism property of cup product:
$$
f^*(\alpha) \smile f^*(\beta) = f^*(\alpha \smile \beta) = f^*(\mu_h) = \mu_g \neq 0.
$$
Because the cup product is non-zero, $f^*(\alpha) \neq 0$.
Thus $\ker(f^*) = \{0\}$, so $f^*: H^1(M_h; \RR) \hookrightarrow H^1(M_g; \RR)$ is an injective linear map.

::: pf-proof

injectivity from non-vanishing cup product.

:::

:::

::: pf-step

Comparing dimensions:
$$
\dim_\RR H^1(M_h; \RR) \le \dim_\RR H^1(M_g; \RR) \implies 2h \le 2g \implies h \le g.
$$

::: pf-proof

$\dim H^1(M_k; \RR) = 2k$.

:::

:::

:::

:::

::: {.pf-step #s2}

Existence, the direction asked for in the printed exercise ($g \ge h \implies$ there is a degree 1 map $M_g \to M_h$):

::: pf-proof

::: pf-step

For $g=h$, the identity has degree $1$.

::: pf-proof

$\deg(\operatorname{id})=1$.
:::

:::

::: pf-step

For $g>h$, let $M_g$ have its standard one-vertex cell structure: loops $a_1,b_1,\dots,a_g,b_g$ and one $2$-cell attached by $\prod_{i=1}^g[a_i,b_i]$, and let $M_h$ have the corresponding loops $c_1,d_1,\dots,c_h,d_h$. Set
$$
X=\bigcup_{i=h+1}^{g}(a_i\cup b_i)
$$
and form the quotient $M_g/X$. The first $2h$ loops map to the loops of $M_h$, and the attaching word of the remaining $2$-cell becomes $\prod_{i=1}^h[c_i,d_i]$. Thus $M_g/X\cong M_h$, with the quotient map carrying the single $2$-cell of $M_g$ once onto the single $2$-cell of $M_h$.

::: pf-proof

The quotient identification is immediate from the two attaching words: the loops in $X$ become the basepoint, so their commutators disappear, and exactly the attaching word of $M_h$ remains. This is the construction in Guanyu Li, [`Hatcher.pdf`](https://guanyulee.github.io/Hatcher.pdf), Exercise 3.3.6 (Hatcher §3.3 #11), printed pp. 57--58 (local file `tmp/sources/hatcher-solutions-guanyu-li.pdf`).
:::

:::

::: pf-step

The quotient map has degree $1$ after the positive generators of the two $2$-cells are chosen as fundamental classes.

::: pf-proof

In these one-$2$-cell structures, the two fundamental classes are the positive $2$-cell chains. The quotient carries one to the other exactly once and with the chosen orientation. This is the degree computation at the top of printed p. 58 of Li's solution; it supplies the existence direction explicitly.
:::

:::

:::

:::
::: pf-step

Conclusion:
Degree 1 maps $M_g \to M_h$ exist if and only if $g \ge h$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
