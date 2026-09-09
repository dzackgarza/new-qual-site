---
schema: qual/card@1
id: P-JNH77
kind: problem
title: A Galois-theoretic proof of the fundamental theorem of algebra
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Give a Galois-theoretic proof of the fundamental theorem of algebra.
What input from real analysis is needed?
:::

::: {.solution}
We prove that $\CC$ has no nontrivial finite algebraic extension.

The analytic input is:

- every real polynomial of odd degree has a real root, by the intermediate value theorem;
- every positive real number has a real square root.

The second fact implies that every complex number has a complex square root.

<1>1. The real field has no nontrivial finite extension of odd degree.
::: {.proof}
Let $E/\RR$ be finite of odd degree. Since the extension is separable, the primitive element theorem gives $E=\RR(\alpha)$. The minimal polynomial of $\alpha$ has odd degree, hence has a real root. Being irreducible over $\RR$, it must therefore be linear. Thus $E=\RR$.
:::

<1>2. The complex field has no quadratic extension.
::: {.proof}
In characteristic different from $2$, every quadratic extension has the form $\CC(\sqrt a)$ for some $a\in\CC^\times$. But every complex number has a square root in $\CC$, so such an extension is trivial.
:::

<1>3. Let $L/\RR$ be a finite Galois extension containing $\CC$. Then $\Gal(L/\CC)$ is trivial.
::: {.proof}
Put
\[
G=\Gal(L/\RR),
\qquad
H=\Gal(L/\CC).
\]
Since $[\CC:\RR]=2$, the subgroup $H$ has index $2$ in $G$.

By <1>1, $|G|$ has no odd prime divisor: if an odd prime $p$ divided $|G|$, Cauchy's theorem would give a subgroup of order $p$, whose fixed field would yield a nontrivial odd-degree finite extension at the corresponding step. Hence $G$ is a $2$-group, and so is $H$.

If $H\neq1$, then the finite $2$-group $H$ has a subgroup $K$ of index $2$. By Galois correspondence,
\[
[L^K:\CC]=[H:K]=2,
\]
contradicting <1>2. Therefore $H=1$, so $L=\CC$.
:::

<1>4. Every nonconstant polynomial in $\CC[x]$ has a root in $\CC$.
::: {.proof}
Let $f\in\CC[x]$ be nonconstant and let $L$ be the Galois closure over $\RR$ of a splitting field of $f$. Then $L/\RR$ is finite Galois and contains $\CC$. By <1>3, $L=\CC$. Hence all roots of $f$ already lie in $\CC$.
:::

Thus $\CC$ is algebraically closed.
:::
