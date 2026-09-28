---
schema: qual/card@1
id: E-SWC3U
kind: problem
title: $\bigl|\frac{w-z}{1-\bar{w}z}\bigr|$ on the closed disk, and $z\mapsto\frac{w-z}{1-\bar{w}z}$
  is an automorphism of $\mathbb{D}$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
  - Schwarz Lemma
relations: []
review: draft
---

::: {.problem}
a.
Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
Prove that
$$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \; \; \; \mbox{if} \; |z| < 1 \; \mbox{and}\; |w| < 1,$$
and also that
$$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \; \; \; \mbox{if} \; |z| = 1 \; \mbox{or}\; |w| = 1.$$

b.
Prove that for fixed $w$ in the unit disk $\mathbb D$, the
mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the following conditions:

  - $F$ maps $\mathbb D$ to itself and is holomorphic. 

  - $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and $F(w) = 0$.

  - $\abs{F(z)} = 1$ if $|z| = 1$.

  - $F: {\mathbb D} \mapsto {\mathbb D}$ is bijective.

> Hint: Calculate $F \circ F$.

:::

::: {.solution}
The key identity is
\[
|1-\overline wz|^2-|w-z|^2
=(1-|w|^2)(1-|z|^2).
\]
Indeed, expanding both squared moduli gives
\[
1-\overline wz-w\overline z+|w|^2|z|^2
-|w|^2+w\overline z+\overline wz-|z|^2,
\]
which factors as claimed.

If $|z|<1$ and $|w|<1$, the right-hand side is positive, so
\[
|w-z|<|1-\overline wz|,
\]
and therefore
\[
\left|\frac{w-z}{1-\overline wz}\right|<1.
\]
If $|z|=1$ or $|w|=1$, the right-hand side is $0$, so the two moduli are
equal and the quotient has modulus $1$ whenever it is defined.

Now fix $w\in\mathbb D$ and put
\[
F(z)=\frac{w-z}{1-\overline wz}.
\]
Because $|\overline wz|<1$ for $z\in\mathbb D$, the denominator never
vanishes there, so $F$ is holomorphic. The first part shows that
$F(\mathbb D)\subset\mathbb D$, and directly
\[
F(0)=w,
\qquad
F(w)=0.
\]
It also shows $|F(z)|=1$ for $|z|=1$.

Finally, a direct substitution gives
\[
F(F(z))=z.
\]
Thus $F$ is its own inverse. Consequently $F:\mathbb D\to\mathbb D$ is
bijective, hence an automorphism of the unit disk.
:::
