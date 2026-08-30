---
title: Arc estimates
order: 30
---

# Arc estimates

Closing a contour adds a piece that was not in the original integral.
The estimate that sends it to zero is what makes the whole method legal, and choosing the wrong one is the usual way a contour argument fails.

Two bounds do nearly all the work, and the second is strictly stronger than the first on the semicircle.

## The ML estimate

[[T-SFXI7]]

:::{.proof}
\[
\abs{ \int_\gamma f(z) \dz }
&\leq \int_\gamma \abs{f(z)} \dz \\
&\leq \int_\gamma \sup_{\xi\in \gamma} \abs{f(\xi)} \dz \\
&\da \int_\gamma M\dz \\
&= M \cdot \length(\gamma)
.\]

:::

:::{.remark title="What it buys"}
If $C_R$ is a circular arc of radius $R$ subtending an angle $\theta$, then $\length(C_R) = R\theta$ and
\[
\abs{\int_{C_R} f\,} \leq MR\theta
.\]
So $M = \bigo\qty{1 \over R^{1+\eps}}$ is enough for the arc to vanish, and $M = \bigo(1/R)$ is not.
Quadratic decay of a rational integrand clears this comfortably; linear decay does not, and that is exactly when Jordan's lemma is needed.

:::

## Jordan's lemma

[[T-ZO5UU]]

:::{.remark title="One power of $z$ stronger than ML"}
Take $f(z) = e^{iz}/(z^2+1)$ on the upper arc.
With $\alpha = 1$,
\[
\abs{ \int_{C_R} { e^{iz} \over z^2 + 1 } \dz } \leq \pi \sup_{z\in C_R} \abs{1\over z^2 +1} \leq {\pi \over R^2 - 1}\to 0
,\]
and the bound uses only the decay of $1/(z^2+1)$, never a bound on $e^{iz}$ itself.
That is the point: $\cos(z)$ and $\sin(z)$ are unbounded on $C_R$, so ML cannot be applied to $f(z)\cos(z)$ at all, while $\abs{e^{iz}} = e^{-\Im z} \leq 1$ on the upper half plane.

:::

:::{.proof title="of Jordan's lemma"}
\[
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
&= {\pi M_R \over a}
.\]

The one inequality doing the work is $2t/\pi \leq \sin(t)$ on $[0, \pi/2]$, which is a picture: $\sin(t)$ is a height on the circle and $2t/\pi$ is a height on the chord below it.

![figures/image_2021-06-09-01-29-22.png](../../../../assets/assets/figures/image_2021-06-09-01-29-22.png)

:::

## The small arc, which does not vanish

An arc shrinking onto a simple pole does not contribute nothing; it contributes a definite fraction of the residue.
For an arc of angle $\theta$ about a simple pole $z_0$, traversed counterclockwise,
\[
\lim_{\eps \decreasesto 0} \int_{\abs{z - z_0} = \eps} f(z) \dz = i\theta \Res_{z=z_0} f
.\]

A half-circle indenting *over* a pole on $\RR$ is traversed clockwise and subtends $\pi$, so it contributes $-i\pi \Res$.
That is where the half-residues in the principal-value formula come from.

## Which one to reach for

- Rational, decay $\bigo(1/R^{2})$ or better: ML.

- Rational times $e^{iaz}$, decay only $\bigo(1/R)$: Jordan.

- An arc closing in on a pole rather than running away from it: the small-arc lemma, and the arc keeps a share of the residue.

## Exercises

[[E-IQQAF]]
[[E-3ZAVQ]]
