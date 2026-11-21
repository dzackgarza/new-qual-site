---
schema: qual/card@1
id: P-CASP07A
kind: problem
title: "True or False: metric space convergence, Möbius transformations, Liouville, removable singularities, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Determine if the statements below are True or False.

(a) Let $(X, d)$ be a metric space, $x \in X$, and $\{x_n\}_{n=1}^{\infty}$ a sequence in $X$.
If every subsequence of $\{x_n\}_{n=1}^{\infty}$ has a subsequence that converges to $x$, then $\{x_n\}_{n=1}^{\infty}$ converges to $x$.

(b) Let $a \neq b$ be positive real numbers.
There exists a Möbius (linear fractional) transformation sending the circular sector $G_1 := \{x + iy : x^2 + y^2 < 1, \, x > 0, \, y > 0\}$ to the ellipsoidal sector $G_2 := \{x + iy : x^2/a^2 + y^2/b^2 < 1, \, x > 0, \, y > 0\}$.

(c) Let $D$ be a discrete subset of $\CC$.
Every bounded analytic function in $\CC \setminus D$ is constant.

(d) Suppose that $f(z)$ is analytic in $G := \DD \setminus \{0\}$ and that $\int_\gamma z^p f(z)\,dz = 0$ for every closed curve $\gamma: [0,1] \to G$ and every nonnegative integer $p$.
Then $f(z)$ has a removable singularity at 0.

(e) Let $a$ be a complex number with $\abs{a} > 1$.
There exists $\epsilon > 0$ such that if a polynomial $p(z)$ satisfies $\abs{p(z)} < \epsilon$ on the closed unit disk $\overline{\DD}$, then $\abs{p(a)} < 1$.
:::

::: {.solution}

The five verdicts are the card's own. The proof of (c) has been repaired: the original argument filled in the points of $D$ and then called the result entire, which is only true when $D$ has no accumulation point, and the step that states the convention under which that holds — together with what happens without it — is now on the card.

::: pf

::: {.pf-step #a}
(a) True: if every subsequence of $(x_{n})$ has a subsequence converging to $x$, then $x_{n}\to x$.

::: pf-proof
Suppose $x_{n}$ does not converge to $x$. Then there is $\varepsilon>0$ such that for every $N$ some $n\ge N$ has $d(x_{n},x)\ge\varepsilon$; choosing such an $n_{k}$ recursively with $n_{k}>n_{k-1}$ gives a subsequence with $d(x_{n_{k}},x)\ge\varepsilon$ for all $k$. Every subsequence of that subsequence also has all its terms at distance at least $\varepsilon$ from $x$, so none of them converges to $x$, contradicting the hypothesis.
:::

:::

::: {.pf-step #b}
(b) False: no Möbius transformation carries the quarter disc $G_{1}$ onto the quarter ellipse $G_{2}$ when $a\ne b$.

::: pf-proof
The boundary of $G_{1}$ contains the arc of the unit circle between $1$ and $i$, and the boundary of $G_{2}$ contains the arc of the ellipse $x^{2}/a^{2}+y^{2}/b^{2}=1$ between $a$ and $ib$. A Möbius transformation carries generalized circles to generalized circles, so it would carry the unit circle onto a generalized circle containing the image of that arc, and the image of the arc would therefore lie on a circle or a line. Since a Möbius map is a homeomorphism of the Riemann sphere carrying $\partial G_{1}$ onto $\partial G_{2}$, the elliptical arc would have to lie on a generalized circle; but an ellipse with $a\ne b$ is neither a circle nor a line, and an arc of it determines the ellipse, so this is impossible.
:::

:::

::: {.pf-step #c}
(c) True, for $D$ discrete in the sense that it has no accumulation point in $\CC$: then every bounded analytic function on $\CC\setminus D$ is constant.

::: pf-proof
Write $D$ as a closed discrete set, so each point $d\in D$ has a neighbourhood meeting $D$ only in $d$; thus $d$ is an isolated singularity of $f$, and $f$ is bounded near it, so the singularity is removable (Riemann's removable singularity theorem). Filling in all the points of $D$ gives a function $F$ holomorphic on $\CC$: away from $D$ it agrees with $f$, and at each point of $D$ the removable singularity has been filled. Since $\abs f\le M$ on the domain and the filled values are limits of values of $f$, $\abs F\le M$ on $\CC$. A bounded entire function is constant (Liouville's theorem), so $f$ is constant.
:::

:::

::: {.pf-step #c-caveat}
(c) If $D$ is required only to have isolated points and is allowed an accumulation point, the conclusion stays true but the argument above does not reach it, and this step records why.

::: pf-proof
Take $D=\{1/n:n\ge1\}$, whose points are isolated and which accumulates at $0\notin D$. Filling in the points of $D$ gives a function holomorphic on $\CC\setminus\{0\}$, not on $\CC$, so Liouville's theorem does not apply directly and $0$ is not an isolated singularity of $f$: every punctured neighbourhood of $0$ meets $D$. The conclusion nevertheless holds, by the removable-singularity theorem for closed sets of zero analytic capacity — the closure of a discrete set is countable, hence of capacity zero (Painlevé's theorem) — applied to the bounded function on $\CC\setminus\overline{D}$, which is constant there, together with the identity theorem on the connected domain $\CC\setminus D$. So the verdict "True" does not depend on the reading of "discrete", but the elementary proof above does.
:::

:::

::: {.pf-step #d}
(d) True: the vanishing of $\int_{\gamma}z^{p}f(z)\,dz$ for all closed $\gamma$ and all $p\ge0$ forces every negative Laurent coefficient of $f$ at $0$ to vanish.

::: pf-proof
$f$ has a Laurent expansion $f(z)=\sum_{k\in\ZZ}a_{k}z^{k}$ on $0<\abs z<1$. For $p\ge0$ the function $z^{p}f(z)=\sum_{k}a_{k}z^{k+p}$ is holomorphic on $G=\DD\setminus\{0\}$, and its residue at $0$ is the coefficient of $z^{-1}$, namely $a_{-p-1}$. Taking $\gamma$ to be the positively oriented circle $\abs z=r$, $0<r<1$ — a closed curve in $G$ — the hypothesis gives
$$
0=\int_{\gamma}z^{p}f(z)\,dz=2\pi i\,a_{-p-1},
$$
so $a_{-p-1}=0$ for every $p\ge0$, that is $a_{k}=0$ for every $k\le-1$. Hence the Laurent series has no negative powers and $f$ extends holomorphically across $0$, which is the assertion.
:::

:::

::: {.pf-step #e}
(e) False: for every $\varepsilon>0$ there is a polynomial below $\varepsilon$ on the closed disc and larger than $1$ at $a$.

::: pf-proof
Let $\varepsilon>0$ and $N\ge1$, and put $p_{N}(z)=\frac{\varepsilon}{2}z^{N}$. On $\overline{\DD}$ one has $\abs{p_{N}(z)}\le\frac{\varepsilon}{2}<\varepsilon$, while $\abs{p_{N}(a)}=\frac{\varepsilon}{2}\abs{a}^{N}$, which exceeds $1$ as soon as $\abs{a}^{N}>2/\varepsilon$, that is for all sufficiently large $N$ because $\abs a>1$. So no $\varepsilon$ has the stated property.
:::

:::

:::
:::
