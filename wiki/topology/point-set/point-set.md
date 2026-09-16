---
order: 100
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

# Point-set topology

## Continuous images

[[PR-ZCUXL]]

## Metric spaces and analysis

[[T-7DICT]]

[[T-PRQ7I]]

[[PR-6T3IL]]

::: {.proof}
Let $f\colon X\to Y$ be continuous with $X$ a compact metric space, and let $\varepsilon>0$.
The sets $f\inv\qty{B_{\varepsilon/2}(y)}$ for $y\in Y$ form an open cover of $X$; let $\delta>0$ be a Lebesgue number for it.
If $d(x,x')<\delta$, then $\ts{x,x'}$ has diameter less than $\delta$, so it lies in some $f\inv\qty{B_{\varepsilon/2}(y)}$, and $d(f(x),f(x'))<\varepsilon$.

:::

[[C-EBAGE]]

::: {.example title="A uniformly continuous function that is not Lipschitz"}
$f(x) = \sqrt x$ on $[0, 1]$ is uniformly continuous, being continuous on a compact set, and is not Lipschitz, since $\abs{f(x)-f(0)}/\abs{x-0} = 1/\sqrt x$ is unbounded as $x\to 0^+$.

:::

[[T-OPK3N]]

[[T-4RLPQ]]

[[T-PCL4H]]

[[T-HH3YP]]

[[FT-6WPJI]]

## Compactness

[[T-3FJK4]]

[[T-UEXBK]]

::: {.proof}
Let $B$ be compact and $A\subseteq B$ closed, and let $\ts{A_i}_{i\in I}$ be a cover of $A$ by sets open in $A$.
By definition of the subspace topology, $A_i = B_i \intersect A$ for some $B_i$ open in $B$.
Since $A$ is closed, $W\coloneqq B\sm A$ is open, and $\ts{B_i}_{i\in I}\union\ts{W}$ is an open cover of $B$.
A finite subcover $\ts{B_{i_1},\ldots,B_{i_k},W}$ exists by compactness, and $\ts{A_{i_1},\ldots,A_{i_k}}$ covers $A$.

:::

[[T-TJBYR]]

::: {.proof}
Let $f\colon X\to Y$ be continuous with $X$ compact, and let $\mathcal{U}$ be a cover of $f(X)$ by open subsets of $Y$.
Since $f$ is continuous, $\ts{f\inv(U) \suchthat U\in\mathcal U}$ is an open cover of $X$, with a finite subcover $f\inv(U_1),\ldots,f\inv(U_k)$.
Then $U_1,\ldots,U_k$ cover $f(X)$.

:::

[[T-JFADP]]

## Separability

[[PR-O7535]]

[[PR-R72XL]]

## Separation axioms

::: {.remark}
A [[D-ZFRV4|Hausdorff space]] is one in which distinct points have disjoint open neighborhoods, and a [[D-YEQC3|normal]] space is one in which disjoint closed sets have disjoint open neighborhoods.
Urysohn's lemma states that in a normal space, disjoint closed sets are separated by a continuous function to $[0,1]$.

:::

[[FT-52GNK]]

## Maps and homeomorphisms

::: {.proof}
It suffices to show that $f$ is a closed map, since then $f\inv$ is continuous.
If $A\subseteq X$ is closed, then $A$ is compact because $X$ is compact, so $f(A)$ is compact, and a compact subset of the Hausdorff space $Y$ is closed.

:::

::: {.example title="Retractions onto points"}
For every $x_0 \in X$, the constant map $r\colon X \to \ts{x_0}$ is a [[D-NCLVD|retraction]] onto $\ts{x_0}$.

:::

[[FT-M5BHD]]

[[T-JSXGR]]

[[T-FA6VI]]

::: {.proof}
See [@Mun00, p. 104].

:::

[[T-N6PYS]]

## The tube lemma

[[T-G4GO4]]

::: {.proof}
Let $N\subseteq X\cross Y$ be open with $\ts{x_0}\cross Y\subseteq N$.
For each $y\in Y$, choose open sets $U_y\subseteq X$ and $V_y\subseteq Y$ with $(x_0,y)\in U_y\cross V_y\subseteq N$.
Since $Y$ is compact, finitely many $V_{y_1},\ldots,V_{y_n}$ cover $Y$.
Let $W\coloneqq \bigcap_{j=1}^n U_{y_j}$, an open set containing $x_0$.
For $(x,y)\in W\cross Y$, choose $j$ with $y\in V_{y_j}$; since $x\in W\subseteq U_{y_j}$, $(x,y)\in U_{y_j}\cross V_{y_j}\subseteq N$.
Hence $W\cross Y\subseteq N$.

:::

::: {.example title="The tube lemma fails without compactness"}
In $\RR\cross\RR$, the open set $N\coloneqq\ts{(x,y) \suchthat \abs y < e^{-x^2}}$ contains the slice $\RR\cross\ts{0}$, and it contains no tube $\RR\cross(-\delta,\delta)$ with $\delta>0$, since $e^{-x^2}<\delta$ for large $\abs x$.
Here the slice is taken in the noncompact factor $\RR$.

![The region between a Gaussian and its reflection](../../../../assets/assets/figures/image_2021-05-21-01-39-26.png)

:::

## Subsets of the real line

[[PR-VGX2B]]

## Exercises

[[E-OYP3Y]]
