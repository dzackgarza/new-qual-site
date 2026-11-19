---
schema: qual/card@1
id: E-SS6.EX-2
kind: problem
title: $\prod_n\frac{n(n+a+b)}{(n+a)(n+b)}=\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+1)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Infinite Products
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the partial product in Gamma functions, its limit, the two
    Euler products, the sine product, and the reflection formula. No retained solution set covers this exercise
    (the collection retains the textbook, not a solutions manual), so the argument is the card's own; the
    partial product and both limits were recomputed for this pass.
---

::: {.exercise}
Prove that

$$
\prod_ {n = 1} ^ {\infty} \frac {n (n + a + b)}{(n + a) (n + b)} = \frac {\Gamma (a + 1) \Gamma (b + 1)}{\Gamma (a + b + 1)}
$$

whenever $a$ and $b$ are positive.
Using the product formula for $\sin \pi s$, give another proof that $\Gamma(s)\Gamma(1 - s) = \pi/\sin \pi s$.
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Two results are used: Euler's product for the reciprocal Gamma function and Euler's product for the sine.

::: pf

::: {.pf-step #partial}
For $N\ge1$ and $a,b>0$,
$$
P_{N}=\prod_{n=1}^{N}\frac{n(n+a+b)}{(n+a)(n+b)}
=\frac{\Gamma(N+1)\Gamma(N+a+b+1)}{\Gamma(N+a+1)\Gamma(N+b+1)}\cdot\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+1)} .
$$

::: pf-proof
From $\Gamma(z+1)=z\Gamma(z)$ one gets $\prod_{n=1}^{N}(n+c)=\frac{\Gamma(N+c+1)}{\Gamma(c+1)}$ for any $c>0$, by induction on $N$: the step multiplies by $(N+1+c)$ and uses $\Gamma(N+c+2)=(N+c+1)\Gamma(N+c+1)$. Applying this with $c=0$ (so $\Gamma(1)=1$), $c=a$, $c=b$ and $c=a+b$ and substituting in $P_{N}$ gives the displayed expression.
:::

:::

::: {.pf-step #limit}
The factor $\dfrac{\Gamma(N+1)\Gamma(N+a+b+1)}{\Gamma(N+a+1)\Gamma(N+b+1)}$ tends to $1$ as $N\to\infty$.

::: pf-proof
By the standard asymptotic $\Gamma(N+c)/\Gamma(N+d)\sim N^{c-d}$,
$$
\frac{\Gamma(N+1)}{\Gamma(N+a+1)}\sim N^{-a},\qquad \frac{\Gamma(N+a+b+1)}{\Gamma(N+b+1)}\sim N^{a},
$$
using $c=1,d=a+1$ for the first and $c=a+b+1,d=b+1$ for the second. The product of the two factors therefore behaves like $N^{-a}\cdot N^{a}=N^{0}=1$, and each factor is asymptotic to a power of $N$, so the product tends to $1$.
:::

:::

::: {.pf-step #product}
$\displaystyle\prod_{n=1}^{\infty}\frac{n(n+a+b)}{(n+a)(n+b)}=\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+1)}$.

::: pf-proof
The partial products $P_{N}$ converge by steps [](#partial){.pf-ref} and [](#limit){.pf-ref} to the constant $\Gamma(a+1)\Gamma(b+1)/\Gamma(a+b+1)$, so the infinite product converges to that value, for positive $a,b$ as required.
:::

:::

::: {.pf-step #euler}
$\dfrac{1}{\Gamma(s)}=se^{\gamma s}\prod_{n\ge1}\bigl(1+\tfrac{s}{n}\bigr)e^{-s/n}$ and $\dfrac{1}{\Gamma(-s)}=-se^{-\gamma s}\prod_{n\ge1}\bigl(1-\tfrac{s}{n}\bigr)e^{s/n}$.

::: pf-proof
The first is Euler's product for $1/\Gamma$. The second is the same identity with $s$ replaced by $-s$: then $1+\frac{-s}{n}=1-\frac{s}{n}$, $e^{\gamma(-s)}=e^{-\gamma s}$ and $e^{-(-s)/n}=e^{s/n}$, and the prefactor $s$ becomes $-s$.
:::

:::

::: {.pf-step #multiply}
$\dfrac{1}{\Gamma(s)\Gamma(-s)}=-s^{2}\displaystyle\prod_{n\ge1}\Bigl(1-\frac{s^{2}}{n^{2}}\Bigr)$.

::: pf-proof
Multiply the two identities of step [](#euler){.pf-ref}: the prefactors give $s\cdot(-s)=-s^{2}$, the exponentials give $e^{\gamma s}e^{-\gamma s}=1$, and each pair of factors gives $\bigl(1+\frac{s}{n}\bigr)\bigl(1-\frac{s}{n}\bigr)e^{-s/n}e^{s/n}=1-\frac{s^{2}}{n^{2}}$. The resulting product converges locally uniformly in $s$, so multiplying term by term is legitimate.
:::

:::

::: {.pf-step #reflection}
$\Gamma(s)\Gamma(1-s)=\dfrac{\pi}{\sin\pi s}$.

::: pf-proof
The sine product gives $\frac{\sin\pi s}{\pi s}=\prod_{n\ge1}\bigl(1-\frac{s^{2}}{n^{2}}\bigr)$, so step [](#multiply){.pf-ref} reads
$$
\frac{1}{\Gamma(s)\Gamma(-s)}=-s^{2}\cdot\frac{\sin\pi s}{\pi s}=-\frac{s\sin\pi s}{\pi},
$$
that is $\Gamma(s)\Gamma(-s)=-\frac{\pi}{s\sin\pi s}$. Multiplying by $-s$ and using $\Gamma(1-s)=(-s)\Gamma(-s)$, the functional equation with $z=-s$, gives
$$
\Gamma(s)\Gamma(1-s)=-s\,\Gamma(s)\Gamma(-s)=-s\Bigl(-\frac{\pi}{s\sin\pi s}\Bigr)=\frac{\pi}{\sin\pi s},
$$
first for $s$ away from the integers, then as an identity of meromorphic functions since both sides are meromorphic and agree on a set with an accumulation point.
:::

:::

:::
:::
