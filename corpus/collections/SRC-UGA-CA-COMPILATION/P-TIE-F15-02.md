---
schema: qual/card@1
id: P-TIE-F15-02
kind: problem
title: Blaschke factors are involutive automorphisms of the disk
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 2.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the LaTeX and restored the label (i) that the source prints as (c) in part (b), against Fall 2015, question 2, pages 8-9 of Questions_from_Tie.pdf.
---

::: {.problem}
(a) Let $z, w$ be complex numbers, such that $\bar{z}w \ne 1$. Prove that
$$
\abs{\frac{w - z}{1 - \bar{w}z}} < 1 \quad \text{if } \abs{z} < 1 \text{ and } \abs{w} < 1,
$$
and also that
$$
\abs{\frac{w - z}{1 - \bar{w}z}} = 1 \quad \text{if } \abs{z} = 1 \text{ or } \abs{w} = 1.
$$

(b) Prove that for fixed $w$ in the unit disk $\DD$, the mapping
$$
F \colon z \mapsto \frac{w - z}{1 - \bar{w}z}
$$
satisfies the following conditions:

(i) $F$ maps $\DD$ to itself and is holomorphic.

(ii) $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and $F(w) = 0$.

(iii) $\abs{F(z)} = 1$ if $\abs{z} = 1$.

(iv) $F \colon \DD \to \DD$ is bijective.

Hint: Calculate $F \circ F$.
:::

::: {.remark}
The source labels the first condition of part (b) "(c)"; it is condition (i) of the list (i)–(iv).
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For all $z,w\in\CC$,
$$
\abs{1-\overline wz}^2-\abs{w-z}^2
=
(1-\abs{w}^2)(1-\abs{z}^2).
$$


::: pf-proof

Expanding both squared moduli gives
$$
\begin{aligned}
\abs{1-\overline wz}^2
&=
(1-\overline wz)(1-w\overline z)\\
&=
1-\overline wz-w\overline z+\abs{w}^2\abs{z}^2,
\end{aligned}
$$
whereas
$$
\begin{aligned}
\abs{w-z}^2
&=
(w-z)(\overline w-\overline z)\\
&=
\abs{w}^2-w\overline z-\overline wz+\abs{z}^2.
\end{aligned}
$$
Subtracting yields
$$
1-\abs{w}^2-\abs{z}^2+\abs{w}^2\abs{z}^2
=(1-\abs{w}^2)(1-\abs{z}^2).
$$

:::

:::

::: {.pf-step #s1-2}

If $\abs{z}<1$ and $\abs{w}<1$, then
$$
\boxed{
\abs{\frac{w-z}{1-\overline wz}}<1.
}
$$


::: pf-proof

Both factors on the right-hand side of step [](#s1-1){.pf-ref} are positive, so
$$
\abs{1-\overline wz}^2
>
\abs{w-z}^2.
$$
Also $1-\overline wz\ne0$ because
$$
\abs{\overline wz}<1.
$$
Dividing by $\abs{1-\overline wz}^2$ and taking square roots gives the result.

:::

:::

::: {.pf-step #s1-3}

If either $\abs{z}=1$ or $\abs{w}=1$, and $\overline zw\ne1$, then
$$
\boxed{
\abs{\frac{w-z}{1-\overline wz}}=1.
}
$$


::: pf-proof

If either $\abs{z}=1$ or $\abs{w}=1$, the right-hand side of step [](#s1-1){.pf-ref} is $0$. Hence
$$
\abs{1-\overline wz}
=
\abs{w-z}.
$$
The hypothesis $\overline zw\ne1$ is equivalent, after complex conjugation, to $\overline wz\ne1$, so the denominator is nonzero. Division gives the asserted modulus.

:::

:::

::: {.pf-step #s1-4}

Fix $w\in\DD$ and define
$$
F(z)
\coloneqq
\frac{w-z}{1-\overline wz}.
$$
Then $F$ is holomorphic on $\DD$ and maps $\DD$ into itself.


::: pf-proof

For $z\in\DD$,
$$
\abs{\overline wz}
<
1,
$$
so the denominator never vanishes there. Thus $F$ is holomorphic on $\DD$. Step [](#s1-2){.pf-ref} gives
$$
\abs{F(z)}<1
$$
for every $z\in\DD$, so $F(\DD)\subset\DD$.

:::

:::

::: {.pf-step #s1-5}

The map $F$ interchanges $0$ and $w$:
$$
F(0)=w,
\qquad
F(w)=0.
$$


::: pf-proof

Direct substitution gives
$$
F(0)=\frac{w}{1}=w
$$
and
$$
F(w)
=
\frac{w-w}{1-\abs{w}^2}
=0.
$$
The denominator in the second expression is nonzero because $\abs{w}<1$.

:::

:::

::: {.pf-step #s1-6}

If $\abs{z}=1$, then
$$
\abs{F(z)}=1.
$$


::: pf-proof

Since $\abs{w}<1$, one has $\overline zw\ne1$ when $\abs{z}=1$. Step [](#s1-3){.pf-ref} therefore applies and gives the claim.

:::

:::

::: {.pf-step #s1-7}

The map $F$ is an involution:
$$
F(F(z))=z
$$
for every $z\in\DD$.


::: pf-proof

Let
$$
u\coloneqq F(z)
=
\frac{w-z}{1-\overline wz}.
$$
Then
$$
\begin{aligned}
w-u
&=
\frac{w(1-\overline wz)-(w-z)}
{1-\overline wz}\\
&=
\frac{(1-\abs{w}^2)z}
{1-\overline wz},
\end{aligned}
$$
and
$$
\begin{aligned}
1-\overline wu
&=
\frac{1-\overline wz-\overline w(w-z)}
{1-\overline wz}\\
&=
\frac{1-\abs{w}^2}
{1-\overline wz}.
\end{aligned}
$$
Therefore
$$
F(u)
=
\frac{w-u}{1-\overline wu}
=z.
$$

:::

:::

::: {.pf-step #s1-8}

The map
$$
F:\DD\to\DD
$$
is bijective.


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
F\circ F
=
\operatorname{id}_{\DD}.
$$
Thus $F$ is its own inverse, so it is both injective and surjective.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} prove part (a). Steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} establish conditions (i)--(iv) of part (b).

:::

:::

:::
