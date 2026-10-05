---
schema: qual/card@1
id: P-MAXAT-5-03
kind: problem
title: Maxim algebraic topology 5.3
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 5, problem 3 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that if an oriented vector bundle has a non-zero section, then it’s Euler class is zero.
:::

::: {.solution}
Let
\[
\xi:E\to X
\]
be an oriented real vector bundle of rank $r$, and suppose it has a nowhere-zero section $s$.

<1>1. Choose a bundle metric on $\xi$ and normalize $s$ to a unit section
\[
\widehat s(x)=\frac{s(x)}{\|s(x)\|}.
\]

::: {.proof}
A vector bundle over the usual paracompact base admits a fiberwise inner product. Since $s(x)\ne0$ for every $x$, its norm is a positive continuous function, so normalization is well-defined and continuous.
:::

<1>2. The unit section spans a trivial oriented line subbundle
\[
\varepsilon^1\subset\xi.
\]

::: {.proof}
Define
\[
X\times\mathbb R\to E,
\qquad
(x,t)\mapsto t\widehat s(x).
\]
This is a fiberwise injective bundle map whose image is the line spanned by $\widehat s(x)$ in each fiber. The chosen vector $\widehat s(x)$ gives the line its standard orientation, so the subbundle is the trivial oriented line bundle.
:::

<1>3. The metric gives an orthogonal splitting
\[
\xi\cong\varepsilon^1\oplus\eta
\]
for a rank-$(r-1)$ bundle $\eta$.

::: {.proof}
Let $\eta_x$ be the orthogonal complement of the line $\mathbb R\widehat s(x)$ in $E_x$. These complements vary continuously and form a vector subbundle. Fiberwise orthogonal projection gives the displayed direct-sum decomposition.
:::

<1>4. The Euler class satisfies the Whitney product formula
\[
e(\xi)=e(\varepsilon^1)\smile e(\eta).
\]

::: {.proof}
For oriented real vector bundles $\alpha$ and $\beta$, the Thom class of $\alpha\oplus\beta$ is the exterior product of their Thom classes. Pulling back along the zero section gives
\[
e(\alpha\oplus\beta)=e(\alpha)\smile e(\beta).
\]
Apply this to the splitting in step <1>3, with the induced orientation on $\eta$ chosen so that the direct-sum orientation agrees with that of $\xi$.
:::

<1>5. The Euler class of the trivial line bundle vanishes:
\[
e(\varepsilon^1)=0.
\]

::: {.proof}
The Euler class of an oriented rank-one bundle lies in $H^1(X;\mathbb Z)$ and is the obstruction to a nowhere-zero section. The trivial line bundle has the constant nowhere-zero section $1$. Equivalently, its classifying map is constant, so every positive-degree characteristic class pulls back to zero.
:::

<1>6. Hence
\[
\boxed{e(\xi)=0.}
\]

::: {.proof}
Substitute step <1>5 into the Whitney formula of step <1>4:
\[
e(\xi)=0\smile e(\eta)=0.
\]
:::

<1>7. Equivalently, this is the primary obstruction interpretation of the Euler class.

::: {.proof}
For an oriented rank-$r$ bundle, $e(\xi)\in H^r(X;\mathbb Z)$ is the primary obstruction to extending a nowhere-zero section over the $r$-skeleton. A global nowhere-zero section already exists by hypothesis, so that obstruction must vanish. This independently gives the conclusion of step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>6 proves the required vanishing.
:::
:::
