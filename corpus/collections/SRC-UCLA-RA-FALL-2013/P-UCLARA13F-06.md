---
schema: qual/card@1
id: P-UCLARA13F-06
kind: problem
title: Derivative bound for a bounded-domain holomorphic self-map fixing zero
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $U\subset\CC$ be bounded and open with $0\in U$, and let $f:U\to\CC$ be holomorphic with $f(U)\subset U$ and $f(0)=0$.
Show that
$$
\abs{f'(0)}\le1.
$$
Hint: consider the iterates $f^n=f\circ\cdots\circ f$.
:::

::: {.solution}

::: pf

::: pf-step

Since $U$ is open and contains $0$, choose $r>0$ such that
$$
\overline{D(0,r)}\subset U.
$$


::: pf-proof

Openness of $U$ at $0$ gives some disk $D(0,R)\subset U$. Choose any $0<r<R$.

:::

:::

::: {.pf-step #s1-2}

Since $U$ is bounded, choose $M>0$ such that
$$
\abs{z}\leq M
\qquad(z\in U).
$$


::: pf-proof

This is the definition of boundedness of $U\subset\CC$.

:::

:::

::: {.pf-step #s1-3}

For every integer $n\geq1$, the iterate
$$
f^n=f\circ\cdots\circ f
$$
is holomorphic on $U$, maps $U$ into $U$, and fixes $0$.


::: pf-proof

The composition of holomorphic maps is holomorphic. Since $f(U)\subset U$, all iterates are defined on $U$ and remain in $U$. Inductively,
$$
f^n(0)=0
$$
because $f(0)=0$.

:::

:::

::: {.pf-step #s1-4}

Cauchy's estimate applied on the circle $\abs{z}=r$ gives
$$
\abs{(f^n)'(0)}\leq\frac Mr
\qquad(n\geq1).
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
\abs{f^n(z)}\leq M
$$
for every $z\in U$, hence in particular on $\abs{z}=r$. Cauchy's derivative formula gives
$$
(f^n)'(0)=\frac1{2\pi i}\int_{\abs{z}=r}\frac{f^n(z)}{z^2}\,dz,
$$
so
$$
\abs{(f^n)'(0)}\leq\frac Mr.
$$

:::

:::

::: {.pf-step #s1-5}

The chain rule gives
$$
(f^n)'(0)=f'(0)^n.
$$


::: pf-proof

Every intermediate point in the derivative of the composition is $0$ because every iterate fixes $0$. Thus the chain rule multiplies $n$ copies of $f'(0)$.

:::

:::

::: {.pf-step #s1-6}

Hence for every $n\geq1$,
$$
\abs{f'(0)}^n\leq\frac Mr.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} and take absolute values.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{\abs{f'(0)}\leq1.}
$$


::: pf-proof

If $\abs{f'(0)}>1$, then $\abs{f'(0)}^n\to\infty$ as $n\to\infty$, contradicting the uniform upper bound $M/r$ in step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required derivative bound.

:::

:::

:::
