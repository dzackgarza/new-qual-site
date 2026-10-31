---
schema: qual/card@1
id: P-TRIV-CA08
kind: problem
title: Laurent series of $1/((z+1)(z+2))$ on its annuli of convergence
classification:
  areas: [complex-analysis]
  topics:
  - Laurent Series
  - Annuli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the Laurent series of $f(z) = \frac{1}{(z + 1)(z + 2)}$ such that it converges in the regions

(a) $\abs{z} < 1$;

(b) $1 < \abs{z} < 2$;

(c) $\abs{z} > 2$;

(d) $0 < \abs{z + 1} < 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The partial-fraction decomposition is
$$
f(z)
=
\frac1{z+1}
-
\frac1{z+2}.
$$


::: pf-proof

One has
$$
\frac1{z+1}
-
\frac1{z+2}
=
\frac{(z+2)-(z+1)}{(z+1)(z+2)}
=
\frac1{(z+1)(z+2)}.
$$

:::

:::

::: {.pf-step #s1-2}

For $\abs{z}<1$,
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}(-1)^n z^n
$$
and
$$
\frac1{z+2}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}z^n.
$$


::: pf-proof

Use
$$
\frac1{1+z}
=
\sum_{n=0}^{\infty}(-z)^n,
$$
valid for $\abs{z}<1$, and
$$
\frac1{z+2}
=
\frac12\frac1{1+z/2}
=
\frac12
\sum_{n=0}^{\infty}
\left(-\frac z2\right)^n,
$$
valid for $\abs{z}<2$.

:::

:::

::: {.pf-step #s1-3}

Therefore, for $\abs{z}<1$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n
\left(
1-\frac1{2^{n+1}}
\right)z^n.
}
$$


::: pf-proof

Subtract the two series in step [](#s1-2){.pf-ref} using step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

For $1<\abs{z}<2$,
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}
(-1)^n z^{-n-1},
$$
while
$$
\frac1{z+2}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}z^n.
$$


::: pf-proof

For the first term,
$$
\frac1{z+1}
=
\frac1z\frac1{1+1/z}
=
\frac1z
\sum_{n=0}^{\infty}
\left(-\frac1z\right)^n,
$$
which converges when $\abs{z}>1$.

The second expansion is the one from step [](#s1-2){.pf-ref} and converges when $\abs{z}<2$.
Thus both are valid simultaneously on $1<\abs{z}<2$.

:::

:::

::: {.pf-step #s1-5}

Hence, for $1<\abs{z}<2$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n z^{-n-1}
-
\sum_{n=0}^{\infty}
\frac{(-1)^n}{2^{n+1}}z^n.
}
$$


::: pf-proof

Substitute step [](#s1-4){.pf-ref} into the partial fractions from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

For $\abs{z}>2$,
$$
\frac1{z+1}
=
\sum_{n=0}^{\infty}
(-1)^n z^{-n-1},
$$
and
$$
\frac1{z+2}
=
\sum_{n=0}^{\infty}
(-2)^n z^{-n-1}.
$$


::: pf-proof

The first series is from step [](#s1-4){.pf-ref}. For the second,
$$
\frac1{z+2}
=
\frac1z\frac1{1+2/z}
=
\frac1z
\sum_{n=0}^{\infty}
\left(-\frac2z\right)^n,
$$
which converges for $\abs{z}>2$.

:::

:::

::: {.pf-step #s1-7}

Therefore, for $\abs{z}>2$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
\bigl((-1)^n-(-2)^n\bigr)
z^{-n-1}.
}
$$


::: pf-proof

Subtract the two negative-power series in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For part (d), set
$$
w=z+1.
$$
Then
$$
f(z)
=
\frac1{w(w+1)}.
$$


::: pf-proof

Since
$$
z+1=w
\qquad\text{and}\qquad
z+2=w+1,
$$
the displayed identity follows.

:::

:::

::: {.pf-step #s1-9}

For $0<\abs{z+1}<1$,
$$
\boxed{
f(z)
=
\sum_{n=0}^{\infty}
(-1)^n(z+1)^{n-1}.
}
$$


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
f(z)
=
\frac1w\frac1{1+w}.
$$
For $\abs{w}<1$,
$$
\frac1{1+w}
=
\sum_{n=0}^{\infty}(-1)^n w^n.
$$
Multiplying by $w^{-1}$ gives the stated Laurent series. The point $w=0$
must be excluded because it is a pole.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref}, [](#s1-5){.pf-ref}, and [](#s1-7){.pf-ref}, and [](#s1-9){.pf-ref} give the requested Laurent series on all
four regions.

:::

:::

:::
