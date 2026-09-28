---
schema: qual/card@1
id: E-SS2.EX-9
kind: problem
title: A self-map of a bounded set with $\varphi(z_0)=z_0$ and $\varphi'(z_0)=1$ is the identity
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
9. Let Ω be a bounded open subset of $\mathbb { C } ,$ and $\varphi : \Omega \to \Omega$ a holomorphic function.
   Prove that if there exists a point $z _ { 0 } \in \Omega$ such that

$$
\varphi (z _ {0}) = z _ {0} \quad \mathrm{and} \quad \varphi^ {\prime} (z _ {0}) = 1
$$

then $\varphi$ is linear.

[Hint: Why can one assume that $z _ { 0 } = 0 ?$ Write $\varphi ( z ) = z + a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ near 0, and prove that if $\varphi _ { k } = \varphi \circ \cdots \circ \varphi$ (where $\varphi$ appears k times), then $\varphi _ { k } ( z ) =$ $z + k a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ . Apply the Cauchy inequalities and let $k \to \infty$ to conclude the proof. Here we use the standard O notation, where $f ( z ) = O ( g ( z ) )$ as $z \to 0$ means that $| f ( z ) | \leq C | g ( z ) |$ for some constant C as $| z | \xrightarrow { } 0 . ]$
:::

::: {.solution}
Translating $\Omega$ by $-z_0$, assume $z_0=0$, so $\varphi(0) = 0$ and $\varphi'(0) = 1$. Since $\Omega$ is bounded, there is $M$ with $\abs z\le M$ for all $z \in \Omega$, and there is $r > 0$ with $\overline{D}_r(0) \subset \Omega$. For $k\ge1$ let $\varphi_k$ be the $k$-fold iterate of $\varphi$; since $\varphi(\Omega)\subseteq\Omega$, $\abs{\varphi_k}\le M$ on $\Omega$.

<1>1. If $\varphi(z) = z + a_n z^n + O(z^{n+1})$ with $n\ge2$, then $\varphi_k(z) = z + k a_n z^n + O(z^{n+1})$ for every $k\ge1$.

::: {.proof}
By induction on $k$; the case $k = 1$ is the hypothesis. If the claim holds for $k$, then
$$\varphi_{k+1}(z) = \varphi_k(z) + a_n \varphi_k(z)^n + O(\varphi_k(z)^{n+1}) = z + (k+1) a_n z^n + O(z^{n+1}),$$
because $\varphi_k(z)^n=z^n+O(z^{n+1})$.
:::

<1>2. Every Taylor coefficient of $\varphi$ at $0$ of order $n\ge2$ vanishes.

::: {.proof}
Suppose not, and let $n \ge 2$ be the least order with $a_n\ne0$, so that $\varphi(z) = z + a_n z^n + O(z^{n+1})$. By step <1>1, $\varphi_k^{(n)}(0)/n! = k a_n$, and the Cauchy inequalities on $\abs z=r$ give $\abs{k a_n} \le M/r^n$ for every $k \ge 1$. Letting $k \to \infty$ gives $a_n = 0$, a contradiction.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, $\varphi(z)=z$ near $0$, so $\varphi(z)=z$ on the connected component of $\Omega$ containing $0$ by the identity theorem. Undoing the translation, $\varphi(z)=z$ there; in particular $\varphi$ is linear when $\Omega$ is connected.
:::
:::

::: {.remark}
Connectedness is needed. For $\Omega=\mathbb D\cup D_1(3)$, the map equal to $z$ on $\mathbb D$ and to the constant $3$ on $D_1(3)$ is holomorphic from $\Omega$ to $\Omega$, fixes $0$ with derivative $1$, and is not linear.
:::
