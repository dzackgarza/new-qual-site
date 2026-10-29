---
schema: qual/card@1
id: P-BKS17-1B
kind: problem
title: Functions whose derivative equals every symmetric difference quotient
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 12 problem 1B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 smoothness-and-differentiation argument. The solution below derives only the twice differentiability needed and makes explicit the passage from the symmetric identity for $f''$ to constancy.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified twice differentiability, both differentiations with respect to $h$, constancy of the second derivative, and the converse substitution.
---

::: {.problem}
Find all differentiable functions $f : \RR \to \RR$ with the property that

$$
f'(x) = \frac{f(x + h) - f(x - h)}{2h}
$$

for all $x \in \RR$ and all $h \neq 0$. (Hint: multiply both sides by $2h$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every differentiable function satisfying the stated identity is twice differentiable.


::: pf-proof

Fix any $h_0\neq0$. The identity gives
$$
f'(x)=\frac{f(x+h_0)-f(x-h_0)}{2h_0}.
$$
Since $f$ is differentiable, the right-hand side is differentiable as a function of $x$. Hence $f'$ is differentiable, so $f''$ exists everywhere.

:::

:::

::: {.pf-step #s1-2}

For every $x\in\RR$ and every $h\neq0$,
$$
f''(x+h)=f''(x-h).
$$


::: pf-proof

Multiplying the given identity by $2h$ yields
$$
2hf'(x)=f(x+h)-f(x-h).
$$
Since $f$ is differentiable, both sides may be differentiated with respect to $h$. This gives
$$
2f'(x)=f'(x+h)+f'(x-h).
$$
By step [](#s1-1){.pf-ref}, $f'$ is differentiable, so differentiating once more with respect to $h$ gives
$$
0=f''(x+h)-f''(x-h),
$$
which is the asserted identity.

:::

:::

::: {.pf-step #s1-3}

The second derivative $f''$ is constant on $\RR$.


::: pf-proof

Let $a,b\in\RR$ with $a\neq b$. Set
$$
x\coloneqq\frac{a+b}{2},
\qquad
h\coloneqq\frac{a-b}{2}.
$$
Then $h\neq0$, $x+h=a$, and $x-h=b$. Step [](#s1-2){.pf-ref} therefore gives $f''(a)=f''(b)$. Thus $f''$ has the same value at every pair of distinct points, and hence is constant.

:::

:::

::: {.pf-step #s1-4}

Every solution has the form
$$
\boxed{f(x)=ax^2+bx+c}
$$
for some $a,b,c\in\RR$.


::: pf-proof

By step [](#s1-3){.pf-ref}, write $f''(x)=2a$ for a constant $a\in\RR$. Integrating once gives $f'(x)=2ax+b$ for some $b\in\RR$, and integrating again gives $f(x)=ax^2+bx+c$ for some $c\in\RR$.

:::

:::

::: {.pf-step #s1-5}

Conversely, every function $f(x)=ax^2+bx+c$ satisfies the required identity.


::: pf-proof

For $h\neq0$,
$$
\begin{aligned}
\frac{f(x+h)-f(x-h)}{2h}
&=\frac{a(x+h)^2+b(x+h)+c-a(x-h)^2-b(x-h)-c}{2h}\\
&=\frac{4axh+2bh}{2h}\\
&=2ax+b\\
&=f'(x).
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} shows that every solution is quadratic, and step [](#s1-5){.pf-ref} shows that every quadratic polynomial has the required property.

:::

:::

:::
