---
order: 20
sort: 020
title: Residues
---

# Residues

:::{.warnings}
A pedantic warning: $\Res_{z=p}(f)$ should really be $\Res_{z=p}(df)$ for $df = f(z) \dz$, since it's only an invariant of the 1-form $df$ and not necessarily $f$ itself.
We freely abuse notation!

:::
:::{.remark}
What to use when:

- $f(z) = p(z)/q(z)$: if $f\in L^1(\RR)$, integrate over semicircle in Q1 or a pie slice $[0, R] \union S_1(R) \union \zeta[0, R]$.
  E.g. $\int_{\RR_{\geq 0} } {1\over 1 + x^n}\dx = {(\pi / n) \over \sin\qty{\pi \over n}}$
- $f(z) = R(\cos\theta, \sin\theta)$ a rational function of sines/cosines: set $z= e^{i\theta}$ and integrate over $S^1$.
  E.g.
  \[
  \int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos \theta}=\int_{S^{1}} \frac{i d z}{(z-a)(a z-1)}=2 \pi i\left(i /\left(a^{2}-1\right)\right)=\frac{2 \pi}{1-a^{2}}
  .\]

- $f(z) = z^a g(z)$ with $g$ rational: semicircle $[0,R] \union S_1(R) \union i[0, R]$ to get $(1-i^a)\int f$
  E.g. setting $w \da e^{\pi i a \over 2}$,
  \[
  \int_{0}^{\infty} \frac{x^{a}}{1+x^{2}} d x =
  \frac{\pi\left(i^{a}-(-i)^{a}\right)}{\left(1-1^{a}\right)}=\pi \frac{\omega-\omega^{3}}{1-\omega^{4}}=\frac{\pi}{\omega+\omega^{-1}}=\frac{\pi}{2 \cos (\pi a / 2)}
  ,\]
  where for $a = 1/3$ this yields $\pi/\sqrt 3$.

:::
## Basics

:::{.remark}
Check: do you need residues at all??
You may be able to just compute an integral!

- Directly by parameterization:
\[
\int_\gamma f \dz = \int_a^b f(z(t))\, z'(t) \dt && \text{for } z(t) \text{ a parameterization of } \gamma
,\]

- Finding a primitive $F$, then
\[
\int_\gamma f = F(b) - F(a)
.\]

  - Note: you can parameterize a circle around $z_0$ using
  \[
  z= z_0 + re^{i \theta }
  .\]

:::
:::{.fact title="Integrating $z^k$ around $S^1$ powers residues"}
The major fact that reduces integrals to residues:
\[
\int_\gamma z^k \dz = \int_0^{2\pi} e^{ik\theta} ie^{i\theta } \dtheta = i\int_0^{2\pi} e^{i(k+1)\theta \dtheta }
=
\begin{cases}
-2\pi i & k=-1
\\
0 & \text{else}.
\end{cases}
\]
Thus
\[
\int \sum_{k\geq -M} c_k z^k = \sum_{k\geq -M} \int c_k z^k = 2\pi i c_{-1}
,\]
i.e. the integral picks out the $c_{-1}$ coefficient in a Laurent series expansion.

