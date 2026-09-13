---
schema: qual/card@1
id: D-L6ERW
kind: definition
title: The Hilbert polynomial, and what its coefficients mean
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomial
  - Degree
  - Arithmetic Genus
relations:
- kind: uses
  target: D-CP2MH
- kind: uses
  target: D-5LJUX
review: draft
prompts:
- What is the Hilbert polynomial of a projective variety?
- What does the leading term of $P_X(r)$ mean?
- What does the constant term of $P_X(r)$ represent?
---

::: {.definition title="Hilbert polynomial"}
For $X \subseteq \PP^n$ closed with homogeneous coordinate ring $S(X) = k[x_0,\ldots,x_n]/I(X)$, the **Hilbert function** is
\[
h_X(r) \da \dim_k S(X)_r .
\]
For $r \gg 0$ it agrees with a polynomial $P_X(r)$, the **Hilbert polynomial** of $X$.
:::

::: {.remark title="Reading off the coefficients"}
Write $\dim X = d$.
Then $\deg P_X = d$, and

- the leading coefficient is $\deg(X)/d!$, which *defines* the degree of $X$;

- the constant term is $\chi(\OO_X) = 1 - p_a(X)$, which defines the arithmetic genus.

Both readings are sensitive to the embedding, because $S(X)$ is: $P_X$ is an invariant of $X \subseteq \PP^n$ together with $\OO_X(1)$, not of $X$ alone.
This is the precise sense in which degree depends on the embedding while the genus of a smooth curve does not.
:::

::: {.remark title="The example to have ready"}
$P_{\PP^n}(r) = \binom{r+n}{n}$, of degree $n$ and leading coefficient $1/n!$, so $\deg \PP^n = 1$ and $p_a(\PP^n) = 0$.

On $\PP^1$ the connection to line bundles is visible: $h^0(\PP^1, \OO(m)) = m+1$, and taking $m = 3r$ recovers the Hilbert polynomial of the twisted cubic, $P(r) = 3r+1$ — degree $3$, arithmetic genus $0$.
:::
