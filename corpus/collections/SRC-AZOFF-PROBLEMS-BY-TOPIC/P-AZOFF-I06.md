---
schema: qual/card@1
id: P-AZOFF-I06
kind: problem
title: Proper self-maps of the disk with a single zero are $\lambda z^k$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF prints f:D→D. The extracted card had lost the arrow
    between the two copies of D; the statement now restores it.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Dividing by z^k removes the unique zero and gives a zero-free analytic
    function g. The boundary-modulus hypothesis implies |g(z)| tends to one
    as |z| tends to one. Maximum-modulus estimates for g and 1/g on circles
    of radius r then force |g|=1 throughout the disk, hence g is a
    unimodular constant.
---

::: {.problem}
[January 2008, Problem $\# 5 \mathrm { b } ]$ Suppose $f : \mathbb { D } \to \mathbb { D }$ is analytic, has a zero of order $k$ at the origin, has no other zeros, and satisfies $\lim_{\abs{z} \to 1} \abs{f(z)} = 1$. Give, with proof, a formula for $f(z)$.
:::

::: {.solution}
Define
$$
g(z)
=
\begin{cases}
\dfrac{f(z)}{z^k},&z\neq0,\\
\dfrac{f^{(k)}(0)}{k!},&z=0.
\end{cases}
$$

::: pf

::: {.pf-step #s1}

The function $g$ is analytic and zero-free on $\DD$.

::: pf-proof

Because $f$ has a zero of order exactly $k$ at the origin, there is an
analytic function $g$ near $0$ with
$$
f(z)=z^kg(z)
$$
and $g(0)\neq0$. This is exactly the extension displayed above. Since $f$
has no zeros away from the origin, $g$ has no zeros anywhere in $\DD$.

:::

:::

::: {.pf-step #s2}

One has
$$
\lim_{\abs{z}\to1}\abs{g(z)}=1.
$$

::: pf-proof

For $z\neq0$,
$$
\abs{g(z)}
=
\frac{\abs{f(z)}}{\abs{z}^k}.
$$
As $\abs{z}\to1$, the numerator tends to $1$ by hypothesis and the
denominator tends to $1$. Hence the quotient tends to $1$.

:::

:::

::: {.pf-step #s3}

For every $z_0\in\DD$,
$$
\abs{g(z_0)}\leq1.
$$

::: pf-proof

Fix $z_0\in\DD$ and choose $r$ with
$$
\abs{z_0}<r<1.
$$
By the maximum modulus principle applied to the disk $\abs{z}\leq r$,
$$
\abs{g(z_0)}
\leq
\max_{\abs{z}=r}\abs{g(z)}.
$$
Step [](#s2){.pf-ref} implies
$$
\max_{\abs{z}=r}\abs{g(z)}
\longrightarrow1
$$
as $r\uparrow1$. Letting $r\uparrow1$ gives the claimed inequality.

:::

:::

::: {.pf-step #s4}

For every $z_0\in\DD$,
$$
\abs{g(z_0)}\geq1.
$$

::: pf-proof

By step [](#s1){.pf-ref}, the function $1/g$ is analytic on $\DD$. Step [](#s2){.pf-ref} gives
$$
\lim_{\abs{z}\to1}\abs{1/g(z)}=1.
$$
Applying step [](#s3){.pf-ref} to $1/g$ yields
$$
\abs{1/g(z_0)}\leq1,
$$
equivalently $\abs{g(z_0)}\geq1$.

:::

:::

::: {.pf-step #s5}

The function $g$ is constant with unimodular value.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give
$$
\abs{g(z)}=1
$$
for every $z\in\DD$. By the open mapping theorem, a nonconstant analytic
function has open image, whereas the unit circle is not open. Hence $g$ is
constant. Write
$$
g\equiv\lambda,
\qquad
\abs{\lambda}=1.
$$

:::

:::

::: {.pf-step #s6}

The required formula is
$$
\boxed{
f(z)=\lambda z^k,
\qquad
\abs{\lambda}=1.
}
$$

::: pf-proof

By the definition of $g$,
$$
f(z)=z^kg(z).
$$
Substitute the constant value from step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the requested formula.

:::

:::

:::
