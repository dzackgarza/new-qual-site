---
title: Casorati-Weierstrass and Picard
order: 40
topics:
- Casorati-Weierstrass
- Picard
---

# Casorati--Weierstrass and Picard

Near an essential singularity a holomorphic function has no limit, and the statements on this page are the three accounts of what its values do instead. Casorati--Weierstrass says the image is dense and is a reduction to the removable-singularity theorem; Picard's theorems say the values are attained with at most one exception, and are deeper.

## Casorati--Weierstrass

[[T-C5VEI]]

The conclusion is about closeness, not attainment: for every $w_0\in\CC$ and every $\varepsilon>0$ there is $z$ in the punctured disc with $\abs{f(z)-w_0}<\varepsilon$, and the theorem says nothing about how many such $z$ there are, or whether $z$ can be chosen with $f(z)=w_0$ exactly.

::: {.remark title="Why the hypothesis is essential"}
At a [[D-BQLJV|removable singularity]] the function extends across $z_0$ and is therefore bounded near it, so the image of a small punctured disc misses a disc. At a [[D-AUD6K|pole]], $\abs{f(z)}\to\infty$ as $z\to z_0$ [@SS03, ch. 3, Corollary 3.2], so the image of a small punctured disc misses a neighbourhood of $0$. Density of the image of every punctured neighbourhood is thus exactly the behaviour of an [[D-VKP6N|essential singularity]], which makes the theorem a criterion as much as a description.
:::

The proof in [@SS03, ch. 3, Theorem 3.3] is a reduction: a value $w_0$ and a radius $\delta>0$ that the image avoids make $1/(f-w_0)$ bounded on the punctured disc, and [[T-ZZJDP|Riemann's removable singularity theorem]] then extends it across $z_0$, after which the singularity of $f$ there is removable or a pole. Nothing in that argument survives the loss of the constant $\delta$, and that is where Picard's theorem begins.

## Picard's great theorem

[[T-DDOWW]]

The conclusion is of a different kind from density: away from at most one value, every value of $\CC$ is taken, and each of them in every neighbourhood of $z_0$, hence infinitely often. It implies Casorati--Weierstrass, since a set containing every value with at most one exception is dense; the converse fails, and the example below shows a function for which the exceptional value is real.

The card states the value-omission form. The value-distribution form is recorded without proof in [@SS03, ch. 3, §3], in the paragraph following Theorem 3.3, and is [@McM17, Theorem 4.35]: an analytic function takes every value in $\CC$, with at most one exception, in every neighbourhood of an essential singularity.

## Picard's little theorem

[[T-HWBWI]]

Casorati--Weierstrass does not give the little theorem: its conclusion is compatible with an omitted value, as the example below shows, and it says nothing about two. The little theorem follows from the great one in the form the card states, applied at infinity. For a nonconstant entire $f$ that omits $a\neq b$, put $g(w)\coloneqq f(1/w)$ on the punctured plane. If $g$ has a removable singularity at $0$, then $f$ is bounded and constant; if $g$ has a pole at $0$, then $f$ is a polynomial, and surjective by [[P-ZZO3P|the fundamental theorem of algebra]]. Neither alternative is available for a nonconstant $f$ that omits $a$, so $g$ has an essential singularity at $0$, and it omits the three distinct points $a$, $b$ and $\infty$ of the Riemann sphere, which the great theorem cannot allow: it would extend $g$ meromorphically across $0$.
So no nonconstant entire function omits two values.

Ahlfors proves the little theorem directly instead, from the modular function and the monodromy theorem [@Ahl73, ch. 8, §3.1, Theorem 5], so a question that asks for the theorem and a question that asks for a route to it have different answers.

## Telling the three apart

| statement | hypothesis | conclusion |
| --- | --- | --- |
| Casorati--Weierstrass | essential singularity | the image of every punctured neighbourhood is dense in $\CC$ |
| Picard, great | essential singularity | every value of $\CC$, with at most one exception, is taken in every neighbourhood |
| Picard, little | $f$ entire and nonconstant | every value of $\CC$, with at most one exception, is taken |

Two substitutions are not available. Quoting Casorati--Weierstrass where a question asks that a value be attained: attainment near a finite essential singularity is the great theorem, and for an entire function it is the little one. Quoting the little theorem at a finite singularity: it carries no hypothesis about one, so it states nothing there.

::: {.example title="$e^{1/z}$ omits only $0$"}
On $\DD\smz$ the function $e^{1/z}$ omits $0$, since the exponential never vanishes.
For $w\in\CC\smz$ the equation $e^{1/z}=w$ reads $1/z=\Log w+2\pi i k$ with $k\in\ZZ$, so its solutions are
$$
z=\frac{1}{\Log w+2\pi i k},
$$
taken over the integers $k$ with $\Log w+2\pi i k\neq0$: every $k$ when $w\neq1$, and $k\neq0$ when $w=1$, where $\Log 1=0$ and the term $k=0$ is the excluded zero denominator.
For those $k$, $\abs z\leq1/\bigl(2\pi\abs k-\abs{\Log w}\bigr)$ once $2\pi\abs k>\abs{\Log w}$, and $z\neq0$; so the solutions tend to $0$ and therefore lie in every punctured disc about $0$: each $w\in\CC\smz$ is taken infinitely often, and the omitted value $0$ is the single exception Picard's theorem allows.
:::

## Problems

### The image of an entire function

Density of the image, and its failure, are decided by what $f$ does at infinity, and the two entries reach the answer by different routes: one through Liouville's theorem, the other through Casorati--Weierstrass applied to $f(1/w)$.

[[P-EMCA9]] [[P-ZRVTI]]

### Values omitted in the entire case

A disc that the image misses is stronger than a value it misses: one of these needs only Liouville's theorem, and the other needs two omitted values and so reaches the little theorem.

[[E-HEJJK]] [[P-SVQNB]]

### Values taken infinitely often

The function is not a polynomial, so it has an essential singularity at infinity; the great theorem counts the values there, and a functional identity turns the count into solutions of an equation.

[[E-XZWER]]
