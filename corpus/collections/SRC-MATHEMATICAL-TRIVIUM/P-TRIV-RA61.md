---
schema: qual/card@1
id: P-TRIV-RA61
kind: problem
title: $\int_0^\pi\log(1-2a\cos x+a^2)\,dx=0$ for $\abs{ a}<1$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 61, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that $\int _ { 0 } ^ { \pi } \log ( 1 - 2 a \cos x + a ^ { 2 } ) d x = 0 { \mathrm { ~ f o r ~ } } \abs{ a } < 1$
:::

::: {.solution}

Assume $a\in\RR$ and $\abs{a}<1$.

::: pf

::: {.pf-step #s1-1}

For every real $x$,
$$
1-2a\cos x+a^2
=
(1-ae^{ix})(1-ae^{-ix}).
$$


::: pf-proof

Expand the right-hand side:
$$
1-a(e^{ix}+e^{-ix})+a^2
=
1-2a\cos x+a^2.
$$

:::

:::

::: {.pf-step #s1-2}

Since $\abs{a}<1$, one has
$$
\log(1-ae^{ix})
=
-\sum_{n=1}^{\infty}
\frac{a^n e^{inx}}n,
$$
and similarly
$$
\log(1-ae^{-ix})
=
-\sum_{n=1}^{\infty}
\frac{a^n e^{-inx}}n.
$$


::: pf-proof

The power series
$$
\log(1-z)
=
-\sum_{n=1}^{\infty}\frac{z^n}{n}
$$
converges absolutely for $\abs{z}<1$. Substitute $z=ae^{\pm ix}$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\log(1-2a\cos x+a^2)
=
-2
\sum_{n=1}^{\infty}
\frac{a^n}{n}
\cos(nx).
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the positive real number
$$
1-2a\cos x+a^2
=
\abs{1-ae^{ix}}^2
$$
is the product of the two conjugate factors. Adding the conjugate logarithm
series from step [](#s1-2){.pf-ref} gives
$$
-\sum_{n=1}^{\infty}
\frac{a^n}{n}
(e^{inx}+e^{-inx}),
$$
which is the displayed cosine series.

:::

:::

::: {.pf-step #s1-4}

The series in step [](#s1-3){.pf-ref} converges uniformly in $x\in[0,\pi]$.


::: pf-proof

For every $x$,
$$
\abs{
\frac{a^n}{n}\cos(nx)
}
\leq
\frac{\abs{a}^n}{n}.
$$
The numerical series
$$
\sum_{n=1}^{\infty}\frac{\abs{a}^n}{n}
$$
converges, so the Weierstrass $M$-test applies.

:::

:::

::: {.pf-step #s1-5}

Hence termwise integration gives
$$
\int_0^\pi
\log(1-2a\cos x+a^2)
\,dx
=
-2
\sum_{n=1}^{\infty}
\frac{a^n}{n}
\int_0^\pi\cos(nx)\,dx.
$$


::: pf-proof

Uniform convergence from step [](#s1-4){.pf-ref} justifies exchanging the sum and integral.

:::

:::

::: {.pf-step #s1-6}

For every integer $n\geq1$,
$$
\int_0^\pi\cos(nx)\,dx=0.
$$


::: pf-proof

One has
$$
\int_0^\pi\cos(nx)\,dx
=
\left[
\frac{\sin(nx)}n
\right]_0^\pi
=0.
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\int_0^\pi
\log(1-2a\cos x+a^2)
\,dx
=0.
}
$$


::: pf-proof

Every term on the right-hand side of step [](#s1-5){.pf-ref} vanishes by step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required identity.

:::

:::

:::
