---
schema: qual/card@1
id: P-WESTOP05-05
kind: problem
title: Characterize the Čech--Stone compactification and an unrecovered cardinality subproblem
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: >-
    Part (b) is badly garbled in the retained extraction: only “What are the
    cardinalities of ββS(? β[,?” survives. The named spaces or sets cannot be
    recovered safely.
---

::: {.problem}
Let $X$ be completely regular Hausdorff and consider its Čech--Stone compactification $\beta X$.

1. State a set of characteristic properties of $\beta X$; describe what it is rather than how to construct it.
2. The source next asks for the cardinalities of several expressions involving $\beta$, but their arguments are unrecovered in the retained extraction. This subproblem is left explicit rather than reconstructed.
:::

::: {.solution}

Let
$$
i:X\hookrightarrow\beta X
$$
denote the canonical embedding.

::: pf

::: {.pf-step #s1-1}

The space $\beta X$ is compact Hausdorff, and
$$
i(X)
$$
is dense in $\beta X$.


::: pf-proof

These are the first defining properties of a compactification of the
completely regular Hausdorff space $X$: the map $i$ is a homeomorphism of
$X$ onto a dense subspace of the compact Hausdorff space $\beta X$.

:::

:::

::: {.pf-step #s1-2}

The Čech--Stone compactification is characterized by the following
universal extension property:

for every compact Hausdorff space $K$ and every continuous map
$$
f:X\to K,
$$
there exists a unique continuous map
$$
\bar f:\beta X\to K
$$
such that
$$
\bar f\circ i=f.
$$


::: pf-proof

This is the defining universal property of the Čech--Stone compactification.
Existence says that every map from $X$ to a compact Hausdorff target extends
across the compactification.

For uniqueness, suppose
$$
F,G:\beta X\to K
$$
are two such extensions. They agree on the dense subset $i(X)$. Since $K$ is
Hausdorff, the equalizer
$$
\{y\in\beta X:F(y)=G(y)\}
$$
is closed. It contains the dense set $i(X)$, hence equals all of $\beta X$.
Thus
$$
F=G.
$$

:::

:::

::: {.pf-step #s1-3}

Equivalently, every bounded continuous real-valued function
$$
f\in C_b(X)
$$
extends uniquely to a continuous function
$$
\bar f\in C(\beta X).
$$


::: pf-proof

If
$$
f:X\to\RR
$$
is bounded, its image lies in some compact interval
$$
[-M,M].
$$
Apply step [](#s1-2){.pf-ref} with
$$
K=[-M,M].
$$

Conversely, the extension property for all compact Hausdorff targets follows
from the real-valued extension property together with the standard embedding
of every compact Hausdorff space into a product of compact intervals by its
continuous real-valued functions. Coordinatewise extension gives the desired
map into the product, and density forces its image into the embedded copy of
$K$.

:::

:::

::: {.pf-step #s1-4}

The pair
$$
(\beta X,i)
$$
is unique up to a unique homeomorphism fixing $X$.


::: pf-proof

Suppose
$$
(Y,j)
$$
is another compactification satisfying the same universal property.
Apply the universal property of $\beta X$ to
$$
j:X\to Y
$$
to obtain
$$
F:\beta X\to Y
$$
with
$$
F\circ i=j.
$$

Similarly, apply the universal property of $Y$ to
$$
i:X\to\beta X
$$
to obtain
$$
G:Y\to\beta X
$$
with
$$
G\circ j=i.
$$

Then
$$
G\circ F:\beta X\to\beta X
$$
and
$$
\operatorname{id}_{\beta X}
$$
agree on the dense set $i(X)$. By uniqueness in step [](#s1-2){.pf-ref},
$$
G\circ F=\operatorname{id}_{\beta X}.
$$
Similarly,
$$
F\circ G=\operatorname{id}_Y.
$$
Thus $F$ is the unique homeomorphism carrying $i(x)$ to $j(x)$ for every
$x\in X$.

:::

:::

::: {.pf-step #s1-5}

Therefore the characteristic description requested in part (1) is:
$$
\boxed{
\begin{gathered}
\beta X\text{ is compact Hausdorff},\\
X\text{ embeds densely in }\beta X,\\
\text{and every continuous }X\to K
\text{ with }K\text{ compact Hausdorff}\
\text{extends uniquely over }\beta X.
\end{gathered}}
$$


::: pf-proof

This is the combined content of steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Part (2) cannot be answered from the retained source.


::: pf-proof

The retained extraction does not preserve the spaces or sets whose
cardinalities are requested. Cardinalities of Čech--Stone compactifications
depend essentially on the underlying spaces; for example,
$$
|\beta X|
$$
cannot be determined from the symbol $\beta$ alone.

Thus supplying numerical or cardinal answers would require reconstructing
missing source data not present in the repository.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} completely answers the recoverable characteristic-property
subproblem, and step [](#s1-6){.pf-ref} records the exact source obstruction for the
unrecoverable cardinality subproblem.

:::

:::

:::
