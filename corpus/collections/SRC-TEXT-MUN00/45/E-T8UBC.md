---
schema: qual/card@1
id: E-T8UBC
kind: problem
title: Graphs as an imbedding of the function space into the hyperspace
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; give $X \times Y$ the corresponding square metric; let $\mathcal{H}$ denote the collection of all nonempty closed, bounded subsets of $X \times Y$, in the resulting Hausdorff metric.
Consider the space $\mathcal{C}(X, Y)$ in the uniform metric; let $\operatorname{gr}: \mathcal{C}(X, Y) \to \mathcal{H}$ be the function that assigns, to each continuous function $f: X \to Y$, its graph

$$
G_f = \ts{x \times f(x) \mid x \in X}.
$$

(a) Show that the map $\operatorname{gr}$ is injective and uniformly continuous.

(b) Let $\mathcal{H}_0$ denote the image set of the map $\operatorname{gr}$; let $g: \mathcal{C}(X, Y) \to \mathcal{H}_0$ be the surjective map obtained from $\operatorname{gr}$.
Show that if $f: X \to Y$ is uniformly continuous, then the map $g^{-1}$ is continuous at the point $G_f$.

(c) Give an example where $g^{-1}$ is not continuous at the point $G_f$.

(d) Theorem.
If $X$ is compact, then $\operatorname{gr}: \mathcal{C}(X, Y) \to \mathcal{H}$ is an imbedding.
:::

::: {.solution}
Write $d_\square((x,y),(x',y'))=\max\{d_X(x,x'),d_Y(y,y')\}$ and $d_H$ for the Hausdorff metric.

(a) Distinct functions have distinct graphs, so $\operatorname{gr}$ is injective. If $\|f-h\|_\infty<\varepsilon$, then for every $x$, $(x,f(x))$ lies within $\varepsilon$ of $(x,h(x))$, and conversely. Thus
\[
d_H(G_f,G_h)\le \|f-h\|_\infty,
\]
so the graph map is $1$-Lipschitz.

(b) Fix uniformly continuous $f$ and $\varepsilon>0$. Choose $\delta<\varepsilon/2$ so that $d_X(x,x')<\delta$ implies $d_Y(f(x),f(x'))<\varepsilon/2$. If $d_H(G_f,G_h)<\delta$, then for each $x$ there is $x'$ with
\[
d_X(x,x')<\delta,\qquad d_Y(h(x),f(x'))<\delta.
\]
Hence
\[
d_Y(h(x),f(x))<\delta+\varepsilon/2<\varepsilon.
\]
Taking the supremum gives $\|h-f\|_\infty<\varepsilon$. Thus $g^{-1}$ is continuous at $G_f$.

(c) Take $X=Y=\mathbb R$, $f(x)=x^2$, and $h_n(x)=(x+1/n)^2$. The graph $G_{h_n}$ is the horizontal translate of $G_f$ by $-1/n$, so
\[
d_H(G_f,G_{h_n})\le 1/n\longrightarrow0.
\]
But
\[
\sup_{x\in\mathbb R}|h_n(x)-f(x)|
=\sup_x|2x/n+1/n^2|=\infty.
\]
Thus $g^{-1}$ is not continuous at $G_f$. (Here $f$ is not uniformly continuous, exactly as part (b) suggests.)

(d) If $X$ is compact, every continuous $f:X\to Y$ is uniformly continuous. By (b), the inverse from the image $\mathcal H_0$ to $C(X,Y)$ is continuous at every graph. Together with (a), $\operatorname{gr}$ is a homeomorphism onto its image, hence an embedding.
:::
