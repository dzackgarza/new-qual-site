---
schema: qual/card@1
id: E-AFAON
kind: problem
title: Arithmetic of convergent sequences
classification:
  areas:
  - topology
  topics:
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Theorem.
Let $x_n \to x$ and $y_n \to y$ in the space $\mathbb{R}$.
Then

$$
\begin{array}{c}
x_n + y_n \to x + y, \\
x_n - y_n \to x - y, \\
x_n y_n \to xy,
\end{array}
$$

and provided that each $y_n \neq 0$ and $y \neq 0$,

$$
x_n / y_n \to x/y.
$$

[Hint: Apply Lemma 21.4; recall from the exercises of §19 that if $x_n \to x$ and $y_n \to y$, then $x_n \times y_n \to x \times y$.]
:::

::: {.solution}
If $F\colon X\to Y$ is continuous and $z_n\to z$ in $X$, then $F(z_n)\to F(z)$ in $Y$: a neighborhood $V$ of $F(z)$ has open preimage containing $z$, which contains $z_n$ for all large $n$.

<1>1. $(x_n,y_n)\to(x,y)$ in $\mathbb R\times\mathbb R$.

::: {.proof}
A sequence in a product converges if and only if each coordinate sequence converges, by [[E-AH7RC]].
:::

<1>2. The maps $S(u,v)=u+v$, $D(u,v)=u-v$, and $M(u,v)=uv$ from $\mathbb R\times\mathbb R$ to $\mathbb R$, and $Q(u,v)=u/v$ from $\mathbb R\times(\mathbb R-\{0\})$ to $\mathbb R$, are continuous.

::: {.proof}
For $(u,v)$ near $(a,b)$,
$$
\abs{(u\pm v)-(a\pm b)}\le\abs{u-a}+\abs{v-b},\qquad \abs{uv-ab}\le\abs u\abs{v-b}+\abs b\abs{u-a},
$$
and the right sides tend to $0$ as $(u,v)\to(a,b)$.
For $b\ne0$ and $\abs{v-b}<\abs b/2$,
$$
\Bigl\lvert\frac uv-\frac ab\Bigr\rvert=\frac{\abs{bu-av}}{\abs{vb}}\le\frac{2\bigl(\abs b\abs{u-a}+\abs a\abs{v-b}\bigr)}{b^2},
$$
which also tends to $0$.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2 and the sequence property of continuous maps, $S(x_n,y_n)\to S(x,y)$, $D(x_n,y_n)\to D(x,y)$, and $M(x_n,y_n)\to M(x,y)$.
When every $y_n\ne0$ and $y\ne0$, the sequence $(x_n,y_n)$ lies in $\mathbb R\times(\mathbb R-\{0\})$ and converges there to $(x,y)$, so $Q(x_n,y_n)\to Q(x,y)$.
:::
:::
