---
schema: qual/card@1
id: P-APAS26E
kind: problem
title: A faithful state yields a faithful tracial state
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The stored solution named theorems instead of proving anything: its three justifications were
    "definition of a faithful state.", "GNS construction / finite-dimensional C*-algebra theory." and
    "Artin--Wedderburn theorem for finite-dimensional C*-algebras.", and one of its steps was wrong as
    written, claiming that a nilpotent with x^2 = 0 also has x*x = 0, which does not follow and is not
    what semisimplicity needs. It is replaced by an argument that uses only the faithful state and the
    finite dimension: the GNS inner product <a,b> = sigma(b*a), left multiplication as a *-representation
    on that finite-dimensional Hilbert space, injectivity of the representation because pi(x)1 = x, and
    the Hilbert-space trace normalized by dim A. The trace is positive, tracial because tr(TS) = tr(ST),
    and faithful because tr(pi(x)*pi(x)) is the sum of squares of the absolute values of the matrix
    entries of pi(x). Checked: the conjugation convention of the exam statement, the identity
    <pi(x)a,b> = <a,pi(x*)b> by associativity, and that sigma(z*) = conj(sigma(z)) follows from
    positivity. Not checked: no published solution of this examination problem was located or
    consulted, so the argument is the card's own.
---

::: {.problem}
Let $\mathcal{A}$ be an algebra which admits a faithful state $\sigma \colon \mathcal{A} \to \CC$.
Prove that $\mathcal{A}$ admits a faithful tracial state $\tau \colon \mathcal{A} \to \CC$.

Note: On this exam, an algebra is a finite-dimensional complex vector space equipped with an associative, bilinear, unital multiplication and an antilinear, antimultiplicative, involutive conjugation.
:::

::: {.solution}

The GNS form of the faithful state turns $\mathcal A$ into a $*$-algebra of operators on a finite-dimensional Hilbert space, and the Hilbert-space trace gives the tracial state. The argument is the card's own; nothing published was consulted for it.

::: pf

::: {.pf-step #inner-product}
The rule $\langle a,b\rangle=\sigma(b^{*}a)$ is an inner product on $\mathcal A$, and $\langle a,a\rangle>0$ for $a\ne0$.

::: pf-proof
$\sigma$ is complex linear, so $\langle\lambda a+\mu a',b\rangle=\sigma\big(b^{*}(\lambda a+\mu a')\big)=\lambda\sigma(b^{*}a)+\mu\sigma(b^{*}a')$: linear in the first argument. Using that $*$ is antilinear and antimultiplicative, $\langle a,\lambda b\rangle=\sigma\big((\lambda b)^{*}a\big)=\sigma\big(\bar{\lambda}b^{*}a\big)=\bar{\lambda}\sigma(b^{*}a)$: antilinear in the second. Conjugate symmetry is $\sigma(b^{*}a)=\overline{\sigma(a^{*}b)}$, which follows from positivity: for every $\lambda\in\CC$ one has $0\le\sigma\big((1+\lambda z)^{*}(1+\lambda z)\big)=1+\lambda\sigma(z)+\bar{\lambda}\sigma(z^{*})+\abs{\lambda}^{2}\sigma(z^{*}z)$; taking $\lambda$ real makes $\sigma(z)+\sigma(z^{*})$ real and taking $\lambda$ purely imaginary makes $i\big(\sigma(z)-\sigma(z^{*})\big)$ real, and the two together say $\sigma(z^{*})=\overline{\sigma(z)}$. Finally $\langle a,a\rangle=\sigma(a^{*}a)\ge0$, and it is $0$ only when $a=0$, which is faithfulness.
:::

:::

::: {.pf-step #left-multiplication}
For $x\in\mathcal A$ the map $\pi(x):\mathcal A\to\mathcal A$, $\pi(x)a=xa$, is linear, and $\langle\pi(x)a,b\rangle=\langle a,\pi(x^{*})b\rangle$ for all $a,b\in\mathcal A$.

::: pf-proof
Linearity is the distributivity of multiplication in $\mathcal A$. For the adjoint identity, $\langle\pi(x)a,b\rangle=\sigma\big(b^{*}(xa)\big)$ and $\langle a,\pi(x^{*})b\rangle=\sigma\big((x^{*}b)^{*}a\big)$; associativity makes the two arguments equal, because $b^{*}(xa)=(b^{*}x)a$ and $(x^{*}b)^{*}a=b^{*}xa$. So the two numbers coincide.
:::

:::

::: {.pf-step #star-representation}
$\pi$ is injective and satisfies $\pi(xy)=\pi(x)\pi(y)$, $\pi(1)=\mathrm{id}$ and $\pi(x^{*})=\pi(x)^{*}$.

::: pf-proof
$\pi(xy)a=(xy)a=x(ya)$, and $\pi(1)a=a$; the adjoint identity of step [](#left-multiplication){.pf-ref} says exactly that $\pi(x^{*})$ is the adjoint of $\pi(x)$. For injectivity, if $\pi(x)=0$ then $x=\pi(x)1=0$.
:::

:::

::: {.pf-step #trace-state}
With $N=\dim_{\CC}\mathcal A$ and $\mathrm{tr}$ the trace of an endomorphism of $\mathcal A$, the functional $\tau(x)=N^{-1}\mathrm{tr}\big(\pi(x)\big)$ satisfies $\tau(1)=1$, $\tau(xy)=\tau(yx)$ and $\tau(x^{*}x)\ge0$, with $\tau(x^{*}x)=0$ only for $x=0$.

::: pf-proof
$\pi(1)$ is the identity of an $N$-dimensional space, whose trace is $N$, so $\tau(1)=1$, and linearity is that of $\pi$ and of the trace. Since $\pi$ is multiplicative, $\pi(xy)=\pi(x)\pi(y)$, and the trace of a product of endomorphisms of a finite-dimensional space is symmetric: $\tau(xy)=\tau(yx)$. Finally $\pi(x^{*})\pi(x)=\pi(x)^{*}\pi(x)$, whose trace is the sum of the squares of the absolute values of the matrix entries of $\pi(x)$ in an orthonormal basis, so $\tau(x^{*}x)\ge0$, and it vanishes only when $\pi(x)=0$, that is, by injectivity, only when $x=0$.
:::

:::

::: {.pf-step #conclusion}
$\tau$ is a faithful tracial state on $\mathcal A$.

::: pf-proof
Steps [](#trace-state){.pf-ref} give a linear functional with $\tau(1)=1$, $\tau(xy)=\tau(yx)$ for all $x,y$ and $\tau(x^{*}x)>0$ for $x\ne0$; these are the defining properties of a faithful tracial state.
:::

:::

::: pf-qed
Steps [](#inner-product){.pf-ref} to [](#conclusion){.pf-ref} produce the faithful tracial state the problem asks for, using only the faithful state and the finite dimension.
:::

:::
:::
