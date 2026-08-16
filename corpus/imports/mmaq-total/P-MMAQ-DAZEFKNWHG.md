---
schema: qual/card@1
id: P-MMAQ-DAZEFKNWHG
kind: problem
title: Let $\phi\in L^\infty(\RR)$. Show that the following limit exists…
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - integrals
  - sequences-of-functions
relations: []
review: draft
---

::: problem
Let $\phi\in L^\infty(\RR)$. Show that the following limit exists and satisfies the equality
$$
\lim _{n \rightarrow \infty}\left(\int_{\mathbb{R}} \frac{|\phi(x)|^{n}}{1+x^{2}} d x\right)^{\frac{1}{n}} = \norm{\phi}_\infty.
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $\phi \in L^\infty(\RR)$. Prove that $\lim_{n\to\infty} \left( \int_\RR \frac{|\phi(x)|^n}{1+x^2}\,dx \right)^{1/n} = \|\phi\|_\infty$.

<1>1. **Probability measure framework.**
  <2>1. Define the measure $d\mu(x) = \frac{1}{\pi(1+x^2)}\,dx$ on $\RR$.
  <2>2. $\mu$ is a finite probability measure on $\RR$ with $\mu(\RR) = \int_{-\infty}^\infty \frac{1}{\pi(1+x^2)}\,dx = \frac{1}{\pi}[\arctan(x)]_{-\infty}^\infty = 1$.
  <2>3. For any $n \geq 1$:
    $$
    I_n \definedas \int_\RR \frac{|\phi(x)|^n}{1+x^2}\,dx = \pi \int_\RR |\phi(x)|^n\,d\mu(x) = \pi \|\phi\|_{L^n(\mu)}^n.
    $$
  <2>4. $(I_n)^{1/n} = \pi^{1/n} \|\phi\|_{L^n(\mu)}$.
    Proof: Take the $n$-th root of both sides.
  <2>5. Since $\lim_{n\to\infty} \pi^{1/n} = 1$, the limit $\lim_{n\to\infty} (I_n)^{1/n}$ exists and equals $\lim_{n\to\infty} \|\phi\|_{L^n(\mu)}$.

<1>2. **Upper bound: $\limsup_{n\to\infty} \|\phi\|_{L^n(\mu)} \leq \|\phi\|_\infty$.**
  <2>1. For almost every $x \in \RR$, $|\phi(x)| \leq \|\phi\|_\infty$.
    Proof: By the definition of the essential supremum norm $\|\cdot\|_\infty$.
  <2>2. For all $n \geq 1$:
    $$
    \|\phi\|_{L^n(\mu)} = \left( \int_\RR |\phi(x)|^n\,d\mu(x) \right)^{1/n} \leq \left( \int_\RR \|\phi\|_\infty^n\,d\mu(x) \right)^{1/n} = \|\phi\|_\infty (\mu(\RR))^{1/n} = \|\phi\|_\infty \cdot 1 = \|\phi\|_\infty.
    $$
  <2>3. $\limsup_{n\to\infty} (I_n)^{1/n} \leq \limsup_{n\to\infty} (\pi^{1/n} \|\phi\|_\infty) = \|\phi\|_\infty$.

<1>3. **Lower bound: $\liminf_{n\to\infty} \|\phi\|_{L^n(\mu)} \geq \|\phi\|_\infty$.**
  <2>1. If $\|\phi\|_\infty = 0$, then $\phi = 0$ a.e., $I_n = 0$, and the limit is trivially $0 = \|\phi\|_\infty$.
  <2>2. Assume $\|\phi\|_\infty > 0$. Let $\eps \in (0, \|\phi\|_\infty)$ be arbitrary.
  <2>3. Define $E_\eps = \{x \in \RR : |\phi(x)| \geq \|\phi\|_\infty - \eps\}$.
  <2>4. $m(E_\eps) > 0$ and $\mu(E_\eps) > 0$.
    Proof: By definition of the essential supremum, $\{x : |\phi(x)| > \|\phi\|_\infty - \eps\}$ has positive Lebesgue measure. Since $\frac{1}{\pi(1+x^2)} > 0$ everywhere, any set of positive Lebesgue measure has strictly positive $\mu$-measure.
  <2>5. Lower bound the integral:
    $$
    \|\phi\|_{L^n(\mu)} \geq \left( \int_{E_\eps} |\phi(x)|^n\,d\mu(x) \right)^{1/n} \geq \left( \int_{E_\eps} (\|\phi\|_\infty - \eps)^n\,d\mu(x) \right)^{1/n} = (\|\phi\|_\infty - \eps) (\mu(E_\eps))^{1/n}.
    $$
  <2>6. Since $\mu(E_\eps) > 0$, $\lim_{n\to\infty} (\mu(E_\eps))^{1/n} = 1$.
  <2>7. Taking the liminf as $n \to \infty$:
    $$
    \liminf_{n\to\infty} (I_n)^{1/n} = \liminf_{n\to\infty} \left[ \pi^{1/n} \|\phi\|_{L^n(\mu)} \right] \geq 1 \cdot (\|\phi\|_\infty - \eps) \cdot 1 = \|\phi\|_\infty - \eps.
    $$
  <2>8. Since $\eps > 0$ was arbitrary, letting $\eps \to 0^+$ gives $\liminf_{n\to\infty} (I_n)^{1/n} \geq \|\phi\|_\infty$.

<1>4. **Conclusion.**
  Combining <1>2 and <1>3:
  $$
  \|\phi\|_\infty \leq \liminf_{n\to\infty} \left(\int_\RR \frac{|\phi(x)|^n}{1+x^2}\,dx\right)^{1/n} \leq \limsup_{n\to\infty} \left(\int_\RR \frac{|\phi(x)|^n}{1+x^2}\,dx\right)^{1/n} \leq \|\phi\|_\infty.
  $$
  Thus the limit exists and equals $\|\phi\|_\infty$. Q.E.D.
:::
