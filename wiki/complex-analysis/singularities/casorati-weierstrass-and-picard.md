---
title: Casorati-Weierstrass and Picard
order: 40
topics:
- Casorati-Weierstrass
- Picard

---

# Casorati-Weierstrass and Picard
How much of the plane a function must cover near an essential singularity.
The two theorems say the same kind of thing at different strengths, and the exam usually wants the weaker one.

## Casorati–Weierstrass

[[T-C5VEI]]

[[FT-2N57U]]

:::{.slogan}
The image of a punctured disc at an essential singularity is dense in $\CC$.

:::

:::{.proof title="of Casorati-Weierstrass"}
Let $f$ have an essential singularity at $z_0$, and suppose toward a contradiction that there is a punctured neighborhood $\Omega$ of $z_0$ and an $\eps>0$ with $f(\Omega) \intersect \DD_\eps(w)$ empty for some $w\in\CC$, so that $\abs{f(z) - w} > \eps$ on $\Omega$.
Write $\tilde \Omega \da \Omega \union \ts{z_0}$.

Define
\[
g(z) \da {1\over f(z) - w}
,\]
which is holomorphic on $\Omega$ and bounded there by $\eps\inv$.
By Riemann's removable singularity theorem $g$ extends holomorphically across $z_0$.

Now $f(z) = {1\over g(z)} + w$.
If $g(z_0) = 0$ then $z_0$ is a zero of finite order for $g$, hence a pole of finite order for $f$, contradicting that $z_0$ is essential.
If $g(z_0) = w_0 \neq 0$ then $\abs{f(z_0)} \leq \eps + \abs{w} < \infty$, making $z_0$ removable, again a contradiction.

:::

:::{.proof title="of Casorati-Weierstrass, Gamelin"}

![](../../../../assets/assets/figures/2021-12-10_18-47-34.png)

:::

:::{.remark title="The shape of the argument"}
Both proofs are the same move: assume the image misses a disc, invert to make a bounded function, and let Riemann's theorem contradict essentiality.
Missing a disc is what makes $1/(f-w)$ bounded, so the hypothesis being contradicted is precisely the one that supplies the bound.

:::

## Picard

Picard strengthens dense to onto, at the cost of two points.

[[T-DDOWW]]

[[T-HWBWI]]

:::{.proof title="Liouville and uniformization"}
Assume the three omitted points are $0, 1, \infty$ and let $f: \CC\to X\da \CP^1\sm\ts{0,1,\infty}$ be holomorphic.
The universal cover of $X$ is $\HH$, so $f$ lifts to a holomorphic map into $\HH$, which the Cayley map turns into a holomorphic $f: \CC\to \DD$.
That is a bounded entire function, hence constant by Liouville.

:::

:::{.remark title="Which one a problem wants"}
Casorati–Weierstrass is elementary and self-contained, and it is what a qual problem expects unless it says otherwise.
Picard is the sharper statement and its proof is not elementary, so quoting it is fine but proving it is not what is being asked.
If a problem can be closed by density, close it by density.

:::

## Exercises

[[E-HEJJK]]
[[E-3ZHRE]]
[[E-27X7K]]
[[E-XZWER]]
[[E-3LIG3]]
