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
\[
i:X\hookrightarrow\beta X
\]
denote the canonical embedding.

<1>1. The space $\beta X$ is compact Hausdorff, and
\[
i(X)
\]
is dense in $\beta X$.

::: {.proof}
These are the first defining properties of a compactification of the
completely regular Hausdorff space $X$: the map $i$ is a homeomorphism of
$X$ onto a dense subspace of the compact Hausdorff space $\beta X$.
:::

<1>2. The Čech--Stone compactification is characterized by the following
universal extension property:

for every compact Hausdorff space $K$ and every continuous map
\[
f:X\to K,
\]
there exists a unique continuous map
\[
\bar f:\beta X\to K
\]
such that
\[
\bar f\circ i=f.
\]

::: {.proof}
This is the defining universal property of the Čech--Stone compactification.
Existence says that every map from $X$ to a compact Hausdorff target extends
across the compactification.

For uniqueness, suppose
\[
F,G:\beta X\to K
\]
are two such extensions. They agree on the dense subset $i(X)$. Since $K$ is
Hausdorff, the equalizer
\[
\{y\in\beta X:F(y)=G(y)\}
\]
is closed. It contains the dense set $i(X)$, hence equals all of $\beta X$.
Thus
\[
F=G.
\]
:::

<1>3. Equivalently, every bounded continuous real-valued function
\[
f\in C_b(X)
\]
extends uniquely to a continuous function
\[
\bar f\in C(\beta X).
\]

::: {.proof}
If
\[
f:X\to\mathbb R
\]
is bounded, its image lies in some compact interval
\[
[-M,M].
\]
Apply step <1>2 with
\[
K=[-M,M].
\]

Conversely, the extension property for all compact Hausdorff targets follows
from the real-valued extension property together with the standard embedding
of every compact Hausdorff space into a product of compact intervals by its
continuous real-valued functions. Coordinatewise extension gives the desired
map into the product, and density forces its image into the embedded copy of
$K$.
:::

<1>4. The pair
\[
(\beta X,i)
\]
is unique up to a unique homeomorphism fixing $X$.

::: {.proof}
Suppose
\[
(Y,j)
\]
is another compactification satisfying the same universal property.
Apply the universal property of $\beta X$ to
\[
j:X\to Y
\]
to obtain
\[
F:\beta X\to Y
\]
with
\[
F\circ i=j.
\]

Similarly, apply the universal property of $Y$ to
\[
i:X\to\beta X
\]
to obtain
\[
G:Y\to\beta X
\]
with
\[
G\circ j=i.
\]

Then
\[
G\circ F:\beta X\to\beta X
\]
and
\[
\operatorname{id}_{\beta X}
\]
agree on the dense set $i(X)$. By uniqueness in step <1>2,
\[
G\circ F=\operatorname{id}_{\beta X}.
\]
Similarly,
\[
F\circ G=\operatorname{id}_Y.
\]
Thus $F$ is the unique homeomorphism carrying $i(x)$ to $j(x)$ for every
$x\in X$.
:::

<1>5. Therefore the characteristic description requested in part (1) is:
\[
\boxed{
\begin{gathered}
\beta X\text{ is compact Hausdorff},\\
X\text{ embeds densely in }\beta X,\\
\text{and every continuous }X\to K
\text{ with }K\text{ compact Hausdorff}\
\text{extends uniquely over }\beta X.
\end{gathered}}
\]

::: {.proof}
This is the combined content of steps <1>1--<1>4.
:::

<1>6. Part (2) cannot be answered from the retained source.

::: {.proof}
The retained extraction does not preserve the spaces or sets whose
cardinalities are requested. Cardinalities of Čech--Stone compactifications
depend essentially on the underlying spaces; for example,
\[
|\beta X|
\]
cannot be determined from the symbol $\beta$ alone.

Thus supplying numerical or cardinal answers would require reconstructing
missing source data not present in the repository.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 completely answers the recoverable characteristic-property
subproblem, and step <1>6 records the exact source obstruction for the
unrecoverable cardinality subproblem.
:::
:::
