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

<1>1. The element $\alpha$ is a root of
$$
h(x)
=
(x^2-2)^2-2
=
x^4-4x^2+2
\in\QQ[x].
$$

::: {.proof}
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

<1>2. The element
$$
\sqrt2=\alpha^2-2
$$
belongs to $K$.

::: {.proof}
The expression $\alpha^2-2$ is a polynomial in $\alpha$ with rational
coefficients, so it lies in $\QQ(\alpha)=K$. Step <1>1 identifies it with
$\sqrt2$.
:::

<1>3. The other positive square root
$$
\beta
\coloneqq
\sqrt{2-\sqrt2}
$$
also belongs to $K$.

::: {.proof}
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

<1>4. The four roots of $h(x)$ are exactly
$$
\pm\alpha,
\qquad
\pm\beta.
$$

::: {.proof}
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

<1>5. The polynomial $h(x)$ splits completely over $K$.

::: {.proof}
By definition $\alpha\in K$, so also $-\alpha\in K$. Step <1>3 gives
$\beta\in K$, hence also $-\beta\in K$. Step <1>4 lists all roots of $h$.
Therefore
$$
h(x)
=
(x-\alpha)(x+\alpha)(x-\beta)(x+\beta)
$$
in $K[x]$.
:::

<1>6. The field $K$ is the splitting field of $h(x)$ over $\QQ$.

::: {.proof}
Since $\alpha$ is a root of $h$, every splitting field of $h$ contains
$$
\QQ(\alpha)=K.
$$
Conversely, step <1>5 shows that $K$ already contains every root of $h$.
Hence $K$ itself is the splitting field.
:::

<1>7. Therefore
$$
\boxed{
\QQ(\sqrt{2+\sqrt2})/\QQ
\text{ is normal}.
}
$$

::: {.proof}
A splitting field of a polynomial over the base field is a normal extension.
Step <1>6 identifies $K$ as the splitting field of
$$
x^4-4x^2+2
$$
over $\QQ$. Hence $K/\QQ$ is normal.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 proves that the statement in the problem is true.
:::
:::
