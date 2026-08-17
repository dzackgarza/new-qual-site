---
schema: qual/card@1
id: P-SLXYN
kind: problem
title: "Let $f(z)$ be bounded and analytic in $\\mathbb C$. Let $a \\neq b$ be"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - residues
  - contour-integration
relations: []
review: draft
solved: true
---

::: problem
Let $f(z)$ be bounded and analytic in $\mathbb C$.
Let $a \neq b$ be any fixed complex numbers.
Show that the following limit exists $$\lim_{R \rightarrow \infty} \int_{|z|=R} \frac{f(z)}{(z-a)(z-b)} dz.$$ Use this to show that $f(z)$ must be a constant (Liouville's theorem).
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f$ bounded and entire and $a \neq b$ fixed, show $\lim_{R\to\infty}\int_{\abs{z}=R} \frac{f(z)}{(z-a)(z-b)}\, dz$ exists, and use it to prove Liouville's theorem (that $f$ is constant).

<1>1. Partial fractions: $\frac{1}{(z-a)(z-b)} = \frac{1}{a-b}\qty(\frac{1}{z-a} - \frac{1}{z-b})$ for $z \neq a, b$.
Proof: Bring the right-hand side to the common denominator $(z-a)(z-b)$: the numerator is $\frac{(z-b) - (z-a)}{a-b} = 1$.

<1>2. For $R > \max(\abs{a}, \abs{b})$, $\int_{\abs{z}=R} \frac{f(z)}{(z-a)(z-b)}\, dz = \frac{2\pi i}{a-b}\qty(f(a) - f(b))$.
Proof: By <1>1 the integral is $\frac{1}{a-b}\qty(\int_{\abs{z}=R} \frac{f(z)}{z-a}\, dz - \int_{\abs{z}=R} \frac{f(z)}{z-b}\, dz)$; by the Cauchy integral formula, each $\int_{\abs{z}=R} \frac{f(z)}{z-c}\, dz = 2\pi i f(c)$ for $R > \abs{c}$.

<1>3. The limit as $R \to \infty$ exists and equals $\frac{2\pi i}{a-b}\qty(f(a) - f(b))$.
Proof: By <1>2, the integral is constant in $R$ for all $R > \max(\abs a, \abs b)$, so the limit exists and equals that constant.

<1>4. The limit in <1>3 is $0$.
Proof: Let $M = \sup_\CC \abs f < \infty$ (since $f$ is bounded and entire).
For $R > \max(\abs a, \abs b)$, $\abs{\int_{\abs{z}=R} \frac{f(z)}{(z-a)(z-b)}\, dz} \leq 2\pi R \cdot \frac{M}{(R - \abs a)(R - \abs b)} \to 0$ as $R \to \infty$, where $2\pi R$ is the length of the circle and $\abs{z-a} \geq R - \abs a$, $\abs{z-b} \geq R - \abs b$ on $\abs{z} = R$.

<1>5. $f(a) = f(b)$ for all $a \neq b$, so $f$ is constant.
Proof: <1>3 and <1>4 give $\frac{2\pi i}{a-b}(f(a) - f(b)) = 0$, hence $f(a) = f(b)$; since $a \neq b$ were arbitrary, $f$ is constant.
(And a bounded entire function is constant — Liouville's theorem.)

<1>6. Q.E.D. Proof: <1>3 shows the limit exists and <1>5 shows $f$ is constant.
:::
