# Surfaces and Manifolds

:::{.remark}
The most common spaces appearing in this theory:

- $\SS ^2$, 
- $\TT^2 \definedas  S^1\cross S^1$, 
- $\RP^2$
- $\KK$ the Klein bottle
- $\bbm$ the Möbius Strip
- $\Sigma_n \definedas \#_{i=1}^n \TT^2$.

The first 4 can be obtained from the following pasting diagrams:

![Pasting Diagrams for Surfaces](../../../../assets/assets/40_Topology/figures/PastingDiagrams.png)

:::

## Classification of Surfaces

[[T-NBARV]]

[[PR-JL5JP]]

[[PR-ZW6XI]]

:::{.remark}
Examples, general procedure?
:::

:::{.fact table="Table of surfaces possible for a given Euler characteristic"}

| Orientable?  | $-4$       | $-3$        | $-2$       | $-1$        | $0$                  | $1$     | $2$         |
| ------------ | ---        | ----        | ----       | ---         | ---                  | ---     | ---         |
| Yes          | $\Sigma_3$ | $\emptyset$ | $\Sigma_2$ | $\emptyset$ | $\TT^2, S^1\cross I$ | $\DD^2$ | $\SS^2$     |
| No           | ?          | ?           | ?          | ?           | $\KK, \bbm$          | $\RP^2$ | $\emptyset$ |

:::

[[PR-QV4U5]]
:::{.proof}
Todo
:::


[[C-CT2NX]]
:::{.proof}
Set $U= A, B=V$, then by definition of the connect sum, $A\cap B = \SS^2$ where $\chi(\SS^2) = 2$
:::

[[PR-GKRFP]]

[[PR-LIXWH]]
:::{.proof}
Todo
:::


[[PR-BDH3V]]
:::{.proof}
Todo
:::


## Manifolds

:::{.remark}
To show something is not a manifold, try looking at local homology. 
Can use point-set style techniques like removing points, i.e. $H_1(X, X-\pt)$; this should essentially always yield $\ZZ$ by excision arguments.
:::

[[PR-ZCPDD]]

[[PR-LR35S]]

[[PR-4X6G2]]

[[PR-AZQ6S]]

[[PR-TU4G5]]

:::{.proof title="?"}
Todo.
Uses Poincaré duality?
:::


[[PR-3FB24]]

[[PR-BQKHS]]

[[T-QNYSB]]


### 3-Manifolds, and Knot Complements

:::{.fact}
Every $\CC\dash$manifold is canonically orientable.
:::

[[PR-UL3KL]]

[[PR-6HORN]]

:::{.proof title="?"}
Todo
:::


[[PR-WCHFF]]

:::{.proof}
Apply Mayer-Vietoris, taking $S^3 = n(K) \cup (S^3-K)$, where $n(K) \homotopic S^1$ and $S^3-K \cap n(K) \homotopic T^2$. 
Use the fact that $S^3-K$ is a connected, open 3-manifold, so $H^3(S^3-K) =0$.
:::
