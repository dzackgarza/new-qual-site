---
schema: qual/card@1
id: P-CHAVAN-CA-7-5
kind: problem
title: The complex plane minus a finite nonempty set is not simply connected
classification: {areas: [complex-analysis], topics: [Simply Connected Domains]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
---

::: {.problem}
Show that the complex plane minus a finite nonempty set is not simply connected.
:::

::: {.solution}

Let
$$
F=\{a_1,\ldots,a_n\}\subset\CC,
\qquad n\geq1,
$$
with the $a_j$ distinct, and put $\Omega=\CC\setminus F$.

::: pf

::: {.pf-step #s1-1}

There is an $r>0$ such that the circle
$$
\gamma(t)=a_1+re^{it},
\qquad 0\leq t\leq2\pi,
$$
is contained in $\Omega$.


::: pf-proof

If $n=1$, any $r>0$ works. If $n>1$, choose
$$
0<r<\min_{2\leq j\leq n}\abs{a_j-a_1}.
$$
Then no point of the circle is one of the deleted points.

:::

:::

::: {.pf-step #s1-2}

The function
$$
h(z)=\frac1{z-a_1}
$$
is holomorphic on $\Omega$, and
$$
\int_\gamma h(z)\,dz=2\pi i.
$$


::: pf-proof

The only pole of $h$ is at $a_1\notin\Omega$. Along the parametrization in
step [](#s1-1){.pf-ref},
$$
h(\gamma(t))=\frac{e^{-it}}r,
\qquad
\gamma'(t)=ire^{it}.
$$
Therefore
$$
\int_\gamma h(z)\,dz
=\int_0^{2\pi}\frac{e^{-it}}r\,ire^{it}\,dt
=\int_0^{2\pi}i\,dt
=2\pi i.
$$

:::

:::

::: {.pf-step #s1-3}

If $\Omega$ were simply connected, then
$$
\int_\gamma h(z)\,dz=0.
$$


::: pf-proof

Under the homotopy definition of simple connectivity used in the source, the
closed curve $\gamma$ would be homotopic in $\Omega$ to the constant curve at
$\gamma(0)$. The homotopy version of Cauchy's theorem would then make the
integral of $h$ along $\gamma$ equal to its integral along that constant curve,
which is zero.

:::

:::

::: {.pf-step #s1-4}

The set $\Omega=\CC\setminus F$ is not simply connected.


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} would give the contradiction $2\pi i=0$ if $\Omega$ were
simply connected.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
