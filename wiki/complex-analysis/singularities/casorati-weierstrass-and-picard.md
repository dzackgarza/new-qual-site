---
title: Casorati-Weierstrass and Picard
order: 40
topics:
- Casorati-Weierstrass
- Picard

---

# Casorati-Weierstrass and Picard

Near an essential singularity, a holomorphic function takes values dense in $\CC$ (Casorati--Weierstrass), and all values of $\CC$ with at most one exception (Picard's great theorem).

## Casorati--Weierstrass

[[T-C5VEI]]

::: {.slogan}
The image of a punctured disc at an essential singularity is dense in $\CC$.

:::

## Picard

Picard's theorems replace density of the image by omission of at most one value of $\CC$.

[[T-DDOWW]]

[[T-HWBWI]]

::: {.proof title="Little Picard theorem, by uniformization"}
Let $f$ be entire and omit two values $a\neq b$.
Replacing $f$ by $(f-a)/(b-a)$, $f$ is a holomorphic map $\CC\to X\coloneqq \CC\sm\theset{0,1}$.
The universal covering space of $X$ is biholomorphic to $\HH$, and since $\CC$ is simply connected, $f$ lifts to a holomorphic map $\tilde f\colon\CC\to\HH$.
Composing with the Cayley map gives a bounded entire function, which is constant by Liouville's theorem, so $\tilde f$ and $f$ are constant.

:::

## Exercises

[[E-HEJJK]] [[E-3ZHRE]] [[E-27X7K]] [[E-XZWER]] [[E-3LIG3]]
