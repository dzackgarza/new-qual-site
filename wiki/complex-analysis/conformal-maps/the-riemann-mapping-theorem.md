---
title: The Riemann mapping theorem
order: 50
topics:
- Riemann Mapping Theorem
- Simply Connected
- Univalent Functions

---

# The Riemann mapping theorem

::: {.slogan}
If $\Omega \subsetneq \CC$ is simply connected then $\Omega$ is biholomorphic to $\DD$.

:::

[[T-4MDS6]]

::: {.remark title="Both hypotheses are necessary"}
$\Omega\neq\CC$: a holomorphic map $F\colon\CC\to\DD$ is bounded and entire, hence constant by Liouville's theorem, so $\CC$ is not biholomorphic to $\DD$.

$\Omega$ simply connected: a biholomorphism is a homeomorphism, and $\DD$ is simply connected.

:::

::: {.proof title="Sketch"}
The proof maximizes $\abs{f'(z_0)}$ over injective holomorphic maps $f\colon\Omega\to\DD$ with $f(z_0)=0$ and shows that a maximizer is surjective.

- Fix $z_0\in \Omega$ and set $\mathcal F = \ts{f\in \Hol(\Omega, \DD) \st f(z_0) = 0,\ f \text{ injective}}$.

- $\mathcal F$ is nonempty.
  Choose $a\in\CC\sm\Omega$.
  Since $z-a$ does not vanish on the simply connected set $\Omega$, it has a holomorphic square root $g$ on $\Omega$, and $g$ is injective.
  By the open mapping theorem $g(\Omega)$ contains a disc $D_r(g(z_0))$, and $g(\Omega)$ is disjoint from $D_r(-g(z_0))$: if $g(z)\in D_r(-g(z_0))$, then $-g(z) = g(z')$ for some $z'\in\Omega$, so $z = z'$ after squaring and $g(z) = 0$, which contradicts $a\notin\Omega$.
  Then $z\mapsto (r/2)/(g(z)+g(z_0))$ is injective and maps $\Omega$ into $\DD$, and composing with the Blaschke factor that sends its value at $z_0$ to $0$ gives an element of $\mathcal F$.

- For $w\in\DD$, the automorphisms $h_w$ of $\DD$ satisfy
$$
\begin{aligned}
h_w(z) &\coloneqq {z-w \over 1-\bar{w} z} \in \Hol(\DD) \\
h'_w(0) &= 1 - \abs{w}^2 \\
h'_w(w) &= {1\over 1 - \abs{w}^2}
\end{aligned}.$$

- A non-surjective $f\in\mathcal F$ is not a maximizer.
  Let $w\in\DD\sm f(\Omega)$; then $w\neq 0$ and $h_w\circ f$ is injective and nonvanishing on $\Omega$, with value $-w$ at $z_0$.
  Let $s$ be a holomorphic square root of $h_w\circ f$, which is injective, and $F\coloneqq h_{s(z_0)}\circ s\in\mathcal F$.
  Then $\abs{s(z_0)}^2 = \abs w$ and
  $$
  \abs{F'(z_0)} = \frac{\abs{s'(z_0)}}{1-\abs w} = \frac{(1-\abs w^2)\abs{f'(z_0)}}{2\sqrt{\abs w}\,(1-\abs w)} = \frac{1+\abs w}{2\sqrt{\abs w}}\abs{f'(z_0)} > \abs{f'(z_0)}
  .$$

- The family is bounded by $1$, hence normal by Montel's theorem.

- Set $m\coloneqq \sup_{f\in \mathcal F} \abs{f'(z_0)}$.
  Then $m>0$ because injective holomorphic maps have nonvanishing derivative, and $m<\infty$ because, for $\overline{D_R(z_0)}\subseteq\Omega$, the Cauchy estimate gives
$$
\abs{f'(z_0)} \leq \max_{\abs{z-z_0} = R} { \abs{f(z)} \over R} \leq {1\over R}
.$$

- Take $\ts{f_k}\subseteq\mathcal F$ with $\abs{f_k'(z_0)} \to m$, and use Montel to extract a locally uniformly convergent subsequence with limit $h$.

- $h\in\mathcal F$: $h$ is holomorphic with $h(z_0)=0$ and $\abs{h'(z_0)} = m>0$, so it is nonconstant, maps into $\DD$ by the maximum modulus principle, and is injective by Hurwitz's theorem as a locally uniform limit of injective maps.

- $h$ is surjective, since a non-surjective element of $\mathcal F$ is not a maximizer.

![](../../../../assets/assets/figures/2021-12-14_16-34-14.png)

![](../../../../assets/assets/figures/2021-12-14_16-34-24.png)

![](../../../../assets/assets/figures/2021-12-14_16-34-50.png)

![](../../../../assets/assets/figures/2021-12-14_17-34-54.png)

:::

::: {.remark title="Ingredients of the proof"}
[[complex-analysis/conformal-maps/normal-families-and-montel|Montel's theorem]] gives a convergent maximizing subsequence, [[complex-analysis/counting-zeros/hurwitz|Hurwitz's theorem]] gives injectivity of the limit, [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|the Cauchy estimate]] gives $m<\infty$, and square roots on simply connected sets together with [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors]] give nonemptiness of $\mathcal F$ and the derivative increase.

:::

[[C-BKYF7]]

[[C-FVT4V]]

::: {.proof}
\envlist

- $f'\neq 0$ on $U$: if $f'(z_0)=0$, then $f - f(z_0)$ has a zero of order $k\geq 2$ at $z_0$, and $f'$ has no other zeros near $z_0$.
  For a small circle $C$ about $z_0$ and $w$ with $0<\abs w<\min_C\abs{f-f(z_0)}$, Rouché's theorem shows that $f - f(z_0) - w$ has $k$ zeros inside $C$, all simple since $f'\neq 0$ away from $z_0$, contradicting injectivity.
- By the open mapping theorem $f(U)$ is open and $f$ maps open sets to open sets, so $g \coloneqq f\inv\colon f(U)\to U$ is continuous.
- For $w, w_0\in f(U)$ with $w\neq w_0$, write $z = g(w)$ and $z_0 = g(w_0)$, so $z\neq z_0$, and $z\to z_0$ as $w\to w_0$ by continuity of $g$:
$$
\frac{g(w)-g\left(w_{0}\right)}{w-w_{0}}=\frac{1}{\frac{w-w_{0}}{g(w)-g\left(w_{0}\right)}}=\frac{1}{\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}}
\convergesto{z\to z_0}
{1\over f'(z_0) } =
{1\over f'(g(w_0))}
.$$

:::

## Exercises

[[P-Z776N]]
