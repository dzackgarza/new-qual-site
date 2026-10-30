---
schema: qual/card@1
id: P-WESTOP05-05
kind: problem
title: Characteristic properties and cardinalities of Čech--Stone compactifications
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
---

::: {.problem}
Let $X$ be completely regular Hausdorff and consider its Čech--Stone compactification $\beta X$.

1. State a set of characteristic properties of $\beta X$; describe what it is rather than how to construct it.
2. What are the cardinalities of $\beta\NN$? $\beta S(\omega_1)$? $\beta[0,1]$?
:::

::: {.remark}
Part 2 was read from the rendered page image; the extraction garbles it. The paper does not define $S(\omega_1)$. The solution treats the two usual readings: the discrete space of cardinality $\aleph_1$, and the ordinal space $[0,\omega_1)$.
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

One has $\cardinality{\beta\NN}=2^{\mathfrak c}$ and
$\cardinality{\beta[0,1]}=\mathfrak c$. If $S(\omega_1)$ is the discrete
space of cardinality $\aleph_1$, then
$\cardinality{\beta S(\omega_1)}=2^{2^{\aleph_1}}$; if it is the ordinal
space $[0,\omega_1)$, then $\cardinality{\beta S(\omega_1)}=\aleph_1$.


::: pf-proof

For an infinite discrete space $D$, the points of $\beta D$ are the
ultrafilters on $D$, and by the Pospíšil--Hausdorff theorem there are
$2^{2^{\cardinality{D}}}$ of them. With $\cardinality{D}=\aleph_0$ this
gives $2^{\mathfrak c}$; with $\cardinality{D}=\aleph_1$ it gives
$2^{2^{\aleph_1}}$.

The interval $[0,1]$ is compact Hausdorff, so the identity has the
universal property of step [](#s1-5){.pf-ref} and $\beta[0,1]=[0,1]$, of
cardinality $\mathfrak c$.

Every continuous $f:[0,\omega_1)\to[0,1]$ is eventually constant, so it
extends continuously to the compact Hausdorff space $[0,\omega_1]$, in
which $[0,\omega_1)$ is dense. Hence $\beta[0,\omega_1)=[0,\omega_1]$, of
cardinality $\aleph_1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers part 1, and step [](#s1-6){.pf-ref}
answers part 2.

:::

:::

:::
