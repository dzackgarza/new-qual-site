---
order: 100
problems:
  topics:
  - Compactness
  - Connectedness
  - Separation Axioms
  - Hausdorff Spaces
  - Normal Spaces
  - Urysohn Lemma
  - Metrizability
  - Paracompactness
  - Local Finiteness
  - Baire Spaces
---

# Point-Set

## Summary and Topics

Some key high-level topics:

- Connectedness
- Compactness
- Metric spaces
- Hausdorff spaces

[[PR-ZCUXL]]

## Metric Spaces and Analysis

[[T-7DICT]]

[[T-PRQ7I]]

[[PR-6T3IL]]

:::{.proof}
Take $\theset{B_{\eps \over 2}(y) \suchthat y\in Y}\covers Y$, pull back to an open cover of $X$, has Lebesgue number $\delta_L > 0$, then $x' \in B_{\delta_L}(x) \implies f(x), f(x') \in B_{\eps \over 2}(y)$ for some $y$. 

:::

[[C-EBAGE]]

:::{.remark}
Counterexample to the converse: $f(x) = \sqrt x$ on $[0, 1]$ has unbounded derivative.

:::

[[T-OPK3N]]

[[T-4RLPQ]]

[[T-PCL4H]]

[[T-HH3YP]]

[[T-HGDAG]]

## Compactness

[[T-3FJK4]]

[[T-UEXBK]]

:::{.proof}
\envlist

- Let $\theset{A_i} \rightrightarrows A$ be a covering of $A$ by sets open in $A$.
- Each $A_i = B_i \intersect A$ for some $B_i$ open in $B$ (definition of subspace topology)
- Define $V = \theset{B_i}$, then $V \rightrightarrows A$ is an open cover.
- Since $A$ is closed, $W\definedas B\setminus A$ is open
- Then $V\union W$ is an open cover of $B$, and has a finite subcover $\theset{V_i}$
- Then $\theset{V_i \intersect A}$ is a finite open cover of $A$.

:::

[[T-TJBYR]]

:::{.proof}
Let $f:X\to f(X)$ be continuous.
Take an open covering $\mathcal{U} \covers f(X)$, then $f\inv(\mathcal{U}) \covers X$, which is cover by opens since $f$ is continuous.
Take a finite subcover by compactness of $X$, then they push forward to a finite subcover of $f(X)$.

:::

[[T-JFADP]]

## Separability

[[PR-O7535]]

[[PR-R72XL]]

## Separation Axioms

:::{.remark}
Hausdorff separates pairs of points; normality separates pairs of disjoint closed sets.
Urysohn's lemma separates disjoint closed sets by a continuous function to $[0,1]$.
:::

[[FT-MHQGF]]

[[FT-52GNK]] [[FT-J7RQV]]

## Maps and Homeomorphism

[[T-WX5Y6]]

:::{.proof}
Show that $f\inv$ is continuous by showing $f$ is a closed map.
If $A\subseteq X$ is closed in a compact space, $A$ is compact.
The continuous image of a compact set is compact, so $f(A)$ is compact.
A compact set in a Hausdorff space is closed, so $f(A)$ is closed in $Y$.

:::

:::{.remark title="On retractions"}
Every space has at least one retraction - for example, the constant map $r:X \into \theset{x_0}$ for any $x\_0 \in X$.

:::

[[FT-M5BHD]]

[[T-JSXGR]]

[[T-FA6VI]]

:::{.proof}
See [@Mun00, p. 104].

:::

[[T-N6PYS]]

## The Tube Lemma

[[T-G4GO4]]

:::{.remark}
Compactness in one factor is a necessary condition.
For a counterexample, $\RR^2$ and let $N$ be the set contained between a Gaussian and its reflection across the $x\dash$axis.
Then no tube about $y=0$ is entirely contained within $N$:

![figures/image_2021-05-21-01-39-26.png](../../../../assets/assets/figures/image_2021-05-21-01-39-26.png)

:::

:::{.proof title="Sketch"}
\envlist

- For each $y\in Y$ choose neighborhoods $A_y, B_y \subseteq Y$ such that 
\[
(x, y) \in A_y \cross B_y \subseteq U
.\]
- By compactness of $Y$, reduce this to finitely many $B_y \covers Y$ so $Y = \Union_{j=1}^n B_{y_j}$
- Set $O\da \intersect_{j=1}^n B_{y_j}$; this works.

:::

:::{.proof title="Detailed proof of the Tube Lemma"}

- Let $\theset{U_j\cross V_j \suchthat j\in J} \covers X\cross Y$. 
- Fix a point $x_0\in X$, then $\theset{x_0}\cross Y \subset N$ for some open set $N$.
- By the tube lemma, there is a $U^x \subset X$ such that the tube $U^x \cross Y \subset N$.
- Since $\theset{x_0}\cross Y \cong Y$ which is compact, there is a finite subcover $\theset{U_j \cross V_j \suchthat j\leq n} \covers \theset{x_0}\cross Y$. 
-   "Integrate the $X$": write 
    $$W = \intersect_{j=1}^n U_j,$$ 
    then $x_0 \in W$ and $W$ is a finite intersection of open sets and thus open.
- Claim: $\theset{U_j \cross V_j \suchthat j\leq n}\covers W\cross Y$
  - Let $(x, y) \in W\cross Y$; want to show $(x, y)\in U_j \cross V_j$ for some $j\leq n$.
  - Then $(x_0, y) \in \theset{x_0}\cross Y$ is on the same horizontal line
  - $(x_0, y)\in U_j \cross V_j$ for some $j$ by construction
  - So $y\in V_j$ for this $j$
  - Since $x\in W$, $x\in U_j$ for *every* $j$, thus $x\in U_j$.
  - So $(x, y) \in U_j \cross V_j$

:::

## "Analysis"-esque Results in Topology

[[PR-VGX2B]]

## Exercises

[[E-OYP3Y]]
