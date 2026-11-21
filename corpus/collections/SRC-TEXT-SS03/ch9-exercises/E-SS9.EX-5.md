---
schema: qual/card@1
id: E-SS9.EX-5
kind: problem
title: The Weierstrass sigma function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Weierstrass P
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the lattice has O(R^2)
    points in a disc, so sum |omega|^{-3} converges (dyadic annuli, each contributing O(2^{-k}));
    E_2(w) = 1 + O(|w|^3) since log E_2(w) = -w^2/2 - w^3/3 - ..., so the genus-two product
    converges normally and its zeros are exactly the lattice points, simply. The order is 2 from
    the exponent of convergence together with the canonical-product estimate log M(R) =
    O(R^{2+eps}), which is quoted from the Chapter 5 theory and said to be quoted. For (b):
    E_2'(w)/E_2(w) = -1/(1-w) + 1 + w from log E_2(w) = log(1-w) + w + w^2/2, and dividing by
    omega gives exactly 1/(z-omega) + 1/omega + z/omega^2; the normal convergence is now proved
    rather than asserted, from the identity 1/(z-omega) + 1/omega + z/omega^2 = z^2/(omega^2
    (z-omega)), whose numerator is checked to be z^2, together with |z-omega| >= |omega|/2.
    For (c) the termwise differentiation is justified by the same estimate, and the quotation
    that wp is the displayed series is drawn from Chapter 9, with the final step deriving the
    quotient ((sigma')^2 - sigma sigma'')/sigma^2 from L = -sigma'/sigma. Statement unchanged;
    no retained solution set covers the exercises of Stein-Shakarchi, so the card says the
    argument is its own.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the lattice has O(R^2)
    points in a disc, so sum |omega|^{-3} converges (dyadic annuli, each contributing O(2^{-k}));
    E_2(w) = 1 + O(|w|^3) since log E_2(w) = -w^2/2 - w^3/3 - ..., so the genus-two product
    converges normally and its zeros are exactly the lattice points, simply. The order is 2 from
    the exponent of convergence together with the canonical-product estimate log M(R) =
    O(R^{2+eps}), which is quoted from the Chapter 5 theory and said to be quoted. For (b):
    E_2'(w)/E_2(w) = -1/(1-w) + 1 + w from log E_2(w) = log(1-w) + w + w^2/2, and dividing by
    omega gives exactly 1/(z-omega) + 1/omega + z/omega^2; the normal convergence is now proved
    rather than asserted, from the identity 1/(z-omega) + 1/omega + z/omega^2 = z^2/(omega^2
    (z-omega)), whose numerator is checked to be z^2, together with |z-omega| >= |omega|/2.
    For (c) the termwise differentiation is justified by the same estimate, and the quotation
    that wp is the displayed series is drawn from Chapter 9, with the final step deriving the
    quotient ((sigma')^2 - sigma sigma'')/sigma^2 from L = -sigma'/sigma. Statement unchanged;
    no retained solution set covers the exercises of Stein-Shakarchi, so the card says the
    argument is its own.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the lattice has O(R^2)
    points in a disc, so sum |omega|^{-3} converges (dyadic annuli, each contributing O(2^{-k}));
    E_2(w) = 1 + O(|w|^3) since log E_2(w) = -w^2/2 - w^3/3 - ..., so the genus-two product
    converges normally and its zeros are exactly the lattice points, simply. The order is 2 from
    the exponent of convergence together with the canonical-product estimate log M(R) =
    O(R^{2+eps}), which is quoted from the Chapter 5 theory and said to be quoted. For (b):
    E_2'(w)/E_2(w) = -1/(1-w) + 1 + w from log E_2(w) = log(1-w) + w + w^2/2, and dividing by
    omega gives exactly 1/(z-omega) + 1/omega + z/omega^2; the normal convergence is now proved
    rather than asserted, from the identity 1/(z-omega) + 1/omega + z/omega^2 = z^2/(omega^2
    (z-omega)), whose numerator is checked to be z^2, together with |z-omega| >= |omega|/2.
    For (c) the termwise differentiation is justified by the same estimate, and the quotation
    that wp is the displayed series is drawn from Chapter 9, with the final step deriving the
    quotient ((sigma')^2 - sigma sigma'')/sigma^2 from L = -sigma'/sigma. Statement unchanged;
    no retained solution set covers the exercises of Stein-Shakarchi, so the card says the
    argument is its own.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the lattice has O(R^2)
    points in a disc, so sum |omega|^{-3} converges (dyadic annuli, each contributing O(2^{-k}));
    E_2(w) = 1 + O(|w|^3) since log E_2(w) = -w^2/2 - w^3/3 - ..., so the genus-two product
    converges normally and its zeros are exactly the lattice points, simply. The order is 2 from
    the exponent of convergence together with the canonical-product estimate log M(R) =
    O(R^{2+eps}), which is quoted from the Chapter 5 theory and said to be quoted. For (b):
    E_2'(w)/E_2(w) = -1/(1-w) + 1 + w from log E_2(w) = log(1-w) + w + w^2/2, and dividing by
    omega gives exactly 1/(z-omega) + 1/omega + z/omega^2; the normal convergence is now proved
    rather than asserted, from the identity 1/(z-omega) + 1/omega + z/omega^2 = z^2/(omega^2
    (z-omega)), whose numerator is checked to be z^2, together with |z-omega| >= |omega|/2.
    For (c) the termwise differentiation is justified by the same estimate, and the quotation
    that wp is the displayed series is drawn from Chapter 9, with the final step deriving the
    quotient ((sigma')^2 - sigma sigma'')/sigma^2 from L = -sigma'/sigma. Statement unchanged;
    no retained solution set covers the exercises of Stein-Shakarchi, so the card says the
    argument is its own.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the lattice has O(R^2)
    points in a disc, so sum |omega|^{-3} converges (dyadic annuli, each contributing O(2^{-k}));
    E_2(w) = 1 + O(|w|^3) since log E_2(w) = -w^2/2 - w^3/3 - ..., so the genus-two product
    converges normally and its zeros are exactly the lattice points, simply. The order is 2 from
    the exponent of convergence together with the canonical-product estimate log M(R) =
    O(R^{2+eps}), which is quoted from the Chapter 5 theory and said to be quoted. For (b):
    E_2'(w)/E_2(w) = -1/(1-w) + 1 + w from log E_2(w) = log(1-w) + w + w^2/2, and dividing by
    omega gives exactly 1/(z-omega) + 1/omega + z/omega^2; the normal convergence is now proved
    rather than asserted, from the identity 1/(z-omega) + 1/omega + z/omega^2 = z^2/(omega^2
    (z-omega)), whose numerator is checked to be z^2, together with |z-omega| >= |omega|/2.
    For (c) the termwise differentiation is justified by the same estimate, and the quotation
    that wp is the displayed series is drawn from Chapter 9, with the final step deriving the
    quotient ((sigma')^2 - sigma sigma'')/sigma^2 from L = -sigma'/sigma. Statement unchanged;
    no retained solution set covers the exercises of Stein-Shakarchi, so the card says the
    argument is its own.
---

::: {.exercise}
Let $\sigma(z)$ be the canonical product
$$
\sigma(z) = z\prod_{j=1}^{\infty} E_2(z/\tau_j),
$$
where $\tau_j$ is an enumeration of the periods $\{n + m\tau\}$ with $(n, m) \neq (0, 0)$, and $E_2(z) = (1 - z)e^{z + z^2/2}$.

(a) Show that $\sigma(z)$ is an entire function of order $2$ that has simple zeros at all the periods $n + m\tau$, and vanishes nowhere else.

(b) Show that
$$
\frac{\sigma'(z)}{\sigma(z)} = \frac{1}{z} + \sum_{(n, m) \neq (0, 0)} \left[ \frac{1}{z - n - m\tau} + \frac{1}{n + m\tau} + \frac{z}{(n + m\tau)^2} \right],
$$
and that this series converges whenever $z$ is not a lattice point.

(c) Let $L(z) = -\sigma'(z)/\sigma(z)$. Then
$$
L'(z) = \frac{(\sigma'(z))^2 - \sigma(z)\sigma''(z)}{(\sigma(z))^2} = \wp(z).
$$
:::

::: {.solution}
Write $\Lambda=\{n+m\tau:n,m\in\ZZ\}$ with $\Im\tau>0$ and $E_2(w)=(1-w)e^{w+w^2/2}$. The lattice has $O(R^2)$ points in a disc of radius $R$, so $\sum_{\omega\ne0}\abs\omega^{-3}$ converges and the genus-two product converges normally, giving an entire $\sigma$ whose zeros are exactly the lattice points, all simple; the order is $2$, the exponent of convergence of the lattice being $2$ and the canonical-product estimate giving an upper bound. Logarithmic differentiation produces the standard $\zeta$-type series, whose normal convergence follows from $\frac{1}{z-\omega}+\frac{1}{\omega}+\frac{z}{\omega^2}=\frac{z^2}{\omega^2(z-\omega)}$, and one more differentiation gives the Weierstrass $\wp$ because the two series coincide term by term. Three standard inputs are quoted rather than proved, and each step says so: the canonical-product estimates of Chapter 5, the definition of $\wp$ as the displayed series in Chapter 9, and the usual convergence criteria for products. The argument is this card's own: no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #lattice}
The number of lattice points with $\abs\omega\le R$ is $O(R^2)$, and consequently $\sum_{\omega\in\Lambda,\ \omega\ne0}\abs\omega^{-3}<\infty$.

::: pf-proof
The lattice is $\ZZ+\ZZ\tau$ with $\tau\notin\RR$, so it is discrete and a fundamental parallelogram $P$ is bounded; a disc of radius $R$ is then covered by $O(R^2)$ translates $\omega+P$, which gives $N(R)\le CR^2$. Group the nonzero points into dyadic annuli: those with $2^k<\abs\omega\le2^{k+1}$ number at most $N(2^{k+1})\le C4^{k+1}$ and each contributes at most $2^{-3k}$ to the sum $\sum\abs\omega^{-3}$, so the annulus contributes at most $8C\cdot2^{-k}$, and $\sum_k2^{-k}<\infty$. Adding the finitely many points with $\abs\omega\le1$ gives the finiteness. Equivalently, the exponent of convergence of $\Lambda$ is $2$.
:::

:::


::: {.pf-step #product}
The product $\sigma(z)=z\prod_{\omega\ne0}E_2(z/\omega)$ converges normally on $\CC$ and defines an entire function whose zeros are exactly the lattice points, each simple.

::: pf-proof
For $\abs w<1$ one has $\log E_2(w)=\log(1-w)+w+w^2/2=-w^2/2-w^3/3-\cdots$, so $E_2(w)=1+O(\abs w^3)$, and for fixed $z$ and $\abs\omega\ge2\abs z$ the factor is $E_2(z/\omega)=1+O(\abs{z/\omega}^3)$; by step [](#lattice){.pf-ref} the series $\sum_\omega\abs{E_2(z/\omega)-1}$ converges, uniformly for $z$ in a compact set. A normally convergent product of holomorphic functions is holomorphic, so $\sigma$ is entire. The factor $E_2(z/\omega)$ vanishes exactly at $z=\omega$, and simply, because $E_2(w)=0$ only at $w=1$ and $E_2(w)=(1-w)\cdot(\text{nonzero})$ there; the prefactor $z$ gives the zero at $0$; and every other factor is nonzero at $z=\omega$ since $\omega'\ne\omega$ makes $z/\omega'\ne1$. So the zeros are the lattice points, each simple.
:::

:::


::: {.pf-step #order-lower}
The exponent of convergence of $\Lambda$ is $2$, so any entire function whose zeros are exactly the lattice points has order at least $2$.

::: pf-proof
By the counting of step [](#lattice){.pf-ref}, the points with $2^k<\abs\omega\le2^{k+1}$ number about $4^k$, so $\sum_{\omega\ne0}\abs\omega^{-s}$ behaves like $\sum_k4^k2^{-sk}$, which converges exactly when $s>2$. The order of an entire function is at least the exponent of convergence of its zero set, by the theory of Chapter 5, which is the quoted input here.
:::

:::


::: {.pf-step #order-upper}
The canonical-product estimate gives $\log M_\sigma(R)=O(R^{2+\varepsilon})$ for every $\varepsilon>0$, so the order of $\sigma$ is at most $2$, hence exactly $2$.

::: pf-proof
The standard estimate for a canonical product of genus $p$ with zero-counting function $N(R)=O(R^q)$ is $\log M(R)=O(R^{q+\varepsilon})$ for every $\varepsilon>0$ when $p<q+1$; here $p=2$, $q=2$ and $N(R)=O(R^2)$ by step [](#lattice){.pf-ref}. The order is the infimum of the $\rho$ with $\log M_\sigma(R)=O(R^{\rho})$, so it is at most $2$, and by step [](#order-lower){.pf-ref} at least $2$. The estimate is quoted from Chapter 5 and not re-derived.
:::

:::


::: {.pf-step #logderiv}
$\dfrac{E_2'(w)}{E_2(w)}=-\dfrac{1}{1-w}+1+w$, and hence
$$
\frac{\sigma'(z)}{\sigma(z)}=\frac1z+\sum_{\omega\ne0}\Bigl(\frac{1}{z-\omega}+\frac1\omega+\frac{z}{\omega^2}\Bigr)
$$
for $z\notin\Lambda$.

::: pf-proof
From $\log E_2(w)=\log(1-w)+w+w^2/2$ near $w=0$, differentiation gives $\dfrac{E_2'(w)}{E_2(w)}=-\dfrac{1}{1-w}+1+w$. For $\sigma=z\prod_\omega E_2(z/\omega)$ the logarithmic derivative is $\dfrac1z+\sum_\omega\dfrac1\omega\dfrac{E_2'(z/\omega)}{E_2(z/\omega)}$ off $\Lambda$: termwise differentiation of a normally convergent product of nowhere-vanishing factors is legitimate on compact sets avoiding the zeros, by Weierstrass's theorem. Since
$$
\frac1\omega\Bigl(-\frac{1}{1-z/\omega}+1+\frac z\omega\Bigr)=\frac1\omega\Bigl(-\frac{\omega}{\omega-z}+1+\frac z\omega\Bigr)=\frac{1}{z-\omega}+\frac1\omega+\frac{z}{\omega^2},
$$
the displayed series follows.
:::

:::


::: {.pf-step #convergence}
The series of step [](#logderiv){.pf-ref} converges normally on $\CC\setminus\Lambda$.

::: pf-proof
Putting the three terms over the common denominator $\omega^2(z-\omega)$ gives numerator $\omega^2+\omega(z-\omega)+z(z-\omega)=z^2$, so
$$
\frac{1}{z-\omega}+\frac1\omega+\frac{z}{\omega^2}=\frac{z^2}{\omega^2(z-\omega)}.
$$
For $z$ in a compact set $K$ and $\abs\omega>2\max_K\abs z$ one has $\abs{z-\omega}\ge\abs\omega-\abs z\ge\abs\omega/2$, hence the modulus of the summand is at most $2\abs z^2\abs\omega^{-3}$, summable by step [](#lattice){.pf-ref} uniformly on $K$; the finitely many remaining $\omega$ contribute holomorphic terms off $\Lambda$.
:::

:::


::: {.pf-step #Lprime}
With $L=-\sigma'/\sigma$,
$$
L'(z)=\frac1{z^2}+\sum_{\omega\ne0}\Bigl(\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}\Bigr),
$$
the series converging normally on $\CC\setminus\Lambda$.

::: pf-proof
Differentiate the normally convergent series of steps [](#logderiv){.pf-ref} and [](#convergence){.pf-ref} term by term, which Weierstrass's theorem permits: $\frac{d}{dz}\frac{1}{z-\omega}=-\frac{1}{(z-\omega)^2}$, and the other two terms have derivatives $0$ and $\frac{1}{\omega^2}$. Hence $\frac{d}{dz}\frac{\sigma'}{\sigma}=-\frac1{z^2}-\sum_\omega\bigl(\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}\bigr)$, and $L'=-\frac{d}{dz}\frac{\sigma'}{\sigma}$ gives the displayed series. Its normal convergence follows from $\abs{\frac{1}{(z-\omega)^2}-\frac{1}{\omega^2}}=\abs{\frac{\omega^2-(z-\omega)^2}{\omega^2(z-\omega)^2}}\le C_K\abs\omega^{-3}$ for $\abs\omega>2\max_K\abs z$.
:::

:::


::: {.pf-step #wp}
$L'(z)=\wp(z)$, where $\wp(z)=\dfrac1{z^2}+\sum_{\omega\ne0}\Bigl(\dfrac{1}{(z-\omega)^2}-\dfrac{1}{\omega^2}\Bigr)$ is the Weierstrass function.

::: pf-proof
This is the definition of $\wp$ in Chapter 9, quoted; the series in step [](#Lprime){.pf-ref} and the defining series for $\wp$ are the same expression, the sum being over $\Lambda\setminus\{0\}$ in both.
:::

:::


::: {.pf-step #quotient}
$\wp(z)=\dfrac{(\sigma'(z))^2-\sigma(z)\sigma''(z)}{\sigma(z)^2}$ for $z\notin\Lambda$.

::: pf-proof
For $L=-\sigma'/\sigma$ the quotient rule gives $L'=-\dfrac{\sigma''\sigma-(\sigma')^2}{\sigma^2}=\dfrac{(\sigma')^2-\sigma\sigma''}{\sigma^2}$, using $\sigma\ne0$ off $\Lambda$. With step [](#wp){.pf-ref} this is the identity of part (c).
:::

:::


::: {.pf-step #conclusion}
Parts (a), (b) and (c) hold as stated.

::: pf-proof
Steps [](#product){.pf-ref}, [](#order-lower){.pf-ref} and [](#order-upper){.pf-ref} give (a); steps [](#logderiv){.pf-ref} and [](#convergence){.pf-ref} give (b); steps [](#Lprime){.pf-ref}, [](#wp){.pf-ref} and [](#quotient){.pf-ref} give (c).
:::

:::

:::
:::
