---
schema: qual/card@1
id: P-BKS19-5B
kind: problem
title: Coefficient bounds for analytic $f$ with $\abs{f(z)}<1/(1-\abs{z})$
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 Cauchy-estimate argument. The choice $r=n/(n+1)$ and the logarithmic proof of $(1+1/n)^n<e$ are correct.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the Cauchy coefficient estimate at radius $n/(n+1)$ and the strict exponential bound for every integer $n\ge1$.
---

::: {.problem}
If $f(z)$ is analytic in the open disc
$$
\DD=\{z:\abs{z}<1\},
$$
and
$$
\abs{f(z)}<\frac1{1-\abs{z}}\qquad(z\in\DD),
$$
show that
$$
\abs{\frac{f^{(n)}(0)}{n!}}\le (n+1)\left(1+\frac1n\right)^n<e(n+1).
$$
:::

::: {.solution}

Fix an integer $n\geq1$ and set
$$
r\coloneqq\frac{n}{n+1}.
$$

::: pf

::: {.pf-step #s1-1}

On the circle $\abs{z}=r$,
$$
\abs{f(z)}<n+1.
$$


::: pf-proof

The hypothesis gives
$$
\abs{f(z)}<\frac1{1-\abs{z}}
=
\frac1{1-r}
=n+1.
$$

:::

:::

::: {.pf-step #s1-2}

Cauchy's coefficient estimate gives
$$
\abs{\frac{f^{(n)}(0)}{n!}}
\leq
(n+1)\left(1+\frac1n\right)^n.
$$


::: pf-proof

Writing
$$
f(z)=\sum_{k=0}^\infty a_kz^k,
\qquad
a_n=\frac{f^{(n)}(0)}{n!},
$$
Cauchy's integral formula on $\abs{z}=r$ gives
$$
\abs{a_n}
\leq
\frac{\max_{\abs{z}=r}\abs{f(z)}}{r^n}.
$$
By step [](#s1-1){.pf-ref},
$$
\abs{a_n}
<
\frac{n+1}{r^n}
=
(n+1)\left(\frac{n+1}{n}\right)^n
=
(n+1)\left(1+\frac1n\right)^n.
$$
The asserted weak inequality follows a fortiori.

:::

:::

::: {.pf-step #s1-3}

For every integer $n\geq1$,
$$
\left(1+\frac1n\right)^n<e.
$$


::: pf-proof

For $x>0$, let
$$
h(x)=\log(1+x)-x.
$$
Then $h(0)=0$ and
$$
h'(x)=\frac1{1+x}-1=-\frac{x}{1+x}<0.
$$
Hence $h(x)<0$ for $x>0$. Taking $x=1/n$ gives
$$
\log\left(1+\frac1n\right)<\frac1n.
$$
Multiplying by $n$ and exponentiating yields the claim.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\abs{\frac{f^{(n)}(0)}{n!}}
\leq
(n+1)\left(1+\frac1n\right)^n
<
e(n+1)
}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required estimate.

:::

:::

:::
