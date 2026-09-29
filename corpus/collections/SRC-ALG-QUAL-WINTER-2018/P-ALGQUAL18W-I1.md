---
schema: qual/card@1
id: P-ALGQUAL18W-I1
kind: problem
title: Normality of $\mathbb Q(\sqrt{2+\sqrt2})/\mathbb Q$
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, Problem 1 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Independently derived the quartic x^4-4x^2+2, constructed the missing
    conjugate sqrt(2-sqrt2) inside Q(alpha), and then compared with the
    recorded source solution. Both show that Q(alpha) is the splitting field.
---

::: {.problem}
True or false?
Justify your answer with a proof or counterexample:
\[
\mathbb Q\!\left(\sqrt{2+\sqrt2}\right)/\mathbb Q
\]
is a normal extension.
:::

::: {.solution}
The statement is true. Put
$$
\alpha=\sqrt{2+\sqrt2},
\qquad
K=\QQ(\alpha).
$$

::: pf

::: {.pf-step #s1}

The element $\alpha$ is a root of
$$
h(x)
=
(x^2-2)^2-2
=
x^4-4x^2+2
\in\QQ[x].
$$

::: pf-proof

By definition,
$$
\alpha^2=2+\sqrt2.
$$
Hence
$$
\alpha^2-2=\sqrt2,
$$
and therefore
$$
(\alpha^2-2)^2=2.
$$
Thus
$$
h(\alpha)=0.
$$

:::

:::

::: pf-step

The element
$$
\sqrt2=\alpha^2-2
$$
belongs to $K$.

::: pf-proof

The expression $\alpha^2-2$ is a polynomial in $\alpha$ with rational
coefficients, so it lies in $\QQ(\alpha)=K$. Step [](#s1){.pf-ref} identifies it with
$\sqrt2$.

:::

:::

::: {.pf-step #s3}

The other positive square root
$$
\beta
\coloneqq
\sqrt{2-\sqrt2}
$$
also belongs to $K$.

::: pf-proof

Define
$$
\gamma
=
\frac{\alpha^2-2}{\alpha}
\in K.
$$
Since
$$
\alpha^2-2=\sqrt2,
$$
one has
$$
\gamma^2
=
\frac{2}{\alpha^2}
=
\frac{2}{2+\sqrt2}
=
2-\sqrt2.
$$
Thus
$$
\gamma=\pm\beta.
$$
Since $K$ is closed under negation and $\gamma\in K$, it follows that
$$
\beta=\sqrt{2-\sqrt2}\in K.
$$

:::

:::

::: {.pf-step #s4}

The four roots of $h(x)$ are exactly
$$
\pm\alpha,
\qquad
\pm\beta.
$$

::: pf-proof

The equation
$$
h(x)=0
$$
is
$$
(x^2-2)^2=2.
$$
Hence
$$
x^2-2=\pm\sqrt2,
$$
so
$$
x^2=2+\sqrt2
\quad\text{or}\quad
x^2=2-\sqrt2.
$$
The corresponding roots are precisely
$$
\pm\sqrt{2+\sqrt2}=\pm\alpha
$$
and
$$
\pm\sqrt{2-\sqrt2}=\pm\beta.
$$

:::

:::

::: {.pf-step #s5}

The polynomial $h(x)$ splits completely over $K$.

::: pf-proof

By definition $\alpha\in K$, so also $-\alpha\in K$. Step [](#s3){.pf-ref} gives
$\beta\in K$, hence also $-\beta\in K$. Step [](#s4){.pf-ref} lists all roots of $h$.
Therefore
$$
h(x)
=
(x-\alpha)(x+\alpha)(x-\beta)(x+\beta)
$$
in $K[x]$.

:::

:::

::: {.pf-step #s6}

The field $K$ is the splitting field of $h(x)$ over $\QQ$.

::: pf-proof

Since $\alpha$ is a root of $h$, every splitting field of $h$ contains
$$
\QQ(\alpha)=K.
$$
Conversely, step [](#s5){.pf-ref} shows that $K$ already contains every root of $h$.
Hence $K$ itself is the splitting field.

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
\QQ(\sqrt{2+\sqrt2})/\QQ
\text{ is normal}.
}
$$

::: pf-proof

A splitting field of a polynomial over the base field is a normal extension.
Step [](#s6){.pf-ref} identifies $K$ as the splitting field of
$$
x^4-4x^2+2
$$
over $\QQ$. Hence $K/\QQ$ is normal.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} proves that the statement in the problem is true.

:::

:::

:::
