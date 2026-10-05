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
Let $U\subset\mathbb C$ be bounded and open with $0\in U$, and let $f:U\to\mathbb C$ be holomorphic with $f(U)\subset U$ and $f(0)=0$.
Show that
\[
|f'(0)|\le1.
\]
Hint: consider the iterates $f^n=f\circ\cdots\circ f$.
:::

::: {.solution}
<1>1. Since $U$ is open and contains $0$, choose $r>0$ such that
\[
\overline{D(0,r)}\subset U.
\]

::: {.proof}
Openness of $U$ at $0$ gives some disk $D(0,R)\subset U$. Choose any $0<r<R$.
:::

<1>2. Since $U$ is bounded, choose $M>0$ such that
\[
|z|\leq M
\qquad(z\in U).
\]

::: {.proof}
This is the definition of boundedness of $U\subset\mathbb C$.
:::

<1>3. For every integer $n\geq1$, the iterate
\[
f^n=f\circ\cdots\circ f
\]
is holomorphic on $U$, maps $U$ into $U$, and fixes $0$.

::: {.proof}
The composition of holomorphic maps is holomorphic. Since $f(U)\subset U$, all iterates are defined on $U$ and remain in $U$. Inductively,
\[
f^n(0)=0
\]
because $f(0)=0$.
:::

<1>4. Cauchy's estimate applied on the circle $|z|=r$ gives
\[
|(f^n)'(0)|\leq\frac Mr
\qquad(n\geq1).
\]

::: {.proof}
By steps <1>2--<1>3,
\[
|f^n(z)|\leq M
\]
for every $z\in U$, hence in particular on $|z|=r$. Cauchy's derivative formula gives
\[
(f^n)'(0)=\frac1{2\pi i}\int_{|z|=r}\frac{f^n(z)}{z^2}\,dz,
\]
so
\[
|(f^n)'(0)|\leq\frac Mr.
\]
:::

<1>5. The chain rule gives
\[
(f^n)'(0)=f'(0)^n.
\]

::: {.proof}
Every intermediate point in the derivative of the composition is $0$ because every iterate fixes $0$. Thus the chain rule multiplies $n$ copies of $f'(0)$.
:::

<1>6. Hence for every $n\geq1$,
\[
|f'(0)|^n\leq\frac Mr.
\]

::: {.proof}
Combine steps <1>4 and <1>5 and take absolute values.
:::

<1>7. Therefore
\[
\boxed{|f'(0)|\leq1.}
\]

::: {.proof}
If $|f'(0)|>1$, then $|f'(0)|^n\to\infty$ as $n\to\infty$, contradicting the uniform upper bound $M/r$ in step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required derivative bound.
:::
:::
