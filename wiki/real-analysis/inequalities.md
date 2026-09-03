---
title: Inequalities
order: 9
topics:
- Norms
- Bounded Operators
---

# Inequalities

The ones the exam expects without derivation, filed by what they bound.

## Between integrals

- **Hölder.** $\norm{fg}_1 \leq \norm f_p\norm g_q$ for conjugate exponents.
  Equality when $\abs f^p$ and $\abs g^q$ are proportional.

- **Minkowski.** $\norm{f+g}_p \leq \norm f_p + \norm g_p$, the triangle inequality, valid for $p\geq 1$ and false below.

- **Minkowski's integral inequality.** $\norm{\int f(\cdot, y)\dy}_p \leq \int \norm{f(\cdot,y)}_p \dy$: the norm of an integral is at most the integral of the norm, which is the continuous form of the triangle inequality.

- **Jensen.** $\varphi\qty(\int f) \leq \int\varphi\circ f$ for convex $\varphi$ on a probability space.
  The normalization matters: without total mass one the inequality is false.

- **Young.** $\norm{f*g}_r \leq \norm f_p\norm g_q$ with $\frac1r = \frac1p+\frac1q-1$.

## Between a norm and a measure

- **Chebyshev.** $\mu(\abs f > t) \leq t^{-p}\norm f_p^p$.
  The only bridge from an integral bound to a pointwise one.

- **Borel--Cantelli.** $\sum \mu(E_n) <\infty$ implies almost every point lies in finitely many $E_n$.
  Chebyshev then Borel--Cantelli is the standard route to almost-everywhere convergence.

## Elementary, and used constantly

- $ab \leq \frac{a^p}p + \frac{b^q}q$, Young's inequality for products, which is what Hölder is proved from.

- $\abs{a+b}^p \leq 2^{p-1}\qty(\abs a^p + \abs b^p)$, by convexity, which replaces Minkowski when a constant is allowed.

- The reverse triangle inequality $\abs{\norm a - \norm b} \leq \norm{a - b}$.

- Cauchy--Schwarz, which is Hölder at $p=q=2$ and the only case with an inner-product proof.

- Bernoulli, $(1+x)^n \geq 1 + nx$, and $1 + x\leq e^x$, the two that turn a sum into a product.

The full statements are on [[real-analysis/appendices/appendix-inequalities|Appendix: common inequalities]].
