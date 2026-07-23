---
sort: 025
title: Residues for Integrals
---

# Residues for Integrals

## Strategies

:::{.remark title="Resources"}
Some resources:

- For guidelines for what techniques to use,
[see this very detailed note](https://math.mit.edu/~jorloff/18.04/notes/topic9.pdf).

- Some good computations [here](https://math.mit.edu/~jorloff/18.04/notes/topic9.pdf).

:::

:::{.remark title="Tricks of the trade"}
\envlist

- The reverse triangle shows up here often!
\[
\abs{z-w} \geq \abs{ \abs{z} - \abs{w}} \implies {1\over \abs{z-w}}\leq \abs{1\over \abs z - \abs w} \\
\abs{z+w} = \abs{z -(-w)} \geq \abs{ \abs{z} - \abs{w}} \implies {1\over \abs{z+w}}\leq \abs{1\over \abs z - \abs w} \\
.\]

- Also often useful: $e^{-x}$ is monotonically decreasing on $\RR$, so
\[
a\leq b \implies e^{-a} \geq e^{-b}
.\]

- All residue theorems assume counterclockwise orientation.
  If your curve is clockwise (e.g. in the lower half-plane), so it traces out $[-R, R]$ on $\RR$), then a negative sign is introduced.

- Some standard contours:

  ![](figures/2021-12-23_18-51-55.png)

Let $\deg$ denote the $z\dash$adic valuation, so $\deg(p(x)/q(x)) = \deg(p) - \deg(q)$.
:::

:::{.remark title="Rational, $\deg(f) \leq -2$ or $f\sim 1/z^{1+\varepsilon}$ "}
For $\int_\RR f$: Semicircle. Always get 
\[
\int_\RR f = \sum_{z_0\in \HH} \Res_{z=z_0}f(z)
.\]

![figures/2021-07-29_18-37-57.png](../../../assets/figures/2021-07-29_18-37-57.png)

For $\int_{\RR_{\geq 0}} f$: use symmetry to convert to $\int_\RR$ (e.g. if $f$ is even), or find a symmetric ray and use a sector:

![](figures/2021-12-21_21-14-04.png)

![](figures/2021-12-21_21-17-25.png)

:::

:::{.remark title="Rational $f$ against a single $\sin$ or $\cos$, if $\deg(f) \geq -1$"}
Semicircles. Realize 
\[
\int_\RR f(z)\cos(z) = \Re\qty{\int_\RR f(z)e^{iz}}
.\]

This works for $f(z)e^{iz}$ where $f(z) = p(z)/q(z)$ with $\deg q \geq \deg p+2$ by the ML estimate, or $\deg q \geq \deg p +1$ by Jordan's lemma.
:::

:::{.remark title="Rational functions of $\cos, \sin$:"}
Set $z=e^{i\theta}$, then
\[
2\cos(z) = z + z\inv, \quad 2i\sin(z) = z - z\inv, && \dtheta = {\dz\over iz}
.\] 
Then $\int_{-\pi}^\pi f(\theta)\dtheta \to \int_{\abs{z} = 1} f(z) \dz$, which reduces to a residue count in $\DD$.

If $f(z) \approx \cos(z), \sin(z), \tan(z), \cdots$: check if $\displaystyle\int f \approx \Re\displaystyle\int (g(e^{iz}))$.

:::

:::{.remark title="Rational functions involving branch cuts ($x^\alpha, \log(x)$, etc)"}
\envlist

- $\int_{\RR_{\geq 0}} f(x)x^\alpha$ for $\alpha$ rational with $\abs{\alpha} < 1$ 

- For $f$ rational with $\deg f\leq -2$, take a keyhole

  ![](figures/2021-12-14_17-19-31.png)

  - A useful fact: 
  \[
\lim_{\eps\decreasesto 0} \ln(x-i\eps) = \ln(x) + 2\pi i
  .\]

  - Another useful fact: for any constant $c$,
  \[
  \lim_{x\to 0} {x\ln(x) \over x^n + c} = 0 
  .\]
  Note that you can't drop the constant!


- $\int_{\RR_{\geq 0}} f(x) \log(x)$: indented semicircular contours

![](figures/2021-12-14_17-20-48.png)

![](figures/2021-12-22_05-14-24.png)

- When a log trick is useful: if $f(z) = \log(z)g(z)$ where $\int g(z)$ is easy, try a contour that is a rotation of $\RR$.
  The substitution usually yields $\log(\zeta x) \leadsto \ln\abs{x} + i\theta$, so $\int \log(\zeta x)g(\zeta x) = \int \log(x)g(x) + \int i\theta g(x)$ if $g$ is $\zeta\dash$invariant.

:::

:::{.remark title="No clear decay on semicircles: replication"}
The replication trick: if $f(z) = f(\zeta_m z)$ for some $m$, try a sector.
If $f(z) = f(z + ib)$ for some $b$, a rectangle.
:::

:::{.remark title="Integrating over singularities: take principal values"}
For real integrals:
\[
\operatorname{PV} \int_{-\infty}^{\infty} \frac{f(x)}{x-x_{0}} d x=\lim _{\epsilon \backslash 0}\left(\int_{-\infty}^{x_{0}-\epsilon} f(x) d x+\int_{x_{0}+\epsilon}^{\infty} f(x) d x\right) .
.\]
The same principle works for complex contours, e.g. for $\int_\RR p(z)/q(z)$ where $q$ has real roots:

![](figures/2021-12-21_23-40-15.png)

The contours along the real line converge to the principal values of the real integral.

:::

## The ML Estimate

:::{.theorem title="ML Estimate"}
\[
\abs{ \int_\gamma f(z) \dz } \leq ML \da \sup_{\xi \in \gamma} \abs{f(\xi)} \cdot \length(\gamma) 
.\]

:::

:::{.remark}
If $C_R$ is a semicircular contour subtending an angle of $\theta$,
\[
\abs{\int_{C_R} f\, }\leq MR\theta
,\]
so provided $M = \bigo\qty{1\over R^{1+\eps}}$, this goes to zero as $R\to\infty$.
If $M = \bigo(R)$, use Jordan's lemma!
:::

:::{.proof title="?"}
\[
\abs{ \int_\gamma f(z) \dz } 
&\leq \int_\gamma \abs{f(z)} \dz \\
&\leq \int_\gamma \sup_{\xi\in \gamma} \abs{f(\xi)} \dz \\
&\da \int_\gamma M\dz \\
&= M \cdot \length(\gamma)
.\]
:::

## Jordan's Lemma

:::{.theorem title="Jordan's Lemma"}

For $\alpha > 0$,
define
\[
C_R \da \ts{ z=Re^{it} \st t\in [0, \pi] }
.\]

![](figures/2021-12-20_20-35-11.png)
\[
\abs{\int_{C_R} e^{i\alpha z} g(z) \dz} \leq \pi\alpha\inv M_R \qquad M_R \da \sup_{z\in C_R} \abs{g(z)}
.\]
Note that if $M_R\to 0$ as $R\to \infty$, this integral vanishes -- so this works if $M_R \in \bigo\qty{1\over R^\eps}$ for $\eps>0$.

For $\alpha < 0$, the same statement holds with the contour replaced by $\tilde C_R\da \ts{Re{it} \st t\in [0, -\pi]}$.
This is because the main estimate involves
\[
\cdots & \leq \lim _{R \rightarrow \infty} \int_{H_{R}} e^{-\alpha R \sin \theta}|F(z)| R d \theta
,\]
which goes to zero if $-\alpha n\sin(\theta)<0$, i.e. 

- $\alpha>0$ and $\sin(\theta)>0$, so $C_R$ is in the upper half-plane, or
- $\alpha < 0$ and $\sin(\theta)<0$, so $C_R$ is in the lower half-plane.

:::

:::{.remark title="Slightly stronger than the ML estimate"}
Compare to the above computation of $\int_\RR { \cos(x) \over x^2 + 1}$.
Taking $\alpha = 1$, this yields
\[
\abs{ \int_{C_R} { e^{iz} \over z^2 + 1 } \dz } \leq \pi \sup_{z\in C_R} \abs{1\over z^2 +1} \leq {\pi \over R^2 - 1}\to 0
.\]
:::

:::{.remark title="On which semicircle to use"}

![](figures/2021-12-21_21-10-30.png)

:::

:::{.proof title="of Jordan's lemma"}
The quick justification:
\[
\lim _{R \rightarrow \infty}\left|\int_{H_{R}} e^{i m z} F(z) d z\right| &=\lim _{R \rightarrow \infty}\left|\int_{H_{R}} e^{i m R \cos \theta-m R \sin \theta} F(z) R e^{i \theta} d \theta\right| \\
& \leq \lim _{R \rightarrow \infty} \int_{H_{R}} e^{-m R \sin \theta}|F(z)| R d \theta
.\]

\[
\abs{ \int_{C_R} f(z)\dz }
&= \abs{ \int_{C_R} e^{iaz}g(z) \dz} \\
&= \abs{ \int_{[0, \pi]} e^{ia\qty{Re^{it}}}g(Re^{it}) iRe^{it} \dt} \\
&\leq \int_{[0, \pi]} \abs{ e^{ia\qty{Re^{it}}}g(Re^{it}) iRe^{it}} \dt \\
&=R \int_{[0, \pi]} \abs{ e^{ia\qty{Re^{it}}}g(Re^{it})} \dt \\
&\leq R M_R \int_{[0, \pi]} \abs{ e^{ia\qty{Re^{it}}}} \dt \\
&= R M_R \int_{[0, \pi]} e^{\Re\qty{iaRe^{it}}}   \dt \\
&= R M_R \int_{[0, \pi]} e^{\Re\qty{iaR\qty{\cos(t) + i\sin(t) } }}   \dt \\
&= R M_R \int_{[0, \pi]} e^{-aR\sin(t) }   \dt \\
&= 2 R M_R \int_{[0, \pi/2]} e^{-aR\sin(t) }   \dt \\
&\leq 2R M_R \int_{[0, \pi/2]} e^{-aR\qty{2t\over \pi} }   \dt \\
&= 2RM_R \qty{\pi \over 2aR}\qty{1-e^{-aR}} \\
&= {\pi M_R \over a}
.\]

where we've used that on $[0, \pi/2]$, there is an inequality $2t/\pi \leq \sin(t)$.
This is obvious from a picture, since $\sin(t)$ is a height on $S^1$ and $2t/\pi$ is a height on a diagonal line:

![figures/image_2021-06-09-01-29-22.png](../../../assets/figures/image_2021-06-09-01-29-22.png)

:::

## Exercises

[[E-QU5E2]]
[[E-5H54G]]
