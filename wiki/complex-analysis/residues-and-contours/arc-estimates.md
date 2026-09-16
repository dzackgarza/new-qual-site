---
title: Arc estimates
order: 30
---

# Arc estimates

Evaluating a real integral by a closed contour requires the integral over the added arc to tend to a known limit.
The ML estimate bounds an integral by the length of the curve times the supremum of the integrand; on a semicircle, Jordan's lemma improves this bound for integrands with a factor $e^{i\alpha z}$.

## The ML estimate

[[T-SFXI7]]

::: {.proof}
$$
\begin{aligned}
\abs{ \int_\gamma f(z) \dz }
&\leq \int_\gamma \abs{f(z)} \abs{\dz} \\
&\leq \int_\gamma \sup_{\xi\in \gamma} \abs{f(\xi)} \abs{\dz} \\
&= M \cdot \length(\gamma)
\end{aligned}.$$

:::

::: {.remark title="Circular arcs"}
If $C_R$ is a circular arc of radius $R$ subtending an angle $\theta$, then $\length(C_R) = R\theta$ and
$$
\abs{\int_{C_R} f\,} \leq MR\theta
.$$
So the arc integral tends to $0$ as $R\to\infty$ when $M = \bigo\qty{1 / R^{1+\varepsilon}}$ for some $\varepsilon>0$, while $M = \bigo(1/R)$ gives only a bounded integral.
For a rational function $p/q$ with $\deg q\geq \deg p + 2$, $M = \bigo(1/R^2)$; for $\deg q = \deg p + 1$, $M = \bigo(1/R)$, and Jordan's lemma applies when the integrand also has a factor $e^{i\alpha z}$ with $\alpha > 0$ on the upper semicircle.

:::

## Jordan's lemma

[[T-ZO5UU]]

::: {.example title="Jordan's lemma with $g(z) = 1/(z^2+1)$"}
On the upper semicircle $C_R$ with $R>1$, with $\alpha = 1$,
$$
\abs{ \int_{C_R} { e^{iz} \over z^2 + 1 } \dz } \leq \pi \sup_{z\in C_R} \abs{1\over z^2 +1} \leq {\pi \over R^2 - 1}\to 0
,$$
using only the bound on $1/(z^2+1)$.
On $C_R$, $\abs{e^{iz}} = e^{-\Im z} \leq 1$, while $\abs{\cos z}$ and $\abs{\sin z}$ reach $\cosh R$ and $\sinh R$ at $z = iR$; so an integrand $g(x)\cos x$ on $\RR$ is written as $\Re\bigl(g(x)e^{ix}\bigr)$ for real-valued $g$ before closing in $\HH$.

:::

::: {.proof title="Jordan's lemma"}
$$
\begin{aligned}
\abs{ \int_{C_R} f(z)\dz }
&= \abs{ \int_{C_R} e^{iaz}g(z) \dz} \\
&= \abs{ \int_{[0, \pi]} e^{ia\qty{Re^{it}}}g(Re^{it}) iRe^{it} \dt} \\
&\leq \int_{[0, \pi]} \abs{ e^{ia\qty{Re^{it}}}g(Re^{it}) iRe^{it}} \dt \\
&=R \int_{[0, \pi]} \abs{ e^{ia\qty{Re^{it}}}g(Re^{it})} \dt \\
&\leq R M_R \int_{[0, \pi]} \abs{ e^{ia\qty{Re^{it}}}} \dt \\
&= R M_R \int_{[0, \pi]} e^{\Re\qty{iaRe^{it}}} \dt \\
&= R M_R \int_{[0, \pi]} e^{\Re\qty{iaR\qty{\cos(t) + i\sin(t) } }} \dt \\
&= R M_R \int_{[0, \pi]} e^{-aR\sin(t) } \dt \\
&= 2 R M_R \int_{[0, \pi/2]} e^{-aR\sin(t) } \dt \\
&\leq 2R M_R \int_{[0, \pi/2]} e^{-aR\qty{2t\over \pi} } \dt \\
&= 2RM_R \qty{\pi \over 2aR}\qty{1-e^{-aR}} \\
&\leq {\pi M_R \over a}
\end{aligned}.$$

Here $a = \alpha$, the equality $\int_0^\pi = 2\int_0^{\pi/2}$ uses $\sin(\pi - t) = \sin t$, and the inequality $2t/\pi \leq \sin(t)$ on $[0, \pi/2]$ holds because $\sin$ is concave there and agrees with $2t/\pi$ at $t=0$ and $t=\pi/2$.

![figures/image_2021-06-09-01-29-22.png](../../../../assets/assets/figures/image_2021-06-09-01-29-22.png)

:::

## Small arcs about a simple pole

The integral over an arc of angle $\theta$ about a simple pole $z_0$, traversed counterclockwise, tends to $i\theta\Res_{z=z_0} f$ as the radius tends to $0$.

[[T-SSNLT]]

::: {.proof}

![](../../../../assets/assets/figures/2021-12-22_05-13-27.png)

:::

A half-circle of radius $\varepsilon$ above a simple pole on $\RR$, traversed clockwise from $z_0-\varepsilon$ to $z_0+\varepsilon$, contributes $-i\pi \Res_{z=z_0} f$ in the limit; these terms give the half-residues in principal-value integrals.

## Summary

- Integrand $\bigo(1/R^{2})$ on large arcs: the ML estimate.

- Integrand $e^{i\alpha z}g(z)$ with $\alpha>0$ and $g = \bigo(1/R)$ on the upper semicircle: Jordan's lemma.

- Arcs of radius $\varepsilon\to 0$ about a simple pole: [[T-SSNLT]], with limit $i\theta\Res$.

## Exercises

[[E-IQQAF]]
[[E-3ZAVQ]]
