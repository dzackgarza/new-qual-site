---
schema: qual/card@1
id: P-BERK77S-06
kind: problem
title: A complete elliptic integral is increasing in its parameter
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Compared the integrands directly for k_1<k_2. Their denominators are
    positive on the whole interval and the k_2 integrand is strictly larger
    except at x=pi/2, so integration gives strict monotonicity.
---

::: {.problem}
Show that
\[
F(k)=\int_0^{\pi/2}\frac{dx}{\sqrt{1-k\cos^2x}},
\qquad 0\le k<1,
\]
is an increasing function of $k$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $k\in[0,1)$, the integrand
$$
x\longmapsto\frac1{\sqrt{1-k\cos^2x}}
$$
is continuous on $[0,\pi/2]$.

::: pf-proof

For every $x\in[0,\pi/2]$,
$$
1-k\cos^2x
\geq
1-k
>
0.
$$
Thus the denominator never vanishes, and the displayed function is
continuous.

:::

:::

::: {.pf-step #s2}

If
$$
0\leq k_1<k_2<1,
$$
then for every $x\in[0,\pi/2)$,
$$
\frac1{\sqrt{1-k_1\cos^2x}}
<
\frac1{\sqrt{1-k_2\cos^2x}}.
$$

::: pf-proof

For $x<\pi/2$, one has $\cos^2x>0$. Hence
$$
1-k_2\cos^2x
<
1-k_1\cos^2x.
$$
Both quantities are positive by step [](#s1){.pf-ref}. Taking positive square roots
and then reciprocals reverses the inequality, giving the claim.

:::

:::

::: {.pf-step #s3}

If $0\leq k_1<k_2<1$, then
$$
F(k_1)<F(k_2).
$$

::: pf-proof

By step [](#s2){.pf-ref}, the $k_2$ integrand is strictly larger than the $k_1$
integrand throughout the interval $[0,\pi/2)$. Both are continuous by step
[](#s1){.pf-ref}. Therefore their difference is a nonnegative continuous function that
is positive on a nonempty interval, so its integral is positive:
$$
F(k_2)-F(k_1)
=
\int_0^{\pi/2}
\left(
\frac1{\sqrt{1-k_2\cos^2x}}
-
\frac1{\sqrt{1-k_1\cos^2x}}
\right)\,dx
>
0.
$$

:::

:::

::: {.pf-step #s4}

The function $F$ is strictly increasing on $[0,1)$.

::: pf-proof

Step [](#s3){.pf-ref} applies to every pair $k_1<k_2$ in the stated interval.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the required monotonicity.

:::

:::

:::
