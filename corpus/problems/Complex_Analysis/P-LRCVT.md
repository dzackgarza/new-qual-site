---
schema: qual/card@1
id: P-LRCVT
kind: problem
title: Blaschke factors as automorphisms of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Biholomorphisms
relations: []
review: draft
---

::: problem
(a) Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
Prove that
$$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \; \; \; \mbox{if} \; |z| < 1 \; \mbox{and}\; |w| < 1,$$
and also that
$$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \; \; \; \mbox{if} \; |z| = 1 \; \mbox{or}\; |w| = 1.$$

(b) Prove that for fixed $w$ in the unit disk $\mathbb D$, the
mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the
following conditions:

(i) $F$ maps $\mathbb D$ to itself and is holomorphic. 

(ii) $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and
$F(w) = 0$.

(iii) $|F(z)| = 1$ if $|z| = 1$.

(iv) $F: {\mathbb D} \mapsto {\mathbb D}$ is bijective.

> Hint: Calculate $F \circ F$.

### Tie's Extra Questions: Fall 2015### Tie's Extra Questions: Fall 2015
:::

::: solution
For (a), compute
\[
|1-\bar wz|^2-|w-z|^2
=(1-|w|^2)(1-|z|^2).
\]
Hence if $|w|<1$ and $|z|<1$, the right-hand side is positive and therefore
\[
\left|\frac{w-z}{1-\bar wz}\right|<1.
\]
If either $|w|=1$ or $|z|=1$, the right-hand side is zero, giving equality of
the two moduli and hence
\[
\left|\frac{w-z}{1-\bar wz}\right|=1.
\]

Now fix $w\in\mathbb D$ and write
\[
F(z)=\frac{w-z}{1-\bar wz}.
\]
The denominator does not vanish on $\mathbb D$, so $F$ is holomorphic there.
Part (a) gives $F(\mathbb D)\subseteq\mathbb D$. Direct substitution gives
\[
F(0)=w,\qquad F(w)=0,
\]
and part (a) also gives $|F(z)|=1$ for $|z|=1$.

Finally,
\[
F(F(z))=z.
\]
Indeed, substituting the formula for $F(z)$ and simplifying gives the identity.
Thus $F$ is its own inverse, so it is bijective from $\mathbb D$ onto itself.
Therefore $F\in\operatorname{Aut}(\mathbb D)$.
:::
