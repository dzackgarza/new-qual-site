---
schema: qual/card@1
id: P-TIE-F11-02
kind: problem
title: Limit of integrals over large circular arcs when $zf(z)\to k$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 2.
---

::: {.problem}
Let $f$ be a continuous function in the region

$$
D = \theset{z \st \abs z > R,\ 0 \leq \arg z \leq \theta} \quad \text{where} \quad 0 \leq \theta \leq 2 \pi .
$$

If there exists $k$ such that $\lim_{z \to \infty} z f(z) = k$ for $z$ in the region $D$, show that

$$
\lim_{R' \to \infty} \int_L f(z)\,dz = i \theta k ,
$$

where $L$ is the part of the circle $\abs z = R'$ which lies in the region $D$.
:::

::: {.solution}

For $r>R$, parametrize the positively oriented arc $L_r$ by
$$
z(t)=re^{it},
\qquad 0\le t\le\theta.
$$

::: pf

::: {.pf-step #s1-1}

The integral over $L_r$ satisfies
$$
\int_{L_r} f(z)\,dz
=
i\int_0^\theta re^{it}f(re^{it})\,dt.
$$


::: pf-proof

Under the parametrization above,
$$
dz=ire^{it}\,dt.
$$
Substitution into the contour integral gives
$$
\int_{L_r} f(z)\,dz
=
\int_0^\theta f(re^{it})ire^{it}\,dt
=
i\int_0^\theta re^{it}f(re^{it})\,dt.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\lim_{r\to\infty}
\int_0^\theta
\left(re^{it}f(re^{it})-k\right)\,dt
=0.
$$


::: pf-proof

Since $zf(z)\to k$ as $z\to\infty$ in $D$, for every $\varepsilon>0$ there exists $M>0$ such that
$$
\abs{zf(z)-k}<\frac{\varepsilon}{1+\theta}
$$
whenever $z\in D$ and $\abs{z}>M$. If $r>M$, then $re^{it}\in D$ and $\abs{re^{it}}=r>M$ for every $t\in[0,\theta]$. Hence
$$
\begin{aligned}
\abs{
\int_0^\theta
\left(re^{it}f(re^{it})-k\right)\,dt
}
&\le
\int_0^\theta
\abs{re^{it}f(re^{it})-k}\,dt \\
&\le
\frac{\theta}{1+\theta}\varepsilon
<\varepsilon.
\end{aligned}
$$
This proves the asserted limit.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\lim_{r\to\infty}\int_{L_r}f(z)\,dz
=i\theta k.
}
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\int_{L_r}f(z)\,dz-i\theta k
=
i\int_0^\theta
\left(re^{it}f(re^{it})-k\right)\,dt.
$$
The right-hand side tends to $0$ by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required limit.

:::

:::

:::
