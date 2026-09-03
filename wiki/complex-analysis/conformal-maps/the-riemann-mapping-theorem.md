---
title: The Riemann mapping theorem
order: 50
topics:
- Riemann Mapping Theorem
- Simply Connected
- Univalent Functions

---

# The Riemann mapping theorem

:::{.slogan}
If $\Omega \subsetneq \CC$ is simply connected then $\Omega$ is biholomorphic to $\DD$.

:::

[[T-4MDS6]]

:::{.remark title="Both hypotheses are necessary"}
Not all of $\CC$: a map $F:\CC\to\Omega$ with $\Omega$ bounded is constant by Liouville, so $\CC$ itself is not biholomorphic to the disc.

Simply connected: since $\pi_1\DD = 1$, a biholomorphism would make every closed curve in $\Omega$ nullhomotopic, by composing a homotopy in $\DD$ with the inverse.

:::

:::{.proof title="Sketch"}
The shape of the argument is: take the family of injective maps into the disc, maximize the derivative at a point, and show the maximizer is onto.

- Fix $z_0\in \Omega$ and set $\mcf = \ts{f\in \Hol(\Omega, \DD) \st f(z_0) = 0,\ f \text{ injective}}$.
  A lemma shows $\mcf$ is nonempty.

- Define the hyperbolic translations and compute
\[
h_w(z) &\da {z-w \over 1-\bar{w} z} \in \Hol(\DD) \\
h'_w(0) &= 1 - \abs{w}^2 \\
h'_w(w) &= {1\over 1 - \abs{w}^2}
.\]

- Show that a non-surjective $f\in\mcf$ admits another member with a larger derivative at $z_0$.
  This is the step that makes the maximizer onto.

- The family is uniformly bounded, hence normal by Montel.

- Set $m\da \sup_{f\in \mcf} \abs{f'(z_0)}$, which satisfies $0<m<\infty$: the Cauchy estimate gives
\[
\abs{f'(z_0)} \leq \max_{\abs{z-z_0} = R} { \abs{f(z)} \over R} \leq {1\over R}
.\]

- Take $\ts{f_k}\subseteq\mcf$ with $\abs{f_k'(z_0)} \to m$, and use Montel to extract a locally uniformly convergent subsequence with limit $h$.

- Show $h\in\mcf$: it is analytic, $h(z_0)=0$, and nonconstant, and Hurwitz makes it injective as a locally uniform limit of injective maps.

- Show $h$ is surjective, by the contrapositive of the earlier step.

![](../../../../assets/assets/figures/2021-12-14_16-34-14.png)

![](../../../../assets/assets/figures/2021-12-14_16-34-24.png)

![](../../../../assets/assets/figures/2021-12-14_16-34-50.png)

![](../../../../assets/assets/figures/2021-12-14_17-34-54.png)

:::

:::{.remark title="What the proof is made of"}
Every ingredient is from earlier in the subject: [[complex-analysis/conformal-maps/normal-families-and-montel|Montel]] supplies compactness, [[complex-analysis/counting-zeros/hurwitz|Hurwitz]] supplies injectivity of the limit, [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|the Cauchy estimate]] bounds the derivative so the supremum is finite, and the Schwarz lemma is behind the hyperbolic translations.
The theorem is not proved by a new idea; it is proved by having all of them at once.

:::

[[C-BKYF7]]

[[C-FVT4V]]

:::{.proof}
\envlist

- Idea: define $(f\inv)'$ directly and show the formula from calculus works.
- By the proposition, $f'(z) \neq 0$ for $z \neq z_0$ in $U$.
- Write $g \da f\inv$ on $\im f$, and replace $V$ by $\im f$.
- For $w, w_0\in V$ with $\abs{w-w_0}$ small and nonzero, write $w=f(z)$, $w_0=f(z_0)$, and compute
\[
\frac{g(w)-g\left(w_{0}\right)}{w-w_{0}}=\frac{1}{\frac{w-w_{0}}{g(w)-g\left(w_{0}\right)}}=\frac{1}{\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}}
\convergesto{z\to z_0}
{1\over f'(z_0) } =
{1\over f'(g(w_0))}
.\]

:::

## Exercises

[[P-Z776N]]