:::
:::{.example}
Consider
\[
f(z) \da {e^{iz} \over 1 + z^2}
\]
where $z\neq \pm i$, and attempt to integrate
\[
\int_\RR f(z) \dz
.\]
Use a semicircular contour $\gamma_R$ where $z = Re^{it}$
and check
\[
\sup_{z\in \gamma_R} \abs{f(z)}
&= \max_{t\in [0, \pi} {1 \over 1 + (Re^{it})^2 } \\
&= \max_{t\in [0, \pi} {1 \over 1 + R^2e^{2it} } \\
&= {1\over R^2 - 1}
.\]

:::
## Estimates
[[PR-ZCMJQ]]

:::{.proof}
\[
\left|\int_{\gamma} f(z) d z\right| \leq \sup _{t \in[a, b]}|f(z(t))| \int_{a}^{b}\left|z^{\prime}(t)\right| d t \leq \sup _{z \in \gamma}|f(z)| \cdot \operatorname{length}(\gamma)
.\]

:::
[[PR-QZEJM]]

:::{.proof}
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

![image_2021-06-09-01-29-22](../../../../assets/assets/figures/image_2021-06-09-01-29-22.png)

:::

:::{.remark}
On strategy: see [chapter 5 of these Cambridge DAMTP methods notes](https://www.damtp.cam.ac.uk/user/reh10/lectures/nst-mmii-chapter5.pdf).

A quick shortcut (?) for the quotient rule:
\[
\dd{}{z} {p(z) \over q(z)} = {p'(z)\over q(z)} - {p(z)q'(z) \over q^2(z)}
.\]
Useful when taking $z\to z_0$ with $z_0$ a root of $p, p', q'$.

:::

:::{.remark}
Pedantic warning: $\Res_{z=p}(f)$ should really be $\Res_{z=p}(df)$ for $df = f(z) \dz$, since it's only an invariant of the 1-form $df$ and not necessarily $f$ itself.
We freely abuse notation!

:::

:::{.remark}
Check: do you need residues at all??
You may be able to just compute an integral!

- If the integrand is holomorphic throughout the region enclosed by $\gamma$, $\int_\gamma f = 0$
- If $f$ has a well-defined primitive $F$ on $\gamma$, then 
\[
\int_\gamma f = \int_\gamma F' = F(\gamma(1)) - F(\gamma(0)) = 0
.\]
- Use Cauchy's theorem when applicable:
\[
\int_\gamma {f(z) \over (z-a)^n} = 2\pi i f^{(n-1)}(a)
.\]

- Compute directly by parameterization:
\[
\int_\gamma f \dz = \int_a^b f(z(t))\, z'(t) \dt && \text{for } z(t) \text{ a parameterization of } \gamma
,\]

  - Note: you can parameterize a circle around $z_0$ using
  \[
  z= z_0 + re^{i \theta }
  .\]

:::

## Residue Formulas

[[T-HRPNO]]
[[PR-2XFT4]]
[[PR-L4Y5F]]
![](../../../../assets/assets/figures/2021-10-29_01-33-46.png)
[[C-Q6BSL]]

:::{.proof}
Apply L'Hopital:
\[
(z-z_0) {g(z) \over h(z)} = {(z-z_0) g(z) \over h(z) } \equalsbecause{LH}
{g(z) + (z-z_0) g'(z) \over h'(z)} \converges{z\to z_0}\too {g(z_0) \over h'(z_0)}
.\]

:::
:::{.example title="Residue of a simple pole (order 1)"}
Let $f(z) = \frac{1}{1+z^2}$, then $g(z) = 1, h(z) = 1+z^2$, and $h'(z) = 2z$ so that $h'(i) = 2i \neq 0$. Thus
\[
\Res_{z=i}{1\over 1+z^2} = \frac{1}{2i}
.\]

:::
[[PR-D3CDJ]]

[[FF-VOO4Q]]

### Exercises
> Some good computations [here](https://math.mit.edu/~jorloff/18.04/notes/topic9.pdf).
[[E-V2VS5]]
[[E-SNRS5]]
[[E-ENWYG]]
[[E-PMURO]]
![image_2021-05-17-13-33-55](../../../../assets/assets/figures/image_2021-05-17-13-33-55.png)

[[T-VE5MW]]

[[T-ESKLY]]

[[C-ZTEH7]]

:::{.warnings}
Note that only the denominator gets differentiated, not the numerator!
To remember this, just rederive the equation from L'Hopital's rule and use the product rule on $(z-z_0)g(z)$.

:::

:::{.proof title="Of derivative formula for simple poles"}
Apply L'Hopital:
\[
(z-z_0) {g(z) \over h(z)} = {(z-z_0) g(z) \over h(z) } \equalsbecause{LH}
{g(z) + (z-z_0) g'(z) \over h'(z)} \converges{z\to z_0}\too {g(z_0) \over h'(z_0)}
.\]

:::

[[T-WFXQP]]

[[T-SSNLT]]

:::{.proof}

![](../../../../assets/assets/figures/2021-12-22_05-13-27.png)

:::

## Exercises

### Avoiding Residue Formulas

[[E-S6663]]
[[E-M5MWL]]
[[E-RGDJ7]]
[[E-M7K4C]]
[[E-AOQLK]]
[[E-TOZQJ]]
[[E-FCYUM]]

### Applying the formulas

[[E-YNZYA]]
[[E-ITVTT]]
[[E-U2A4C]]
