---
schema: qual/card@1
id: P-TIE-F15-15
kind: problem
title: Schwarz lemma for functions with positive real part
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 15.
---

::: {.problem}
(1) Let $f ( z ) \in H ( \mathbb { D } ) , \operatorname { R e } ( f ( z ) ) > 0 , f ( 0 ) = a > 0$ . Show that

$$
| \frac { f ( z ) - a } { f ( z ) + a } | \leq | z | , | f ^ { \prime } ( 0 ) | \leq 2 a .
$$

(2) Show that the above is still true if $\mathrm { R e } ( f ( z ) ) > 0$ is replaced with $\mathrm { R e } ( f ( z ) ) \geq 0$
:::

::: pf

::: pf-step

Under the hypotheses of part (1), the function
$$
\phi(z)
\coloneqq
\frac{f(z)-a}{f(z)+a}
$$
is a holomorphic self-map of $\DD$ satisfying $\phi(0)=0$.


::: pf-proof

Since $\operatorname{Re}f(z)>0$ and $a>0$, one has
$$
\operatorname{Re}(f(z)+a)>a>0,
$$
so the denominator never vanishes and $\phi$ is holomorphic.

For any complex number $w$ with $\operatorname{Re}w>0$,
$$
\begin{aligned}
\abs{w+a}^2-\abs{w-a}^2
&=
(w+a)(\overline w+a)-(w-a)(\overline w-a)\\
&=
4a\operatorname{Re}w
>0.
\end{aligned}
$$
Hence
$$
\abs{\frac{w-a}{w+a}}<1.
$$
Taking $w=f(z)$ shows $\phi(\DD)\subset\DD$. Finally,
$$
\phi(0)
=
\frac{f(0)-a}{f(0)+a}
=0.
$$

:::

:::

::: pf-step

For every $z\in\DD$,
$$
\boxed{
\abs{\frac{f(z)-a}{f(z)+a}}
\le
\abs{z}.
}
$$


::: pf-proof

By step <1>1, $\phi:\DD\to\DD$ is holomorphic and $\phi(0)=0$. Schwarz's lemma therefore gives
$$
\abs{\phi(z)}\le\abs{z},
$$
which is exactly the displayed inequality.

:::

:::

::: pf-step

One has
$$
\boxed{\abs{f'(0)}\le2a.}
$$


::: pf-proof

Differentiate the function from step <1>1:
$$
\phi'(z)
=
\frac{f'(z)(f(z)+a)-f'(z)(f(z)-a)}
{(f(z)+a)^2}
=
\frac{2af'(z)}{(f(z)+a)^2}.
$$
Since $f(0)=a$,
$$
\phi'(0)
=
\frac{f'(0)}{2a}.
$$
Schwarz's lemma gives $\abs{\phi'(0)}\le1$, hence
$$
\abs{f'(0)}\le2a.
$$

:::

:::

::: pf-step

If instead $\operatorname{Re}f(z)\ge0$ on $\DD$, then in fact
$$
\operatorname{Re}f(z)>0
$$
for every $z\in\DD$.


::: pf-proof

Let
$$
u(z)\coloneqq\operatorname{Re}f(z).
$$
Then $u$ is harmonic, $u\ge0$ on $\DD$, and
$$
u(0)=a>0.
$$
If $u(z_0)=0$ at some interior point, then $u$ would attain its minimum value $0$ at $z_0$. By the strong minimum principle for harmonic functions, $u$ would be constant on the connected disk, hence identically $0$. This contradicts $u(0)=a>0$. Therefore $u>0$ throughout $\DD$.

:::

:::

::: pf-step

The conclusions of part (1) remain valid under the non-strict hypothesis $\operatorname{Re}f\ge0$.


::: pf-proof

By step <1>4, the non-strict hypothesis together with $f(0)=a>0$ implies the strict hypothesis of part (1). Steps <1>2 and <1>3 therefore apply unchanged.

:::

:::

::: pf-qed

Steps <1>2 and <1>3 prove part (1), and step <1>5 proves part (2).

:::

:::
