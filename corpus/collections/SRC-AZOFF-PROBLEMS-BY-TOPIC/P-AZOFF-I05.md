---
schema: qual/card@1
id: P-AZOFF-I05
kind: problem
title: Sharp bound for $|f'(0)|$ for maps of the disk into the right half-plane
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF asks for a bound on |f'(0)| with one closing absolute
    value bar. The card had an extra OCR-derived bar after the math span;
    that extraction artifact has been removed.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Composed f with the Cayley map (w-2)/(w+2), which maps the right
    half-plane to the unit disk and sends f(0)=2 to zero. Schwarz's lemma
    gives |f'(0)|/4<=1, and 2(1+z)/(1-z) attains equality.
---

::: {.problem}
[Fall 2010, Problem $\# 5 ]$ Let $H : = \{ z \in \mathbb { C } : \operatorname { R e } ( z ) > 0 \}$ . Suppose $f$ is an analytic function which maps the open unit disk $D$ into $H$ and satisfies $f ( 0 ) = 2$ . Find a sharp upper bound for $\left| f ^ { \prime } ( 0 ) \right|$, justifying your bound by a proof and its sharpness by an example.
:::

::: {.solution}
Define
$$
\Phi(w)=\frac{w-2}{w+2}.
$$

::: pf

::: {.pf-step #s1}

The map $\Phi$ sends the right half-plane $H$ into the open unit
disk.

::: pf-proof

If $w\in H$, then $\operatorname{Re}w>0$. Hence
$$
\begin{aligned}
\abs{w+2}^2-\abs{w-2}^2
&=
(w+2)(\bar w+2)-(w-2)(\bar w-2)\\
&=
8\operatorname{Re}w\\
&>
0.
\end{aligned}
$$
Therefore
$$
\abs{w-2}<\abs{w+2},
$$
so $\abs{\Phi(w)}<1$.

:::

:::

::: {.pf-step #s2}

The function
$$
g=\Phi\circ f
$$
is an analytic self-map of the unit disk satisfying $g(0)=0$.

::: pf-proof

The denominator $w+2$ does not vanish on $H$, so $\Phi$ is analytic there.
Since $f$ is analytic and maps the unit disk into $H$, step [](#s1){.pf-ref} shows that
$g$ is an analytic self-map of the unit disk. Moreover,
$$
g(0)
=
\frac{f(0)-2}{f(0)+2}
=
0.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\abs{g'(0)}\leq1.
$$

::: pf-proof

This is Schwarz's lemma applied to the function in step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The derivatives satisfy
$$
g'(0)=\frac{f'(0)}4.
$$

::: pf-proof

Differentiating
$$
\Phi(w)=\frac{w-2}{w+2}
$$
gives
$$
\Phi'(w)=\frac4{(w+2)^2}.
$$
By the chain rule and $f(0)=2$,
$$
g'(0)
=
\Phi'(f(0))f'(0)
=
\frac4{(2+2)^2}f'(0)
=
\frac{f'(0)}4.
$$

:::

:::

::: {.pf-step #s5}

The sharp upper bound is
$$
\boxed{
\abs{f'(0)}\leq4.
}
$$

::: pf-proof

Combining steps [](#s3){.pf-ref} and [](#s4){.pf-ref} gives
$$
\frac{\abs{f'(0)}}4
=
\abs{g'(0)}
\leq1.
$$

:::

:::

::: {.pf-step #s6}

The bound in step [](#s5){.pf-ref} is attained by
$$
f_0(z)=2\frac{1+z}{1-z}.
$$

::: pf-proof

The Cayley transform
$$
\frac{1+z}{1-z}
$$
maps the open unit disk into the right half-plane, so $f_0$ maps the disk
into $H$. Also
$$
f_0(0)=2.
$$
Differentiating gives
$$
f_0'(z)=\frac4{(1-z)^2},
$$
and hence
$$
\abs{f_0'(0)}=4.
$$
Thus equality occurs in step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the upper bound, and step [](#s6){.pf-ref} proves its sharpness.

:::

:::

:::
