---
schema: qual/card@1
id: P-BJP24
kind: problem
title: Cauchy's formula for an exterior region
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
solved: true
---

::: problem
(Cauchy's formula for "exterior" region) Let $\gamma$ be piecewise
smooth simple closed curve with interior $\Omega_1$ and exterior
$\Omega_2$. Assume $f'(z)$ exists in an open set containing $\gamma$
and $\Omega_2$ and $\lim_{z \rightarrow \infty } f(z) = A$. Show
that
$$\frac{1}{2 \pi i} \int_\gamma \frac{f(\xi)}{\xi - z} \, d \xi =
\begin{cases}
A,          &     \text{if\ $z \in \Omega_1$}, \\
-f (z) + A, &  \text{if\ $z \in \Omega_2$}
\end{cases}$$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $\gamma$ be a piecewise smooth simple closed curve with interior $\Omega_1$ and exterior $\Omega_2$; assume $f'$ exists on an open set containing $\gamma \cup \Omega_2$ and $\lim_{z\to\infty} f(z) = A$. Show $\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = A$ for $z \in \Omega_1$ and $= -f(z) + A$ for $z \in \Omega_2$.

<1>1. Fix $z$ and $R$ large enough that $\gamma \subseteq \overline{D_R(0)}$ and $\abs{z} < R$; let $\Gamma_R = \theset{\abs{\xi} = R}$ oriented counterclockwise, and consider the region $\Omega_2 \cap D_R(0)$ whose positively oriented boundary is $\Gamma_R$ together with $\gamma$ traversed clockwise.
    Proof: The region between $\gamma$ and the large circle is $\Omega_2 \cap D_R(0)$; its boundary is $\Gamma_R$ plus $\gamma$ with the opposite of its (counterclockwise) orientation, since $\Omega_2$ lies outside $\gamma$.

<1>2. $\int_{\Gamma_R} \frac{f(\xi)}{\xi - z}\, d\xi \to 2\pi i A$ as $R \to \infty$, uniformly in $z$ with $\abs{z}$ bounded.
    Proof: Write $f = A + (f - A)$. Then $\int_{\Gamma_R} \frac{A}{\xi - z}\, d\xi = 2\pi i A$ for $R > \abs{z}$ by the Cauchy integral formula applied to the constant $A$. For the remainder, $\abs{\int_{\Gamma_R} \frac{f(\xi) - A}{\xi - z}\, d\xi} \leq 2\pi R \cdot \frac{\sup_{\abs{\xi} = R}\abs{f(\xi) - A}}{R - \abs{z}} \to 0$, since $f(\xi) \to A$ as $\xi \to \infty$.

<1>3. If $z \in \Omega_2$, then $\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = -f(z) + A$.
    Proof: On the region of <1>1, the function $\xi \mapsto \frac{f(\xi)}{\xi - z}$ is holomorphic except for the simple pole at $\xi = z$ with residue $f(z)$. By the residue theorem, $\int_{\Gamma_R} \frac{f(\xi)}{\xi - z}\, d\xi - \int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = 2\pi i f(z)$ (the boundary of the region, with $\gamma$ clockwise, contributes $\int_{\Gamma_R} - \int_\gamma$). Rearranging and taking $R \to \infty$ with <1>2 gives $\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = A - f(z)$.

<1>4. If $z \in \Omega_1$, then $\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = A$.
    Proof: For $z \in \Omega_1$ the function $\xi \mapsto \frac{f(\xi)}{\xi - z}$ is holomorphic on the whole region of <1>1 (its only possible pole, at $\xi = z$, is outside), so by the Cauchy integral theorem $\int_{\Gamma_R} \frac{f(\xi)}{\xi - z}\, d\xi - \int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = 0$. Taking $R \to \infty$ and using <1>2 yields $\frac{1}{2\pi i}\int_\gamma \frac{f(\xi)}{\xi - z}\, d\xi = A$.

<1>5. Q.E.D.
    Proof: <1>3 proves the claim for $z \in \Omega_2$ and <1>4 for $z \in \Omega_1$, which is the full statement.

:::
