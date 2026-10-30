---
schema: qual/card@1
id: P-UCLARA13S-01
kind: problem
title: Translation difference quotient forces constancy
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Suppose $f:\RR\to\RR$ is bounded and Lebesgue measurable, and
$$
\lim_{h\to0^+}\frac1h\int_0^1 \abs{f(x+h)-f(x)}\,dx=0.
$$
Show that $f$ is almost everywhere constant on $[0,1]$.
:::

::: {.solution}

Define
$$
F(x)
\coloneqq
\int_0^x f(t)\,dt.
$$

::: pf

::: {.pf-step #s1-1}

There is a measurable set $E\subset[0,1]$ of full measure such that for every $x\in E$,
$$
\lim_{h\to0^+}
\frac{F(x+h)-F(x)}{h}
=
f(x).
$$


::: pf-proof

Because $f$ is bounded, it belongs to $L^1_{\mathrm{loc}}(\RR)$. The Lebesgue differentiation theorem therefore gives
$$
\lim_{h\to0^+}
\frac1h
\int_x^{x+h}f(t)\,dt
=
f(x)
$$
for almost every $x$. Since
$$
F(x+h)-F(x)
=
\int_x^{x+h}f(t)\,dt,
$$
the displayed limit follows on a full-measure subset $E$ of $[0,1]$.

:::

:::

::: {.pf-step #s1-2}

If $a,b\in E$ with $a<b$, then
$$
f(a)=f(b).
$$


::: pf-proof

For $0<h<b-a$, one has
$$
\begin{aligned}
&\bigl(F(a+h)-F(a)\bigr)
-
\bigl(F(b+h)-F(b)\bigr)\\
&\qquad=
\int_a^{a+h}f(t)\,dt
-
\int_b^{b+h}f(t)\,dt\\
&\qquad=
\int_a^b f(t)\,dt
-
\int_{a+h}^{b+h}f(t)\,dt\\
&\qquad=
\int_a^b
\bigl(f(t)-f(t+h)\bigr)\,dt.
\end{aligned}
$$
Hence
$$
\begin{aligned}
&\abs{
\frac{F(a+h)-F(a)}{h}
-
\frac{F(b+h)-F(b)}{h}
}\\
&\qquad\le
\frac1h
\int_a^b
\abs{f(t+h)-f(t)}\,dt\\
&\qquad\le
\frac1h
\int_0^1
\abs{f(t+h)-f(t)}\,dt.
\end{aligned}
$$
The last quantity tends to $0$ by hypothesis. By step [](#s1-1){.pf-ref}, the left-hand side tends to
$$
\abs{f(a)-f(b)}.
$$
Therefore $f(a)=f(b)$.

:::

:::

::: {.pf-step #s1-3}

There is a constant $c\in\RR$ such that
$$
f(x)=c
$$
for almost every $x\in[0,1]$.


::: pf-proof

The set $E$ from step [](#s1-1){.pf-ref} has full measure and is therefore nonempty. Fix $a_0\in E$ and set
$$
c=f(a_0).
$$
For any $x\in E$, step [](#s1-2){.pf-ref} applied to the ordered pair $a_0,x$ gives
$$
f(x)=c.
$$
Thus $f=c$ on the full-measure set $E$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the desired almost-everywhere constancy.

:::

:::

:::
