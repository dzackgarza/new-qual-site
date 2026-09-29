---
schema: qual/card@1
id: P-BERK86S-05
kind: problem
title: The identity is the only field automorphism of $\mathbb R$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Showed that every field automorphism fixes Q and preserves positivity,
    hence preserves the usual order on R. Density of Q then forces every
    real number to be fixed.
---

::: {.problem}
Prove that the identity is the only field automorphism of $\mathbb R$.
:::

::: {.solution}
Let
$$
\sigma:\RR\to\RR
$$
be a field automorphism.

::: pf

::: {.pf-step #fixes-rationals}
The automorphism $\sigma$ fixes every rational number.

::: pf-proof
A field automorphism preserves $0$ and $1$. Hence, for every positive
integer $n$,
$$
\sigma(n)
=
\sigma(\underbrace{1+\cdots+1}_{n\text{ terms}})
=n.
$$
It follows that $\sigma(-n)=-n$. If $m\in\ZZ$ and $n\in\ZZ$ is nonzero,
then
$$
\sigma\left(\frac{m}{n}\right)
=
\frac{\sigma(m)}{\sigma(n)}
=
\frac{m}{n}.
$$
Thus $\sigma(q)=q$ for every $q\in\QQ$.
:::

:::

::: {.pf-step #preserves-positivity}
If $x>0$, then
$$
\sigma(x)>0.
$$

::: pf-proof
Every positive real number is a nonzero square:
$$
x=y^2
$$
for some $y\neq0$. Since $\sigma$ is injective,
$$
\sigma(y)\neq0.
$$
Therefore
$$
\sigma(x)
=
\sigma(y)^2
>0.
$$
:::

:::

::: {.pf-step #preserves-order}
The automorphism $\sigma$ preserves the usual order on $\RR$:
$$
x<y
\quad\Longrightarrow\quad
\sigma(x)<\sigma(y).
$$

::: pf-proof
If $x<y$, then $y-x>0$. By step [](#preserves-positivity){.pf-ref},
$$
\sigma(y)-\sigma(x)
=
\sigma(y-x)
>0.
$$
Hence $\sigma(x)<\sigma(y)$.
:::

:::

::: {.pf-step #fixes-every-real}
Every $x\in\RR$ satisfies
$$
\sigma(x)=x.
$$

::: pf-proof
Suppose first that
$$
x<\sigma(x).
$$
By density of $\QQ$ in $\RR$, choose $q\in\QQ$ with
$$
x<q<\sigma(x).
$$
Step [](#preserves-order){.pf-ref} applied to $x<q$, together with step [](#fixes-rationals){.pf-ref}, gives
$$
\sigma(x)<\sigma(q)=q,
$$
contradicting $q<\sigma(x)$.

If instead
$$
\sigma(x)<x,
$$
choose $q\in\QQ$ with
$$
\sigma(x)<q<x.
$$
Step [](#preserves-order){.pf-ref} applied to $q<x$ gives
$$
q=\sigma(q)<\sigma(x),
$$
contradicting $\sigma(x)<q$.

Both strict inequalities are impossible, so $\sigma(x)=x$.
:::

:::

::: {.pf-step #identity-boxed}
Therefore
$$
\boxed{\sigma=\operatorname{id}_{\RR}}.
$$

::: pf-proof
Step [](#fixes-every-real){.pf-ref} shows that $\sigma$ fixes every real number.
:::

:::

::: pf-qed
Since $\sigma$ was an arbitrary field automorphism, step [](#identity-boxed){.pf-ref} proves that
the identity is the only one.
:::

:::
:::
