---
schema: qual/card@1
id: P-TIE-F09-02
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 2.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the garbled set-builder LaTeX against Fall 2009, question 2, page 1 of Questions_from_Tie.pdf, whose text layer reads 1 <= theta <= 2 pi, so the bound is kept as printed.
---

::: {.problem}
Let $f$ be a continuous function in the region
$$
D = \{z \mid \abs{z} > R,\ 0 \le \arg z \le \theta\} \quad \text{where} \quad 0 \le \theta \le 2\pi.
$$
If there exists $k$ such that $\lim_{z\to\infty} zf(z) = k$ for $z$ in the region $D$. Show that
$$
\lim_{R'\to\infty} \int_L f(z)\,dz = i\theta k,
$$
where $L$ is the part of the circle $\abs{z} = R'$ which lies in the region $D$.
:::

::: {.solution}

For $R'>R$, parametrize the arc $L$ counterclockwise by
$$
\gamma_{R'}(t)=R'e^{it},
\qquad
0\le t\le\theta.
$$

::: pf

::: {.pf-step #s1-1}

The arc integral can be written as
$$
\int_L f(z)\,dz
=
i\int_0^\theta
\gamma_{R'}(t)f(\gamma_{R'}(t))\,dt.
$$


::: pf-proof

Since
$$
\gamma_{R'}'(t)=iR'e^{it}=i\gamma_{R'}(t),
$$
the definition of a contour integral gives
$$
\int_L f(z)\,dz
=
\int_0^\theta
f(\gamma_{R'}(t))\gamma_{R'}'(t)\,dt
=
i\int_0^\theta
\gamma_{R'}(t)f(\gamma_{R'}(t))\,dt.
$$

:::

:::

::: {.pf-step #s1-2}

For every $\varepsilon>0$, there exists $R_\varepsilon>R$ such that
$$
\abs{
\gamma_{R'}(t)f(\gamma_{R'}(t))-k
}
<\varepsilon
$$
for every $R'>R_\varepsilon$ and every $t\in[0,\theta]$.


::: pf-proof

The hypothesis
$$
\lim_{\substack{z\to\infty\\ z\in D}}zf(z)=k
$$
means that for every $\varepsilon>0$ there is $R_\varepsilon$ such that
$$
\abs{zf(z)-k}<\varepsilon
$$
whenever $z\in D$ and $\abs{z}>R_\varepsilon$.

For $R'>R_\varepsilon$ and $t\in[0,\theta]$, one has
$$
\gamma_{R'}(t)\in D,
\qquad
\abs{\gamma_{R'}(t)}=R'>R_\varepsilon,
$$
so the asserted estimate follows.

:::

:::

::: {.pf-step #s1-3}

For $R'>R_\varepsilon$,
$$
\abs{
\int_L f(z)\,dz-i\theta k
}
\le
\theta\varepsilon.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\int_L f(z)\,dz-i\theta k
&=
i\int_0^\theta
\left(
\gamma_{R'}(t)f(\gamma_{R'}(t))-k
\right)\,dt.
\end{aligned}
$$
Therefore step [](#s1-2){.pf-ref} gives
$$
\begin{aligned}
\abs{
\int_L f(z)\,dz-i\theta k
}
&\le
\int_0^\theta
\abs{
\gamma_{R'}(t)f(\gamma_{R'}(t))-k
}dt\\
&\le
\theta\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{
\lim_{R'\to\infty}\int_L f(z)\,dz=i\theta k
}.
$$


::: pf-proof

If $\theta=0$, then $L$ is a single point and both sides are $0$. Let $\theta>0$. Given any $\delta>0$, apply step [](#s1-3){.pf-ref} with
$$
\varepsilon=\frac{\delta}{\theta}.
$$
Then for all sufficiently large $R'$,
$$
\abs{
\int_L f(z)\,dz-i\theta k
}
<\delta.
$$
This is exactly the asserted limit.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::

::: remark
One printing of this problem restricts to $1\le\theta\le2\pi$. The proof does not use the restriction.
:::
