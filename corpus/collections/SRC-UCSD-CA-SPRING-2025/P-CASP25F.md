---
schema: qual/card@1
id: P-CASP25F
kind: problem
title: "Three-circles type theorem for holomorphic functions vanishing only at 0"
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Three-Circles Theorem
  - Harmonic Functions
  - Maximum Principle
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/SP25_220_Complex_Analysis_Qual.pdf,
    the problem defining M(r) = max_{|z| = r} |f(z)| for a holomorphic f on the disc with f(z) != 0
    for z != 0 and asking for (i) harmonicity of h_s, (ii) the existence of s with
    max_{|z|=1/2} h_s = max_{|z|=1/8} h_s, (iii) M(1/4)^2 <= M(1/2) M(1/8), and (iv) equality iff
    f(z) = a z^n. The card's four parts are the printed four.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the facts the prose used
    silently: that M(1/2) and M(1/8) are positive because f is continuous and nonvanishing on those
    circles, so the logarithm is defined; the derivation of s log 2 = (log M(1/8) - log M(1/2))/2
    from the defining equation of s, which is what turns the maximum principle on the annulus into
    the three-circles inequality at the radii 1/8, 1/4, 1/2; and the reason equality forces
    s + n = 0, namely that log|g| is bounded near 0 while log|z| is not. Checked the case f = a z^n
    directly against the inequality. No retained published solution covers this problem.
---

::: {.problem}
Let $f : \DD \to \CC$ be holomorphic and assume $f(z) \neq 0$ for $z \neq 0$.
For $0 \leq r < 1$, let $M(r) = \max_{\abs{z}=r} \abs{f(z)}$.

(i) Show that the function $h_s(z) = s \log \abs{z} + \log \abs{f(z)}$ is harmonic in $\DD \setminus \{0\}$ for all $s \in \RR$.

(ii) Show that there exists $s \in \RR$ such that $\max_{\abs{z}=\frac{1}{2}} h_s(z) = \max_{\abs{z}=\frac{1}{8}} h_s(z)$.

(iii) Show that $M\!\left(\frac{1}{4}\right)^2 \leq M\!\left(\frac{1}{2}\right) M\!\left(\frac{1}{8}\right)$.

(iv) Show that equality holds if and only if $f(z) = az^n$ for some $a \in \CC$ and some integer $n \geq 0$.
:::

::: {.solution}
This is the fourth problem of the UCSD complex-analysis qualifying exam of Spring 2025 (`assets/attachments/SP25_220_Complex_Analysis_Qual.pdf`). No published solution set is transcribed: the argument is the card's own, and it is the Hadamard three-circles argument in the degenerate form the exam asks for.

::: pf

::: {.pf-step #harmonic}
(i) $h_{s}(z)=s\log\abs{z}+\log\abs{f(z)}$ is harmonic on $\DD\setminus\{0\}$ for every $s\in\RR$, and $\max_{\abs{z}=r}h_{s}=s\log r+\log M(r)$ for $0<r<1$.

::: pf-proof
$f$ has no zeros on $\DD\setminus\{0\}$ by hypothesis, so on that punctured disc $\log\abs{f}=\operatorname{Re}\log f$ for a holomorphic branch $\log f$, and a real part of a holomorphic function is harmonic; $\log\abs{z}=\operatorname{Re}\log z$ is harmonic on $\CC\setminus\{0\}$ for the principal branch, and $z\mapsto s\log\abs{z}$ is harmonic as a real multiple. On the circle $\abs{z}=r$ the first term is the constant $s\log r$, so the maximum of the sum there is $s\log r+\log M(r)$.
:::
:::

::: {.pf-step #choose}
(ii) There is a real $s$ with $\max_{\abs{z}=1/2}h_{s}=\max_{\abs{z}=1/8}h_{s}$.

::: pf-proof
By step [](#harmonic){.pf-ref} the two maxima are $s\log\frac12+\log M(\frac12)$ and $s\log\frac18+\log M(\frac18)$, and $M(\frac12),M(\frac18)>0$ because $f$ is continuous and nonvanishing on the two circles. The equation
$$s\left(\log\frac12-\log\frac18\right)=\log M\left(\frac18\right)-\log M\left(\frac12\right)$$
has the unique solution $s=\left(\log M(\frac18)-\log M(\frac12)\right)/\log4$, since $\log\frac12-\log\frac18=\log4\neq0$.
:::
:::

::: {.pf-step #maxprinciple}
(iii) With this $s$, $M(\frac14)^{2}\leq M(\frac12)M(\frac18)$.

::: pf-proof
The closed annulus $\frac18\leq\abs{z}\leq\frac12$ is compact, and $h_{s}$ is harmonic on a neighbourhood of it by step [](#harmonic){.pf-ref}, so the maximum of $h_{s}$ on the annulus is attained on one of the two boundary circles, and steps [](#choose){.pf-ref} give the common value $\max_{\abs{z}=1/2}h_{s}=\max_{\abs{z}=1/8}h_{s}=:A$ there. The circle $\abs{z}=\frac14$ lies inside the annulus, so
$$s\log\frac14+\log M\left(\frac14\right)\leq A=s\log\frac12+\log M\left(\frac12\right).$$
Moreover $2\log\frac14=\log\frac12+\log\frac18$, and from the choice of $s$,
$$\log M\left(\frac18\right)-\log M\left(\frac12\right)=s\left(\log\frac12-\log\frac18\right)=2s\log2 .$$
Writing $s\log\frac12=s\log\frac14+s\log2$, the inequality becomes
$$\log M\left(\frac14\right)\leq s\log2+\log M\left(\frac12\right)=\frac{\log M(\frac18)-\log M(\frac12)}{2}+\log M\left(\frac12\right),$$
that is $2\log M(\frac14)\leq\log M(\frac18)+\log M(\frac12)$; exponentiating gives the assertion.
:::
:::

::: {.pf-step #monomial}
(iv) If $f(z)=az^{n}$ then equality holds in (iii).

::: pf-proof
For $f(z)=az^{n}$ one has $M(r)=\abs{a}r^{n}$, so $M(\frac14)^{2}=\abs{a}^{2}4^{-2n}$ and $M(\frac12)M(\frac18)=\abs{a}^{2}2^{-n}8^{-n}=\abs{a}^{2}2^{-4n}=\abs{a}^{2}4^{-2n}$, and the two sides agree.
:::
:::

::: {.pf-step #equality}
(iv) If equality holds in (iii), then $f(z)=az^{n}$ for some $a\in\CC$ and some integer $n\geq0$.

::: pf-proof
Equality in step [](#maxprinciple){.pf-ref} says that $h_{s}$ attains its maximum $A$ at every point of the circle $\abs{z}=\frac14$, an interior circle of the annulus. A harmonic function attaining its maximum at an interior point of a domain is constant there, so $h_{s}\equiv A$ on the annulus $\frac18<\abs{z}<\frac12$. Let $n\geq0$ be the order of the zero of $f$ at $0$, and write $f(z)=z^{n}g(z)$ with $g$ holomorphic and nonvanishing on $\DD$; then $h_{s}=(s+n)\log\abs{z}+\log\abs{g(z)}$ on the annulus. The function $\log\abs{g}$ is harmonic on the whole disc, since $g$ is nonvanishing there, so $\log\abs{g}$ is bounded near $0$, while $\log\abs{z}\to-\infty$. Constancy of $h_{s}$ therefore forces $s+n=0$, and then $\log\abs{g}\equiv A$ is constant. A holomorphic function of constant modulus on the connected disc is constant, so $g\equiv a$, and $f(z)=az^{n}$.
:::
:::
:::

:::
