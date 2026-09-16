---
title: Morera and converses
order: 40
topics:
- Morera

---

# Morera and converses

By Goursat's theorem, a holomorphic function has vanishing integrals over triangles.
Morera's theorem is the converse for continuous functions, and it shows that locally uniform limits and series of holomorphic functions are holomorphic.

## Morera's theorem

[[T-LHSMY]]

[[FT-B73T5]]

::: {.slogan}
A continuous function whose integral over every triangle vanishes is holomorphic.

:::

::: {.proof}
Holomorphy is local, so let $D\subseteq\Omega$ be an open disc with center $z_0$.
For $z\in D$ define $F(z) \coloneqq \int_{[z_0, z]} f(\xi) \dxi$, the integral along the segment from $z_0$ to $z$.
For $z, z+h\in D$, the triangle with vertices $z_0, z, z+h$ lies in $D$, so the hypothesis gives
$$
\frac{F(z+h) - F(z)}{h} - f(z) = \frac1h\int_{[z, z+h]} \qty{f(\xi) - f(z)} \dxi
.$$
The right side has modulus at most $\sup_{\xi\in[z,z+h]}\abs{f(\xi)-f(z)}$, which tends to $0$ as $h\to 0$ by continuity of $f$.
So $F$ is holomorphic on $D$ with $F' = f$, and $f$ is holomorphic because derivatives of holomorphic functions are holomorphic.

:::

::: {.remark title="Hypotheses"}
The hypotheses are continuity of $f$ and vanishing of its triangle integrals; differentiability of $f$ is not assumed.
The theorem therefore applies to a locally uniform limit of holomorphic functions, whose differentiability is not known in advance.
Some texts state it for rectangles with sides parallel to the axes, and the proof is the same with the segment replaced by a horizontal segment followed by a vertical one.

:::

## Locally uniform limits

[[C-TODSQ]]

::: {.proof}
Let $D$ be an open disc with $\overline D\subseteq\Omega$.
Each $f_n$ is continuous and $f_n\to f$ uniformly on $\overline D$, so $f$ is continuous on $D$.
For a triangle $T\subseteq D$, Goursat's theorem gives $\int_{\bd T} f_n = 0$, and uniform convergence on $\bd T$ gives $\int_{\bd T} f = \lim_n \int_{\bd T} f_n = 0$.
By Morera's theorem $f$ is holomorphic on $D$, hence on $\Omega$.

For the derivatives, let $K\subseteq\Omega$ be compact and choose $r>0$ such that $K_r \coloneqq \ts{z : \operatorname{dist}(z, K)\leq r}\subseteq\Omega$; $K_r$ is compact.
For $z\in K$, Cauchy's estimate on the circle $\abs{\xi - z} = r$ gives $\abs{f_n'(z) - f'(z)} \leq \sup_{K_r}\abs{f_n - f}/r$, which tends to $0$ uniformly in $z\in K$.

:::

::: {.remark}
Applied to partial sums, the corollary shows that a series $\sum_k f_k$ of holomorphic functions converging uniformly on compact subsets of $\Omega$ is holomorphic and can be differentiated term by term.

:::

## Goursat

Goursat's theorem proves Cauchy's theorem for triangles and rectangles with no continuity assumption on $f'$.

[[T-B3BDO]]

::: {.proof title="from Gamelin"}
The argument is written for a rectangle; for a triangle, the midpoints of the sides divide it into four triangles, each with half the perimeter, and the same estimates hold.

![](../../../../assets/assets/figures/2021-12-10_19-47-54.png)

Let $R$ be a closed rectangle contained, with its interior, in $\Omega$, subdivided into four equal subrectangles.
The integral around $\partial R$ is the sum of the integrals around the four, so at least one, call it $R_1$, satisfies
$$
\left|\int_{\partial R_{1}} f(z) \dz \right| \geq \frac{1}{4}\left|\int_{\partial R} f(z) \dz \right|
.$$
Subdividing repeatedly yields nested $\ts{R_n}$ with
$$
\left|\int_{\partial R_{n}} f(z) \dz\right| \geq \frac{1}{4}\left|\int_{\partial R_{n-1}} f(z) \dz \right| \geq \cdots \geq \frac{1}{4^{n}}\left|\int_{\partial R} f(z) \dz\right|
.$$
The $R_n$ decrease with diameters tending to zero, so their intersection is a single point $z_0 \in R$.
Differentiability at $z_0$ gives
$$
\left|\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}-f^{\prime}\left(z_{0}\right)\right| \leq \varepsilon_{n}, \quad z \in R_{n}
,$$
with $\varepsilon_n \to 0$.
Writing $L$ for the length of $\partial R$, the length of $\partial R_n$ is $L/2^n$, and for $z \in R_n$,
$$
\left|f(z)-f\left(z_{0}\right)-f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)\right| \leq \varepsilon_{n}\left|z-z_{0}\right| \leq 2 \varepsilon_{n} L / 2^{n}
.$$
Since $f(z_0)+f'(z_0)(z-z_0)$ has a primitive, its integral over the closed curve $\partial R_n$ vanishes, and the ML estimate gives
$$
\begin{aligned}
\left|\int_{\partial R_{n}} f(z) \dz\right| &=\left|\int_{\partial R_{n}}\left[f(z)-f\left(z_{0}\right)-f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)\right] \dz\right| \\
& \leq\left(2 \varepsilon_{n} L / 2^{n}\right) \cdot\left(L / 2^{n}\right)=2 L^{2} \varepsilon_{n} / 4^{n}
\end{aligned},$$
hence
$$
\left|\int_{\partial R} f(z) \dz\right| \leq 4^{n}\left|\int_{\partial R_{n}} f(z) \dz\right| \leq 2 L^{2} \varepsilon_{n}
.$$
Since $\varepsilon_n \to 0$, the integral over $\partial R$ vanishes.

:::

## Exercises

[[E-WIANB]]
