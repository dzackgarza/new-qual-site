---
title: Casorati-Weierstrass and Picard
order: 40
topics:
- Casorati-Weierstrass
- Picard

---

# Casorati-Weierstrass and Picard

Near an essential singularity, a holomorphic function takes values dense in $\CC$ (Casorati–Weierstrass), and all values of $\CC$ with at most one exception (Picard's great theorem).

## Casorati–Weierstrass

[[T-C5VEI]]

[[FT-2N57U]]

::: {.slogan}
The image of a punctured disc at an essential singularity is dense in $\CC$.

:::

::: {.proof title="Casorati–Weierstrass theorem"}
Let $f$ have an essential singularity at $z_0$, and suppose toward a contradiction that there is a punctured neighborhood $\Omega$ of $z_0$, a point $w\in\CC$, and $\varepsilon>0$ with $f(\Omega) \intersect \DD_\varepsilon(w)$ empty, so that $\abs{f(z) - w} \geq \varepsilon$ on $\Omega$.

Define
$$
g(z) \coloneqq {1\over f(z) - w}
,$$
which is holomorphic on $\Omega$ and bounded there by $\varepsilon\inv$, and not identically zero.
By Riemann's removable singularity theorem $g$ extends holomorphically across $z_0$.

Now $f(z) = {1\over g(z)} + w$.
If $g(z_0) = 0$ then $z_0$ is a zero of finite order for $g$, hence a pole of finite order for $f$, contradicting that $z_0$ is essential.
If $g(z_0) \neq 0$ then $1/g + w$ is holomorphic near $z_0$ and equals $f$ off $z_0$, so $z_0$ is removable, again a contradiction.

:::

::: {.proof title="Casorati–Weierstrass theorem, from Gamelin"}

![](../../../../assets/assets/figures/2021-12-10_18-47-34.png)

:::

## Picard

Picard's theorems replace density of the image by omission of at most one value of $\CC$.

[[T-DDOWW]]

[[T-HWBWI]]

::: {.proof title="Little Picard theorem, by uniformization"}
Let $f$ be entire and omit two values $a\neq b$.
Replacing $f$ by $(f-a)/(b-a)$, $f$ is a holomorphic map $\CC\to X\coloneqq \CC\sm\ts{0,1}$.
The universal covering space of $X$ is biholomorphic to $\HH$, and since $\CC$ is simply connected, $f$ lifts to a holomorphic map $\tilde f\colon\CC\to\HH$.
Composing with the Cayley map gives a bounded entire function, which is constant by Liouville's theorem, so $\tilde f$ and $f$ are constant.

:::

## Exercises

[[E-HEJJK]]
[[E-3ZHRE]]
[[E-27X7K]]
[[E-XZWER]]
[[E-3LIG3]]
