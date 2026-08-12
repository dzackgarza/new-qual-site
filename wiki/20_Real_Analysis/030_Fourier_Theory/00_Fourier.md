---
order: 40
---

# Fourier Transform and Convolution

> Some nice reading: <https://people.math.gatech.edu/~heil/7338/fall09/approxid.pdf>

## The Fourier Transform

[[PR-47TTS]]

[[PR-IGMH4]]

:::{.remark}
Note that this implies there can be no identity for convolution: if there existed a function $\delta$ with $\delta(x) = 0$ for $x\neq 0$ and $\int\delta = 1$, then
\[
\widehat{\delta}(\xi)=\int \delta(x) e^{-2 \pi i \xi x} d x=\int \delta(x) d x=1
,\]
contradicting Riemann-Lebesgue.
:::

:::{.proof title="?"}
\envlist

- Boundedness:
\[
\abs{\hat f(\xi)} 
\leq \int \abs{f}\cdot \abs{e^{2\pi i x\cdot \xi }} 
= \pnorm{f}{1}
.\]

- Continuity:
- $\abs{\hat{f}(\xi_{n}) - \hat{f} (\xi) }$
- Apply DCT to show $a\converges{n\to\infty}\to 0$.

:::
   
[[T-DTXIA]]

:::{.warnings}
Fubini-Tonelli does not work here!
:::
    
:::{.proof title="?"}
Idea: Fubini-Tonelli doesn't work directly, so introduce a convergence factor, take limits, and use uniqueness of limits.

- Take the modified integral:

\[
I_{t}(x)
&= \int \hat f(\xi) ~e^{2\pi i x \cdot \xi} ~e^{-\pi t^2 \abs{\xi}^2} \\
&= \int \hat f(\xi) \phi(\xi) \\
&= \int f(\xi) \hat \phi(\xi) \\
&= \int f(\xi) \widehat{\hat g}(\xi - x) \\
&= \int f(\xi) g_{t}(x - \xi)  ~d\xi \\
&= \int f(y-x) g_{t}(y) ~dy  \quad (\xi = y-x)\\
&= (f \ast g_{t}) \\
&\to f \text{ in $L^1$ as }t \to 0
.\]

- We also have
\[
\lim_{t\to 0} I_{t}(x)
&= 
\lim_{t\to 0} \int \hat f(\xi) ~e^{2\pi i x \cdot \xi} ~e^{-\pi t^2 \abs{\xi}^2} \\
&= 
\lim_{t\to 0} \int \hat f(\xi) \phi(\xi) \\
&=_{DCT} 
\int \hat f(\xi) \lim_{t\to 0} \phi(\xi) \\
&=
\int \hat f(\xi) ~e^{2\pi i x \cdot \xi} \\
.\]

- So 
\[
I_{t}(x) \to \int \hat f(\xi) ~e^{2\pi i x \cdot \xi} ~\text{ pointwise and }~\pnorm{I_{t}(x) - f(x)}{1} \to 0
.\]

- So there is a subsequence $I_{t_{n}}$ such that $I_{t_{n}}(x) \to f(x)$ almost everywhere
- Thus $f(x) = \int \hat f(\xi) ~e^{2\pi i x \cdot \xi}$ almost everywhere by uniqueness of limits. 

:::

[[PR-DPRY7]]

[[PR-DY2B3]]

:::{.example title="Some transform pairs"}
\[
\text{Dirichlet:}
&& \chi_{\theset{-\frac{1}{2} \leq x \leq \frac{1}{2}}}
&\iff \mathrm{sinc}(\xi) \\
\text{Fejer:}
&& \chi_{\theset{-1 \leq x \leq 1}} (1 - \abs{x})
&\iff \mathrm{sinc}^2(\xi) \\
\text{Poisson:}
&& \frac{1}{\pi} \frac{1}{1+x^2}
&\iff e^{2\pi \abs{\xi}} \\
\text{Gauss-Weierstrass:}
&& e^{-\pi x^2}
&\iff e^{-\pi \xi^2}
.\]
:::

## Approximate Identities 

:::{.example title="of an approximation to the identity."}
\[
\phi(x) \da e^{-\pi x^2}
.\]

:::

[[T-HHFGB]]

:::{.proof title="?"}
\[
\norm{f - f\ast \phi_{t}}_1 
&= \int f(x) - \int f(x-y)\phi_{t}(y) ~dy dx \\
&= \int f(x)\int \phi_{t}(y) ~dy - \int f(x-y)\phi_{t}(y) ~dy dx \\
&= \int \int \phi_{t}(y)[f(x) - f(x-y)] ~dy dx \\
&=_{FT} \int \int \phi_{t}(y)[f(x) - f(x-y)] ~dx dy \\
&= \int \phi_{t}(y) \int f(x) - f(x-y) ~dx dy \\
&= \int \phi_{t}(y) \norm{f - \tau_{y} f}_1 dy \\
&= \int_{y < \delta} \phi_{t}(y) \norm{f - \tau_{y} f}_1 dy  +
\int_{y \geq \delta} \phi_{t}(y) \norm{f - \tau_{y} f}_1 dy \\
&\leq \int_{y < \delta} \phi_{t}(y) \varepsilon +
\int_{y \geq \delta} \phi_{t}(y) \left( \norm{f}_1 + \norm{\tau_{y} f}_1 \right) dy \quad\text{by continuity in } L^1 \\
&\leq \varepsilon + 
2\norm{f}_1 \int_{y \geq \delta} \phi_{t}(y) dy \\
&\leq \varepsilon + 2\norm{f}_1 \cdot \varepsilon \quad\text{since $\phi_{t}$ has small tails} \\
&\converges{\eps\to 0}\to 0 
.\]

:::

[[T-3UXK7]]

:::{.proof title="?"}

- Choose $M \geq f,g$.

- By small tails, choose $N$ such that $\int_{B_{N}^c} \abs{f}, \int_{B_{n}^c} \abs{g} < \varepsilon$

- Note 
\[
\abs{f \ast g} \leq \displaystyle\int \abs{f(x-y)} ~\abs{g(y)} ~dy \da I
.\]

- Use $\abs{x} \leq \abs{x-y} + \abs{y}$, take $\abs{x}\geq 2N$ so either
\[
\abs{x-y} \geq N \implies I \leq \int_{\theset{x-y \geq N}} \abs{f(x-y)}M ~dy\leq \varepsilon M \to 0
\]
  then
\[
\abs{y} \geq N \implies I \leq \int_{\theset{y \geq N}} M\abs{g(y)} ~dy\leq  M \varepsilon \to 0
.\]

:::

[[PR-PRSKG]]

[[PR-A7UFG]]
