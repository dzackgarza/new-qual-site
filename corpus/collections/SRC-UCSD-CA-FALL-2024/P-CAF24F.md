---
schema: qual/card@1
id: P-CAF24F
kind: problem
title: 'Meromorphic function with poles in the disc and $\abs{f-1}\le 1/\abs{z}^2$ outside'
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: boundedness near infinity from the hypothesis, giving the removable
    singularity with value 1; the reason a meromorphic function on the sphere is a ratio of
    polynomials; the local computation of f'/f at a zero or pole, and the conclusion that the
    difference from the sum of simple poles is holomorphic and vanishes at infinity; and the
    verification that f = 1 + O(z^-2) gives f' = O(z^-3) and hence f'/f = O(z^-3), so that the
    coefficients of z^-1 and z^-2 both vanish. Not claimed: a retained solution set; the
    provenance names the examination paper.
---

::: {.problem}
Let $f$ be meromorphic in $\CC$ with finitely many zeros and poles.
Write $\alpha_1,\ldots,\alpha_n$ for the zeros and poles of $f$, and let $m_1,\ldots,m_n$ be their orders.
Assume that

- the poles of $f$ are in the unit disc $\DD$,

- $\abs{f(z) - 1} \le \dfrac{1}{\abs{z}^2}$ for all $\abs{z} \ge 1$.

(i) Show that $f$ is a rational function.

(ii) Show that $\displaystyle\sum_{i=1}^{n} m_i \alpha_i = 0$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2024 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $f$ is meromorphic on $\CC$ with finitely many zeros and poles, $\alpha_1,\dots,\alpha_n$ are those points with signed orders $m_i$ — positive at a zero, negative at a pole — the poles of $f$ lie in $\DD$, and $\abs{f(z)-1}\le\abs z^{-2}$ for $\abs z\ge1$.

::: pf

::: {.pf-step #part-i-removable}
$\infty$ is a removable singularity of $f$, with $f(\infty)=1$.

::: pf-proof
For $\abs z\ge1$ the hypothesis gives $\abs{f(z)}\le1+\abs z^{-2}\le2$, so $f$ is bounded in a neighbourhood of $\infty$; a bounded isolated singularity of a meromorphic function is removable (Riemann's theorem), and the limit of $f$ at $\infty$ is $1$, since $\abs{f(z)-1}\le\abs z^{-2}\to0$.

:::

:::

::: {.pf-step #part-i-rational}
$f$ is rational.

::: pf-proof
$f$ is meromorphic on $\CC$ with finitely many poles, all in $\DD$, and by step [](#part-i-removable){.pf-ref} it has no pole at $\infty$; extended by $f(\infty)=1$ it is meromorphic on the Riemann sphere. Such a function is the quotient of two holomorphic functions on the sphere, and a holomorphic function on the sphere is a polynomial (it is entire, and its only possible singularity is a pole at $\infty$); so $f$ is a ratio of polynomials.
:::

:::

::: {.pf-step #log-derivative}
$\dfrac{f'(z)}{f(z)}=\displaystyle\sum_{i=1}^n\frac{m_i}{z-\alpha_i}$ away from the $\alpha_i$, and
$$
\frac{f'(z)}{f(z)}=\frac{\sum_im_i}{z}+\frac{\sum_im_i\alpha_i}{z^2}+O(z^{-3})\quad(z\to\infty).
$$

::: pf-proof
Near a zero or pole of order $m_i$, write $f(z)=(z-\alpha_i)^{m_i}h(z)$ with $h$ holomorphic and nonzero; then $f'/f=m_i/(z-\alpha_i)+h'/h$ with $h'/h$ holomorphic there. So $f'/f-\sum_im_i/(z-\alpha_i)$ is holomorphic on $\CC$ and vanishes at $\infty$, hence is identically zero. For the expansion, $1/(z-\alpha_i)=z^{-1}\sum_{k\ge0}(\alpha_i/z)^k=1/z+\alpha_i/z^2+O(z^{-3})$ for $\abs z>\max_i\abs{\alpha_i}$, and summing against $m_i$ gives the displayed series.

:::

:::

::: {.pf-step #vanishing}
$f'/f=O(z^{-3})$ as $z\to\infty$, so the coefficients of $z^{-1}$ and $z^{-2}$ in the expansion vanish.

::: pf-proof
By the hypothesis $f(z)=1+O(z^{-2})$ near $\infty$, so $f-1$ has a zero of order at least $2$ at $\infty$; differentiating the Laurent series term by term gives $f'(z)=O(z^{-3})$, and $1/f$ is holomorphic near $\infty$ with value $1$, so $f'/f=O(z^{-3})$. A series $\sum_{k\ge1}a_kz^{-k}$ that is $O(z^{-3})$ has $a_1=a_2=0$.

:::

:::

::: {.pf-step #part-ii}
$\displaystyle\sum_{i=1}^nm_i\alpha_i=0$.

::: pf-proof
Comparing the two descriptions of $f'/f$ in steps [](#log-derivative){.pf-ref} and [](#vanishing){.pf-ref}, the coefficient of $z^{-2}$ is $\sum_im_i\alpha_i$, and it is $0$. (The coefficient of $z^{-1}$, namely $\sum_im_i$, also vanishes, which says that $f$ has as many zeros as poles on the sphere, consistent with $f(\infty)=1\ne0$.)

:::

:::

:::
:::
